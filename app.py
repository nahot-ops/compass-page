"""
愛媛大学工学部「学校推薦型選抜Ⅰ」面接対策アプリ
Streamlit + OpenAI API による対話型面接シミュレーター
"""

import re

import streamlit as st

try:
    from openai import OpenAI
    import openai as openai_module
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


# ============================================================
# 定数定義
# ============================================================

APP_TITLE = "愛媛大学工学部 学校推薦型選抜Ⅰ 面接対策アプリ"

COURSE_CONTEXT = {
    "工学科 社会基盤工学コース": (
        "河川・海岸工学、防災工学、都市・地域計画、交通工学、環境工学など、"
        "社会基盤（インフラ）の整備・維持管理・防災に関わる分野。"
        "四国・愛媛特有の豪雨災害や南海トラフ地震への備え、離島・中山間地域における"
        "インフラの老朽化対策など、地域課題との関連が特に重視される。"
    ),
    "建築・社会デザインコース": (
        "建築意匠・構造・環境工学、都市デザイン、地域再生・まちづくりに関わる分野。"
        "愛媛県内の歴史的建築物の保存活用、地域コミュニティと連携した空き家再生、"
        "瀬戸内の景観デザインなど、地域課題との関連が特に重視される。"
    ),
}

GENERAL_TOPICS = [
    (
        "志望理由",
        "なぜ愛媛大学工学部、特に受験者が選択した志望コースを志望するのか、その理由を尋ねる質問をしてください。",
    ),
    (
        "活動報告書・高校生活",
        "活動報告書の内容や、高校生活における探究活動・部活動・資格取得など、"
        "受験者情報の『高校での取り組み』『アピールしたい活動』に触れながら、"
        "具体的なエピソードを尋ねる質問をしてください。",
    ),
    (
        "将来のキャリア像",
        "大学卒業後の将来のキャリア像や、大学で学びたい具体的な分野・研究テーマについて尋ねる質問をしてください。",
    ),
]

ORAL_SUBJECTS = [
    (
        "math",
        "数学",
        "微分・積分、ベクトル、関数、図形の性質など高校数学の概念や定理について、"
        "その本質的な意味を自分の言葉で論理的に説明させる問題を1問出題してください。"
        "例えば「微分の考え方を日常生活や工学の事象に例えて説明してください」"
        "「ベクトルとは何か、スカラーとの違いを交えて説明してください」のような問題です。"
        "必要であれば志望コースに関連する工学的な事象（インフラ・建築等）に絡めても構いません。",
    ),
    (
        "english",
        "英語",
        "工学に関連する平易な短い英文（2〜4文程度）を問題文の中に提示し、"
        "その要約または和訳を求める、あるいは英文の内容に関する簡単な質問を投げかけ"
        "英語または日本語で回答させる問題を1問出題してください。",
    ),
    (
        "japanese",
        "国語",
        "科学技術の発展と環境問題、防災・インフラの老朽化、地域社会の課題など、"
        "社会的なテーマに関する短い文章やテーマを提示し、それに対する受験者自身の主張と"
        "その論理的根拠を述べさせる問題を1問出題してください。",
    ),
]

FEEDBACK_INSTRUCTION = """
ここまでで、一般面接・口頭試問（数学・英語・国語）・逆質問のすべてのやり取りが終了しました。
面接官として、これまでの全会話を踏まえた詳細な講評を作成してください。

出力は Markdown 形式・日本語で、以下の構成に厳密に従ってください。見出しのレベルも変更しないでください。

## 総合講評
(3〜4文程度で、受験者の面接全体の印象を総括してください)

## 評価詳細

### 1. 論理的思考力・説明力(特に口頭試問での説明の筋道)
評価: [A/B/C/Dのいずれか1文字]

(具体的な発言内容に触れながら、3〜5文程度で評価理由を説明してください)

### 2. 専門分野への意欲・適性(工学への興味、愛媛大学・志望コースへの志望度の高さ)
評価: [A/B/C/Dのいずれか1文字]

(3〜5文程度で評価理由を説明してください)

### 3. コミュニケーション能力(言葉遣い、簡潔さ)
評価: [A/B/C/Dのいずれか1文字]

(3〜5文程度で評価理由を説明してください)

## 4. 今後の改善ポイントと模範回答例
(口頭試問を中心に、特に改善の余地があった質問を2〜3個取り上げ、それぞれについて
「何が不足していたか」と「模範的な回答の方向性(例)」を箇条書きで具体的に示してください)

評価基準: A=非常に優れている、B=良好、C=やや改善の余地あり、D=大きく改善が必要
上記の評価基準の説明文はそのまま出力に含めないでください。
"""

GRADE_PATTERN = re.compile(r"評価[:：]\s*([A-D])")


# ============================================================
# セッション状態の初期化
# ============================================================

def init_session_state():
    defaults = {
        "interview_started": False,
        "messages": [],
        "phase": "setup",  # setup / general / oral / closing / ready_for_feedback / feedback
        "general_idx": 0,
        "oral_idx": 0,
        "oral_followup_used": False,
        "profile": {},
        "api_key": "",
        "model": "gpt-4o-mini",
        "feedback_text": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def reset_interview():
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    init_session_state()


# ============================================================
# LLM 呼び出し
# ============================================================

def build_persona() -> str:
    p = st.session_state.profile
    course = p.get("course", "")
    course_desc = COURSE_CONTEXT.get(course, "")
    return f"""あなたは愛媛大学工学部「学校推薦型選抜Ⅰ」(共通テスト免除型)の面接官です。

# あなたの人格
厳粛かつ知性的で、受験者の本質的な論理的思考力を引き出そうとする、国立大学工学部の面接官(教授)です。
高圧的にはならず、しかし安易に迎合もせず、常に的確な問いを1つずつ投げかけます。

# 受験者情報
- 志望コース: {course}
- コースの特色: {course_desc}
- 得意科目: {p.get('favorite_subject', '')}
- 高校での取り組み: {p.get('activities', '')}
- アピールしたい活動: {p.get('appeal_points', '')}

# 厳守事項
- 必ず日本語で発言してください(口頭試問の英文提示部分を除く)。
- 1回の発言で複数の質問を同時に投げかけないでください。必ず1問だけにしてください。
- 面接官として自然な話し言葉で、簡潔に(長くても3〜4文程度)発言してください。
- 「はい、それでは」等の定型的な前置きを多用しすぎないでください。
- 受験者への問いかけは、これまでの会話の流れを踏まえ、自然な敬語で行ってください。
- 指示された内容以外の発言(例えば合否に関するコメント等)は行わないでください。
"""


class LLMError(Exception):
    pass


def call_llm(instruction: str, max_tokens: int = 400) -> str:
    if not OPENAI_AVAILABLE:
        raise LLMError("openai ライブラリがインストールされていません。`pip install openai` を実行してください。")

    api_key = st.session_state.api_key.strip()
    if not api_key:
        raise LLMError("OpenAI APIキーが設定されていません。サイドバーから入力してください。")

    try:
        client = OpenAI(api_key=api_key)
        messages = [{"role": "system", "content": build_persona()}]
        messages += [
            {"role": m["role"], "content": m["content"]} for m in st.session_state.messages
        ]
        messages.append({"role": "system", "content": instruction})

        response = client.chat.completions.create(
            model=st.session_state.model,
            messages=messages,
            temperature=0.7,
            max_tokens=max_tokens,
        )
        content = response.choices[0].message.content
        if not content:
            raise LLMError("AIからの応答が空でした。もう一度お試しください。")
        return content.strip()

    except openai_module.AuthenticationError:
        raise LLMError("OpenAI APIキーが正しくありません。サイドバーのAPIキーをご確認ください。")
    except openai_module.RateLimitError:
        raise LLMError("APIの利用上限に達しました。しばらく待ってから再度お試しください。")
    except openai_module.APIConnectionError:
        raise LLMError("OpenAI APIへの通信に失敗しました。ネットワーク環境をご確認の上、再度お試しください。")
    except openai_module.APIError as e:
        raise LLMError(f"OpenAI APIでエラーが発生しました: {e}")
    except Exception as e:
        raise LLMError(f"予期しないエラーが発生しました: {e}")


def safe_call_llm(instruction: str, max_tokens: int = 400):
    """成功時は (True, 応答テキスト)、失敗時は (False, エラーメッセージ) を返す。"""
    try:
        return True, call_llm(instruction, max_tokens=max_tokens)
    except LLMError as e:
        return False, str(e)


# ============================================================
# フェーズ遷移ロジック
# ============================================================

def strip_control_tag(reply: str):
    """先頭の [FOLLOWUP] / [NEXT] タグを取り除き、(tag, 本文) を返す。"""
    m = re.match(r"^\s*\[(FOLLOWUP|NEXT)\]\s*", reply, flags=re.IGNORECASE)
    if not m:
        return "NEXT", reply.strip()
    tag = m.group(1).upper()
    body = reply[m.end():].strip()
    return tag, body


def start_interview():
    st.session_state.messages = []
    st.session_state.general_idx = 0
    st.session_state.oral_idx = 0
    st.session_state.oral_followup_used = False

    _, first_instruction = GENERAL_TOPICS[0]
    instruction = (
        "面接の冒頭です。受験者に落ち着いた簡潔な挨拶(1文)をした後、"
        f"次の指示に従い最初の質問をしてください。{first_instruction}"
    )
    ok, reply = safe_call_llm(instruction)
    if not ok:
        st.session_state.interview_started = False
        return False, reply

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.session_state.phase = "general"
    st.session_state.interview_started = True
    return True, reply


def handle_general_answer():
    idx = st.session_state.general_idx
    if idx + 1 < len(GENERAL_TOPICS):
        next_idx = idx + 1
        _, topic_instruction = GENERAL_TOPICS[next_idx]
        instruction = (
            "直前の受験者の回答を踏まえ、短く自然な相槌(1文)を挟んでから、"
            f"次の指示に従い質問してください。{topic_instruction}"
        )
        ok, reply = safe_call_llm(instruction)
        if ok:
            st.session_state.general_idx = next_idx
        return ok, reply

    subject_key, subject_label, subject_prompt = ORAL_SUBJECTS[0]
    instruction = (
        "一般質問がすべて終了しました。直前の回答に短く触れてから(1文)、"
        "『ここからは学力に関する口頭試問に移ります』という趣旨を一言伝えた上で、"
        f"次の指示に従い問題を出題してください。{subject_prompt}"
    )
    ok, reply = safe_call_llm(instruction)
    if ok:
        st.session_state.phase = "oral"
        st.session_state.oral_idx = 0
        st.session_state.oral_followup_used = False
    return ok, reply


def handle_oral_answer():
    subject_idx = st.session_state.oral_idx
    subject_key, subject_label, subject_prompt = ORAL_SUBJECTS[subject_idx]
    is_last_subject = subject_idx == len(ORAL_SUBJECTS) - 1

    if is_last_subject:
        next_step_text = (
            '面接の最後の質問として、『最後に何か質問や言い残したことはありますか?』'
            "という趣旨の質問"
        )
    else:
        next_subject_label = ORAL_SUBJECTS[subject_idx + 1][1]
        next_subject_prompt = ORAL_SUBJECTS[subject_idx + 1][2]
        next_step_text = f"次の科目である{next_subject_label}の口頭試問の問題({next_subject_prompt})"

    if not st.session_state.oral_followup_used:
        instruction = f"""直前の受験者の回答(現在の科目: {subject_label}の口頭試問)を評価してください。
出力は次のいずれかの形式で、日本語で1つの発言のみを返してください。前置きの説明は不要です。

パターンA(回答が抽象的・表面的で、論理的な説明の道筋が不足していると判断した場合):
先頭に半角の「[FOLLOWUP]」とだけ書き、続けて「具体的にはどういうことですか?」のような、
掘り下げのための短い質問を1文だけ返してください。

パターンB(回答が具体的・論理的で十分だと判断した場合):
先頭に半角の「[NEXT]」とだけ書き、続けて回答への短い受け止め(1文)に続けて、
{next_step_text}を出題してください。
"""
        ok, reply = safe_call_llm(instruction)
        if not ok:
            return ok, reply

        tag, body = strip_control_tag(reply)
        if tag == "FOLLOWUP":
            st.session_state.oral_followup_used = True
            return True, body

        st.session_state.oral_followup_used = False
        st.session_state.oral_idx += 1
        if st.session_state.oral_idx >= len(ORAL_SUBJECTS):
            st.session_state.phase = "closing"
        return True, body

    instruction = (
        "直前の受験者の回答は、先ほどの掘り下げ質問に対する回答です。"
        "短い受け止め(1文)に続けて、"
        f"{next_step_text}を出題してください。先頭に余計なタグは付けないでください。"
    )
    ok, reply = safe_call_llm(instruction)
    if not ok:
        return ok, reply

    st.session_state.oral_followup_used = False
    st.session_state.oral_idx += 1
    if st.session_state.oral_idx >= len(ORAL_SUBJECTS):
        st.session_state.phase = "closing"
    return True, reply


def handle_closing_answer():
    instruction = (
        "受験者からの最後の発言(逆質問・言い残したこと)を受け取りました。"
        "面接官として、短く丁寧に締めの言葉(2文程度)を述べてください。"
        "合否に関する言及は絶対に行わないでください。"
    )
    ok, reply = safe_call_llm(instruction)
    if ok:
        st.session_state.phase = "ready_for_feedback"
    return ok, reply


def generate_feedback():
    ok, reply = safe_call_llm(FEEDBACK_INSTRUCTION, max_tokens=1600)
    if ok:
        st.session_state.feedback_text = reply
        st.session_state.phase = "feedback"
    return ok, reply


# ============================================================
# UI: サイドバー
# ============================================================

def render_sidebar():
    st.sidebar.header("面接設定")

    if not st.session_state.interview_started:
        course = st.sidebar.selectbox("志望コース", list(COURSE_CONTEXT.keys()))

        api_key = st.sidebar.text_input(
            "OpenAI APIキー",
            type="password",
            value=st.session_state.api_key,
            help="sk- から始まるAPIキーを入力してください。このセッション内でのみ使用されます。",
        )

        with st.sidebar.expander("詳細設定"):
            model = st.selectbox(
                "使用モデル", ["gpt-4o-mini", "gpt-4o"], index=0
            )

        st.sidebar.subheader("受験生の基本情報")
        favorite_subject = st.sidebar.selectbox(
            "得意科目", ["数学", "英語", "国語", "理科", "地理歴史・公民", "その他"]
        )
        activities = st.sidebar.text_area(
            "高校での取り組み(部活動・生徒会・資格など)",
            placeholder="例: 3年間野球部に所属し、副部長としてチームをまとめた。危険物取扱者乙種4類を取得。",
        )
        appeal_points = st.sidebar.text_area(
            "特にアピールしたい活動・探究活動",
            placeholder="例: 地域の河川氾濫について調査し、文化祭で発表した探究活動。",
        )

        start_clicked = st.sidebar.button("🎬 面接開始", type="primary", use_container_width=True)

        if start_clicked:
            errors = []
            if not api_key.strip():
                errors.append("OpenAI APIキーを入力してください。")
            if not activities.strip():
                errors.append("『高校での取り組み』を入力してください。")
            if not appeal_points.strip():
                errors.append("『アピールしたい活動・探究活動』を入力してください。")

            if errors:
                for e in errors:
                    st.sidebar.error(e)
            else:
                st.session_state.api_key = api_key
                st.session_state.model = model
                st.session_state.profile = {
                    "course": course,
                    "favorite_subject": favorite_subject,
                    "activities": activities.strip(),
                    "appeal_points": appeal_points.strip(),
                }
                with st.spinner("面接官が入室しています..."):
                    ok, msg = start_interview()
                if not ok:
                    st.sidebar.error(msg)
    else:
        p = st.session_state.profile
        st.sidebar.success("面接を実施中です")
        st.sidebar.markdown(f"**志望コース**: {p.get('course', '')}")
        st.sidebar.markdown(f"**得意科目**: {p.get('favorite_subject', '')}")
        st.sidebar.markdown(f"**使用モデル**: {st.session_state.model}")

        phase_labels = {
            "general": "第1フェーズ: 一般面接",
            "oral": "第2フェーズ: 口頭試問",
            "closing": "第3フェーズ: 逆質問・締め",
            "ready_for_feedback": "フィードバック待機中",
            "feedback": "フィードバック表示中",
        }
        st.sidebar.info(f"現在: {phase_labels.get(st.session_state.phase, '')}")

        if st.sidebar.button("🔄 最初からやり直す", use_container_width=True):
            reset_interview()
            st.rerun()


# ============================================================
# UI: メインエリア
# ============================================================

def render_grade_summary(feedback_text: str):
    grades = GRADE_PATTERN.findall(feedback_text)
    labels = ["論理的思考力・説明力", "専門分野への意欲・適性", "コミュニケーション能力"]
    if len(grades) >= 3:
        cols = st.columns(3)
        for col, label, grade in zip(cols, labels, grades[:3]):
            col.metric(label, grade)


def render_main():
    st.title(APP_TITLE)

    if not st.session_state.interview_started:
        st.info(
            "サイドバーで志望コース・OpenAI APIキー・受験生の基本情報を入力し、"
            "「面接開始」ボタンを押してください。\n\n"
            "一般面接(志望理由・活動報告書等)に続き、数学・英語・国語の口頭試問を行い、"
            "最後にAI面接官による詳細なフィードバックを受け取ることができます。"
        )
        return

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    phase = st.session_state.phase

    if phase in ("general", "oral", "closing"):
        prompt = st.chat_input("回答を入力してください...")
        if prompt:
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            with st.chat_message("assistant"):
                with st.spinner("面接官が確認しています..."):
                    if phase == "general":
                        ok, reply = handle_general_answer()
                    elif phase == "oral":
                        ok, reply = handle_oral_answer()
                    else:
                        ok, reply = handle_closing_answer()

                if ok:
                    st.markdown(reply)
                    st.session_state.messages.append({"role": "assistant", "content": reply})
                else:
                    st.error(reply)
                    st.caption("もう一度回答を送信するか、APIキーやネットワーク環境をご確認ください。")

    if st.session_state.phase == "ready_for_feedback":
        st.divider()
        st.success("すべての質疑応答が終了しました。")
        if st.button("📝 面接を終了してフィードバックを見る", type="primary"):
            with st.spinner("面接官が講評を作成しています..."):
                ok, msg = generate_feedback()
            if ok:
                st.rerun()
            else:
                st.error(msg)

    if st.session_state.phase == "feedback":
        st.divider()
        st.header("📋 面接フィードバック")
        render_grade_summary(st.session_state.feedback_text)
        st.markdown(st.session_state.feedback_text)


# ============================================================
# エントリーポイント
# ============================================================

def main():
    st.set_page_config(page_title=APP_TITLE, page_icon="🎓", layout="centered")
    init_session_state()

    if not OPENAI_AVAILABLE:
        st.error(
            "openai ライブラリが見つかりません。`pip install openai streamlit` を実行してから、"
            "再度アプリを起動してください。"
        )
        return

    render_sidebar()
    render_main()


if __name__ == "__main__":
    main()
