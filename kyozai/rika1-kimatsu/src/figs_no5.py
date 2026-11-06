# ミニテストNo.5「気体の発生とその性質」の図をかき直す試作（モノトーン）
# 使い方: python3 figs_no5.py   → img/no5_*.png
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle, Circle, Ellipse
import numpy as np
plt.rcParams["font.family"] = ["IPAGothic"]
OUT = "img/"
K = "k"
LIQ = "#DDDDDD"


def save(fig, name):
    fig.savefig(OUT + name, dpi=220, bbox_inches="tight", pad_inches=0.04, facecolor="white")
    plt.close(fig)


def blank(w, h, xlim, ylim):
    fig, ax = plt.subplots(figsize=(w, h))
    ax.set_xlim(*xlim); ax.set_ylim(*ylim); ax.set_aspect("equal"); ax.axis("off")
    return fig, ax


def rot(pts, ang, ox, oy):
    a = np.radians(ang)
    c, s = np.cos(a), np.sin(a)
    return [(ox + x * c - y * s, oy + x * s + y * c) for x, y in pts]


def tube_outline(L, w, n=24):
    # 試験管：底(0,0)が丸く、口が(0,L)。局所座標
    r = w / 2
    t = np.linspace(np.pi, 2 * np.pi, n)
    bottom = [(r * np.cos(a), r + r * np.sin(a)) for a in t]
    return [(-r, L)] + bottom + [(r, L)]


def testtube(ax, ox, oy, ang=0, L=5.0, w=0.9, liquid=0.0, z=3):
    """ang：鉛直から反時計回りの角度。liquid：底からの液の高さ"""
    pts = rot(tube_outline(L, w), ang, ox, oy)
    ax.add_patch(Polygon(pts, closed=True, facecolor="white", edgecolor="none", zorder=z - 1.5))  # 後ろの線をかくす
    if liquid > 0:
        r = w / 2
        t = np.linspace(np.pi, 2 * np.pi, 24)
        lq = [(-r, liquid)] + [(r * np.cos(a), r + r * np.sin(a)) for a in t] + [(r, liquid)]
        ax.add_patch(Polygon(rot(lq, ang, ox, oy), closed=True, facecolor=LIQ, edgecolor="none", zorder=z - 1))
    xs, ys = zip(*pts)
    ax.plot(xs, ys, color=K, lw=1.3, zorder=z)
    return pts


def glass(ax, path, z=4, rubber=None):
    """ガラス管（黒い太線の上に白い細線を重ねて2本線に見せる）。rubber=(i, j)でゴム管の区間"""
    xs, ys = zip(*path)
    ax.plot(xs, ys, color=K, lw=3.4, zorder=z, solid_capstyle="butt", solid_joinstyle="round")
    ax.plot(xs, ys, color="white", lw=1.5, zorder=z + 0.1, solid_capstyle="butt", solid_joinstyle="round")
    if rubber:
        rx, ry = zip(*rubber)
        ax.plot(rx, ry, color=K, lw=4.2, zorder=z + 0.2, solid_capstyle="round")


def stopper(ax, cx, cy, w=0.95, h=0.55, ang=0, z=5):
    pts = [(-w / 2 + 0.06, 0), (w / 2 - 0.06, 0), (w / 2, h), (-w / 2, h)]
    ax.add_patch(Polygon(rot(pts, ang, cx, cy), closed=True, facecolor="#555555", edgecolor=K, lw=1.0, zorder=z))


def label(ax, txt, xy, at, ha="left", va="center", size=9):
    ax.plot([xy[0], at[0]], [xy[1], at[1]], color=K, lw=0.7, zorder=8)
    ax.text(at[0] + (0.08 if ha == "left" else -0.08), at[1], txt, ha=ha, va=va, fontsize=size, zorder=9)


def stones(ax, cx, cy, n, spread, size=0.16, seed=1, color="#333333"):
    rnd = np.random.RandomState(seed)
    for _ in range(n):
        x = cx + rnd.uniform(-spread, spread); y = cy + rnd.uniform(0, 0.35)
        k = rnd.randint(5, 7)
        a = np.sort(rnd.uniform(0, 2 * np.pi, k))
        pts = [(x + size * (0.7 + 0.3 * rnd.rand()) * np.cos(t), y + size * (0.7 + 0.3 * rnd.rand()) * np.sin(t)) for t in a]
        ax.add_patch(Polygon(pts, closed=True, facecolor=color, edgecolor=K, lw=0.5, zorder=4))


def bubbles(ax, pts, r=0.09):
    for x, y in pts:
        ax.add_patch(Circle((x, y), r, facecolor="white", edgecolor=K, lw=0.6, zorder=6))


# ---------- 1 二酸化炭素（石灰石＋うすい塩酸 → 石灰水） ----------
def fig1():
    fig, ax = blank(3.0, 3.0, (-2.6, 5.4), (-0.6, 7.2))
    # 試験管立て
    ax.plot([-1.0, -1.0, 1.0, 1.0], [-0.3, 1.6, 1.6, -0.3], color=K, lw=1.2, zorder=2)
    ax.plot([-1.2, 1.2], [-0.3, -0.3], color=K, lw=1.4, zorder=2)
    ax.plot([-1.0, 1.0], [1.2, 1.2], color=K, lw=0.8, zorder=2)
    testtube(ax, 0, 0, 0, L=5.0, liquid=2.0)
    stones(ax, 0, 0.12, 6, 0.25, seed=3)
    stopper(ax, 0, 5.0)
    # 石灰水の試験管（右に傾ける）
    ang = 22
    testtube(ax, 4.3, 0.2, ang, L=5.6, liquid=2.4)
    top = rot([(0, 6.3)], ang, 4.3, 0.2)[0]
    deep = rot([(0, 0.7)], ang, 4.3, 0.2)[0]
    glass(ax, [(0, 5.4), (0, 6.45), (top[0] - 0.4, 6.45), top, deep],
          rubber=[(0.9, 6.45), (top[0] - 0.6, 6.45)])
    label(ax, "うすい塩酸", (-0.3, 1.9), (-1.5, 3.3), ha="right")
    label(ax, "石灰石", (-0.2, 0.35), (-1.5, 2.3), ha="right")
    p = rot([(0.2, 1.3)], ang, 4.3, 0.2)[0]
    label(ax, "石灰水", p, (4.9, 3.4))
    save(fig, "no5_1.png")


# ---------- 2 アンモニア（加熱して上方置換法） ----------
def fig2():
    fig, ax = blank(3.4, 3.3, (-4.6, 4.2), (-1.6, 8.4))
    # スタンド
    ax.add_patch(Rectangle((-0.6, -1.4), 2.4, 0.3, facecolor="white", edgecolor=K, lw=1.2))
    ax.plot([0.6, 0.6], [-1.1, 6.0], color=K, lw=2.4, zorder=1)
    # 加熱する試験管（口を少し下げる）
    ang = -95  # ほぼ横向き。底が左、口が少し下（できた水が底に流れないように）
    bot = (-3.6, 3.6)
    testtube(ax, bot[0], bot[1], ang, L=5.3, w=0.95)
    # 中の粉（塩化アンモニウムと水酸化カルシウム）
    for i in range(40):
        rnd = np.random.RandomState(i)
        lx, ly = rnd.uniform(-0.35, 0.05), rnd.uniform(0.3, 2.2)
        x, y = rot([(lx, ly)], ang, *bot)[0]
        ax.add_patch(Circle((x, y), 0.05, facecolor="#666666", edgecolor="none", zorder=4))
    mouth = rot([(0, 5.6)], ang, *bot)[0]
    s0 = rot([(0, 5.0)], ang, *bot)[0]
    stopper(ax, s0[0], s0[1], ang=ang, w=1.0, h=0.6)
    # クランプ
    cy = rot([(0, 4.0)], ang, *bot)[0][1]
    ax.add_patch(Rectangle((0.25, cy - 0.4), 0.7, 0.8, facecolor="#BBBBBB", edgecolor=K, lw=1.0, zorder=5))
    # ガスバーナー
    ax.add_patch(Rectangle((-3.2, -1.4), 0.6, 2.6, facecolor="white", edgecolor=K, lw=1.2, zorder=2))
    ax.add_patch(Polygon([(-3.1, 1.3), (-2.7, 1.3), (-2.9, 2.6)], facecolor="#CCCCCC", edgecolor=K, lw=0.8, zorder=2))
    # 上方置換で集める試験管（口を下）
    up = (3.0, 7.9)
    testtube(ax, up[0], up[1], 180, L=4.4, w=0.9)
    end = (mouth[0] - 0.1, mouth[1])
    glass(ax, [end, (3.0, end[1]), (3.0, 7.3)])
    label(ax, "塩化アンモニウムと\n水酸化カルシウム", rot([(-0.15, 1.2)], ang, *bot)[0], (-4.4, 5.6), ha="left", va="bottom")
    save(fig, "no5_2.png")


# ---------- 三角フラスコ（ろうとつき） ----------
def flask(ax, ox=0, oy=0, cock=True, liquid_label=None):
    body = [(ox - 1.6, oy), (ox + 1.6, oy), (ox + 0.45, oy + 3.0), (ox + 0.45, oy + 3.9), (ox - 0.45, oy + 3.9), (ox - 0.45, oy + 3.0)]
    ax.add_patch(Polygon([(ox - 1.48, oy + 0.08), (ox + 1.48, oy + 0.08), (ox + 1.2, oy + 0.85), (ox - 1.2, oy + 0.85)], facecolor=LIQ, edgecolor="none", zorder=1))
    ax.add_patch(Polygon(body, closed=True, facecolor="none", edgecolor=K, lw=1.3, zorder=3))
    stopper(ax, ox, oy + 3.75, w=1.05, h=0.6)
    # ろうと（コックつき）
    ax.plot([ox - 0.12, ox - 0.12], [oy + 0.5, oy + 5.6], color=K, lw=1.0, zorder=4)
    ax.plot([ox + 0.12, ox + 0.12], [oy + 0.5, oy + 5.6], color=K, lw=1.0, zorder=4)
    if cock:
        ax.add_patch(Rectangle((ox - 0.5, oy + 5.0), 1.0, 0.25, facecolor="white", edgecolor=K, lw=1.0, zorder=5))
        ax.plot([ox - 0.85, ox - 0.5], [oy + 5.12, oy + 5.12], color=K, lw=1.8, zorder=5)
    cup = [(ox - 0.12, oy + 5.6), (ox - 0.9, oy + 6.6), (ox - 0.9, oy + 7.1), (ox + 0.9, oy + 7.1), (ox + 0.9, oy + 6.6), (ox + 0.12, oy + 5.6)]
    ax.add_patch(Polygon([(ox - 0.12, oy + 5.6), (ox - 0.8, oy + 6.5), (ox + 0.8, oy + 6.5), (ox + 0.12, oy + 5.6)], facecolor=LIQ, edgecolor="none", zorder=3))
    xs, ys = zip(*cup); ax.plot(xs, ys, color=K, lw=1.2, zorder=4)
    return (ox + 0.25, oy + 4.15)  # 横の管の出口（栓の上）


# ---------- 3 酸素（二酸化マンガン＋うすい過酸化水素水 → 水上置換法） ----------
def fig3():
    fig, ax = blank(4.0, 3.0, (-2.4, 9.8), (-0.6, 7.6))
    side = flask(ax)
    stones(ax, 0, 0.12, 8, 1.0, size=0.13, seed=7, color="#222222")
    # 水そう
    ax.add_patch(Rectangle((4.3, 0), 5.2, 2.6, facecolor=LIQ, edgecolor="none", zorder=1))
    ax.plot([4.3, 4.3, 9.5, 9.5], [3.3, 0, 0, 3.3], color=K, lw=1.3, zorder=3)
    # 水で満たした試験管（口を下）
    tt = (7.4, 5.6)
    ax.add_patch(Rectangle((7.0, 0.55), 0.8, 4.6, facecolor=LIQ, edgecolor="none", zorder=1))
    testtube(ax, tt[0], tt[1], 180, L=5.0, w=0.85)
    glass(ax, [(side[0], side[1] + 0.1), (side[0], 4.6), (3.2, 4.6), (5.0, 1.5), (6.3, 0.45), (7.2, 0.45)],
          rubber=[(1.0, 4.6), (3.0, 4.6)])
    bubbles(ax, [(7.45, 1.0), (7.35, 1.7), (7.5, 2.5)])
    label(ax, "うすい過酸化水素水", (0.6, 6.4), (1.6, 7.2))
    label(ax, "二酸化マンガン", (1.0, 0.35), (2.1, -0.35))
    label(ax, "水", (9.0, 1.5), (9.9, 1.5))
    save(fig, "no5_3.png")


# ---------- 4 水素（亜鉛＋うすい塩酸） ----------
def fig4():
    fig, ax = blank(2.6, 3.0, (-2.4, 5.6), (-0.6, 7.6))
    side = flask(ax, cock=False)
    stones(ax, 0, 0.12, 7, 1.0, size=0.17, seed=11, color="#888888")
    glass(ax, [(side[0], side[1] + 0.1), (side[0], 4.6), (2.6, 4.6), (3.4, 3.9)], rubber=[(1.0, 4.6), (2.4, 4.6)])
    label(ax, "うすい塩酸", (0.6, 6.4), (1.6, 7.2))
    label(ax, "亜鉛", (1.0, 0.4), (2.1, -0.3))
    save(fig, "no5_4.png")


# ---------- 5 集め方 A・B・C ----------
def bottle(ax, ox, oy, down=False, fill=None):
    # 集気びん。down=True で口を下に向ける
    pts = [(-1.0, 0), (1.0, 0), (1.0, 3.0), (0.55, 3.45), (0.55, 3.9), (-0.55, 3.9), (-0.55, 3.45), (-1.0, 3.0)]
    if down:
        pts = [(x, 3.9 - y) for x, y in pts]
    pts = [(ox + x, oy + y) for x, y in pts]
    if fill:
        ax.add_patch(Polygon(pts, closed=True, facecolor=fill, edgecolor="none", zorder=1.5))
    ax.add_patch(Polygon(pts, closed=True, facecolor="none", edgecolor=K, lw=1.3, zorder=3))


def fig5():
    fig, ax = blank(5.4, 2.6, (-1.6, 14.4), (-0.8, 6.0))
    # A 上方置換法：びんは口が下、管は下からびんの奥へ
    bottle(ax, 0, 0.6, down=True)
    glass(ax, [(-1.4, -0.3), (0, -0.3), (0, 4.0)])
    ax.text(0, 5.3, "A", ha="center", va="center", fontsize=12)
    # B 下方置換法：びんは口が上、管は上からびんの底へ、ガラス板
    bottle(ax, 5.0, 0)
    ax.plot([4.2, 6.2], [4.0, 4.15], color=K, lw=1.0, zorder=4)
    glass(ax, [(3.6, 5.0), (4.8, 5.0), (4.8, 0.4)])
    ax.text(5.0, 5.6, "B", ha="center", va="center", fontsize=12)
    # C 水上置換法：水そうの中で、水を満たしたびん（口が下）
    ax.add_patch(Rectangle((8.2, 0), 5.6, 2.2, facecolor=LIQ, edgecolor="none", zorder=1))
    ax.plot([8.2, 8.2, 13.8, 13.8], [2.9, 0, 0, 2.9], color=K, lw=1.3, zorder=3)
    bottle(ax, 11.0, 0.5, down=True, fill=LIQ)
    glass(ax, [(8.6, 3.6), (9.2, 3.0), (9.9, 0.3), (10.9, 0.3)])
    bubbles(ax, [(11.0, 1.4), (11.1, 2.4)])
    ax.text(11.0, 5.3, "C", ha="center", va="center", fontsize=12)
    save(fig, "no5_5.png")


if __name__ == "__main__":
    fig1(); fig2(); fig3(); fig4(); fig5()
    print("ok")
