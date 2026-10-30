# 理科1年 単元2「身のまわりの物質」の図（モノトーン）
# 使い方: python3 figs.py   → img/ にPNGを書き出す
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon, Circle, Ellipse, FancyBboxPatch
import numpy as np
import random
plt.rcParams["font.family"] = ["IPAGothic"]
OUT = "img/"
K = "k"


def save(fig, name):
    fig.savefig(OUT + name, dpi=220, bbox_inches="tight", pad_inches=0.04, facecolor="white")
    plt.close(fig)


def blank(w, h, xlim, ylim):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


# ---------- メスシリンダー（物体を入れる前・後） ----------
def cylinder(ax, x0, level, label, obj=False, top=None):
    # 目盛り 1cm³ ごと、50～60 を拡大して描く。y = (目盛り-50)*0.5
    W = 1.6
    yl = (level - 50) * 0.5
    ax.add_patch(Rectangle((x0, -0.6), W, yl + 0.6, facecolor="#DDDDDD", edgecolor="none", zorder=1))
    ax.plot([x0, x0], [-0.6, 6.2], color=K, lw=1.4); ax.plot([x0 + W, x0 + W], [-0.6, 6.2], color=K, lw=1.4)
    ax.plot([x0, x0 + W], [yl, yl], color=K, lw=1.0, zorder=3)
    for v in range(50, 62):
        y = (v - 50) * 0.5
        L = 0.55 if v % 5 == 0 else 0.3
        ax.plot([x0, x0 + L], [y, y], color=K, lw=0.9, zorder=4)
        if v in (50, 55, 60):
            ax.text(x0 - 0.15, y, str(v), ha="right", va="center", fontsize=11)
    if obj:
        ax.add_patch(Rectangle((x0 + 0.95, -0.5), 0.45, 0.7, facecolor="#777777", edgecolor=K, zorder=5))
        ax.plot([x0 + 1.175, x0 + 1.175], [0.2, 6.6], color=K, lw=0.8, zorder=5)
        ax.text(x0 + 1.3, 6.65, "糸", ha="left", va="bottom", fontsize=10)
        ax.text(x0 + W + 0.15, -0.15, "物体X", ha="left", va="center", fontsize=10)
    ax.text(x0 + W / 2, -1.1, label, ha="center", va="top", fontsize=11)


def fig_mess():
    fig, ax = blank(3.6, 3.0, (-1.2, 7.4), (-2.0, 7.2))
    cylinder(ax, 0.0, 50.0, "入れる前")
    ax.annotate("", xy=(3.3, 2.6), xytext=(2.3, 2.6), arrowprops=dict(arrowstyle="-|>", color=K, lw=1.2))
    cylinder(ax, 4.4, 56.0, "入れた後", obj=True)
    save(fig, "mess.png")


# ---------- ガスバーナー ----------
def fig_burner():
    fig, ax = blank(2.2, 3.2, (-2.4, 2.6), (-0.6, 7.0))
    ax.add_patch(Polygon([(-1.6, 0), (1.6, 0), (1.1, 0.7), (-1.1, 0.7)], closed=True, facecolor="white", edgecolor=K, lw=1.3))
    ax.add_patch(Rectangle((-0.35, 0.7), 0.7, 5.3, facecolor="white", edgecolor=K, lw=1.3))  # 筒
    # 下のねじ（ガス）・上のねじ（空気）
    ax.add_patch(Rectangle((-0.6, 1.5), 1.2, 0.55, facecolor="#BBBBBB", edgecolor=K, lw=1.2))
    ax.add_patch(Rectangle((-0.55, 2.6), 1.1, 0.75, facecolor="#E5E5E5", edgecolor=K, lw=1.2))
    for yy in (2.75, 2.95, 3.15):
        ax.plot([-0.55, 0.55], [yy, yy], color=K, lw=0.6)
    # ガス管・コック
    ax.plot([0.6, 2.0], [1.0, 1.0], color=K, lw=1.3); ax.plot([0.6, 2.0], [1.3, 1.3], color=K, lw=1.3)
    ax.add_patch(Rectangle((1.25, 1.3), 0.3, 0.45, facecolor="white", edgecolor=K, lw=1.1))
    ax.plot([0.35, 0.6], [1.0, 1.0], color=K, lw=1.3); ax.plot([0.35, 0.6], [1.3, 1.3], color=K, lw=1.3)
    ax.text(1.7, 2.0, "コック", ha="left", va="center", fontsize=9)
    # 引き出し線（文字は線の外）
    ax.plot([-0.6, -1.4], [2.98, 3.6], color=K, lw=0.8); ax.text(-1.5, 3.65, "A", ha="right", va="center", fontsize=13)
    ax.plot([-0.6, -1.4], [1.78, 1.2], color=K, lw=0.8); ax.text(-1.5, 1.15, "B", ha="right", va="center", fontsize=13)
    save(fig, "burner.png")


# ---------- 気体の集め方（3つ） ----------
def tube(ax, x, ybot, ytop, w=0.55, up=True, fill=None):
    # 試験管（up=True:口が下＝水上・上方, up=False:口が上＝下方）
    if up:
        ax.plot([x - w / 2, x - w / 2], [ybot, ytop - w / 2], color=K, lw=1.2)
        ax.plot([x + w / 2, x + w / 2], [ybot, ytop - w / 2], color=K, lw=1.2)
        t = np.linspace(0, np.pi, 30); ax.plot(x + w / 2 * np.cos(t), ytop - w / 2 + w / 2 * np.sin(t), color=K, lw=1.2)
    else:
        ax.plot([x - w / 2, x - w / 2], [ybot + w / 2, ytop], color=K, lw=1.2)
        ax.plot([x + w / 2, x + w / 2], [ybot + w / 2, ytop], color=K, lw=1.2)
        t = np.linspace(np.pi, 2 * np.pi, 30); ax.plot(x + w / 2 * np.cos(t), ybot + w / 2 + w / 2 * np.sin(t), color=K, lw=1.2)


def fig_atsume():
    fig, ax = blank(6.2, 2.6, (-0.3, 13.4), (-1.6, 4.4))
    # 水上置換法
    ax.add_patch(Rectangle((0, 0), 3.6, 1.6, facecolor="#DDDDDD", edgecolor="none"))
    ax.plot([0, 0, 3.6, 3.6], [2.2, 0, 0, 2.2], color=K, lw=1.3)
    ax.add_patch(Rectangle((2.15, 0.6), 0.55, 1.0, facecolor="#DDDDDD", edgecolor="none", zorder=2))
    tube(ax, 2.43, 0.6, 3.6)
    ax.plot([0.3, 1.9, 1.9], [3.0, 3.0, 0.9], color=K, lw=1.2)
    ax.plot([1.9, 2.3], [0.9, 0.9], color=K, lw=1.2)
    ax.text(1.0, 0.75, "水", ha="center", va="center", fontsize=10)
    ax.text(1.8, -0.5, "水上置換法", ha="center", va="top", fontsize=11)
    # 上方置換法
    tube(ax, 6.6, 0.4, 3.6)
    ax.plot([5.2, 6.6, 6.6], [0.0, 0.0, 3.1], color=K, lw=1.2)
    ax.text(6.6, -0.5, "上方置換法", ha="center", va="top", fontsize=11)
    # 下方置換法
    tube(ax, 11.0, 0.0, 3.2, up=False)
    ax.plot([9.6, 11.0, 11.0], [4.0, 4.0, 0.6], color=K, lw=1.2)
    ax.text(11.0, -0.5, "下方置換法", ha="center", va="top", fontsize=11)
    save(fig, "atsume.png")


# ---------- 溶解度曲線 ----------
T = [0, 10, 20, 40, 60, 80]
KNO3 = [13.3, 22.0, 31.6, 63.9, 109.2, 168.8]
NACL = [37.6, 37.7, 37.8, 38.3, 39.0, 40.0]


def smooth(xs, ys):
    xx = np.linspace(xs[0], xs[-1], 200)
    # 単調な3次エルミート（行き過ぎない）
    from numpy import interp
    xs, ys = np.array(xs, float), np.array(ys, float)
    d = np.diff(ys) / np.diff(xs)
    m = np.r_[d[0], (d[:-1] + d[1:]) / 2, d[-1]]
    out = []
    for x in xx:
        i = min(np.searchsorted(xs, x, side="right") - 1, len(xs) - 2)
        h = xs[i + 1] - xs[i]; t = (x - xs[i]) / h
        h00, h10, h01, h11 = 2*t**3-3*t**2+1, t**3-2*t**2+t, -2*t**3+3*t**2, t**3-t**2
        out.append(h00*ys[i] + h10*h*m[i] + h01*ys[i+1] + h11*h*m[i+1])
    return xx, np.array(out)


def sol_axes(ax):
    ax.set_xlim(0, 80); ax.set_ylim(0, 180)
    ax.set_xticks(range(0, 81, 20)); ax.set_yticks(range(0, 181, 20))
    ax.set_xticks(range(0, 81, 10), minor=True); ax.set_yticks(range(0, 181, 10), minor=True)
    ax.grid(which="both", color="#BBBBBB", lw=0.5)
    ax.tick_params(labelsize=9)
    ax.set_xlabel("水の温度〔℃〕", fontsize=10)
    ax.set_ylabel("100gの水にとける物質の質量〔g〕", fontsize=9)
    x, y = smooth(T, np.log(KNO3)); y = np.exp(y); ax.plot(x, y, color=K, lw=1.8)
    x, y = smooth(T, NACL); ax.plot(x, y, color=K, lw=1.8, ls="--")
    ax.text(47, 112, "硝酸カリウム", fontsize=10, ha="right", va="center", bbox=dict(fc="white", ec="none", pad=1))
    ax.text(78, 29, "塩化ナトリウム", fontsize=10, ha="right", va="center", bbox=dict(fc="white", ec="none", pad=1))


def fig_youkaido():
    fig, ax = plt.subplots(figsize=(3.3, 3.0))
    sol_axes(ax)
    save(fig, "youkaido.png")


def fig_youkaido_ans(m=80, name="youkaido_ans.png"):
    fig, ax = plt.subplots(figsize=(3.5, 3.1))
    sol_axes(ax)
    # 60℃でm gとかした → 20℃に冷やす（点で止める）
    ax.plot([60], [m], "o", color=K, ms=5, zorder=5)
    ax.plot([20], [m], "o", color=K, ms=5, mfc="white", zorder=5)
    ax.plot([20], [31.6], "o", color=K, ms=5, zorder=5)
    ax.annotate("", xy=(21.5, m), xytext=(58.5, m), arrowprops=dict(arrowstyle="-|>", color=K, lw=1.2))
    ax.text(31, m + 3, "冷やす", ha="center", va="bottom", fontsize=9, bbox=dict(fc="white", ec="none", pad=1))
    ax.plot([20, 20], [33, m - 1.5], color=K, lw=2.4)
    ax.text(18, (m + 31.6) / 2 + 6, f"結晶\n{m - 31.6:.1f}g", ha="right", va="center", fontsize=8.5, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(22, 22, "31.6g", ha="left", va="center", fontsize=8.5, bbox=dict(fc="white", ec="none", pad=1))
    ax.text(60, m + 4, f"{m}g", ha="center", va="bottom", fontsize=8.5, bbox=dict(fc="white", ec="none", pad=1))
    save(fig, name)


# ---------- 水を加熱したときの温度変化 ----------
def fig_water():
    fig, ax = plt.subplots(figsize=(3.6, 2.5))
    xs = [0, 2, 5, 9, 15, 18]; ys = [-20, 0, 0, 100, 100, 125]
    ax.plot(xs, ys, color=K, lw=1.8)
    ax.set_xlim(0, 18); ax.set_ylim(-30, 135)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ("top", "right"): ax.spines[s].set_visible(False)
    ax.plot([0, 2], [0, 0], color=K, lw=0.7, ls=":"); ax.plot([0, 9], [100, 100], color=K, lw=0.7, ls=":")
    ax.text(-0.4, 0, "X", ha="right", va="center", fontsize=11)
    ax.text(-0.4, 100, "Y", ha="right", va="center", fontsize=11)
    ax.text(3.5, 9, "A", ha="center", va="bottom", fontsize=11)
    ax.text(12, 109, "B", ha="center", va="bottom", fontsize=11)
    ax.set_xlabel("加熱した時間", fontsize=10); ax.set_ylabel("温度〔℃〕", fontsize=10)
    save(fig, "water.png")


# ---------- 粒子のモデル（ア 固体／イ 液体／ウ 気体 を並べかえて使う） ----------
def box_particles(ax, x0, kind, label, rnd):
    ax.add_patch(Rectangle((x0, 0), 3.0, 3.0, facecolor="white", edgecolor=K, lw=1.2))
    r = 0.17
    if kind == "solid":
        pts = [(x0 + 0.9 + i * 0.4, 0.3 + j * 0.4) for i in range(4) for j in range(4)]
    elif kind == "liquid":
        pts = [(x0 + 0.5 + i * 0.62 + rnd.uniform(-0.1, 0.1), 0.35 + j * 0.42 + rnd.uniform(-0.06, 0.06)) for i in range(4) for j in range(4)]
    else:
        pts = [(x0 + 0.42 + i * 0.72 + rnd.uniform(-0.18, 0.18), 0.42 + j * 0.72 + rnd.uniform(-0.18, 0.18)) for i in range(4) for j in range(4)]
    for p in pts:
        ax.add_patch(Circle(p, r, facecolor="#888888", edgecolor=K, lw=0.6))
    ax.text(x0 + 1.5, -0.25, label, ha="center", va="top", fontsize=12)


def fig_ryuushi(kinds=("liquid", "gas", "solid"), labels=("ア", "イ", "ウ"), name="ryuushi.png"):
    rnd = random.Random(3)
    fig, ax = blank(4.6, 1.9, (-0.2, 11.4), (-1.0, 3.2))
    for i, (k, lb) in enumerate(zip(kinds, labels)):
        box_particles(ax, 4.1 * i, k, lb, rnd)
    save(fig, name)


# ---------- 水溶液の粒子モデル（ビーカー3つ） ----------
def beaker(ax, x0, mode, label, rnd):
    ax.plot([x0, x0, x0 + 2.4, x0 + 2.4], [3.0, 0, 0, 3.0], color=K, lw=1.3)
    ax.plot([x0, x0 + 2.4], [2.5, 2.5], color=K, lw=0.8)
    lo, hi = {"bottom": (0.18, 0.75), "even": (0.25, 2.2), "top": (1.8, 2.35)}[mode]
    rows = 3 if mode != "even" else 4
    cols = 7 if mode != "even" else 5
    pts = [(x0 + 0.3 + i * (1.8 / (cols - 1)) + rnd.uniform(-0.06, 0.06),
            lo + j * ((hi - lo) / (rows - 1)) + rnd.uniform(-0.04, 0.04)) for i in range(cols) for j in range(rows)][:20]
    for p in pts:
        ax.add_patch(Circle(p, 0.11, facecolor="#666666", edgecolor=K, lw=0.5))
    ax.text(x0 + 1.2, -0.25, label, ha="center", va="top", fontsize=12)


def fig_model():
    rnd = random.Random(7)
    fig, ax = blank(4.4, 1.9, (-0.2, 9.8), (-1.0, 3.2))
    beaker(ax, 0, "bottom", "ア", rnd)
    beaker(ax, 3.6, "even", "イ", rnd)
    beaker(ax, 7.2, "top", "ウ", rnd)
    save(fig, "model.png")


# ---------- 蒸留の装置 ----------
def fig_jouryuu():
    fig, ax = blank(4.0, 3.2, (-3.2, 8.6), (-0.8, 8.4))
    # 枝つきフラスコ
    t = np.linspace(0, 2 * np.pi, 80)
    ax.add_patch(Circle((0, 2.6), 1.2, facecolor="white", edgecolor=K, lw=1.3, zorder=2))
    ax.add_patch(Polygon([(-1.05, 2.0), (1.05, 2.0), (0.95, 1.85), (0.7, 1.6), (0, 1.4), (-0.7, 1.6), (-0.95, 1.85)], facecolor="#DDDDDD", edgecolor="none", zorder=3))
    ax.add_patch(Rectangle((-0.3, 3.7), 0.6, 2.4, facecolor="white", edgecolor=K, lw=1.3, zorder=3))
    ax.add_patch(Rectangle((-0.27, 3.6), 0.54, 0.3, facecolor="white", edgecolor="none", zorder=4))
    # 枝（首の途中から右下へ）
    ax.plot([0.3, 5.6], [5.2, 2.4], color=K, lw=1.3, zorder=3)
    ax.plot([0.3, 5.6], [4.9, 2.1], color=K, lw=1.3, zorder=3)
    # 温度計（球部は枝の高さ）
    ax.add_patch(Rectangle((-0.07, 4.95), 0.14, 3.0, facecolor="white", edgecolor=K, lw=1.0, zorder=5))
    ax.add_patch(Circle((0, 4.95), 0.13, facecolor="#555555", edgecolor=K, lw=0.8, zorder=6))
    # 沸騰石
    for p in [(-0.35, 1.75), (0.15, 1.65), (0.45, 1.8)]:
        ax.add_patch(Circle(p, 0.09, facecolor="#333333", zorder=4))
    # 試験管と冷水
    ax.add_patch(Rectangle((4.6, -0.4), 2.6, 2.6, facecolor="#E8E8E8", edgecolor="none", zorder=1))
    ax.plot([4.6, 4.6, 7.2, 7.2], [3.0, -0.4, -0.4, 3.0], color=K, lw=1.2, zorder=2)
    tube(ax, 5.9, -0.2, 3.4, w=0.6, up=False)
    ax.add_patch(Rectangle((5.62, -0.1), 0.56, 0.6, facecolor="#999999", edgecolor="none", zorder=1.5))
    # ガスバーナー（簡略）
    ax.add_patch(Rectangle((-0.25, -0.6), 0.5, 1.2, facecolor="white", edgecolor=K, lw=1.1))
    ax.add_patch(Polygon([(-0.18, 0.62), (0.18, 0.62), (0, 1.25)], facecolor="#BBBBBB", edgecolor=K, lw=0.8))
    # ラベル（引き出し線は文字の手前で止める）
    ax.plot([0.1, 1.2], [7.4, 7.4], color=K, lw=0.7); ax.text(1.3, 7.4, "温度計", ha="left", va="center", fontsize=9)
    ax.plot([0.35, 1.6], [5.75, 6.4], color=K, lw=0.7); ax.text(1.7, 6.45, "枝つきフラスコ", ha="left", va="center", fontsize=9)
    ax.plot([-1.1, -1.9], [3.0, 3.6], color=K, lw=0.7); ax.text(-2.0, 3.7, "水と\nエタノール\nの混合物", ha="right", va="bottom", fontsize=8.5)
    ax.plot([-0.3, -1.6], [1.7, 1.0], color=K, lw=0.7); ax.text(-1.7, 0.95, "沸騰石", ha="right", va="center", fontsize=9)
    ax.plot([3.5, 3.9], [3.5, 4.3], color=K, lw=0.7); ax.text(3.95, 4.4, "ガラス管", ha="left", va="bottom", fontsize=9)
    ax.plot([7.2, 7.6], [1.0, 1.0], color=K, lw=0.7); ax.text(7.65, 1.0, "水", ha="left", va="center", fontsize=9)
    save(fig, "jouryuu.png")


# ---------- エタノールの加熱（宿題の作図） ----------
ETH = [(0, 20.0), (1, 40.5), (2, 62.0), (3, 78.0), (4, 78.0), (5, 78.0), (6, 78.0)]


def eth_axes(ax):
    ax.set_xlim(0, 6); ax.set_ylim(0, 100)
    ax.set_xticks(range(0, 7)); ax.set_yticks(range(0, 101, 20))
    ax.set_yticks(range(0, 101, 10), minor=True); ax.set_xticks(np.arange(0, 6.01, 0.5), minor=True)
    ax.grid(which="both", color="#BBBBBB", lw=0.5)
    ax.tick_params(labelsize=9)
    ax.set_xlabel("加熱した時間〔分〕", fontsize=10); ax.set_ylabel("温度〔℃〕", fontsize=10)


def fig_eth():
    fig, ax = plt.subplots(figsize=(3.4, 2.6)); eth_axes(ax); save(fig, "eth_grid.png")
    fig, ax = plt.subplots(figsize=(3.4, 2.6)); eth_axes(ax)
    xs, ys = zip(*ETH)
    ax.plot(xs, ys, color=K, lw=1.6)
    ax.plot(xs, ys, "o", color=K, ms=4)
    ax.plot([3, 3], [0, 76.5], color=K, lw=0.9, ls=":")
    ax.text(3.4, 50, "沸騰が始まる\n（約3分後・約78℃）", fontsize=8.5, ha="left", va="center", bbox=dict(fc="white", ec="none", pad=1))
    save(fig, "eth_ans.png")


if __name__ == "__main__":
    fig_mess(); fig_burner(); fig_atsume(); fig_youkaido(); fig_youkaido_ans(); fig_youkaido_ans(60, "youkaido_ans60.png")
    fig_water(); fig_ryuushi(); fig_ryuushi(("solid", "liquid", "gas"), ("固体", "液体", "気体"), "ryuushi_yoten.png"); fig_model(); fig_jouryuu(); fig_eth()
    print("ok")
