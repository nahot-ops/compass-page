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

def dimarc(ax, p, q, bulge, text, gap, pw=1.0, fs=10, toff=0.0):
    (x0, y0), (x1, y1) = p, q
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    L = np.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = uy, -ux
    t = np.linspace(-1, 1, 300)
    f = (1 - t ** 2) ** pw  # pw<1 で両はしが立ち上がった形
    xs = mx + ux * t * L / 2 + nx * bulge * f
    ys = my + uy * t * L / 2 + ny * bulge * f
    k = np.abs(t) * L / 2 > gap
    ax.plot(xs[(t < 0) & k], ys[(t < 0) & k], "k", lw=1)
    ax.plot(xs[(t > 0) & k], ys[(t > 0) & k], "k", lw=1)
    k2 = (bulge * 1.15 if pw == 1.0 else bulge) + (toff if bulge > 0 else -toff)
    ax.text(mx + nx * k2, my + ny * k2, text, fontsize=fs, ha="center", va="center")

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
def road(name, w=20, h=12, d=2, vx=8, hy=5, size=(2.6, 1.7)):
    """道は白、花だん4つは斜線（手書きの図と同じ形）"""
    fig, ax = plt.subplots(figsize=size)
    for (x0, x1) in ((0, vx), (vx + d, w)):
        for (y0, y1) in ((0, hy), (hy + d, h)):
            ax.add_patch(Rectangle((x0, y0), x1 - x0, y1 - y0, fill=False, hatch="////", edgecolor="k", lw=1.2))
    ax.plot([0, w, w, 0, 0], [0, 0, h, h, 0], "k", lw=1.5)
    ax.text(vx + d / 2, hy + d / 2, "道", fontsize=9, ha="center", va="center")
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

# ---- 放物線と直線（y=x^2、A(-1,1)、B(3,9)）
def para(name, ans=False, size=(2.3, 2.7)):
    fig, ax = plt.subplots(figsize=size)
    xs = np.linspace(-3.1, 3.25, 300)
    if ans:
        ax.add_patch(Polygon([(0, 0), (-1, 1), (3, 9)], closed=True, facecolor="#d0d0d0", edgecolor="none", zorder=0))
        ax.plot([0, 0], [0, 3], "k--", lw=1)
        ax.plot([-1, 0, 3], [1, 0, 9], "k", lw=1)
        ax.plot(0, 3, "ks", ms=3.5, zorder=5)
        ax.text(-0.35, 3.0, "C", fontsize=10, ha="right", va="center", family="serif")
    ax.annotate("", xy=(3.9, 0), xytext=(-3.4, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 11.0), xytext=(0, -0.8), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.plot(xs, xs ** 2, "k", lw=1.5)
    lx = np.linspace(-2.2, 3.5, 10); ax.plot(lx, 2 * lx + 3, "k", lw=1.3)
    for p, s_, o in (((-1, 1), "A", (-0.7, 0.05)), ((3, 9), "B", (-0.7, 0.7))):
        ax.plot(*p, "ko", ms=3.5, zorder=5); ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=11, ha="center", va="center", family="serif")
    ax.text(3.85, -0.6, "x", fontsize=12, style="italic", family="serif")
    ax.text(0.25, 10.6, "y", fontsize=12, style="italic", family="serif")
    ax.text(-0.75, -0.75, "O", fontsize=10, family="serif")
    ax.text(-3.4, 10.4, "$y=x^2$", fontsize=9)
    ax.set_xlim(-3.6, 4.3); ax.set_ylim(-1.2, 11.3); ax.set_aspect(0.55); ax.axis("off")
    save(fig, name)
para("h1_para.png"); para("h1_para_ans.png", ans=True)

# ---- 道はばの解説：道をはしに寄せる図（上：もとの図 → 下：寄せた図）
def road_move(name, w=20, h=12, d=2.6, size=(2.9, 4.6)):
    fig, ax = plt.subplots(figsize=size)
    oy = h + 11  # 上の図の位置
    # 上：もとの図
    vx, hy = 8, 5
    for (x0, x1) in ((0, vx), (vx + d, w)):
        for (y0, y1) in ((0, hy), (hy + d, h)):
            ax.add_patch(Rectangle((x0, oy + y0), x1 - x0, y1 - y0, fill=False, hatch="////", edgecolor="k", lw=1.2))
    ax.plot([0, w, w, 0, 0], [oy, oy, oy + h, oy + h, oy], "k", lw=1.5)
    ax.text(vx + d / 2, oy + hy + d / 2, "道", fontsize=9, ha="center", va="center")
    dimarc(ax, (0, oy + h), (w, oy + h), -1.6, "20m", 1.3)
    dimarc(ax, (w, oy + h), (w, oy), -1.6, "12m", 1.3)
    # 矢印
    ax.annotate("", xy=(w / 2, h + 5.0), xytext=(w / 2, oy - 1.0), arrowprops=dict(arrowstyle="->", lw=1.3, color="k"))
    ax.text(w / 2 + 1.0, (h + 5.0 + oy - 1.0) / 2, "道を左と下のはしに寄せる", fontsize=8, ha="left", va="center")
    # 下：寄せた図
    d = 4.2
    ax.add_patch(Rectangle((d, d), w - d, h - d, fill=False, hatch="////", edgecolor="k", lw=1.2))
    ax.plot([0, w, w, 0, 0], [0, 0, h, h, 0], "k", lw=1.5)
    ax.plot([d, d, w], [h, d, d], "k", lw=1.2)
    ax.text(d / 2 + 1.5, d / 2, "道", fontsize=9, ha="center", va="center")
    dimarc(ax, (0, h), (d, h), -1.3, "$x$m", 1.4, pw=0.5, fs=9)
    dimarc(ax, (d, h), (w, h), -1.3, "$(20−x)$m", 4.0, pw=0.5, fs=9)
    dimarc(ax, (0, h), (w, h), -3.6, "20m", 1.6, pw=0.35)
    dimarc(ax, (w, h), (w, d), -1.0, "$(12−x)$m", 0, pw=0.5, fs=9, toff=3.9)
    dimarc(ax, (w, d), (w, 0), -1.0, "$x$m", 0, pw=0.5, fs=9, toff=1.8)
    dimarc(ax, (w, h), (w, 0), -10.2, "12m", 1.4, pw=0.35)
    ax.set_xlim(-1, w + 12.5); ax.set_ylim(-1, oy + h + 2.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
road_move("h1_road_ans.png")

# ---- 放物線と直線の解説：△AOBを、底辺がx軸上の三角形に変形する（手書きの図と同じ形）
def para_ans(name, size=(2.9, 3.2)):
    fig, ax = plt.subplots(figsize=size)
    ax.add_patch(Polygon([(-1, 0), (0, 3), (3, 0)], closed=True, fill=False, hatch="////", edgecolor="k", lw=1.2, zorder=1))
    xs = np.linspace(-3.1, 3.25, 300)
    ax.annotate("", xy=(4.4, 0), xytext=(-3.6, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 11.2), xytext=(0, -1.4), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.plot(xs, xs ** 2, "k", lw=1.5)
    lx = np.linspace(-2.3, 3.7, 10); ax.plot(lx, 2 * lx + 3, "k", lw=1.3)
    ax.plot([-1, 0, 3], [1, 0, 9], "k", lw=1.0)                 # もとの△AOB
    for (x0, y0) in ((-1, 1), (3, 9)):                            # 底辺に下ろす矢印
        ax.annotate("", xy=(x0, 0.15), xytext=(x0, y0 - 0.2), arrowprops=dict(arrowstyle="->", lw=1, ls="--", color="k"))
    for p in ((-1, 1), (3, 9), (0, 3), (-1, 0), (3, 0)): ax.plot(*p, "ko", ms=3.5, zorder=5)
    ax.text(-1.6, 1.6, "A(−1, 1)", fontsize=9, ha="right", va="center")
    ax.text(3.25, 9.0, "B(3, 9)", fontsize=9, ha="left", va="center")
    ax.text(-0.3, 3.4, "C", fontsize=10, ha="right", va="center", family="serif")
    ax.text(-0.3, 5.5, "(0, 3)", fontsize=9, ha="right", va="center")
    ax.text(-0.6, -1.0, "O", fontsize=10, family="serif")
    ax.text(4.3, -0.75, "x", fontsize=12, style="italic", family="serif")
    ax.text(0.25, 10.8, "y", fontsize=12, style="italic", family="serif")
    ax.text(-3.4, 10.6, "$y=x^2$", fontsize=9)
    ax.text(3.75, 10.7, "$y=2x+3$", fontsize=9, ha="left")
    ax.set_xlim(-4.2, 6.6); ax.set_ylim(-1.6, 11.5); ax.set_aspect(0.55); ax.axis("off")
    save(fig, name)
para_ans("h1_para_ans.png")


# ======================= 第2回（関数 y=ax^2） =======================
def pfig(name, a, xr, yr, pts, segs=(), lines=(), hatch=None, dashed=(), eqs=(), size=(2.4, 2.6), aspect=None):
    """放物線 y=ax^2 と点・線分。pts: [(名前, (x,y), (dx,dy))]、lines: 直線 (m,b,x0,x1)"""
    fig, ax = plt.subplots(figsize=size)
    if hatch: ax.add_patch(Polygon(hatch, closed=True, fill=False, hatch="////", edgecolor="k", lw=1.0, zorder=1))
    (x0, x1), (y0, y1) = xr, yr
    ax.annotate("", xy=(x1, 0), xytext=(x0, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, y1), xytext=(0, y0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    xs = np.linspace(x0 + 0.3, x1 - 0.5, 400); ys = a * xs ** 2; k = (ys <= y1 - 0.6 * (y1 - y0) / 12) & (ys >= y0)
    ax.plot(xs[k], ys[k], "k", lw=1.5)
    for (m, b, lx0, lx1) in lines:
        ax.plot([lx0, lx1], [m * lx0 + b, m * lx1 + b], "k", lw=1.2)
    for (p, q) in segs: ax.plot([p[0], q[0]], [p[1], q[1]], "k", lw=1.0)
    for (p, q) in dashed: ax.plot([p[0], q[0]], [p[1], q[1]], "k--", lw=1.0)
    for (s_, p, o) in pts:
        ax.plot(*p, "ko", ms=3.5, zorder=5)
        if s_: ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=10, ha="center", va="center", family="serif")
    for (s_, p) in eqs: ax.text(*p, s_, fontsize=9, ha="center", va="center")
    dy = (y1 - y0) / 22
    ax.text(x1 - 0.1, -1.6 * dy, "x", fontsize=12, style="italic", family="serif")
    ax.text(0.15 * (x1 - x0) / 8, y1 - dy, "y", fontsize=12, style="italic", family="serif", ha="left")
    ax.text(-0.35 * (x1 - x0) / 8, -1.6 * dy, "O", fontsize=10, family="serif", ha="right")
    ax.set_xlim(x0, x1 + 0.3); ax.set_ylim(y0, y1)
    if aspect: ax.set_aspect(aspect)
    ax.axis("off"); save(fig, name)

# 応用＜1＞：y=1/2x^2、A(-2,2)、B(4,8)
pfig("s2_p1.png", 0.5, (-4.5, 6), (-1.2, 10.5), [("A", (-2, 2), (-0.5, 0.5)), ("B", (4, 8), (-0.6, 0.6))],
     lines=[(1, 4, -4.2, 5.5)], eqs=[("$y=\\frac{1}{2}x^2$", (-3.0, 9.6))], aspect=0.6)
# 応用＜3＞：y=x^2、A(-1,1)、B(2,4)、C(1,1)
pfig("s2_p3.png", 1.0, (-2.6, 3.2), (-0.8, 5.6), [("A", (-1, 1), (-0.35, 0.3)), ("B", (2, 4), (-0.35, 0.35)), ("C", (1, 1), (0.35, -0.3))],
     segs=[((-1, 1), (1, 1)), ((1, 1), (2, 4)), ((-1, 1), (2, 4))], eqs=[("$y=x^2$", (-1.9, 5.0))], aspect=0.75)
pfig("s2_p3_ans.png", 1.0, (-2.6, 3.2), (-0.8, 5.6), [("A", (-1, 1), (-0.35, 0.3)), ("B", (2, 4), (-0.35, 0.35)), ("C", (1, 1), (0.35, -0.3)), ("M", (1.5, 2.5), (0.4, -0.1))],
     segs=[((-1, 1), (1, 1)), ((1, 1), (2, 4)), ((-1, 1), (2, 4))], dashed=[((-1, 1), (1.5, 2.5))], hatch=[(-1, 1), (1, 1), (1.5, 2.5)],
     eqs=[("$y=x^2$", (-1.9, 5.0))], aspect=0.75)
# 宿題＜3＞：y=1/2x^2、A(-2,2)、B(6,18)
pfig("h2_p.png", 0.5, (-5, 8), (-2, 21), [("A", (-2, 2), (-1.2, 0.2)), ("B", (6, 18), (-0.9, 0.9))],
     lines=[(2, 6, -4.6, 7.3)], eqs=[("$y=\\frac{1}{2}x^2$", (-3.3, 19.5))], aspect=0.45, size=(2.4, 3.4))
pfig("h2_p_ans.png", 0.5, (-5, 8), (-2, 21), [("A", (-2, 2), (-1.2, 0.2)), ("B", (6, 18), (-0.9, 0.9)), ("M", (2, 10), (-0.8, 0.9))],
     lines=[(2, 6, -4.6, 7.3)], segs=[((-2, 2), (0, 0)), ((0, 0), (6, 18))], dashed=[((0, 0), (2, 10))], hatch=[(0, 0), (-2, 2), (2, 10)],
     eqs=[("$y=\\frac{1}{2}x^2$", (-3.3, 19.5))], aspect=0.45, size=(2.4, 3.4))

# 応用＜2＞：正方形ABCD（1辺6cm）。PはA→B、QはA→D。△APQ
def sq(name, s=6, px=2.5, size=(2.0, 2.0)):
    fig, ax = plt.subplots(figsize=size)
    ax.add_patch(Polygon([(0, s), (0, s - px), (px, s)], closed=True, fill=False, hatch="////", edgecolor="k", lw=1.2))
    ax.plot([0, 0, s, s, 0], [s, 0, 0, s, s], "k", lw=1.5)
    corners(ax, s, s)
    dimarc(ax, (s, s), (s, 0), -1.0, f"{s}cm", 0.9)
    point(ax, (0, s - px), "P", (-0.7, 0), ((-1.5, 0.6), (-1.5, -0.9)))
    point(ax, (px, s), "Q", (0, 0.65), ((-0.6, 1.6), (0.9, 1.6)))
    ax.set_ylim(-1.0, s + 2.4)
    ax.set_xlim(-2.4, s + 2.0); ax.set_ylim(-1.0, s + 2.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
sq("s2_sq.png")

# 宿題＜6＞：DE//BC の三角形
def tri_par(name, size=(2.4, 1.9)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C = (2.2, 6), (0, 0), (7, 0); t = 4 / 6
    D = (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t); E = (A[0] + (C[0] - A[0]) * t, A[1] + (C[1] - A[1]) * t)
    ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], "k", lw=1.5); ax.plot([D[0], E[0]], [D[1], E[1]], "k", lw=1.3)
    for s_, p, o in (("A", A, (0, 0.5)), ("B", B, (-0.4, -0.4)), ("C", C, (0.4, -0.4)), ("D", D, (-0.45, 0.1)), ("E", E, (0.45, 0.1))):
        ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=10, ha="center", va="center", family="serif")
    for p, q, txt, side in ((A, D, "4cm", -1), (D, B, "2cm", -1), (A, E, "6cm", 1), (E, C, "$x$cm", 1)):
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2; L = np.hypot(q[0] - p[0], q[1] - p[1]); nx, ny = (q[1] - p[1]) / L, -(q[0] - p[0]) / L
        ax.text(mx - side * nx * 0.75, my - side * ny * 0.75, txt, fontsize=9, ha="center", va="center")
    ax.text((D[0] + E[0]) / 2, D[1] + 0.35, "$y$cm", fontsize=9, ha="center", va="bottom")
    ax.text(3.5, -0.6, "9cm", fontsize=9, ha="center", va="center")
    ax.set_xlim(-1.4, 8.4); ax.set_ylim(-1.1, 6.9); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
tri_par("h2_tri.png")
