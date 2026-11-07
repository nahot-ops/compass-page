#!/usr/bin/env python3
"""冬休み〜3学期 案内記事2本＋プレビューを生成する（ComPassロゴ配色）"""
import pathlib

D = pathlib.Path('/home/user/compass-page/news/2026-winter')

# ---- 色（ComPassロゴ） ----
NAVY = '#1E2B3C'; TEXT = '#333333'; SUB = '#5B6675'
BLUE = '#2BA9E1'; BLUE_D = '#1A86BE'; BLUE_L = '#EEF7FD'; BLUE_B = '#BFE3F5'
ORANGE = '#F39221'; ORANGE_D = '#C25E00'; CREAM = '#FFF5E9'; CREAM_B = '#F6C78F'
YELLOW = '#F9D02B'; WARN = '#D2491E'
LINE = '#06C755'
LINE_URL = 'https://cuiy3qe5.autosns.app/line'
FRIEND = LINE_URL


def dots():
    # ロゴの黄色いドットをイメージした飾り
    d = ''.join(f'<span style="display:inline-block; width:7px; height:7px; margin:0 5px; border-radius:50%; background:{c};"></span>'
                for c in [YELLOW, ORANGE, YELLOW, BLUE, YELLOW])
    return f'<div style="margin:0 0 0.6em; line-height:1;">{d}</div>'


def h2(text, eyebrow='', id_=''):
    idattr = f' id="{id_}"' if id_ else ''
    eb = (f'<span style="display:block; margin:0 0 0.15em; color:{ORANGE_D}; font-size:0.62em; font-weight:bold; letter-spacing:0.12em;">{eyebrow}</span>'
          if eyebrow else '')
    return (f'<h2{idattr} style="margin:2.6em 0 1em; padding:0 0 0.45em; border:0; border-bottom:3px solid {BLUE_B}; background:none; '
            f'color:{NAVY}; font-size:1.32em; line-height:1.45; position:relative;">{eb}'
            f'<span style="display:inline-block; width:0.62em; height:0.62em; margin:0 0.4em 0.08em 0; border:3px solid {BLUE}; border-radius:50%; box-sizing:border-box; vertical-align:middle;"></span>{text}</h2>')


def h3(text):
    return (f'<h3 style="margin:1.8em 0 0.6em; padding:0 0 0 0.6em; border:0; border-left:4px solid {ORANGE}; background:none; '
            f'color:{NAVY}; font-size:1.1em; line-height:1.5;">{text}</h3>')


def p(html, extra=''):
    return f'<p style="margin:0.8em 0; {extra}">{html}</p>'


def note(html):
    return f'<p style="margin:0.5em 0; color:{SUB}; font-size:0.9em;">{html}</p>'


TH = f'padding:0.6em 0.5em; border:1px solid {BLUE_B}; background:{BLUE_L}; color:{NAVY}; text-align:left; font-weight:bold;'
TD = f'padding:0.6em 0.5em; border:1px solid {BLUE_B}; background:#ffffff;'


def kv_table(rows):
    out = []
    for i, (k, v) in enumerate(rows):
        w = ' width:5.2em;' if i == 0 else ''
        out.append(f'<tr><th style="{TH}{w}">{k}</th><td style="{TD}">{v}</td></tr>')
    return (f'<table style="width:100%; margin:1em 0 1.2em; border-collapse:collapse; border-spacing:0; font-size:0.95em;"><tbody>'
            + ''.join(out) + '</tbody></table>')


def grid_table(head, rows, center=True, fs='0.92em', hl_col=None):
    al = ' text-align:center;' if center else ''
    hs = []
    for i, h in enumerate(head):
        bg = f' background:{CREAM}; color:{ORANGE_D};' if i == hl_col else ''
        hs.append(f'<th style="{TH}{al}{bg} padding:0.55em 0.35em;">{h}</th>')
    rs = []
    for r in rows:
        cells = []
        for i, c in enumerate(r):
            bold = ' font-weight:bold;' if i == 0 else ''
            bg = ' background:#FFFBF4;' if i == hl_col else ''
            dim = ' color:#A0A8B3;' if c == '―' else ''
            cells.append(f'<td style="{TD}{al}{bold}{bg}{dim} padding:0.55em 0.35em;">{c}</td>')
        rs.append('<tr>' + ''.join(cells) + '</tr>')
    return (f'<table style="width:100%; margin:0 0 1em; border-collapse:collapse; border-spacing:0; font-size:{fs};">'
            f'<thead><tr>{"".join(hs)}</tr></thead><tbody>{"".join(rs)}</tbody></table>')


def box(html, kind='blue', extra=''):
    st = {
        'blue': f'background:{BLUE_L}; border:1px solid {BLUE_B};',
        'cream': f'background:{CREAM}; border:2px solid {CREAM_B};',
        'warn': f'background:#FFF4EF; border:2px solid {WARN};',
        'white': f'background:#ffffff; border:1px solid {BLUE_B};',
    }[kind]
    return f'<div style="margin:1.2em 0; padding:1.1em 1em; {st} border-radius:12px; {extra}">{html}</div>'


def msg_box(text):
    return (f'<span style="display:inline-block; margin:0.3em 0 0; padding:0.35em 0.9em; background:#ffffff; border:2px dashed {LINE}; '
            f'border-radius:8px; color:{NAVY}; font-weight:bold; letter-spacing:0.02em;">{text}</span>')


def line_btn(label, text, lead):
    return (f'<div style="margin:1.8em 0; padding:1.3em 1em 1.1em; background:#F3FBF6; border:2px solid #BDE8CF; border-radius:14px; text-align:center;">'
            f'<p style="margin:0 0 0.8em; color:{NAVY}; font-weight:bold;">{lead}</p>'
            f'<a href="{LINE_URL}" target="_blank" rel="noopener noreferrer" style="display:block; width:100%; max-width:360px; margin:0 auto 0.8em; '
            f'padding:0.95em 1em; background:{LINE}; border-radius:999px; box-shadow:0 3px 0 #04A346; color:#ffffff !important; font-size:1.08em; '
            f'font-weight:bold; text-decoration:none; text-align:center; box-sizing:border-box;">{label}</a>'
            f'<p style="margin:0; color:{TEXT}; font-size:0.92em;">トーク画面が開いたら、<br>次の文面を送ってください。<br>{msg_box(text)}</p></div>')


def small_line_btn(label):
    return (f'<a href="{LINE_URL}" target="_blank" rel="noopener noreferrer" style="display:block; width:100%; max-width:360px; margin:0.5em auto; '
            f'padding:0.9em 1em; background:{LINE}; border-radius:999px; box-shadow:0 3px 0 #04A346; color:#ffffff !important; font-size:1.05em; '
            f'font-weight:bold; text-decoration:none; text-align:center; box-sizing:border-box;">{label}</a>')


def msg_list(items):
    li = ''.join(f'<span style="display:block; margin:0.35em 0;"><span style="display:inline-block; width:4.5em; color:{SUB}; font-size:0.9em;">{g}</span>{msg_box(t)}</span>'
                 for g, t in items)
    return (f'<p style="margin:0.8em 0 0.2em; color:{TEXT}; font-size:0.92em;">トーク画面が開いたら、<br>お子さまの学年の文面を送ってください。</p>'
            f'<div style="display:inline-block; text-align:left;">{li}</div>')


def grade_card(href, badge, title, lines, color):
    li = '<br>'.join(lines)
    return (f'<a href="#{href}" style="display:block; flex:1 1 200px; min-width:0; padding:0.9em 0.9em 0.8em; background:#ffffff; '
            f'border:2px solid {color}; border-radius:14px; color:{TEXT} !important; text-decoration:none; box-sizing:border-box;">'
            f'<span style="display:inline-block; padding:0.15em 0.7em; background:{color}; border-radius:999px; color:#ffffff; font-size:0.9em; font-weight:bold;">{badge}</span>'
            f'<span style="display:block; margin:0.4em 0 0.2em; color:{NAVY}; font-size:1.08em; font-weight:bold;">{title}</span>'
            f'<span style="display:block; color:{SUB}; font-size:0.88em; line-height:1.6;">{li}</span>'
            f'<span style="display:block; margin-top:0.5em; color:{BLUE_D}; font-size:0.9em; font-weight:bold;">くわしく見る ↓</span></a>')


def cards(*cs):
    return f'<div style="display:flex; flex-wrap:wrap; gap:10px; margin:1em 0 1.4em;">{"".join(cs)}</div>'


def key_dates(items, foot=''):
    rows = []
    for d, label, strong in items:
        c = ORANGE if strong else BLUE
        rows.append(
            f'<div style="display:flex; gap:12px; align-items:flex-start; padding:0.7em 0; border-bottom:1px dashed {BLUE_B};">'
            f'<div style="flex:0 0 6.4em; padding:0.25em 0; background:{c}; border-radius:8px; color:#ffffff; font-weight:bold; text-align:center; line-height:1.35; font-size:0.92em;">{d}</div>'
            f'<div style="flex:1 1 auto; min-width:0; color:{NAVY}; line-height:1.6;">{label}</div></div>')
    return box(''.join(rows) + foot, 'white', 'padding:0.4em 1em 0.8em;')


def steps(items):
    out = []
    for i, (t, d) in enumerate(items, 1):
        out.append(
            f'<div style="display:flex; gap:12px; align-items:flex-start; margin:0 0 0.9em;">'
            f'<div style="flex:0 0 2.1em; height:2.1em; border-radius:50%; background:{BLUE}; color:#ffffff; font-weight:bold; text-align:center; line-height:2.1em;">{i}</div>'
            f'<div style="flex:1 1 auto; min-width:0; padding-top:0.15em;"><span style="display:block; color:{NAVY}; font-weight:bold;">{t}</span>'
            + (f'<span style="display:block; color:{TEXT}; font-size:0.95em;">{d}</span>' if d else '') + '</div></div>')
    return f'<div style="margin:1.2em 0;">{"".join(out)}</div>'


def faq(items):
    out = []
    for q, a in items:
        out.append(
            f'<details style="margin:0.7em 0; padding:0.85em 0.9em; border:1px solid {BLUE_B}; border-radius:10px; background:#ffffff;">'
            f'<summary style="color:{NAVY}; font-weight:bold; cursor:pointer;"><span style="color:{BLUE_D};">Q.</span> {q}</summary>'
            f'<p style="margin:0.7em 0 0;"><span style="color:{ORANGE_D}; font-weight:bold;">A.</span> {a}</p></details>')
    return ''.join(out)


def hero(eyebrow, title, sub, chips):
    ch = ''.join(
        f'<div style="flex:1 1 28%; min-width:5em; padding:0.5em 0.4em; background:#ffffff; border-radius:10px; text-align:center; box-sizing:border-box;">'
        f'<span style="display:block; color:{SUB}; font-size:0.78em; font-weight:bold;">{k}</span>'
        f'<span style="display:block; color:{NAVY}; font-size:0.95em; font-weight:bold; line-height:1.4;">{v}</span></div>' for k, v in chips)
    return (
        f'<div style="margin:0.5em 0 1.6em; padding:1.4em 1.1em 1.2em; background:{BLUE_L}; border-radius:18px; border-top:6px solid {BLUE};">'
        + dots() +
        f'<p style="margin:0; color:{ORANGE_D}; font-size:0.85em; font-weight:bold; letter-spacing:0.12em;">{eyebrow}</p>'
        f'<p style="margin:0.2em 0 0.5em; color:{NAVY}; font-size:1.55em; font-weight:bold; line-height:1.4;">{title}</p>'
        f'<p style="margin:0 0 1em; color:{TEXT}; line-height:1.8;">{sub}</p>'
        f'<div style="display:flex; flex-wrap:wrap; gap:8px; margin:0 0 0.6em;">{ch}</div>'
        + '</div>')


def wrap(body):
    return ('<!-- wp:html -->\n'
            f'<div style="max-width:860px; margin:0 auto; color:{TEXT}; font-size:16px; line-height:1.8; overflow-wrap:anywhere;">\n'
            + body + '\n</div>\n<!-- /wp:html -->\n')


def zanseki():
    return ('<!-- 残席ここから -->\n'
            + h2('受付状況', 'STATUS')
            + box(p('受付状況は、決まり次第この欄でお知らせします。<br>今の空き状況は、公式LINEからお問い合わせください。', 'margin:0;'))
            + '\n<!-- 残席ここまで -->\n')


def kakutei(extra, word='確定'):
    return box(f'<p style="margin:0; text-align:center;"><strong style="color:{WARN}; font-size:1.1em;">LINEを送っただけでは、<br>お申込みは{word}しません。</strong></p>'
               f'<p style="margin:0.6em 0 0; text-align:center;">{extra}</p>', 'warn')


def footer(cross_label, cross_text):
    return (
        f'<div style="margin:2.2em 0 0; padding:1.2em 1em; background:{BLUE_L}; border-radius:12px;">'
        f'<p style="margin:0 0 0.4em; color:{NAVY}; font-weight:bold;">学習塾ComPass</p>'
        f'<p style="margin:0.4em 0;">〒791-1102<br>愛媛県松山市来住町230-1</p>'
        f'<p style="margin:0.4em 0 0;">電話：<a href="tel:0899977388" style="color:{BLUE_D};">089-997-7388</a><br>'
        f'公式LINE：<a href="{FRIEND}" target="_blank" rel="noopener noreferrer" style="color:{BLUE_D};">友だち追加はこちら</a></p></div>'
        f'<p style="margin:1.4em 0 0; padding:0.9em 1em; border:2px dashed {BLUE_B}; border-radius:12px; font-size:0.95em;">{cross_label}'
        f'<a href="#" style="color:{BLUE_D}; font-weight:bold;">{cross_text}</a> '
        f'<span style="background:#ffe9a8; color:#a33;">【公開後に差し替え】</span></p>')


# =====================================================================
# 記事1：小学生
# =====================================================================
def article1():
    b = []
    b.append(hero('2026 WINTER｜小学生',
                  '冬期講習・冬の体験',
                  '冬休みは短いですが、<br>2学期までに習ったことを<br>落ち着いて見直せる時間です。<br>新しい学年を安心して迎える準備を、<br>この冬に一緒に進めましょう。',
                  [('対象', '小1〜小6'), ('期間', '12/25〜1/8'), ('申込締切', '12/23(水)')]))

    b.append(p(f'<strong style="color:{NAVY};">お子さまの学年を選んでください。</strong><br>押すと、日程・料金・申込みボタンへ移動します。', 'margin:0 0 0.2em;'))
    b.append(cards(
        grade_card('winter-sho6', '小6', '冬期講習', ['英語・算数・国語から選択', '全4日｜1教科 3,300円（税込）'], ORANGE),
        grade_card('winter-sho5', '小5', '冬期講習', ['算数・国語', '全4日｜1教科 3,300円（税込）'], BLUE),
        grade_card('winter-kids', '小1〜小4', 'コンパスキッズ 冬の体験', ['4コマを選んで参加', '全4回 5,500円（税込）'], '#E8A400'),
    ))

    b.append(h2('大事な日付', 'SCHEDULE'))
    b.append(key_dates([
        ('12/10(木)', 'LINEで仮押さえすると、早期申込の料金になる期限<br><span style="color:#5B6675; font-size:0.9em;">各学年の料金欄をご覧ください</span>', False),
        ('12/19(土)', 'パーティーに参加する方の、窓口での手続きの期限', False),
        ('12/21(月)', 'クリスマスパーティー兼オリエンテーション<br><span style="color:#5B6675; font-size:0.9em;">17:00〜19:00</span>', False),
        ('12/23(水)', '<strong>お申込み締切</strong><br><span style="color:#5B6675; font-size:0.9em;">この日までに窓口で手続きしてください</span>', True),
    ], note('※12/10は申込締切ではありません。お申込みは12/23(水)まで受け付けます。')))

    # パーティー
    b.append(h2('クリスマスパーティー兼オリエンテーション', 'EVENT'))
    b.append(p('講習が始まる前に、教室に来ていただける機会です。<br>先生や、一緒に講習を受ける友だちと顔を合わせておけるので、<br>初めての方も、講習の初日を気楽に迎えられます。'))
    b.append(kv_table([
        ('日時', '12月21日(月)<br>17:00〜19:00'),
        ('対象', '12月19日(土)までに、冬期講習・冬の体験の<br>窓口での手続きを終えた小学生<br>（ComPassに通っているかどうかは問いません）'),
        ('場所', '学習塾ComPass'),
    ]))
    b.append(box(p('講習のお申込みは12月23日(水)まで受け付けます。<br>'
                   f'ただし、<strong style="color:{WARN};">12月20日(日)以降に窓口で手続きされた場合は、<br>パーティーにはご参加いただけません。</strong>', 'margin:0;')
                 + p('パーティーにも参加したい方は、<br>早めにお申込みください。', 'margin:0.6em 0 0;'), 'cream'))

    # 小6
    b.append(h2('小6｜冬期講習', 'GRADE 6', 'winter-sho6'))
    b.append(p('小学校の学習を見直しながら、<br>中学の勉強につながる土台を整えます。'))
    b.append(box(p(f'<strong style="color:{NAVY};">最初のテストまでに、勉強の進め方を身につけておくと、<br>中1のスタートがぐっと楽になります。</strong>', 'margin:0;'), 'blue'))
    b.append(kv_table([
        ('対象', '現在の小学6年生'),
        ('教科', '英語・算数・国語から選べます<br>（1教科から受講できます）'),
        ('日程', '全4日<br>12/26(土)・1/4(月)・1/6(水)・1/8(金)'),
        ('料金', f'1教科 3,300円（税込）<br><span style="color:{ORANGE_D}; font-weight:bold;">12月10日(木)までの仮押さえで 2,640円（税込）</span>'),
    ]))
    b.append(h3('時間割'))
    b.append(p(f'<strong style="color:{WARN};">1/8(金)だけ、時間が変わります。</strong>', 'margin:0 0 0.6em; font-size:0.95em;'))
    b.append(grid_table(['教科', '12/26(土)<br>1/4(月)<br>1/6(水)', '1/8(金)<br>のみ'], [
        ['英語', '13:20〜14:00', '14:05〜14:45'],
        ['算数', '14:05〜14:45', '14:50〜15:30'],
        ['国語', '14:50〜15:30', '15:35〜16:15'],
    ], center=False, hl_col=2))
    b.append(note('※1回40分×4回。1教科あたり合計160分です。'))
    b.append(h3('冬期講習のあとは'))
    b.append(steps([
        ('講習の最終日', '面談の日程を決めます。'),
        ('1月の面談', '講習中の様子をお伝えし、<br>中学に向けた準備についてご相談します。'),
        ('中学準備の講座', '冬期のあとに、中学準備の講座も予定しています。<br>冬期講習を受けた方は、席を優先して確保します。'),
    ]))
    b.append(line_btn('小6｜LINEで申し込む', '小6 冬期講習 申込希望', '小6の冬期講習は、こちらからお申込みください。'))

    # 小5
    b.append(h2('小5｜冬期講習', 'GRADE 5', 'winter-sho5'))
    b.append(p('中学に向けて必要な、算数・国語の土台を固めます。<br>あわせて、家で勉強する習慣づくりも大切にしています。'))
    b.append(kv_table([
        ('対象', '現在の小学5年生'),
        ('教科', '算数・国語<br>（1教科から受講できます）'),
        ('日程', '全4日<br>12/25(金)・12/28(月)・1/5(火)・1/7(木)'),
        ('時間', '4日とも同じ時間です<br>算数 14:05〜14:45<br>国語 14:50〜15:30'),
        ('料金', f'1教科 3,300円（税込）<br><span style="color:{ORANGE_D}; font-weight:bold;">12月10日(木)までの仮押さえで 2,640円（税込）</span>'),
    ]))
    b.append(note('※1回40分×4回。1教科あたり合計160分です。'))
    b.append(h3('冬期講習のあとは'))
    b.append(steps([
        ('講習の最終日', '面談の日程を決めます。'),
        ('面談', '講習中の様子をもとに、<br>4月からの小学部についてご案内します。'),
    ]))
    b.append(line_btn('小5｜LINEで申し込む', '小5 冬期講習 申込希望', '小5の冬期講習は、こちらからお申込みください。'))

    # キッズ
    b.append(h2('コンパスキッズ（小1〜小4）｜冬の体験', 'KIDS', 'winter-kids'))
    b.append(p(f'コンパスキッズは、小1〜小4を対象にした<br><strong style="color:{NAVY};">「学びを好きになるための土台づくり」</strong>のプログラムです。'))
    b.append(p('冬休みは、ふだんの授業を体験できる<br>「冬の体験（全4回）」として募集します。<br>開講しているコマの中から、4コマを選んで参加できます。'))
    b.append(kv_table([
        ('対象', '小学1年生〜小学4年生'),
        ('時間', 'コマ① 11:00〜12:00<br>コマ② 13:00〜14:00'),
        ('受け方', '下の開講日の中から、4コマを選びます'),
        ('料金', f'冬の体験（全4回）5,500円（税込）<br><span style="color:{ORANGE_D}; font-weight:bold;">12月10日(木)までの仮押さえで 4,400円（税込）</span>'),
    ]))
    b.append(h3('開講日'))
    rows = [[d, '○', '○'] for d in ['12/26(土)', '12/28(月)', '1/4(月)', '1/5(火)', '1/6(水)', '1/7(木)']]
    rows.append(['1/8(金)', '―', '○'])
    b.append(grid_table(['日付', 'コマ①<br>11:00〜12:00', 'コマ②<br>13:00〜14:00'], rows))
    b.append(note('※1/8(金)は午後のみ（13:00〜14:00）です。<br>※コマごとの空き状況は、LINEをいただいたあとにご連絡します。'))
    b.append(line_btn('キッズ｜LINEで申し込む', 'キッズ 冬休み体験 申込希望', 'キッズの冬の体験は、こちらからお申込みください。'))

    # 料金一覧
    b.append(h2('料金一覧', 'PRICE'))
    b.append(p('料金はすべて税込です。<br>教材費・プリント代なども含まれています。', 'margin:0 0 0.6em; font-size:0.95em;'))
    b.append(grid_table(['学年・科目', '時間', '授業料', '12/10(木)<br>までの<br>仮押さえ'], [
        ['キッズ<br>冬の体験<br>（全4回）', '11:00〜<br>12:00<br>または<br>13:00〜<br>14:00', '5,500円', '4,400円'],
        ['小5<br>算数', '14:05〜<br>14:45', '3,300円', '2,640円'],
        ['小5<br>国語', '14:50〜<br>15:30', '3,300円', '2,640円'],
        ['小6<br>英語', '13:20〜<br>14:00', '3,300円', '2,640円'],
        ['小6<br>算数', '14:05〜<br>14:45', '3,300円', '2,640円'],
        ['小6<br>国語', '14:50〜<br>15:30', '3,300円', '2,640円'],
    ], center=False, fs='0.88em', hl_col=3))
    b.append(note('※小5・小6は1教科あたり、40分×4回（合計160分）です。<br>'
                  '※表の時間は基本の時間です。<strong>小6は1/8(金)のみ時間が変わります</strong>（小6の時間割をご覧ください）。<br>'
                  '※12月10日(木)までに、公式LINEで仮押さえした方が<br>右の列の料金になります。<br>お申込みの締切は12月23日(水)です。'))

    # 特典
    b.append('<!-- 特典ここから -->\n')
    b.append(h2('冬の特典', 'BENEFIT'))
    b.append(box(
        p(f'<span style="display:inline-block; padding:0.1em 0.6em; background:{ORANGE}; border-radius:999px; color:#fff; font-size:0.85em; font-weight:bold;">全学年</span><br>'
          f'<strong style="color:{NAVY}; font-size:1.05em;">入会金が半額</strong><br>冬期講習・冬の体験を受けたあとに入会される場合、<br>入会金が半額になります。<br>'
          '<!-- 入会金半額 期限 要確認 --><span style="background:#ffe9a8; color:#a33;">【要確認：入会の期限】</span>', 'margin:0 0 1em;')
        + p(f'<span style="display:inline-block; padding:0.1em 0.6em; background:{ORANGE}; border-radius:999px; color:#fff; font-size:0.85em; font-weight:bold;">小6</span><br>'
            f'<strong style="color:{NAVY}; font-size:1.05em;">中学準備講座の席を優先して確保</strong><br>冬期講習を受けた方は、冬期のあとに予定している<br>中学準備講座の席を優先して確保します。', 'margin:0 0 1em;')
        + p(f'<span style="display:inline-block; padding:0.1em 0.6em; background:{ORANGE}; border-radius:999px; color:#fff; font-size:0.85em; font-weight:bold;">12/10(木)まで</span><br>'
            f'<strong style="color:{NAVY}; font-size:1.05em;">早期申込の料金</strong><br>12月10日(木)までに公式LINEで仮押さえすると、<br>料金一覧の右の列の金額になります。', 'margin:0;'),
        'cream'))
    b.append('<!-- 特典ここまで -->\n')

    b.append(zanseki())

    # 申込の流れ
    b.append(h2('お申込みの流れ', 'FLOW'))
    b.append(steps([
        ('公式LINEにメッセージを送信', '各学年の欄にある文面を送ってください。'),
        ('教室から日程のご連絡・席の仮押さえ', 'キッズは、コマの空き状況もお伝えします。<br>12月10日(木)までに仮押さえした方は、<br>早期申込の料金になります。'),
        ('窓口に来ていただく時間を予約', '公式LINEから予約できます。'),
        ('窓口で手続き', '講習料・体験料のお支払いと、<br>申込用紙のご記入で、お申込み完了です。<br>仮押さえから1週間以内にお越しください。'),
    ]))
    b.append(note('※仮押さえから1週間以内でも、窓口での手続きは<br>12月23日(水)までです。<br>※パーティーに参加する方は、12月19日(土)までに手続きしてください。'))
    b.append(kakutei('窓口でのお支払いと申込用紙のご記入をもって、<br>お申込み完了となります。', '完了'))

    b.append(h2('よくある質問', 'Q&amp;A'))
    b.append(faq([
        ('ComPassに通っていなくても参加できますか？', 'はい。初めての方も参加できます。<br>クリスマスパーティーも、通っているかどうかを問わず参加できます。'),
        ('1教科だけでも受けられますか？', 'はい。小5・小6は1教科から受講できます。'),
        ('キッズのコマは、どうやって選びますか？', '開講日の表の中から、4コマを選んでください。<br>LINEをいただいたあと、空き状況を確認してご連絡します。'),
        ('12月10日と12月23日は、何が違いますか？', '12月10日(木)は、公式LINEで仮押さえすると<br>早期申込の料金になる期限です。<br>12月23日(水)は、窓口での手続きの締切です。'),
        ('窓口には、いつ行けばいいですか？', '公式LINEから、窓口に来ていただく時間を予約してください。<br>仮押さえから1週間以内にお越しください。'),
        ('パーティーだけの参加はできますか？', 'パーティーは、冬期講習・冬の体験のお申込みをされた小学生が対象です。<br>12月19日(土)までに、窓口での手続きを終えてください。'),
    ]))

    b.append(h2('基本情報', 'INFO'))
    b.append(kv_table([
        ('締切', '12月23日(水)まで<br>（窓口での手続き）'),
        ('場所', '学習塾ComPass<br>（松山市来住町230-1）'),
        ('休塾日', '12/24(木)<br>12/27(日)<br>12/29(火)〜1/3(日)'),
    ]))

    # 最後のCTA
    b.append(
        f'<div style="margin:2.4em 0 0; padding:1.5em 1em 1.3em; background:{BLUE_L}; border-radius:18px; text-align:center;">'
        + dots() +
        f'<p style="margin:0 0 0.2em; color:{NAVY}; font-size:1.15em; font-weight:bold;">公式LINEからお申込みください</p>'
        f'<p style="margin:0 0 0.8em; color:{TEXT}; font-size:0.95em;">窓口での手続きは12月23日(水)までです。</p>'
        + small_line_btn('公式LINEで申し込む')
        + msg_list([('小6', '小6 冬期講習 申込希望'), ('小5', '小5 冬期講習 申込希望'), ('キッズ', 'キッズ 冬休み体験 申込希望')])
        + '</div>')

    b.append(footer('中学生の方へ：', '3学期スタート 2週間体験（中1・中2）のご案内はこちら'))
    return wrap('\n'.join(b))


# =====================================================================
# 記事2：中学生
# =====================================================================
def trial_table(dates, skip):
    rows = [[d, '○', '―' if d in skip else '○'] for d in dates]
    rows.append(['回数', '6回', '4回'])
    return grid_table(['日付', '5教科<br>（英数国理社）', '3教科<br>（英数国）'], rows)


def article2():
    b = []
    b.append(hero('3学期スタート｜中1・中2',
                  '3学期スタート<br>2週間体験',
                  '2学期の期末テスト、<br>おつかれさまでした。<br>3学期は、新しい単元に入る区切りです。<br>このタイミングから、<br>ふだんの授業に合流してみませんか。',
                  [('対象', '中1・中2'), ('体験', '1/14〜'), ('受付', '1/13(水)まで')]))

    b.append(h2('こんな方に', 'FOR YOU'))
    chk = ''.join(
        f'<li style="list-style:none; position:relative; margin:0.5em 0; padding-left:1.8em;">'
        f'<span style="position:absolute; left:0; top:0.15em; width:1.25em; height:1.25em; border-radius:50%; background:{BLUE}; color:#fff; font-size:0.8em; line-height:1.25em; text-align:center; font-weight:bold;">✓</span>{t}</li>'
        for t in ['2学期に「分かったつもり」で通り過ぎたところがある',
                  'テストの点数だけでなく、<br>勉強の進め方そのものを見直したい',
                  '部活と両立できる時間帯で通いたい'])
    b.append(box(f'<ul style="margin:0; padding:0;">{chk}</ul>', 'white'))
    b.append(p('2学期に通り過ぎたところは、<br>3学期や学年末テストに持ち越されやすくなります。<br>'
               'ComPassでは、解き方だけでなく、<br>ワークの直し方や、計算の途中式の書き方など、<br>勉強の進め方から伝えています。'))

    b.append(h2('なぜ冬期講習ではなく、3学期からなのか', 'WHY'))
    b.append(p('ComPassの冬期講習は、<br>塾生がすでに習った単元の復習が中心です。<br>初めての方がいきなり入ると、<br>授業についていくのがむずかしくなってしまいます。'))
    b.append(box(p(f'<strong style="color:{NAVY};">そこで外部の方には、<br>3学期のスタートからの体験を<br>おすすめしています。</strong><br>'
                   '新しい単元に入るところから、<br>塾生と同じ授業を受けるので、<br>無理なく合流していただけます。', 'margin:0;'), 'blue'))
    b.append(p('体験は、3学期の最初の授業（模試の直し）が<br>終わったあとから始まります。'))

    b.append(p(f'<strong style="color:{NAVY};">学年を選んでください。</strong><br>押すと、日程・料金・相談ボタンへ移動します。', 'margin:1.6em 0 0.2em;'))
    b.append(cards(
        grade_card('trial-chu1', '中1', '2週間体験', ['火・木・土 19:30〜21:55', '1/14(木)スタート'], ORANGE),
        grade_card('trial-chu2', '中2', '2週間体験', ['月・火・金 19:30〜21:55', '1/15(金)スタート'], BLUE),
    ))

    # 中1
    b.append(h2('中1｜3学期スタート 2週間体験', 'GRADE 1', 'trial-chu1'))
    b.append(p('2学期でつまずいたところを確かめながら、<br>ふだんの授業で、勉強の進め方を体験してください。'))
    b.append(p('授業は部活動が終わったあとの時間帯です。<br>食事をとってから参加できます。'))
    b.append(h3('授業の曜日と時間'))
    b.append(kv_table([
        ('火曜日', '英語・国語・数学'),
        ('木曜日', '数学・英語・英数テスト'),
        ('土曜日', '理科・社会・理社テスト'),
        ('時間', '19:30〜21:55'),
    ]))
    b.append(h3('2週間体験の日程'))
    b.append(p(f'<strong style="color:{NAVY};">1月14日(木)スタート</strong>です。', 'margin:0 0 0.6em;'))
    b.append(trial_table(['1/14(木)', '1/16(土)', '1/19(火)', '1/21(木)', '1/23(土)', '1/26(火)'], {'1/16(土)', '1/23(土)'}))
    b.append(note('※3教科の場合は、理社の日（土曜日）を除いた4回です。<br>※3学期の最初の授業（1/9・1/12）は模試の直しのため、<br>体験は1/14(木)からになります。'))
    b.append(h3('2週間体験の料金'))
    b.append(grid_table(['受講教科', '料金'], [
        ['5教科（英数国理社）', '5,500円（税込）'],
        ['3教科（英数国）', '4,400円（税込）'],
    ], center=False, fs='0.95em'))
    b.append(line_btn('中1｜LINEで相談する', '中1 3学期体験 相談希望', '中1の2週間体験は、こちらからご相談ください。'))

    # 中2
    b.append(h2('中2｜3学期スタート 2週間体験', 'GRADE 2', 'trial-chu2'))
    b.append(p('中2も、3学期のスタートから体験を受け付けます。<br>授業の進め方は中1と同じです。'))
    b.append(kv_table([
        ('曜日', '月・火・金'),
        ('時間', '19:30〜21:55'),
        ('料金', '5教科（英数国理社）5,500円（税込）<br>3教科（英数国）4,400円（税込）'),
    ]))
    b.append(p(f'<strong style="color:{NAVY};">1月15日(金)スタート</strong>です。', 'margin:0 0 0.6em;'))
    b.append(trial_table(['1/15(金)', '1/18(月)', '1/19(火)', '1/22(金)', '1/25(月)', '1/26(火)'], {'1/19(火)', '1/26(火)'}))
    b.append(note('※3教科の場合は、理社の日（火曜日）を除いた4回です。<br>※3学期の最初の授業（1/11・1/12）は模試の直しのため、<br>体験は1/15(金)からになります。'))
    b.append(line_btn('中2｜LINEで相談する', '中2 3学期体験 相談希望', '中2の2週間体験は、こちらからご相談ください。'))

    # 大切にしていること
    b.append(h2('ComPassが大切にしていること', 'POLICY'))
    pol = [('勉強の仕方そのものを渡す', '解き方だけでなく、直し方や進め方まで伝えます。'),
           ('1学年1クラスの少人数制', '分からないところは、その場で聞けます。'),
           ('やり切るための厳しさも', '定期テストの前などは、<br>やり切るための厳しさも大切にしています。')]
    b.append(''.join(
        f'<div style="margin:0.7em 0; padding:0.9em 1em; background:#ffffff; border:1px solid {BLUE_B}; border-left:5px solid {c}; border-radius:10px;">'
        f'<span style="display:block; color:{NAVY}; font-weight:bold;">{t}</span><span style="display:block; font-size:0.95em;">{d}</span></div>'
        for (t, d), c in zip(pol, [BLUE, ORANGE, BLUE])))

    # 流れ
    b.append(h2('体験までの流れ', 'FLOW'))
    b.append(steps([
        ('公式LINEでご相談', '1月13日(水)まで受け付けます。'),
        ('今の学習状況の確認', '教室から日程をご連絡し、今の学習状況を<br>確認させていただきます。<br>（学校の進み具合や、2学期の定期テストの答案など）'),
        ('2週間体験', '3学期のスタートから2週間、<br>ふだんの授業で体験していただきます。'),
        ('体験の最後に面談', ''),
    ]))
    b.append(note('※冬期講習の期間中（12/25〜1/8）は、<br>ご連絡が遅れることがあります。'))
    b.append(note('※確認の結果によっては、春の新学年からのスタートを<br>おすすめすることがあります。'))
    b.append(kakutei('学習状況の確認のあと、教室からのご連絡をもって、<br>お申込みの確定となります。'))

    b.append('<!-- 特典ここから -->\n')
    b.append(h2('体験のあとの特典', 'BENEFIT'))
    b.append(box(p(f'<strong style="color:{NAVY}; font-size:1.05em;">入会金が半額</strong><br>3学期の2週間体験を受けたあとに入会される場合、<br>入会金が半額になります。<br>'
                   '<!-- 入会金半額 期限 要確認 --><span style="background:#ffe9a8; color:#a33;">【要確認：入会の期限】</span>', 'margin:0;'), 'cream'))
    b.append('<!-- 特典ここまで -->\n')

    b.append(zanseki())

    b.append(h2('よくある質問', 'Q&amp;A'))
    b.append(faq([
        ('冬期講習には参加できませんか？', '冬期講習は、塾生がすでに習った単元の復習が中心です。<br>外部の方には、無理なく合流できる3学期のスタートからの体験をおすすめしています。'),
        ('3教科だけでも体験できますか？', 'はい。3教科（英数国）の場合は、理社の日を除いた4回です。<br>料金は4,400円（税込）です。'),
        ('部活があっても通えますか？', '授業は19:30〜21:55です。<br>部活動が終わったあとの時間帯なので、食事をとってから参加できます。'),
        ('相談したら、すぐ体験が決まりますか？', '先に、今の学習状況を確認させていただきます。<br>確認の結果によっては、春の新学年からのスタートをおすすめすることがあります。'),
    ]))

    b.append(h2('基本情報', 'INFO'))
    b.append(kv_table([
        ('受付', '1月13日(水)まで'),
        ('場所', '学習塾ComPass<br>（松山市来住町230-1）'),
    ]))

    b.append(
        f'<div style="margin:2.4em 0 0; padding:1.5em 1em 1.3em; background:{BLUE_L}; border-radius:18px; text-align:center;">'
        + dots() +
        f'<p style="margin:0 0 0.2em; color:{NAVY}; font-size:1.15em; font-weight:bold;">まずはLINEでご相談ください</p>'
        f'<p style="margin:0 0 0.8em; color:{TEXT}; font-size:0.95em;">受付は1月13日(水)までです。</p>'
        + small_line_btn('公式LINEで相談する')
        + msg_list([('中1', '中1 3学期体験 相談希望'), ('中2', '中2 3学期体験 相談希望')])
        + '</div>')

    b.append(footer('小学生の方へ：', '冬期講習・冬の体験（小1〜小6）のご案内はこちら'))
    return wrap('\n'.join(b))


def preview(a, b):
    def strip(s):
        return s.replace('<!-- wp:html -->', '').replace('<!-- /wp:html -->', '')
    return f'''<!doctype html>
<html lang="ja"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>冬〜3学期 記事プレビュー</title>
<style>
body{{margin:0;background:#e6ebf0;font-family:"Hiragino Sans","Noto Sans JP",sans-serif;}}
.bar{{position:sticky;top:0;z-index:10;background:{NAVY};color:#fff;padding:10px 16px;display:flex;flex-wrap:wrap;gap:8px;align-items:center;font-size:14px;}}
.bar button{{border:0;border-radius:4px;padding:6px 12px;cursor:pointer;background:#fff;color:{NAVY};font-weight:bold;}}
.bar button.on{{background:{YELLOW};}}
.frame{{margin:24px auto;background:#fff;padding:24px 16px;box-sizing:border-box;box-shadow:0 1px 6px rgba(0,0,0,.15);}}
.frame h1{{font-size:20px;color:{NAVY};margin:0 0 8px;}}
.label{{font-size:12px;color:#888;margin:0 0 16px;}}
.w375 .frame{{width:375px;}} .wfull .frame{{max-width:1000px;}}
</style></head>
<body class="w375">
<div class="bar">表示幅：
<button id="b375" class="on" onclick="setW('w375')">スマホ 375px</button>
<button id="bfull" onclick="setW('wfull')">PC</button>
<span style="margin-left:auto">記事1 → 記事2 の順に並んでいます</span></div>
<div class="frame"><p class="label">記事1｜post_shogakusei.html</p><h1>2026 学習塾ComPass 冬期講習・冬の体験｜小1〜小6募集のご案内</h1>
{strip(a)}
</div>
<div class="frame"><p class="label">記事2｜post_chugakusei.html</p><h1>2026 学習塾ComPass 3学期スタート 2週間体験｜中1・中2募集のご案内</h1>
{strip(b)}
</div>
<script>function setW(c){{document.body.className=c;document.getElementById('b375').className=c=='w375'?'on':'';document.getElementById('bfull').className=c=='wfull'?'on':'';}}</script>
</body></html>
'''


if __name__ == '__main__':
    a, b = article1(), article2()
    (D / 'post_shogakusei.html').write_text(a, encoding='utf-8')
    (D / 'post_chugakusei.html').write_text(b, encoding='utf-8')
    (D / 'preview.html').write_text(preview(a, b), encoding='utf-8')
    for n, s in [('1', a), ('2', b)]:
        print(n, len(s.encode()) // 1024, 'KB')
