# 中3 期末対策の図（線と文字を重ねない／動点は斜線・弧の寸法・点と矢印は外側）
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Rectangle
import numpy as np
plt.rcParams["font.family"] = ["IPAGothic"]
plt.rcParams["hatch.linewidth"] = 0.8
OUT = "img/"

def save(fig, name):
    fig.savefig(OUT + name, dpi=200, bbox_inches="tight", pad_inches=0.05); plt.close(fig)

def dimarc(ax, p, q, bulge, text, gap):
    (x0, y0), (x1, y1) = p, q
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    L = np.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = uy, -ux
    t = np.linspace(-1, 1, 300)
    xs = mx + ux * t * L / 2 + nx * bulge * (1 - t ** 2)
    ys = my + uy * t * L / 2 + ny * bulge * (1 - t ** 2)
    k = np.abs(t) * L / 2 > gap
    ax.plot(xs[(t < 0) & k], ys[(t < 0) & k], "k", lw=1)
    ax.plot(xs[(t > 0) & k], ys[(t > 0) & k], "k", lw=1)
    ax.text(mx + nx * bulge * 1.15, my + ny * bulge * 1.15, text, fontsize=10, ha="center", va="center")

def corners(ax, w, h):
    for s_, (x, y), (dx, dy) in (("A", (0, h), (-0.6, 0.35)), ("B", (0, 0), (-0.6, -0.5)), ("C", (w, 0), (0.6, -0.5)), ("D", (w, h), (0.6, 0.35))):
        ax.text(x + dx, y + dy, s_, fontsize=11, ha="center", va="center", family="serif")

def point(ax, p, name, lab, arrow):
    ax.plot(*p, "ko", ms=4.5, zorder=5)
    ax.text(p[0] + lab[0], p[1] + lab[1], name, fontsize=11, ha="center", va="center", family="serif")
    (a0, b0), (a1, b1) = arrow
    ax.annotate("", xy=(p[0] + a1, p[1] + b1), xytext=(p[0] + a0, p[1] + b0), arrowprops=dict(arrowstyle="->", lw=1.1, color="k"))

# ---- 第1回 応用＜2＞：長方形ABCD（AB=10, BC=20）。PはA→B、QはB→C。△PBQ
def pq(name, w=20, h=10, px=4, qx=8, size=(3.0, 1.9)):
    fig, ax = plt.subplots(figsize=size)
    ax.add_patch(Polygon([(0, h - px), (0, 0), (qx, 0)], closed=True, fill=False, hatch="////", edgecolor="k", lw=1.2))
    ax.plot([0, 0, w, w, 0], [h, 0, 0, h, h], "k", lw=1.5)
    corners(ax, w, h)
    dimarc(ax, (0, h), (w, h), -1.6, f"{w}cm", 1.4)
    dimarc(ax, (w, h), (w, 0), -1.6, f"{h}cm", 1.3)
    point(ax, (0, h - px), "P", (-0.9, 0), ((-2.0, 1.2), (-2.0, -1.4)))
    point(ax, (qx, 0), "Q", (0, -1.0), ((-0.6, -2.8), (1.8, -2.8)))
    ax.set_xlim(-3.0, w + 3.2); ax.set_ylim(-3.6, h + 2.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
pq("s1_pq.png")

# ---- 第1回 宿題＜2＞：縦12m、横20mの土地と、たて・よこの道
def road(name, w=20, h=12, d=2, size=(2.6, 1.7)):
    fig, ax = plt.subplots(figsize=size)
    ax.add_patch(Rectangle((0, 0), w, h, fill=False, lw=1.5))
    ax.add_patch(Rectangle((8, 0), d, h, facecolor="#d0d0d0", edgecolor="k", lw=1))
    ax.add_patch(Rectangle((0, 6), w, d, facecolor="#d0d0d0", edgecolor="k", lw=1))
    ax.text(9, 7, "道", fontsize=9, ha="center", va="center")
    dimarc(ax, (0, h), (w, h), -1.6, f"{w}m", 1.3)
    dimarc(ax, (w, h), (w, 0), -1.6, f"{h}m", 1.3)
    ax.set_xlim(-1, w + 3.2); ax.set_ylim(-1, h + 2.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
road("h1_road.png")

# ---- 第1回 応用＜3＞：カードを1段目から1枚、3枚、5枚…と並べる
def cards(name, rows=4, size=(2.6, 1.6)):
    fig, ax = plt.subplots(figsize=size)
    num = 1
    for r in range(1, rows + 1):
        cnt = 2 * r - 1
        y = -r
        for k in range(cnt):
            x = k - (cnt - 1) / 2
            ax.add_patch(Rectangle((x - 0.5, y - 0.5), 1, 1, fill=False, lw=1))
            ax.text(x, y, str(num), fontsize=8, ha="center", va="center", family="serif")
            num += 1
        ax.text(-rows - 0.6, y, f"{r}段目", fontsize=8, ha="right", va="center")
    for dy in (0.75, 1.0, 1.25): ax.plot(0, -rows - dy, "ko", ms=1.2)
    ax.set_xlim(-rows - 2.6, rows + 0.2); ax.set_ylim(-rows - 1.5, -0.3); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
cards("s1_cards.png")
