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
def tri_par(name, size=(2.6, 2.6)):
    """DE//BC の三角形。辺の長さは弧で両はしをつないで書く（手書きの図と同じ形）"""
    fig, ax = plt.subplots(figsize=size)
    A, B, C = (4.0, 7.5), (1.0, 0), (8.0, 0); t = 4 / 6
    D = (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t); E = (A[0] + (C[0] - A[0]) * t, A[1] + (C[1] - A[1]) * t)
    ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], "k", lw=1.5); ax.plot([D[0], E[0]], [D[1], E[1]], "k", lw=1.3)
    for p in (D, E): ax.plot(*p, "ko", ms=3.5, zorder=5)
    for s_, p, o in (("A", A, (0, 0.55)), ("B", B, (-0.3, -0.55)), ("C", C, (0.35, -0.55)), ("D", D, (-1.7, 0.3)), ("E", E, (1.7, 0.3))):
        ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=11, ha="center", va="center", family="serif")
    dimarc(ax, A, D, 1.2, "4cm", 1.0)
    dimarc(ax, D, B, 1.2, "2cm", 0.75)
    dimarc(ax, A, E, -1.2, "6cm", 1.0)
    dimarc(ax, E, C, -1.2, "$x$cm", 0.8)
    dimarc(ax, D, E, 0.6, "$y$cm", 0.8)
    dimarc(ax, B, C, 0.8, "9cm", 0.8)
    ax.set_xlim(-2.4, 11.4); ax.set_ylim(-1.6, 8.5); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
tri_par("h2_tri.png")

# 宿題＜5＞：相似な四角形 ABCD と EFGH（相似比 2：3）
def quads(name, size=(3.0, 1.7)):
    fig, ax = plt.subplots(figsize=size)
    base = [(0.4, 2.0), (0, 0), (3.2, 0), (2.0, 3.0)]  # A B C D
    for names, k, ox in ((("A", "B", "C", "D"), 1.0, 0), (("E", "F", "G", "H"), 1.5, 5.8)):
        pts = [(ox + x * k, y * k) for x, y in base]
        ax.plot([p[0] for p in pts + pts[:1]], [p[1] for p in pts + pts[:1]], "k", lw=1.5)
        for s_, p, o in zip(names, pts, ((-0.45, 0.1), (-0.35, -0.4), (0.35, -0.4), (0.1, 0.45))):
            ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=11, ha="center", va="center", family="serif")
    ax.set_xlim(-0.9, 11.1); ax.set_ylim(-0.9, 5.2); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
quads("h2_quads.png")

# ---- 比を「〇・□・△の数字」と「×3」で表す解説の図
def mark(ax, kind, digit, p, fs=8, r=0.5):
    """比の記号（〇・□・△）の中に数字。記号は数字より十分大きくする"""
    x, y = p
    if kind == "circle":
        ax.add_patch(matplotlib.patches.Circle((x, y), r, fill=False, lw=0.9))
    elif kind == "box":
        ax.add_patch(Rectangle((x - r, y - r), 2 * r, 2 * r, fill=False, lw=0.9))
    else:  # triangle：数字は下寄りに置く
        h = 2.2 * r
        ax.add_patch(Polygon([(x - 1.25 * r, y - 0.45 * h), (x + 1.25 * r, y - 0.45 * h), (x, y + 0.75 * h)], closed=True, fill=False, lw=0.9))
        y -= 0.12 * h
    ax.text(x, y, digit, fontsize=fs, ha="center", va="center", family="serif")

def times(ax, p, q, txt, rad=-0.5, tp=None):
    ax.annotate("", xy=q, xytext=p, arrowprops=dict(arrowstyle="->", lw=0.9, color="k", connectionstyle=f"arc3,rad={rad}"))
    if tp: ax.text(*tp, txt, fontsize=9, ha="center", va="center")

def tri_par_ans(name, size=(3.0, 2.9)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C = (4.0, 7.5), (1.0, 0), (8.0, 0); t = 4 / 6
    D = (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t); E = (A[0] + (C[0] - A[0]) * t, A[1] + (C[1] - A[1]) * t)
    ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], "k", lw=1.5); ax.plot([D[0], E[0]], [D[1], E[1]], "k", lw=1.3)
    for p in (D, E): ax.plot(*p, "ko", ms=3.5, zorder=5)
    for s_, p, o in (("A", A, (0, 0.55)), ("B", B, (-0.3, -0.55)), ("C", C, (0.35, -0.55)), ("D", D, (-1.7, 0.3)), ("E", E, (1.7, 0.3))):
        ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=11, ha="center", va="center", family="serif")
    dimarc(ax, A, D, 1.2, "4cm", 1.0); dimarc(ax, D, B, 1.2, "2cm", 0.75)
    dimarc(ax, A, E, -1.2, "6cm", 1.0); dimarc(ax, E, C, -1.2, "$x$cm", 0.8)
    dimarc(ax, D, E, 0.6, "$y$cm", 0.8); dimarc(ax, B, C, 0.8, "9cm", 0.8)
    # AD：DB＝②：①
    mark(ax, "circle", "2", (0.4, 6.9)); mark(ax, "circle", "1", (-1.6, 3.3))
    # AE：EC＝[2]：[1]（×3）
    mark(ax, "box", "2", (6.9, 7.7)); times(ax, (7.45, 7.5), (7.3, 6.0), "×3", -0.9, (8.7, 6.9))
    mark(ax, "box", "1", (9.9, 3.5)); times(ax, (10.45, 3.3), (10.1, 1.95), "×3", -0.9, (11.5, 2.7))
    # DE：BC＝△2：△3（×3）
    mark(ax, "tri", "2", (3.4, 3.5)); times(ax, (4.1, 3.3), (4.3, 1.75), "×3", -0.9, (5.5, 3.1))
    mark(ax, "tri", "3", (2.4, -2.3)); times(ax, (3.1, -2.3), (3.75, -1.25), "×3", 0.7, (4.5, -2.5))
    ax.set_xlim(-2.4, 12.4); ax.set_ylim(-3.0, 8.7); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
tri_par_ans("h2_tri_ans.png")

def quads_ans(name, size=(3.6, 2.2)):
    fig, ax = plt.subplots(figsize=size)
    base = [(0.4, 2.0), (0, 0), (3.2, 0), (2.0, 3.0)]
    P1 = [(x, y) for x, y in base]; P2 = [(7.6 + x * 1.5, y * 1.5) for x, y in base]
    for names, pts in ((("A", "B", "C", "D"), P1), (("E", "F", "G", "H"), P2)):
        ax.plot([p[0] for p in pts + pts[:1]], [p[1] for p in pts + pts[:1]], "k", lw=1.5)
        for s_, p, o in zip(names, pts, ((-0.45, 0.25), (-0.35, -0.4), (0.35, -0.4), (0.1, 0.45))):
            ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=11, ha="center", va="center", family="serif")
    # AB と EF、CD と GH に弧
    dimarc(ax, P1[0], P1[1], 0.5, "", 0); ax.text(-1.0, 0.7, "4cm", fontsize=9, ha="center", va="center")
    dimarc(ax, P1[3], P1[2], -0.5, "", 0)
    dimarc(ax, P2[0], P2[1], 0.6, "", 0)
    dimarc(ax, P2[3], P2[2], -0.6, "", 0); ax.text(12.9, 2.6, "10cm", fontsize=9, ha="center", va="center")
    # 相似比 ②：③（×2）、[2]：[3]（×3）
    mark(ax, "circle", "2", (-1.4, 2.4)); times(ax, (-1.95, 2.3), (-1.6, 0.85), "×2", 0.9, (-3.1, 1.7))
    mark(ax, "box", "2", (4.5, 2.9)); times(ax, (5.05, 2.7), (4.8, 1.5), "", -0.9); ax.text(6.0, 2.0, r"$\times\frac{10}{3}$", fontsize=10, ha="center", va="center")
    mark(ax, "circle", "3", (6.9, 4.5)); times(ax, (6.35, 4.3), (6.4, 2.6), "×2", 0.9, (5.7, 4.9))
    mark(ax, "box", "3", (12.9, 4.1)); times(ax, (13.45, 3.9), (13.35, 2.85), "", -0.9); ax.text(14.8, 3.4, r"$\times\frac{10}{3}$", fontsize=10, ha="center", va="center")
    ax.set_xlim(-3.6, 15.8); ax.set_ylim(-0.9, 5.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
quads_ans("h2_quads_ans.png")

# 宿題＜4＞：△ABC と △DEF（3辺 6,8,10 と 9,12,15）。辺の長さは弧で示す
def tri_pair(name, size=(4.2, 2.3)):
    """△ABC（AB=6, BC=12, CA=9）と △DEF（DE=10, EF=20, FD=15）。辺の長さは弧で示す"""
    fig, ax = plt.subplots(figsize=size)
    ax0 = 4.125; ay0 = (36 - ax0 ** 2) ** 0.5
    for names, k, ox, lens in ((("A", "B", "C"), 1.0, 0, ("6cm", "12cm", "9cm")), (("D", "E", "F"), 5 / 3, 17.5, ("10cm", "20cm", "15cm"))):
        A, B, C = (ox + ax0 * k, ay0 * k), (ox, 0), (ox + 12 * k, 0)
        ax.plot([A[0], B[0], C[0], A[0]], [A[1], B[1], C[1], A[1]], "k", lw=1.5)
        for s_, p, o in zip(names, (A, B, C), ((0, 2.0), (-1.1, -0.4), (1.1, -0.4))):
            ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=11, ha="center", va="center", family="serif")
        dimarc(ax, A, B, 2.3, lens[0], 1.9, fs=9)
        dimarc(ax, B, C, 2.0, lens[1], 2.3, fs=9)
        dimarc(ax, C, A, 2.3, lens[2], 1.9, fs=9)
    ax.set_xlim(-4.6, 42.0); ax.set_ylim(-4.0, 12.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
tri_pair("h2_tripair.png")

# 第2回 応用＜1＞の解説図：y=1/2x^2、A(-2,2)、B(4,8)、C(0,4)、ABの中点M(1,5)
pfig("s2_p1_ans.png", 0.5, (-4.5, 6), (-1.2, 10.5), [("A", (-2, 2), (-0.5, 0.5)), ("B", (4, 8), (-0.6, 0.6)), ("C", (0, 4), (-0.5, 0.4)), ("M", (1, 5), (-0.5, 0.5))],
     lines=[(1, 4, -4.2, 5.5)], segs=[((-2, 2), (0, 0)), ((0, 0), (4, 8))], dashed=[((0, 0), (1.2, 6))], hatch=[(0, 0), (-2, 2), (1, 5)],
     eqs=[("$y=\\frac{1}{2}x^2$", (-3.0, 9.6))], aspect=0.6)

# 第2回 応用＜1＞の解説図（手書きの形）：△OABを、底辺がx軸上の三角形に変形。中点M(1,5)とy=5x
def para_ans2(name, size=(3.0, 3.1)):
    fig, ax = plt.subplots(figsize=size)
    ax.add_patch(Polygon([(-2, 0), (0, 4), (4, 0)], closed=True, fill=False, hatch="////", edgecolor="k", lw=1.1, zorder=1))
    ax.annotate("", xy=(5.6, 0), xytext=(-5.0, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 11.0), xytext=(0, -1.6), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    xs = np.linspace(-4.3, 4.6, 300); ax.plot(xs, xs ** 2 / 2, "k", lw=1.5)
    lx = np.linspace(-4.8, 5.4, 10); ax.plot(lx, lx + 4, "k", lw=1.3)          # 直線AB
    ox = np.linspace(-0.3, 2.0, 10); ax.plot(ox, 5 * ox, "k", lw=1.0)           # y=5x（Oと中点Mを通る）
    ax.plot([-2, 0, 4], [2, 0, 8], "k", lw=1.0)                                 # もとの△OAB
    for (x0, y0) in ((-2, 2), (4, 8)):
        ax.annotate("", xy=(x0, 0.15), xytext=(x0, y0 - 0.25), arrowprops=dict(arrowstyle="->", lw=1, ls="--", color="k"))
    for p in ((-2, 2), (4, 8), (0, 4), (1, 5), (-2, 0), (4, 0)): ax.plot(*p, "ko", ms=3.5, zorder=5)
    ax.text(-2.25, 2.5, "A", fontsize=11, ha="right", va="center", family="serif")
    ax.text(-2.95, 2.5, "(−2, 2)", fontsize=9, ha="right", va="center")
    ax.text(3.75, 8.4, "B", fontsize=11, ha="right", va="center", family="serif")
    ax.text(4.5, 7.6, "(4, 8)", fontsize=9, ha="left", va="center")
    ax.text(-0.25, 4.5, "C", fontsize=11, ha="right", va="center", family="serif")
    ax.text(-0.85, 4.95, "(0, 4)", fontsize=9, ha="right", va="center")
    ax.text(1.25, 4.45, "M", fontsize=11, ha="left", va="center", family="serif")
    ax.text(0.8, 6.0, "(1, 5)", fontsize=9, ha="right", va="center", bbox=dict(boxstyle="square,pad=0.05", fc="white", ec="none"), zorder=6)
    ax.text(2.1, 10.3, "$y=5x$", fontsize=9, ha="left", va="center")
    ax.text(-0.95, -1.05, "O", fontsize=10, family="serif")
    ax.text(5.4, -0.9, "x", fontsize=12, style="italic", family="serif")
    ax.text(0.3, 10.7, "y", fontsize=12, style="italic", family="serif")
    ax.text(-4.4, 10.0, "$y=\\frac{1}{2}x^2$", fontsize=9)
    ax.set_xlim(-6.2, 7.2); ax.set_ylim(-1.8, 11.4); ax.set_aspect(0.65); ax.axis("off")
    save(fig, name)
para_ans2("s2_p1_ans.png")

# 第2回 応用＜3＞の解説図（手書きの形）：y=x^2、A(-1,1)、B(2,4)、C(1,1)、CBの中点M(3/2,5/2)、直線AM
def para3_ans(name, size=(2.9, 2.9)):
    fig, ax = plt.subplots(figsize=size)
    ax.annotate("", xy=(3.4, 0), xytext=(-2.7, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 5.6), xytext=(0, -0.7), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    xs = np.linspace(-2.25, 2.3, 300); ax.plot(xs, xs ** 2, "k", lw=1.5)
    ax.plot([-1, 1, 2, -1], [1, 1, 4, 1], "k", lw=1.1)                          # △ACB
    lx = np.array([-1.6, 2.6]); ax.plot(lx, 0.6 * lx + 1.6, "k", lw=1.1)       # 直線AM y=3/5x+8/5
    for p in ((-1, 1), (2, 4), (1, 1), (1.5, 2.5)): ax.plot(*p, "ko", ms=4, zorder=5)
    ax.text(-1.12, 1.25, "A", fontsize=11, ha="right", va="bottom", family="serif")
    ax.text(-1.5, 1.25, "(−1, 1)", fontsize=9, ha="right", va="bottom")
    ax.text(1.85, 4.3, "B", fontsize=11, ha="right", va="bottom", family="serif")
    ax.text(2.2, 4.1, "(2, 4)", fontsize=9, ha="left", va="center")
    ax.text(1.12, 0.85, "C", fontsize=11, ha="left", va="top", family="serif")
    ax.text(1.45, 0.75, "(1, 1)", fontsize=9, ha="left", va="center")
    ax.text(1.68, 2.45, "M", fontsize=11, ha="left", va="top", family="serif")
    ax.text(2.15, 2.1, r"$(\frac{3}{2}, \frac{5}{2})$", fontsize=10, ha="left", va="center")
    ax.text(-0.15, -0.15, "O", fontsize=10, ha="right", va="top", family="serif")
    ax.text(3.3, -0.25, "x", fontsize=12, style="italic", family="serif", va="top")
    ax.text(0.12, 5.5, "y", fontsize=12, style="italic", family="serif")
    ax.text(-2.4, 5.2, "$y=x^2$", fontsize=9)
    ax.set_xlim(-2.8, 3.9); ax.set_ylim(-0.8, 5.9); ax.set_aspect(0.8); ax.axis("off")
    save(fig, name)
para3_ans("s2_p3_ans.png")

# 第2回 宿題＜3＞の解説図：y=1/2x^2、A(-2,2)、B(6,18)、C(0,6)、ABの中点M(2,10)、y=5x。△OABを変形
def para_ans_h2(name, size=(3.0, 3.6)):
    fig, ax = plt.subplots(figsize=size)
    ax.add_patch(Polygon([(-2, 0), (0, 6), (6, 0)], closed=True, fill=False, hatch="////", edgecolor="k", lw=1.1, zorder=1))
    ax.annotate("", xy=(8.0, 0), xytext=(-5.6, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 21.5), xytext=(0, -2.5), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    xs = np.linspace(-5.0, 6.3, 300); ax.plot(xs, xs ** 2 / 2, "k", lw=1.5)
    lx = np.linspace(-4.8, 7.2, 10); ax.plot(lx, 2 * lx + 6, "k", lw=1.3)
    ox = np.linspace(-0.4, 3.9, 10); ax.plot(ox, 5 * ox, "k", lw=1.0)
    ax.plot([-2, 0, 6], [2, 0, 18], "k", lw=1.0)
    for (x0, y0) in ((-2, 2), (6, 18)):
        ax.annotate("", xy=(x0, 0.3), xytext=(x0, y0 - 0.5), arrowprops=dict(arrowstyle="->", lw=1, ls="--", color="k"))
    for p in ((-2, 2), (6, 18), (0, 6), (2, 10), (-2, 0), (6, 0)): ax.plot(*p, "ko", ms=3.5, zorder=5)
    ax.text(-2.45, 2.3, "A", fontsize=11, ha="right", va="center", family="serif")
    ax.text(-3.3, 2.3, "(−2, 2)", fontsize=9, ha="right", va="center")
    ax.text(5.6, 19.2, "B", fontsize=11, ha="right", va="center", family="serif")
    ax.text(6.4, 16.9, "(6, 18)", fontsize=9, ha="left", va="center")
    ax.text(-0.35, 6.9, "C", fontsize=11, ha="right", va="center", family="serif")
    ax.text(-0.6, 8.6, "(0, 6)", fontsize=9, ha="right", va="center")
    ax.text(2.4, 9.2, "M", fontsize=11, ha="left", va="center", family="serif")
    ax.text(1.6, 11.3, "(2, 10)", fontsize=9, ha="right", va="center", bbox=dict(boxstyle="square,pad=0.05", fc="white", ec="none"), zorder=6)
    ax.text(3.9, 21.0, "$y=5x$", fontsize=9, ha="center", va="center")
    ax.text(-0.5, -1.4, "O", fontsize=10, ha="right", va="center", family="serif")
    ax.text(7.7, -1.8, "x", fontsize=12, style="italic", family="serif")
    ax.text(0.4, 20.8, "y", fontsize=12, style="italic", family="serif")
    ax.text(-5.4, 19.8, "$y=\\frac{1}{2}x^2$", fontsize=9)
    ax.set_xlim(-7.4, 9.6); ax.set_ylim(-2.8, 22.6); ax.set_aspect(0.5); ax.axis("off")
    save(fig, name)
para_ans_h2("h2_p_ans.png")


# ======================= 第3回（相似） =======================
def lab(ax, s_, p, o, fs=11):
    ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=fs, ha="center", va="center", family="serif")

def seg(ax, *pts, lw=1.5, ls="-"):
    ax.plot([p[0] for p in pts], [p[1] for p in pts], "k", lw=lw, ls=ls)

def angle_mark(ax, v, p, q, r=0.7, n=1):
    """頂点vで、v→p と v→q のあいだに角の印（弧）を n 本"""
    a1 = np.arctan2(p[1] - v[1], p[0] - v[0]); a2 = np.arctan2(q[1] - v[1], q[0] - v[0])
    if a2 < a1: a1, a2 = a2, a1
    if a2 - a1 > np.pi: a1, a2 = a2, a1 + 2 * np.pi
    for k in range(n):
        t = np.linspace(a1, a2, 50); rr = r + 0.18 * k
        ax.plot(v[0] + rr * np.cos(t), v[1] + rr * np.sin(t), "k", lw=0.9)

# 基本＜5＞(1)：DE//BC、AD=6, DB=3, AE=4, EC=x
def k5_tri(name, size=(2.2, 2.2)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C = (3.5, 7.5), (0, 0), (8, 0); t = 6 / 9
    D = (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t); E = (A[0] + (C[0] - A[0]) * t, A[1] + (C[1] - A[1]) * t)
    seg(ax, A, B, C, A); seg(ax, D, E, lw=1.3)
    for p in (D, E): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (0, 0.6)); lab(ax, "B", B, (-0.4, -0.55)); lab(ax, "C", C, (0.4, -0.55)); lab(ax, "D", D, (-1.4, 0.35)); lab(ax, "E", E, (1.4, 0.35))
    dimarc(ax, A, D, 1.2, "6cm", 1.0); dimarc(ax, D, B, 1.0, "3cm", 0.7)
    dimarc(ax, A, E, -1.2, "4cm", 1.0); dimarc(ax, E, C, -1.0, "$x$cm", 0.75)
    ax.set_xlim(-2.4, 10.4); ax.set_ylim(-1.3, 8.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
k5_tri("s3_k5a.png")

# 基本＜5＞(3)：ℓ//m//n と2本の直線。4cm, 6cm と 6cm, x cm
def k5_par(name, size=(2.4, 2.0)):
    fig, ax = plt.subplots(figsize=size)
    ys = (6, 3.6, 0)
    for y, nm in zip(ys, ("ℓ", "m", "n")):
        ax.plot([-0.5, 9.5], [y, y], "k", lw=1.3); ax.text(9.9, y, nm, fontsize=11, style="italic", ha="left", va="center", family="IPAGothic" if nm == "ℓ" else "serif")
    P = [(1.6, 6), (2.4, 3.6), (3.6, 0)]; Q = [(6.0, 6), (6.9, 3.6), (8.25, 0)]
    seg(ax, (1.3, 6.9), (3.9, -0.9), lw=1.2); seg(ax, (5.65, 7.0), (8.6, -1.0), lw=1.2)
    dimarc(ax, P[0], P[1], 0.9, "4cm", 0.65, fs=9); dimarc(ax, P[1], P[2], 0.9, "6cm", 0.8, fs=9)
    dimarc(ax, Q[0], Q[1], -0.9, "6cm", 0.65, fs=9); dimarc(ax, Q[1], Q[2], -0.9, "$x$cm", 0.85, fs=9)
    ax.set_xlim(-1.4, 11.0); ax.set_ylim(-1.4, 7.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
k5_par("s3_k5c.png")

# 応用＜1＞：△ABC、辺AC上の点D、∠ABD＝∠ACB
def o1_proof(name, ans=False, size=(2.6, 2.2)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C = (3.0, 6.0), (0, 0), (9.0, 0)
    D = (A[0] + (C[0] - A[0]) * 4 / 9, A[1] + (C[1] - A[1]) * 4 / 9)   # AD=4, AC=9
    seg(ax, A, B, C, A); seg(ax, B, D, lw=1.2)
    ax.plot(*D, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (0, 0.55)); lab(ax, "B", B, (-0.45, -0.45)); lab(ax, "C", C, (0.45, -0.45)); lab(ax, "D", D, (0.45, 0.4))
    angle_mark(ax, B, A, D, 1.1); angle_mark(ax, C, A, B, 1.1)
    if ans:
        angle_mark(ax, A, B, C, 0.75, 2)
        dimarc(ax, A, B, 1.0, "6cm", 0.8, fs=9); dimarc(ax, C, A, 1.3, "9cm", 0.9, fs=9)
    ax.set_xlim(-1.6, 10.4); ax.set_ylim(-1.1, 7.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
o1_proof("s3_o1.png"); o1_proof("s3_o1_ans.png", ans=True)

# 応用＜2＞：台形ABCD（AD//BC）、AD=4, BC=6、対角線の交点O、Oを通りBCに平行な直線とAB、DCの交点E、F
def o2_trap(name, ans=False, size=(2.8, 2.1)):
    fig, ax = plt.subplots(figsize=size)
    A, D, B, C = (2.5, 5.0), (6.5, 5.0), (1.5, 0), (7.5, 0)
    # 交点 O：AO:OC = 4:6
    O = (A[0] + (C[0] - A[0]) * 0.4, A[1] + (C[1] - A[1]) * 0.4)
    E = (A[0] + (B[0] - A[0]) * 0.4, A[1] + (B[1] - A[1]) * 0.4); F = (D[0] + (C[0] - D[0]) * 0.4, D[1] + (C[1] - D[1]) * 0.4)
    seg(ax, A, D, C, B, A); seg(ax, A, C, lw=1.1); seg(ax, B, D, lw=1.1); seg(ax, E, F, lw=1.3)
    for p in (O, E, F): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (-0.3, 0.45)); lab(ax, "D", D, (0.3, 0.45)); lab(ax, "B", B, (-0.4, -0.45)); lab(ax, "C", C, (0.4, -0.45))
    lab(ax, "O", O, (0, 0.55)); lab(ax, "E", E, (-0.5, 0)); lab(ax, "F", F, (0.5, 0))
    dimarc(ax, A, D, -0.9, "4cm", 0.8, fs=9); dimarc(ax, B, C, 0.9, "6cm", 0.8, fs=9)
    ax.set_xlim(0.0, 9.2); ax.set_ylim(-1.6, 6.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
o2_trap("s3_o2.png")

# 応用＜3＞：平行四辺形ABCD、AE:ED=2:1、BEとACの交点F、BEの延長とCDの延長の交点G
def o3_para(name, size=(3.0, 2.4)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C, D = (2.0, 5.0), (0, 0), (9.0, 0), (11.0, 5.0)
    E = (A[0] + (D[0] - A[0]) * 2 / 3, 5.0)
    # 直線BEとCDの延長の交点G
    def inter(p1, p2, p3, p4):
        x1, y1 = p1; x2, y2 = p2; x3, y3 = p3; x4, y4 = p4
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    F = inter(B, E, A, C); G = inter(B, E, C, D)
    seg(ax, A, B, C, D, A); seg(ax, A, C, lw=1.1); seg(ax, B, G, lw=1.1); seg(ax, D, G, lw=1.1, ls="--")
    for p in (E, F, G): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (-0.3, 0.45)); lab(ax, "B", B, (-0.4, -0.45)); lab(ax, "C", C, (0.4, -0.45)); lab(ax, "D", D, (0.5, -0.2))
    lab(ax, "E", E, (-0.2, 0.5)); lab(ax, "F", F, (-0.1, -0.6)); lab(ax, "G", G, (0.45, 0.2))
    ax.set_xlim(-1.2, 14.0); ax.set_ylim(-1.2, G[1] + 0.9); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
    return G
print("G", o3_para("s3_o3.png"))

# 宿題＜1＞：△ABC、AB上のD、AC上のE、∠ADE＝∠ACB
def h3_anti(name, size=(2.4, 2.1)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C = (3.0, 6.0), (0, 0), (9.0, 0)
    D = (A[0] + (B[0] - A[0]) * 0.55, A[1] + (B[1] - A[1]) * 0.55); E = (A[0] + (C[0] - A[0]) * 0.33, A[1] + (C[1] - A[1]) * 0.33)
    seg(ax, A, B, C, A); seg(ax, D, E, lw=1.2)
    for p in (D, E): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (0, 0.55)); lab(ax, "B", B, (-0.45, -0.45)); lab(ax, "C", C, (0.45, -0.45)); lab(ax, "D", D, (-0.5, 0.1)); lab(ax, "E", E, (0.45, 0.25))
    angle_mark(ax, D, A, E, 0.8); angle_mark(ax, C, A, B, 1.1)
    ax.set_xlim(-1.2, 10.2); ax.set_ylim(-1.1, 7.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
h3_anti("h3_anti.png")

# 宿題＜2＞：DE//BC、AD=4, DB=2, AE=5, EC=x, DE=6, BC=y
def h3_par(name, ans=False, size=(2.6, 2.6)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C = (4.0, 7.5), (1.0, 0), (8.0, 0); t = 4 / 6
    D = (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t); E = (A[0] + (C[0] - A[0]) * t, A[1] + (C[1] - A[1]) * t)
    seg(ax, A, B, C, A); seg(ax, D, E, lw=1.3)
    for p in (D, E): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (0, 0.55)); lab(ax, "B", B, (-0.3, -0.55)); lab(ax, "C", C, (0.35, -0.55)); lab(ax, "D", D, (-1.7, 0.3)); lab(ax, "E", E, (1.7, 0.3))
    dimarc(ax, A, D, 1.2, "4cm", 1.0); dimarc(ax, D, B, 1.2, "2cm", 0.75)
    dimarc(ax, A, E, -1.2, "5cm", 1.0); dimarc(ax, E, C, -1.2, "$x$cm", 0.8)
    dimarc(ax, D, E, 0.6, "6cm", 0.8); dimarc(ax, B, C, 0.8, "$y$cm", 0.8)
    if ans:
        mark(ax, "circle", "2", (-0.6, 6.6)); times(ax, (-0.1, 6.4), (1.05, 5.8), "", -0.4); ax.text(0.5, 7.4, "×2", fontsize=9, ha="center", va="center")
        mark(ax, "circle", "1", (-2.3, 3.0)); times(ax, (-1.8, 2.75), (-0.75, 2.1), "", -0.4); ax.text(-1.3, 3.75, "×2", fontsize=9, ha="center", va="center")
        mark(ax, "box", "2", (9.1, 7.0)); times(ax, (8.6, 6.8), (7.35, 5.85), "", 0.4); ax.text(10.4, 7.5, r"$\times\frac{5}{2}$", fontsize=10, ha="center", va="center")
        mark(ax, "box", "1", (11.2, 3.3)); times(ax, (10.7, 3.05), (9.8, 2.2), "", 0.4); ax.text(12.5, 3.8, r"$\times\frac{5}{2}$", fontsize=10, ha="center", va="center")
        mark(ax, "tri", "2", (3.5, 0.7)); times(ax, (4.1, 0.75), (4.35, 1.4), "", 0.0); ax.text(5.5, 0.8, "×3", fontsize=9, ha="center", va="center")
        mark(ax, "tri", "3", (2.0, -2.4)); times(ax, (2.65, -2.4), (3.7, -1.3), "", 0.5); ax.text(4.6, -2.7, "×3", fontsize=9, ha="center", va="center")
    ax.set_xlim(-3.4 if ans else -2.4, 13.6 if ans else 10.6); ax.set_ylim(-3.0 if ans else -1.6, 8.7); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
h3_par("h3_par.png"); h3_par("h3_par_ans.png", ans=True)

# 宿題＜4＞：△ABC、AB上のD、AC上のE（AD=4, AB=12, AE=6, AC=8）。角の印なし、長さは問題文で示す
def h3_sas(name, size=(2.4, 2.1)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C = (3.0, 6.0), (0, 0), (9.0, 0)
    D = (A[0] + (B[0] - A[0]) * 0.45, A[1] + (B[1] - A[1]) * 0.45); E = (A[0] + (C[0] - A[0]) * 0.35, A[1] + (C[1] - A[1]) * 0.35)
    seg(ax, A, B, C, A); seg(ax, D, E, lw=1.2)
    for p in (D, E): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (0, 0.55)); lab(ax, "B", B, (-0.45, -0.45)); lab(ax, "C", C, (0.45, -0.45)); lab(ax, "D", D, (-0.5, 0.1)); lab(ax, "E", E, (0.45, 0.25))
    ax.set_xlim(-1.2, 10.2); ax.set_ylim(-1.1, 7.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
h3_sas("h3_sas.png")

# 宿題＜5＞：台形ABCD（AD//BC）、AD=6, BC=12、AE：EB=1：2、EF//BC。解説は対角線ACとEFの交点G
def h3_trap(name, ans=False, size=(2.8, 2.3)):
    """台形ABCD（AD//BC）、AD=6, BC=12、AE：EB=1：2、EF//BC。解説はAからDCに平行な線AH（EFとの交点G）"""
    fig, ax = plt.subplots(figsize=size)
    A, D, B, C = (3.0, 9.0), (9.0, 9.0), (0, 0), (12.0, 0)
    E, F = (2.0, 6.0), (10.0, 6.0)
    seg(ax, A, D, C, B, A); seg(ax, E, F, lw=1.3)
    for p in (E, F): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (-0.3, 0.6)); lab(ax, "D", D, (0.3, 0.6)); lab(ax, "B", B, (-0.5, -0.5)); lab(ax, "C", C, (0.5, -0.5))
    lab(ax, "E", E, (-0.7, 0)); lab(ax, "F", F, (0.7, 0))
    dimarc(ax, A, D, -1.1, "6cm", 0.9, fs=9); dimarc(ax, B, C, 1.6, "12cm", 1.2, fs=9)
    if ans:
        G, H = (4.0, 6.0), (6.0, 0)
        seg(ax, A, H, lw=1.1, ls="--")
        for p in (G, H): ax.plot(*p, "ko", ms=3.5, zorder=5)
        lab(ax, "G", G, (0.55, -0.6)); lab(ax, "H", H, (0, -0.6))
        dimarc(ax, E, G, 0.8, "2cm", 0.6, fs=8); dimarc(ax, G, F, -0.9, "6cm", 0.9, fs=8)
        dimarc(ax, B, H, -0.8, "6cm", 0.8, fs=8); dimarc(ax, H, C, -0.8, "6cm", 0.8, fs=8)
        mark(ax, "circle", "1", (1.0, 8.4), r=0.5); mark(ax, "circle", "2", (-0.7, 3.4), r=0.5)
        mark(ax, "box", "1", (3.0, 7.2), r=0.42); times(ax, (3.45, 7.1), (3.1, 5.35), "", -0.9); ax.text(4.5, 7.5, "×2", fontsize=9, ha="center", va="center")
        mark(ax, "box", "3", (2.4, 2.6), r=0.42); times(ax, (2.85, 2.5), (3.0, 1.15), "", -0.9); ax.text(4.0, 2.7, "×2", fontsize=9, ha="center", va="center")
    ax.set_xlim(-1.8, 13.8); ax.set_ylim(-2.5, 10.3); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
h3_trap("h3_trap.png"); h3_trap("h3_trap_ans.png", ans=True)


# 平行線と線分の比の2つの型（タケノコ型・チョウチョ型）。Naho の手書きの図と同じ形：
# 辺ごとに弧をかき、弧のまん中に〇・□・△の記号。全体の辺は外側の大きな弧。平行な辺には向きの印（＜）
def arcmark(ax, p, q, bulge, kind, digit, gap=0.55, pw=0.6):
    (x0, y0), (x1, y1) = p, q
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    L = np.hypot(x1 - x0, y1 - y0); ux, uy = (x1 - x0) / L, (y1 - y0) / L
    nx, ny = uy, -ux
    t = np.linspace(-1, 1, 300); f = (1 - t ** 2) ** pw
    xs = mx + ux * t * L / 2 + nx * bulge * f; ys = my + uy * t * L / 2 + ny * bulge * f
    k = np.abs(t) * L / 2 > gap
    ax.plot(xs[(t < 0) & k], ys[(t < 0) & k], "k", lw=0.9); ax.plot(xs[(t > 0) & k], ys[(t > 0) & k], "k", lw=0.9)
    mark(ax, kind, digit, (mx + nx * bulge, my + ny * bulge), r=0.38)

def para_arrow(ax, p, q):
    """平行の印：線分のまん中に「＜」"""
    mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
    ux, uy = (q[0] - p[0]), (q[1] - p[1]); L = np.hypot(ux, uy); ux, uy = ux / L, uy / L
    for s_ in (1, -1):
        ax.plot([mx, mx + 0.45 * ux + s_ * 0.3 * (-uy)], [my, my + 0.45 * uy + s_ * 0.3 * ux], "k", lw=1.0)

def two_types(name, size=(4.4, 2.6)):
    fig, ax = plt.subplots(figsize=size)
    # タケノコ型
    A, B, C = (3.5, 7.0), (0, 0), (7.0, 0); t = 2 / 3
    D = (A[0] + (B[0] - A[0]) * t, A[1] + (B[1] - A[1]) * t); E = (A[0] + (C[0] - A[0]) * t, A[1] + (C[1] - A[1]) * t)
    seg(ax, A, B, C, A); seg(ax, D, E, lw=1.3)
    para_arrow(ax, D, E); para_arrow(ax, B, C)
    arcmark(ax, A, D, 0.9, "circle", "2"); arcmark(ax, D, B, 0.8, "circle", "1", 0.45)
    arcmark(ax, A, B, 2.2, "circle", "3", 0.6, 0.45)
    arcmark(ax, A, E, -0.9, "box", "2"); arcmark(ax, E, C, -0.8, "box", "1", 0.45)
    arcmark(ax, A, C, -2.2, "box", "3", 0.6, 0.45)
    arcmark(ax, D, E, 0.8, "tri", "2", 0.6); arcmark(ax, B, C, 0.9, "tri", "3", 0.7)
    ax.text(3.5, -2.4, "タケノコ型", fontsize=11, ha="center", va="center", family="IPAGothic")
    # チョウチョ型（上の辺が短い）
    ox = 11.5
    P, Q, R, S = (ox + 1.4, 7.0), (ox + 4.6, 7.0), (ox + 0, 0), (ox + 6.0, 0)
    seg(ax, P, Q); seg(ax, R, S); seg(ax, P, S, lw=1.2); seg(ax, Q, R, lw=1.2)
    O = (ox + 3.0, 7.0 * 2 / 5 + 0.0 + 7.0 * 0)  # 交点（上：下 = 2：3）
    O = (P[0] + (S[0] - P[0]) * 0.4, P[1] + (S[1] - P[1]) * 0.4)
    para_arrow(ax, P, Q); para_arrow(ax, R, S)
    arcmark(ax, P, Q, -0.9, "circle", "2", 0.5); arcmark(ax, R, S, 0.9, "circle", "3", 0.6)
    arcmark(ax, P, O, 0.8, "box", "2", 0.45); arcmark(ax, O, S, -0.9, "box", "3", 0.5)
    arcmark(ax, Q, O, -0.8, "tri", "2", 0.45)
    arcmark(ax, O, R, 0.9, "tri", "3", 0.5)
    ax.text(ox + 3.0, -2.4, "チョウチョ型", fontsize=11, ha="center", va="center", family="IPAGothic")
    ax.set_xlim(-3.0, 19.2); ax.set_ylim(-3.1, 8.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
two_types("s3_types.png")


# ======================= 第3回（作り直し：相似の証明まで） =======================
def right_mark(ax, v, p, q, s=0.45):
    """頂点vの直角の印（v→p、v→q の方向に s だけの小さな四角）"""
    ux, uy = (p[0] - v[0]), (p[1] - v[1]); L = np.hypot(ux, uy); ux, uy = ux / L * s, uy / L * s
    wx, wy = (q[0] - v[0]), (q[1] - v[1]); M_ = np.hypot(wx, wy); wx, wy = wx / M_ * s, wy / M_ * s
    ax.plot([v[0] + ux, v[0] + ux + wx, v[0] + wx], [v[1] + uy, v[1] + uy + wy, v[1] + wy], "k", lw=0.9)

# 応用＜1＞：∠BAC＝90°の△ABC、AからBCに垂線AD。AB=6, BC=10
def o1_rt(name, size=(2.8, 1.9)):
    fig, ax = plt.subplots(figsize=size)
    B, C, A = (0, 0), (10, 0), (3.6, 4.8); D = (3.6, 0)
    seg(ax, A, B, C, A); seg(ax, A, D, lw=1.2)
    ax.plot(*D, "ko", ms=3.5, zorder=5)
    right_mark(ax, A, B, C); right_mark(ax, D, A, C)
    lab(ax, "A", A, (0, 0.55)); lab(ax, "B", B, (-0.45, -0.4)); lab(ax, "C", C, (0.45, -0.4)); lab(ax, "D", D, (0, -0.55))
    dimarc(ax, A, B, 1.0, "6cm", 0.8, fs=9); dimarc(ax, B, C, 1.5, "10cm", 1.0, fs=9)
    ax.set_xlim(-1.6, 11.2); ax.set_ylim(-2.4, 5.8); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
o1_rt("s3b_o1.png")

# 応用＜2＞：y=x^2、A(-1,1)、B(3,9)、直線AB。解説：Oを通りABに平行な直線 y=2x とPの位置、Q(0,6)
def o2_eq(name, ans=False, size=(2.6, 3.0)):
    fig, ax = plt.subplots(figsize=size)
    ax.annotate("", xy=(4.3, 0), xytext=(-3.0, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 11.4), xytext=(0, -1.2), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    xs = np.linspace(-2.6, 3.25, 300); ax.plot(xs, xs ** 2, "k", lw=1.5)
    lx = np.linspace(-2.3, 3.8, 10); ax.plot(lx, 2 * lx + 3, "k", lw=1.3)
    ax.plot([-1, 0, 3], [1, 0, 9], "k", lw=1.0)
    pts = [(-1, 1), (3, 9)]
    ax.text(-1.25, 1.3, "A", fontsize=11, ha="right", va="center", family="serif")
    ax.text(2.75, 9.4, "B", fontsize=11, ha="right", va="center", family="serif")
    if ans:
        ox = np.linspace(-0.6, 3.4, 10); ax.plot(ox, 2 * ox, "k--", lw=1.0)
        pts += [(2, 4), (0, 3), (0, 6)]
        ax.text(2.25, 3.6, "P", fontsize=11, ha="left", va="center", family="serif")
        ax.text(-0.2, 3.0, "C", fontsize=11, ha="right", va="center", family="serif")
        ax.text(-0.2, 6.0, "Q", fontsize=11, ha="right", va="center", family="serif")
        ax.text(3.45, 6.4, "$y=2x$", fontsize=9, ha="left", va="center")
    for p in pts: ax.plot(*p, "ko", ms=3.5, zorder=5)
    ax.text(-0.45, -0.75, "O", fontsize=10, family="serif")
    ax.text(4.15, -0.8, "x", fontsize=12, style="italic", family="serif")
    ax.text(0.2, 11.0, "y", fontsize=12, style="italic", family="serif")
    ax.text(-2.8, 10.4, "$y=x^2$", fontsize=9)
    ax.set_xlim(-3.4, 5.0); ax.set_ylim(-1.4, 11.8); ax.set_aspect(0.55); ax.axis("off")
    save(fig, name)
o2_eq("s3b_o2.png"); o2_eq("s3b_o2_ans.png", ans=True)

# 応用＜3＞：平行四辺形ABCD、AD上のE（AE：ED＝2：1）、BEとACの交点F
def o3_pf(name, ans=False, size=(2.8, 1.8)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C, D = (2.0, 5.0), (0, 0), (9.0, 0), (11.0, 5.0)
    E = (A[0] + (D[0] - A[0]) * 2 / 3, 5.0)
    F = (A[0] + (C[0] - A[0]) * 0.4, A[1] + (C[1] - A[1]) * 0.4)
    seg(ax, A, B, C, D, A); seg(ax, A, C, lw=1.1); seg(ax, B, E, lw=1.1)
    for p in (E, F): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (-0.3, 0.45)); lab(ax, "B", B, (-0.4, -0.45)); lab(ax, "C", C, (0.4, -0.45)); lab(ax, "D", D, (0.4, 0.45))
    lab(ax, "E", E, (0, 0.5)); lab(ax, "F", F, (0.05, -0.65))
    if ans:
        angle_mark(ax, E, F, A, 0.8); angle_mark(ax, B, F, C, 1.1)          # 錯角（●）
        angle_mark(ax, A, F, E, 0.8, 2); angle_mark(ax, C, F, B, 0.9, 2)    # 錯角（〇〇）
    ax.set_xlim(-1.2, 12.2); ax.set_ylim(-1.2, 6.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
o3_pf("s3b_o3.png"); o3_pf("s3b_o3_ans.png", ans=True)

# 宿題＜5＞：∠ACB＝90°の△ABC、CからABに垂線CH。AC=6, AB=9
def h3_rt(name, size=(2.6, 1.8)):
    fig, ax = plt.subplots(figsize=size)
    A, B = (0, 0), (9, 0); C = (4.0, 20 ** 0.5); H = (4.0, 0)
    seg(ax, A, B, C, A); seg(ax, C, H, lw=1.2)
    ax.plot(*H, "ko", ms=3.5, zorder=5)
    right_mark(ax, C, A, B); right_mark(ax, H, C, B)
    lab(ax, "A", A, (-0.45, -0.4)); lab(ax, "B", B, (0.45, -0.4)); lab(ax, "C", C, (0, 0.55)); lab(ax, "H", H, (0, -0.55))
    dimarc(ax, C, A, 1.0, "6cm", 0.8, fs=9); dimarc(ax, A, B, 1.4, "9cm", 0.9, fs=9)
    ax.set_xlim(-1.6, 10.4); ax.set_ylim(-2.3, 5.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
h3_rt("h3b_rt.png")


# ======================= 第3回 発展プリント =======================
# ＜1＞ y=x^2、A(-1,1)、B(2,4)、直線ABとx軸の交点C(-2,0)。△OBCをx軸のまわりに回転
def adv1(name, ans=False, size=(2.6, 2.4)):
    fig, ax = plt.subplots(figsize=size)
    ax.annotate("", xy=(3.4, 0), xytext=(-3.2, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 5.4 if not ans else 5.4), xytext=(0, -4.6 if ans else -0.8), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    xs = np.linspace(-2.2, 2.25, 300); ax.plot(xs, xs ** 2, "k", lw=1.5)
    lx = np.linspace(-2.6, 2.8, 10); ax.plot(lx, lx + 2, "k", lw=1.3)
    ax.add_patch(Polygon([(0, 0), (-2, 0), (2, 4)], closed=True, fill=False, hatch="////", edgecolor="k", lw=1.0))
    if ans:
        ax.plot([-2, 2, 0], [0, -4, 0], "k--", lw=1.0)
        ax.plot([2, 2], [-4, 4], "k--", lw=1.0)
        t = np.linspace(0, 2 * np.pi, 200); ax.plot(2 + 0.5 * np.cos(t), 4 * np.sin(t), "k", lw=0.8)
        ax.plot(2, 0, "ko", ms=3)
        ax.text(2.25, -0.4, "H", fontsize=10, family="serif")
    for p in ((-1, 1), (2, 4), (-2, 0)): ax.plot(*p, "ko", ms=3.5, zorder=5)
    ax.text(-1.25, 1.3, "A", fontsize=11, ha="right", va="center", family="serif")
    ax.text(1.75, 4.4, "B", fontsize=11, ha="right", va="center", family="serif")
    ax.text(-2.1, 0.45, "C", fontsize=11, ha="right", va="center", family="serif")
    ax.text(0.15, -0.5, "O", fontsize=10, family="serif")
    ax.text(3.25, -0.55, "x", fontsize=12, style="italic", family="serif")
    ax.text(0.15, 5.1, "y", fontsize=12, style="italic", family="serif")
    ax.text(-2.9, 4.8, "$y=x^2$", fontsize=9)
    ax.set_xlim(-3.4, 3.8); ax.set_ylim(-4.8 if ans else -1.0, 5.7); ax.set_aspect(0.8); ax.axis("off")
    save(fig, name)
adv1("s3c_1.png"); adv1("s3c_1_ans.png", ans=True)

# ＜2＞ 長方形ABCD（AB=8, BC=12）。PはBからCへ毎秒2cm、QはCからDへ毎秒1cm。△PCQ
def adv2(name, size=(2.6, 1.9)):
    fig, ax = plt.subplots(figsize=size)
    w, h = 12, 8; px, qy = 4.0, 2.0
    ax.add_patch(Polygon([(px, 0), (w, 0), (w, qy)], closed=True, fill=False, hatch="////", edgecolor="k", lw=1.2))
    ax.plot([0, 0, w, w, 0], [h, 0, 0, h, h], "k", lw=1.5)
    corners(ax, w, h)
    dimarc(ax, (0, h), (w, h), -1.3, f"{w}cm", 1.2); dimarc(ax, (0, h), (0, 0), 1.3, f"{h}cm", 1.0)
    point(ax, (px, 0), "P", (0, -0.9), ((-0.8, -1.9), (1.4, -1.9)))
    point(ax, (w, qy), "Q", (0.9, 0), ((1.9, -0.6), (1.9, 1.6)))
    ax.set_xlim(-3.0, w + 3.0); ax.set_ylim(-2.8, h + 2.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
adv2("s3c_2.png")

# ＜3＞ 正三角形ABC、BC上のD、AC上のE、∠ADE=60°
def adv3(name, ans=False, size=(2.4, 2.2)):
    fig, ax = plt.subplots(figsize=size)
    s_ = 9.0; B, C = (0, 0), (s_, 0); A = (s_ / 2, s_ * 3 ** 0.5 / 2)
    D = (3.0, 0)
    # CE = 2（AB=9, BD=3 のとき）
    E = (C[0] + (A[0] - C[0]) * 2 / 9, C[1] + (A[1] - C[1]) * 2 / 9)
    seg(ax, A, B, C, A); seg(ax, A, D, lw=1.2); seg(ax, D, E, lw=1.2)
    for p in (D, E): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (0, 0.6)); lab(ax, "B", B, (-0.5, -0.4)); lab(ax, "C", C, (0.5, -0.4)); lab(ax, "D", D, (0, -0.6)); lab(ax, "E", E, (0.55, 0.3))
    angle_mark(ax, D, A, E, 0.9)
    if ans:
        angle_mark(ax, B, A, C, 1.0); angle_mark(ax, C, A, B, 1.0)
        angle_mark(ax, A, B, D, 1.3, 2); angle_mark(ax, D, E, C, 1.3, 2)
    ax.set_xlim(-1.4, 10.4); ax.set_ylim(-1.3, 8.9); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
adv3("s3c_3.png"); adv3("s3c_3_ans.png", ans=True)

# 基本＜5＞：△ABC∽△DEF（相似比 4：5）。∠A=∠D=50°、∠B=∠E=70°、AB=8cm、EF=15cm
def k5_pair(name, size=(3.4, 1.8)):
    fig, ax = plt.subplots(figsize=size)
    import math
    A_, B_ = math.radians(50), math.radians(70)
    def tri(ox, k):
        AB = 8 * k
        B = (ox, 0)
        # Cは B から角70°方向、A は ... ここでは BC を底辺に置く
        C_ = math.pi - A_ - B_
        BC = AB * math.sin(A_) / math.sin(C_)
        C = (ox + BC, 0)
        A = (ox + AB * math.cos(B_), AB * math.sin(B_))
        return A, B, C
    s = 0.55
    A, B, C = tri(0, s); D, E, F = tri(7.0, s * 1.25)
    for (P1, P2, P3), names in (((A, B, C), "ABC"), ((D, E, F), "DEF")):
        seg(ax, P1, P2, P3, P1)
        lab(ax, names[0], P1, (0, 0.5)); lab(ax, names[1], P2, (-0.45, -0.35)); lab(ax, names[2], P3, (0.45, -0.35))
    dimarc(ax, A, B, 0.6, "8cm", 0.6, fs=9)
    dimarc(ax, E, F, 0.7, "15cm", 0.8, fs=9)
    ax.text(A[0] + 0.05, A[1] - 1.7, "50°", fontsize=8, ha="center", va="center")
    ax.text(E[0] + 1.55, E[1] + 0.5, "70°", fontsize=8, ha="center", va="center")
    angle_mark(ax, A, B, C, 0.7); angle_mark(ax, E, D, F, 0.8)
    ax.set_xlim(-1.2, 15.0); ax.set_ylim(-1.8, 6.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
k5_pair("s3b_k5.png")


# ======================= 第4回（大問の特訓） =======================
import math as _m
def tri_pair_r(name, k=4/3, AB=9, EF=16, angA=50, angB=70, size=(3.4, 1.9)):
    fig, ax = plt.subplots(figsize=size)
    A_, B_ = _m.radians(angA), _m.radians(angB); C_ = _m.pi - A_ - B_
    def tri(ox, s):
        ab = AB * s; bc = ab * _m.sin(A_) / _m.sin(C_)
        B = (ox, 0); C = (ox + bc, 0); A = (ox + ab * _m.cos(B_), ab * _m.sin(B_)); return A, B, C
    s = 0.5
    A, B, C = tri(0, s); D, E, F = tri(7.2, s * k)
    for (P1, P2, P3), nm in (((A, B, C), "ABC"), ((D, E, F), "DEF")):
        seg(ax, P1, P2, P3, P1)
        lab(ax, nm[0], P1, (0, 0.5)); lab(ax, nm[1], P2, (-0.45, -0.35)); lab(ax, nm[2], P3, (0.45, -0.35))
    dimarc(ax, A, B, 0.6, f"{AB}cm", 0.6, fs=9); dimarc(ax, E, F, 0.7, f"{EF}cm", 0.8, fs=9)
    ax.set_xlim(-1.2, 16.5); ax.set_ylim(-1.8, 6.8); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
tri_pair_r("s4_k5.png")

# 応用＜1＞ タイル：n番目は1辺(n+1)枚の正方形。まわりが灰色、内側が白
def tiles(name, ns=(1, 2, 3), size=(3.6, 1.6)):
    fig, ax = plt.subplots(figsize=size)
    ox = 0
    for n in ns:
        m = n + 1
        for i in range(m):
            for j in range(m):
                edge = i in (0, m - 1) or j in (0, m - 1)
                ax.add_patch(Rectangle((ox + i, j), 1, 1, facecolor="#9a9a9a" if edge else "white", edgecolor="k", lw=0.8))
        ax.text(ox + m / 2, -0.8, f"{n}番目", fontsize=9, ha="center", va="center")
        ox += m + 1.5
    ax.text(ox - 0.3, 1.5, "…", fontsize=12, ha="center", va="center")
    ax.set_xlim(-0.5, ox + 0.5); ax.set_ylim(-1.4, 4.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
tiles("s4_tiles.png")

# 応用＜2＞ 正方形ABCD（1辺6cm）。PはA→Bを毎秒1cm、QはA→D→Cを毎秒2cm
def sq2(name, size=(2.2, 2.2)):
    fig, ax = plt.subplots(figsize=size)
    s_ = 6
    ax.add_patch(Polygon([(0, s_), (0, s_ - 2), (4, s_)], closed=True, fill=False, hatch="////", edgecolor="k", lw=1.2))
    ax.plot([0, 0, s_, s_, 0], [s_, 0, 0, s_, s_], "k", lw=1.5)
    corners(ax, s_, s_)
    dimarc(ax, (s_, s_), (s_, 0), -1.0, f"{s_}cm", 0.9)
    point(ax, (0, s_ - 2), "P", (-0.7, 0), ((-1.5, 0.6), (-1.5, -0.9)))
    point(ax, (4, s_), "Q", (0, 0.65), ((3.0 - 4, 1.6), (5.2 - 4, 1.6)))
    ax.set_xlim(-2.4, s_ + 2.0); ax.set_ylim(-1.0, s_ + 2.4); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
sq2("s4_sq.png")

# グラフ用の方眼（x:0〜6秒、y:0〜18cm²）
def area_grid(name, pts=None, size=(2.5, 2.9)):
    fig, ax = plt.subplots(figsize=size)
    for v in range(0, 7): ax.plot([v, v], [0, 18 / 3], color="#b0b0b0", lw=0.6)
    for v in range(0, 19, 2): ax.plot([0, 6], [v / 3, v / 3], color="#b0b0b0", lw=0.6)
    ax.annotate("", xy=(6.8, 0), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 6.8), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    for t in range(1, 7): ax.text(t, -0.35, str(t), fontsize=8, ha="center", va="center", family="serif")
    for t in range(2, 19, 2): ax.text(-0.3, t / 3, str(t), fontsize=8, ha="right", va="center", family="serif")
    ax.text(-0.3, -0.35, "O", fontsize=9, ha="center", va="center", family="serif")
    ax.text(6.9, 0.35, "$x$", fontsize=11); ax.text(6.9, -0.5, "(秒)", fontsize=7)
    ax.text(0, 7.2, "(cm²) $y$", fontsize=9, ha="center")
    if pts:
        xs = np.linspace(0, 3, 50); ax.plot(xs, xs ** 2 / 3, "k", lw=1.8)
        ax.plot([3, 6], [9 / 3, 18 / 3], "k", lw=1.8)
    ax.set_xlim(-1.4, 7.6); ax.set_ylim(-0.8, 7.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
area_grid("h4_grid.png"); area_grid("h4_grid_ans.png", pts=True)

# 応用＜3＞ y=1/2x^2、A(-2,2)、B(4,8)、平行四辺形OACB（C(2,10)）
def par_ob(name, ans=False, size=(2.5, 3.0)):
    fig, ax = plt.subplots(figsize=size)
    ax.annotate("", xy=(5.6, 0), xytext=(-4.4, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 12.0), xytext=(0, -1.0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    xs = np.linspace(-4.0, 4.6, 300); k = xs ** 2 / 2 <= 11.0; ax.plot(xs[k], xs[k] ** 2 / 2, "k", lw=1.5)
    O, A, B, C = (0, 0), (-2, 2), (4, 8), (2, 10)
    ax.plot([O[0], A[0], C[0], B[0], O[0]], [O[1], A[1], C[1], B[1], O[1]], "k", lw=1.3)
    for p in (A, B, C): ax.plot(*p, "ko", ms=3.5, zorder=5)
    ax.text(-2.3, 2.3, "A", fontsize=11, ha="right", va="center", family="serif")
    ax.text(4.3, 7.8, "B", fontsize=11, ha="left", va="center", family="serif")
    ax.text(1.7, 10.5, "C", fontsize=11, ha="right", va="center", family="serif")
    if ans:
        ax.plot([-2, 4], [2, 8], "k--", lw=1.0)
        for p, nm in (((0, 4), "(0, 4)"), ((0, 20 / 3), "P")):
            ax.plot(*p, "ks", ms=3.5, zorder=5)
        ax.text(0.25, 3.4, "(0, 4)", fontsize=8, ha="left", va="center")
        ax.text(-0.25, 20 / 3, "P", fontsize=11, ha="right", va="center", family="serif")
        ax.plot([-2, 0, 4], [2, 20 / 3, 8], "k:", lw=1.1)
    ax.text(-0.5, -0.7, "O", fontsize=10, family="serif")
    ax.text(5.4, -0.8, "x", fontsize=12, style="italic", family="serif")
    ax.text(0.25, 11.6, "y", fontsize=12, style="italic", family="serif")
    ax.text(-4.2, 10.6, "$y=\\frac{1}{2}x^2$", fontsize=9)
    ax.set_xlim(-4.8, 6.0); ax.set_ylim(-1.2, 12.4); ax.set_aspect(0.55); ax.axis("off")
    save(fig, name)
par_ob("s4_par.png"); par_ob("s4_par_ans.png", ans=True)

# 宿題＜1＞ 碁石の正三角形（n番目は1辺n個）
def stones(name, ns=(1, 2, 3, 4), size=(3.6, 1.5)):
    fig, ax = plt.subplots(figsize=size)
    ox = 0
    for n in ns:
        for r in range(n):
            for c in range(r + 1):
                ax.add_patch(matplotlib.patches.Circle((ox + c - r / 2 + (n - 1) / 2, n - 1 - r), 0.38, facecolor="k"))
        ax.text(ox + (n - 1) / 2, -1.0, f"{n}番目", fontsize=9, ha="center", va="center")
        ox += n + 1.4
    ax.text(ox - 0.2, 1.0, "…", fontsize=12, ha="center", va="center")
    ax.set_xlim(-0.8, ox + 0.5); ax.set_ylim(-1.6, 4.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
stones("h4_stones.png")

# 宿題＜3＞ y=x^2、A(-2,4)、B(1,1)
pfig("h4_p.png", 1.0, (-3.0, 2.8), (-0.8, 6.2), [("A", (-2, 4), (-0.35, 0.3)), ("B", (1, 1), (0.35, -0.35))],
     lines=[(-1, 2, -2.6, 2.2)], segs=[((-2, 4), (0, 0)), ((0, 0), (1, 1))], eqs=[("$y=x^2$", (2.2, 5.6))], aspect=0.75)
pfig("h4_p_ans.png", 1.0, (-3.0, 2.8), (-0.8, 6.2), [("A", (-2, 4), (-0.35, 0.3)), ("B", (1, 1), (0.35, -0.35)), ("M", (-0.5, 2.5), (0.1, 0.45))],
     lines=[(-1, 2, -2.6, 2.2)], segs=[((-2, 4), (0, 0)), ((0, 0), (1, 1))], dashed=[((0, 0), (-0.6, 3.0))], hatch=[(0, 0), (-2, 4), (-0.5, 2.5)],
     eqs=[("$y=x^2$", (2.2, 5.6))], aspect=0.75)

# 宿題＜4＞ △ABC、AB上のD、∠ACD=∠ABC
def h4_tri(name, size=(2.4, 2.0)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C = (0, 0), (9, 0), (3.0, 4.6)
    D = (4, 0)
    seg(ax, A, B, C, A); seg(ax, C, D, lw=1.2); ax.plot(*D, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (-0.45, -0.35)); lab(ax, "B", B, (0.45, -0.35)); lab(ax, "C", C, (0, 0.55)); lab(ax, "D", D, (0, -0.55))
    angle_mark(ax, C, A, D, 0.9); angle_mark(ax, B, A, C, 1.3)
    ax.set_xlim(-1.2, 10.2); ax.set_ylim(-1.2, 5.6); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
h4_tri("h4_tri.png")

# 発展＜1＞ y=1/2x^2、A(-2,2)、B(4,8)、Oを通りABに平行な直線 y=x とQ(2,2)
def adv4_1(name, ans=False, size=(2.5, 2.9)):
    fig, ax = plt.subplots(figsize=size)
    ax.annotate("", xy=(5.6, 0), xytext=(-4.0, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 10.4), xytext=(0, -1.0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    xs = np.linspace(-3.8, 4.4, 300); ax.plot(xs, xs ** 2 / 2, "k", lw=1.5)
    lx = np.linspace(-3.4, 5.2, 10); ax.plot(lx, lx + 4, "k", lw=1.2)
    ax.plot([-2, 0, 4], [2, 0, 8], "k", lw=1.0)
    for p in ((-2, 2), (4, 8)): ax.plot(*p, "ko", ms=3.5, zorder=5)
    ax.text(-2.3, 2.3, "A", fontsize=11, ha="right", va="center", family="serif")
    ax.text(3.7, 8.5, "B", fontsize=11, ha="right", va="center", family="serif")
    if ans:
        ox = np.linspace(-0.8, 3.4, 10); ax.plot(ox, ox, "k--", lw=1.0)
        ax.plot(2, 2, "ko", ms=3.5, zorder=5); ax.text(2.3, 1.7, "Q(2, 2)", fontsize=8, ha="left", va="center")
        ax.plot([-2, 2, 4], [2, 2, 8], "k:", lw=1.0)
        ax.text(3.5, 3.6, "$y=x$", fontsize=8, ha="left")
    ax.text(-0.5, -0.7, "O", fontsize=10, family="serif"); ax.text(5.4, -0.8, "x", fontsize=12, style="italic", family="serif")
    ax.text(0.25, 10.0, "y", fontsize=12, style="italic", family="serif"); ax.text(-3.9, 9.2, "$y=\\frac{1}{2}x^2$", fontsize=9)
    ax.set_xlim(-4.4, 6.0); ax.set_ylim(-1.2, 10.8); ax.set_aspect(0.6); ax.axis("off")
    save(fig, name)
adv4_1("a4_1.png"); adv4_1("a4_1_ans.png", ans=True)

# 発展＜3＞ 平行四辺形ABCD、BC上のE（BE:EC=3:2）、AEとBDの交点F
def adv4_3(name, ans=False, size=(2.8, 1.8)):
    fig, ax = plt.subplots(figsize=size)
    A, B, C, D = (2.0, 5.0), (0, 0), (10.0, 0), (12.0, 5.0)
    E = (6.0, 0)
    # F = AE ∩ BD : AF:FE = AD:BE = 10:6 = 5:3
    F = (A[0] + (E[0] - A[0]) * 5 / 8, A[1] + (E[1] - A[1]) * 5 / 8)
    seg(ax, A, B, C, D, A); seg(ax, A, E, lw=1.1); seg(ax, B, D, lw=1.1)
    for p in (E, F): ax.plot(*p, "ko", ms=3.5, zorder=5)
    lab(ax, "A", A, (-0.3, 0.45)); lab(ax, "B", B, (-0.4, -0.45)); lab(ax, "C", C, (0.4, -0.45)); lab(ax, "D", D, (0.4, 0.45))
    lab(ax, "E", E, (0, -0.55)); lab(ax, "F", F, (0.55, 0.1))
    if ans:
        angle_mark(ax, A, F, D, 0.8); angle_mark(ax, E, F, B, 0.9)
        angle_mark(ax, D, F, A, 0.9, 2); angle_mark(ax, B, F, E, 1.0, 2)
    ax.set_xlim(-1.2, 13.2); ax.set_ylim(-1.2, 6.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
adv4_3("a4_3.png"); adv4_3("a4_3_ans.png", ans=True)
