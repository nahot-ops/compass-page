import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import numpy as np
plt.rcParams["font.family"] = ["IPAGothic"]
from PIL import Image, ImageOps, ImageEnhance
import sys
OUT = "img/"

# logo grayscale
im = Image.open(sys.argv[1]).convert("RGBA")
bg = Image.new("RGBA", im.size, "white"); bg.alpha_composite(im)
g = ImageOps.grayscale(bg.convert("RGB"))
g = ImageEnhance.Contrast(g).enhance(1.6)
g.save(OUT + "logo_gray.png")


def segdist(p, s):
    (x, y), (x1, y1, x2, y2) = p, s
    dx, dy = x2 - x1, y2 - y1
    t = 0 if dx == dy == 0 else max(0, min(1, ((x - x1) * dx + (y - y1) * dy) / (dx * dx + dy * dy)))
    return np.hypot(x - (x1 + t * dx), y - (y1 + t * dy))


class Fig:
    """線を「障害物」として覚えておき、文字は線からいちばん離れた候補位置に置く"""

    def __init__(self, size, xlim, ylim):
        self.fig, self.ax = plt.subplots(figsize=size)
        self.ax.set_xlim(*xlim); self.ax.set_ylim(*ylim)
        self.segs, self.labels = [], []
        self.white = False  # 方眼のときだけ文字の下を白くぬる

    def seg(self, x1, y1, x2, y2, obstacle=True, **kw):
        self.ax.plot([x1, x2], [y1, y2], color="k", lw=kw.get("lw", 1.6), ls=kw.get("ls", "-"), zorder=kw.get("zorder", 2))
        if obstacle: self.segs.append((x1, y1, x2, y2))

    def arrow(self, x1, y1, x2, y2):
        self.ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
        self.segs.append((x1, y1, x2, y2))

    def line(self, a, b, x0, x1, y0, y1, **kw):
        # y=ax+b を枠 [x0,x1]×[y0,y1] で切って描く
        xs = np.linspace(x0, x1, 2001); ys = a * xs + b
        k = (ys >= y0) & (ys <= y1)
        if k.any():
            self.seg(xs[k][0], ys[k][0], xs[k][-1], ys[k][-1], **kw)
            return (xs[k][0], ys[k][0], xs[k][-1], ys[k][-1])

    def text(self, s, anchor, cands, size=12, style="normal", family="serif", r=0.35, rot=0):
        best, bs = None, -1
        for i, (dx, dy) in enumerate(cands):
            p = (anchor[0] + dx, anchor[1] + dy)
            d = min([segdist(p, sg) for sg in self.segs] + [np.hypot(p[0] - q[0], p[1] - q[1]) - r for q in self.labels] + [9])
            score = min(d, 3 * r) - i * 0.002  # 十分離れていれば先の候補を優先
            if score > bs: best, bs = p, score
        self.labels.append(best)
        self.ax.text(*best, s, fontsize=size, style=style, family=family, ha="center", va="center", zorder=6, rotation=rot,
                     bbox=dict(boxstyle="square,pad=0.08", fc="white", ec="none") if self.white else None)
        return best

    def dot(self, p, m="o", ms=3.5):
        self.ax.plot(*p, "k" + m, ms=ms, zorder=7)

    def save(self, name):
        self.ax.set_aspect("equal"); self.ax.axis("off")
        self.fig.savefig(OUT + name, dpi=200, bbox_inches="tight", pad_inches=0.05); plt.close(self.fig)


def around(d, n=12, start=0):
    return [(d * np.cos(start + 2 * np.pi * k / n), d * np.sin(start + 2 * np.pi * k / n)) for k in range(n)]


# ---------- 方眼のグラフ ----------
LIM = 6
def gridfig(lines=(), size=(3.2, 3.2)):
    f = Fig(size, (-LIM - 0.9, LIM + 1.1), (-LIM - 0.9, LIM + 1.1))
    f.white = True
    for v in range(-LIM, LIM + 1):
        f.ax.plot([v, v], [-LIM, LIM], color="#b0b0b0", lw=0.6, zorder=0)
        f.ax.plot([-LIM, LIM], [v, v], color="#b0b0b0", lw=0.6, zorder=0)
    f.arrow(-LIM - 0.4, 0, LIM + 0.8, 0); f.arrow(0, -LIM - 0.4, 0, LIM + 0.8)
    ends = [f.line(a, b, -LIM, LIM, -LIM, LIM, **kw) for (a, b, kw) in lines]
    return f, ends

def gridlabels(f):
    f.text("x", (LIM + 0.8, 0), [(0.15, -0.55), (0.15, 0.55)], size=13, style="italic")
    f.text("y", (0, LIM + 0.8), [(0.55, 0), (-0.55, 0)], size=13, style="italic")
    f.text("O", (0, 0), [(-0.45, -0.5), (0.45, -0.5), (-0.45, 0.5), (0.45, 0.5)], size=11, r=0.3)
    for v in (5, -5):
        f.text(str(v), (v, 0), [(0, -0.55), (0, 0.55)], size=10, r=0.3)
        f.text(str(v), (0, v), [(-0.6, 0), (0.6, 0)], size=10, r=0.3)

def linelabel(f, s, end):
    # 直線の端（枠の上か下）の外側に番号を置く
    x1, y1, x2, y2 = end
    ex, ey = (x2, y2) if y2 >= y1 else (x1, y1)
    if abs(ey) < LIM - 0.01:  # 左右の枠で切れたとき
        ex, ey = (x2, y2) if x2 > x1 else (x1, y1)
    f.text(s, (ex, ey), [(0, 0.55), (0.55, 0.3), (-0.55, 0.3), (0.6, 0), (-0.6, 0), (0.55, -0.3)], size=13, family="IPAGothic", r=0.4)

def graph(name, lines, labs, dots=(), extra=None):
    f, ends = gridfig([(a, b, {}) for a, b in lines])
    if extra: extra(f)
    for p in dots: f.dot(p)
    for s, e in zip(labs, ends): linelabel(f, s, e)
    gridlabels(f)
    f.save(name)

graph("grid_blank.png", [], [])
graph("j1_read.png", [(2, -3), (-0.5, 2)], ["①", "②"])
graph("h_read.png", [(-2, 3), (0.5, -2)], ["①", "②"])
graph("o_graph_ans.png", [(-2 / 3, 2), (2, -3)], ["①", "②"], dots=[(0, 2), (3, 0), (0, -3), (1, -1)])
def steps(f):
    f.seg(0, -2, 4, -2, ls=":", lw=1.3); f.seg(4, -2, 4, 1, ls=":", lw=1.3)
# 「右へ4」「上へ3」は steps の後で置く
f, ends = gridfig([(0.75, -2, {}), (-0.5, 2, {}), (0, -3, {})])
steps(f)
for p in [(0, -2), (4, 1), (0, 2), (4, 0)]: f.dot(p)
f.text("右へ4", (2, -2), [(0, 0.45), (0, -0.45)], size=8, family="IPAGothic", r=0.3)
f.text("上へ3", (4, -1.3), [(0.95, 0), (-0.95, 0)], size=8, family="IPAGothic", r=0.3)
for s, e in zip(["①", "②", "③"], ends): linelabel(f, s, e)
gridlabels(f)
f.save("h_graph_ans.png")


# ---------- 2直線と三角形 ----------
def trifig(name, xlim, ylim, L1, L2, A, B, C, size, extra=None, shade=False, names=("A", "B", "C")):
    f = Fig(size, xlim, ylim)
    x0, x1 = xlim[0] + 0.3, xlim[1] - 0.6
    y0, y1 = ylim[0] + 0.2, ylim[1] - 0.6
    if shade: f.ax.add_patch(Polygon([A, B, C], closed=True, color="#cfcfcf", zorder=0))
    f.arrow(xlim[0] + 0.2, 0, xlim[1] - 0.3, 0); f.arrow(0, ylim[0] + 0.1, 0, ylim[1] - 0.2)
    e1 = f.line(L1[0], L1[1], x0, x1, y0, y1); e2 = f.line(L2[0], L2[1], x0, x1, y0, y1)
    if extra: extra(f)
    for p in (A, B, C): f.dot(p)
    pts = around(0.8, 16, np.pi / 16)
    for p, nm in zip((A, B, C), names): f.text(nm, p, pts)
    for (s, e) in ((L1[2], e1), (L2[2], e2)):
        ex, ey = (e[2], e[3]) if e[3] > e[1] else (e[0], e[1])
        f.text(s, (ex, ey), around(0.6, 12), size=13, style="italic", family=("IPAGothic" if s == "ℓ" else "serif"), r=0.4)
    f.text("x", (xlim[1] - 0.3, 0), [(0.1, -0.55), (0.1, 0.55)], size=13, style="italic")
    f.text("y", (0, ylim[1] - 0.2), [(0.5, -0.1), (-0.5, -0.1)], size=13, style="italic")
    if "O" not in names: f.text("O", (0, 0), [(-0.45, -0.55), (0.45, -0.55), (-0.5, 0.5)], size=11, r=0.3)
    f.save(name)

T1 = dict(xlim=(-4.5, 9.2), ylim=(-1.6, 8.2), L1=(2, 4, "ℓ"), L2=(-1, 7, "m"), A=(1, 6), B=(-2, 0), C=(7, 0), size=(3.4, 2.6))
trifig("o1_tri.png", **T1)
def ex1(f):
    f.seg(1, 0, 1, 6, ls="--", lw=1)
    f.seg(1, 6, 2.6, -0.4, ls="-.", lw=1.2)   # A と BC の中点 M
    f.seg(-2, 0, 4.6, 3.3, ls=":", lw=1.3)              # B と AC の中点 N
    f.dot((2.5, 0), "s", 3); f.dot((4, 3), "s", 3)
    f.text("M", (2.5, 0), around(0.6, 16, np.pi / 16), size=10)
    f.text("N", (4, 3), around(0.6, 16, np.pi / 16), size=10)
    f.text("高さ6", (1, 3.5), [(-0.45, 0)], size=8, family="IPAGothic", r=0.3, rot=90)
    f.text("底辺9", (2.5, 0), [(1.6, -0.7), (-1.6, -0.7), (0, -0.75)], size=9, family="IPAGothic", r=0.45)
trifig("o1_tri_ans.png", **T1, extra=ex1, shade=True)

T2 = dict(xlim=(-8.2, 8.8), ylim=(-1.6, 7.8), L1=(-1, 6, "ℓ"), L2=(0.5, 3, "m"), A=(2, 4), B=(-6, 0), C=(6, 0), size=(3.6, 2.4))
trifig("h_tri.png", **T2)
def ex2(f):
    f.seg(2, 0, 2, 4, ls="--", lw=1)
    f.seg(-0.3, -0.6, 2, 4, ls="-.", lw=1.2)          # A と BC の中点（原点）
    f.seg(-2.8, 2.2, 6, 0, ls=":", lw=1.3)          # C と AB の中点 N
    f.dot((-2, 2), "s", 3)
    f.text("N", (-2, 2), around(0.6, 16, np.pi / 16), size=10)
trifig("h_tri_ans.png", **T2, extra=ex2, shade=True)


# ---------- 線分図（速さ） ----------
# 線分の上に道のり、下に速さと時間。区間ごとの弧と、全体の大きな弧（手書きの図と同じ形）
def arc(ax, x0, x1, y0, h, up=True, gap=0.0):
    t = np.linspace(0, np.pi, 300)
    xs = (x0 + x1) / 2 - (x1 - x0) / 2 * np.cos(t)
    ys = y0 + (h if up else -h) * np.sin(t)
    if gap:  # まん中を文字のためにあける
        k = np.abs(xs - (x0 + x1) / 2) > gap
        left = xs < (x0 + x1) / 2
        ax.plot(xs[k & left], ys[k & left], "k", lw=1.1); ax.plot(xs[k & ~left], ys[k & ~left], "k", lw=1.1)
    else:
        ax.plot(xs, ys, "k", lw=1.1)

def speed(name, start, goal, dist, v1, v2, t1, t2, total, split=5.5):
    fig, ax = plt.subplots(figsize=(5.0, 3.2))
    X0, XM, X1 = 0, split, 10
    ax.plot([X0, X1], [0, 0], "k", lw=1.6)
    for x in (X0, XM, X1): ax.plot([x, x], [-0.18, 0.18], "k", lw=1.4)
    ax.text(X0 - 0.35, 0, start, fontsize=11, ha="right", va="center")
    ax.text(X1 + 0.35, 0, goal, fontsize=11, ha="left", va="center")
    # 上：道のり
    arc(ax, X0, XM, 0.05, 1.0, gap=1.0); ax.text((X0 + XM) / 2, 1.05, "$x$ km", fontsize=12, ha="center", va="center")
    arc(ax, XM, X1, 0.05, 1.0, gap=0.9); ax.text((XM + X1) / 2, 1.05, "$y$ km", fontsize=12, ha="center", va="center")
    arc(ax, X0, X1, 0.05, 2.1, gap=0.9); ax.text((X0 + X1) / 2, 2.15, dist, fontsize=12, ha="center", va="center")
    # 下：速さ（矢印）と時間
    for xa, xb, sp in ((X0, XM, v1), (XM, X1, v2)):
        c = (xa + xb) / 2
        ax.annotate("", xy=(c + 0.7, -0.35), xytext=(c - 0.7, -0.35), arrowprops=dict(arrowstyle="-|>", lw=1.1, color="k"))
        ax.text(c, -0.75, sp, fontsize=10, ha="center", va="center")
    arc(ax, X0, XM, -0.05, 1.6, up=False, gap=1.4); ax.text((X0 + XM) / 2, -1.8, t1 + " 時間", fontsize=14, ha="center", va="center")
    arc(ax, XM, X1, -0.05, 1.6, up=False, gap=1.3); ax.text((XM + X1) / 2, -1.8, t2 + " 時間", fontsize=14, ha="center", va="center")
    arc(ax, X0, X1, -0.05, 3.1, up=False, gap=1.4); ax.text((X0 + X1) / 2, -3.15, total, fontsize=12, ha="center", va="center")
    ax.set_xlim(-1.6, 12.0); ax.set_ylim(-3.45, 2.5); ax.set_aspect("equal"); ax.axis("off")
    fig.savefig(OUT + name, dpi=200, bbox_inches="tight", pad_inches=0.05); plt.close(fig)

speed("h_speed.png", "家", "公園", "14km", "時速12km", "時速4km", r"$\frac{x}{12}$", r"$\frac{y}{4}$", "1時間30分")


# ======================= 第2回 =======================
graph("j2_read.png", [(-3, 2), (2 / 3, -1)], ["①", "②"])

T3 = dict(xlim=(-3.2, 6.8), ylim=(-1.4, 9.9), L1=(-2, 8, "ℓ"), L2=(1, 2, "m"), A=(2, 4), B=(0, 8), C=(0, 2), size=(2.9, 3.0))
trifig("o2_tri.png", **T3)

# 宿題：グラフをかく（③は x=−2）
f, ends = gridfig([(-1.5, 3, {}), (1.5, -2, {})])
f.seg(-3, -LIM, -3, LIM)
f.seg(0, 3, 2, 3, ls=":", lw=1.3); f.seg(2, 3, 2, 0, ls=":", lw=1.3)
for p in [(0, 3), (2, 0), (0, -2), (2, 1)]: f.dot(p)
f.text("右へ2", (1, 3), [(0, 0.45), (0, -0.45)], size=8, family="IPAGothic", r=0.3)
f.text("下へ3", (2, 1.5), [(1.3, -0.6), (1.3, -1.2)], size=8, family="IPAGothic", r=0.3)
for s_, e in zip(["①", "②"], ends): linelabel(f, s_, e)
linelabel(f, "③", (-3, -LIM, -3, LIM))
gridlabels(f)
f.save("h2_graph_ans.png")

speed("h2_speed.png", "A地点", "B地点", "18km", "時速4km", "時速6km", r"$\frac{x}{4}$", r"$\frac{y}{6}$", "4時間", split=6)

T4 = dict(xlim=(-3.2, 7.2), ylim=(-1.4, 7.6), L1=(-1, 6, "ℓ"), L2=(2, 0, "m"), A=(2, 4), B=(0, 6), C=(0, 0), size=(2.9, 2.6), names=("A", "B", "O"))
trifig("h2_tri.png", **T4)
def ex3(f):
    f.seg(0, 0, 1.25, 6.25, ls="-.", lw=1.2)   # O と AB の中点 N を通る直線
    f.dot((1, 5), "s", 3)
    f.text("N", (1, 5), around(0.6, 16, np.pi / 16), size=10)
    f.seg(0, 4, 2, 4, ls="--", lw=1)          # 高さ（Aのx座標）
trifig("h2_tri_ans.png", **T4, extra=ex3, shade=True)


# ======================= 第2回（一次関数の後半） =======================
def dia(name, xmax, ymax, xgrid, ygrid, xticks, yticks, paths=(), size=(3.4, 3.0), ylab="(m)", xlab="(分)",
        places=(), extra=None, labels=()):
    """ダイヤグラム：横が時間、縦が道のり。方眼つき"""
    sx, sy = 10 / xmax, 10 * 0.85 / ymax  # 縦横の見た目をそろえる
    f = Fig(size, (-4.3, 11.9), (-1.6, 10 * 0.85 + 1.3))
    f.white = True
    for v in np.arange(0, xmax + 1e-9, xgrid): f.ax.plot([v * sx] * 2, [0, ymax * sy], color="#b0b0b0", lw=0.6, zorder=0)
    for v in np.arange(0, ymax + 1e-9, ygrid): f.ax.plot([0, xmax * sx], [v * sy] * 2, color="#b0b0b0", lw=0.6, zorder=0)
    f.arrow(0, 0, xmax * sx + 0.8, 0); f.arrow(0, 0, 0, ymax * sy + 0.8)
    for (pts, kw) in paths:
        for (x1, y1), (x2, y2) in zip(pts[:-1], pts[1:]):
            f.seg(x1 * sx, y1 * sy, x2 * sx, y2 * sy, lw=kw.get("lw", 1.8), ls=kw.get("ls", "-"))
    if extra: extra(f, sx, sy)
    for t in xticks: f.ax.text(t * sx, -0.45, str(t), fontsize=9, ha="center", va="center", family="serif")
    for t in yticks: f.ax.text(-0.25, t * sy, str(t), fontsize=9, ha="right", va="center", family="serif")
    for (t, s) in places: f.ax.text(-2.7, t * sy, s, fontsize=9, ha="right", va="center")
    f.ax.text(-0.3, -0.45, "O", fontsize=10, ha="center", va="center", family="serif")
    f.ax.text(xmax * sx + 1.0, 0.45, "$x$", fontsize=12, ha="center", va="center")
    f.ax.text(xmax * sx + 1.15, -1.0, xlab, fontsize=8, ha="center", va="center")
    f.ax.text(0, ymax * sy + 1.15, ylab + " $y$", fontsize=10, ha="center", va="center")
    for (s, p, cands) in labels: f.text(s, (p[0] * sx, p[1] * sy), cands, size=10, family="IPAGothic", r=0.45)
    f.save(name)

# 基本＜2＞：家→（分速80m）→800mで10分止まる→分速120mで2000m
dia("j2b_dia.png", 30, 2000, 2, 200, [10, 20, 30], [400, 800, 1200, 1600, 2000],
    paths=[([(0, 0), (10, 800), (20, 800), (30, 2000)], {})], places=[(2000, "駅"), (0, "家")])

# 応用＜1＞：弟は分速60mで2400m先の駅へ（兄の線は生徒がかかない）
dia("o2b_dia.png", 45, 2400, 5, 300, [10, 20, 30, 40], [600, 1200, 1800, 2400],
    paths=[([(0, 0), (40, 2400)], {})], places=[(2400, "駅"), (0, "家")],
    labels=[("弟", (28, 1680), [(1.0, -0.6), (-0.9, 0.6)])])

# 宿題＜1＞：姉は家→公園（分速100m）、妹は公園→家（分速50m）
H1 = dict(name="h2b_dia.png", xmax=30, ymax=1500, xgrid=2, ygrid=100, xticks=[10, 20, 30], yticks=[500, 1000, 1500],
          paths=[([(0, 0), (15, 1500)], {}), ([(0, 1500), (30, 0)], {})], places=[(1500, "公園"), (0, "家")],
          labels=[("姉", (6, 600), [(-0.9, 0.5), (0.9, -0.5)]), ("妹", (24, 300), [(0.9, 0.5), (-0.9, -0.5)])])
dia(**H1)
def cross(f, sx, sy):
    f.seg(10 * sx, 0, 10 * sx, 1000 * sy, ls="--", lw=1); f.seg(0, 1000 * sy, 10 * sx, 1000 * sy, ls="--", lw=1)
    f.dot((10 * sx, 1000 * sy))
dia(**{**H1, "name": "h2b_dia_ans.png", "extra": cross})


def rect(name, w, h, tri, pname, ppos, arrow, labels=True, size=(2.3, 1.9)):
    """長方形ABCD（A左上、B左下、C右下、D右上）と動く点P。tri の三角形をグレーにぬる"""
    fig, ax = plt.subplots(figsize=size)
    ax.add_patch(Polygon(tri, closed=True, color="#bfbfbf", zorder=0))
    ax.plot([0, 0, w, w, 0], [h, 0, 0, h, h], "k", lw=1.5)
    ax.plot(*zip(*(tri + [tri[0]])), "k", lw=1.0)
    for s, (x, y), (dx, dy) in (("A", (0, h), (-0.35, 0.3)), ("B", (0, 0), (-0.35, -0.35)), ("C", (w, 0), (0.35, -0.35)), ("D", (w, h), (0.35, 0.3))):
        ax.text(x + dx, y + dy, s, fontsize=11, ha="center", va="center", family="serif")
    ax.plot(*ppos, "ko", ms=3.5, zorder=5)
    ax.text(ppos[0] + arrow[2], ppos[1] + arrow[3], pname, fontsize=11, ha="center", va="center", family="serif")
    ax.annotate("", xy=(ppos[0] + arrow[0], ppos[1] + arrow[1]), xytext=ppos, arrowprops=dict(arrowstyle="-|>", lw=1, color="k"))
    if labels:
        ax.text(w + 0.55, h / 2, f"{h}cm", fontsize=9, ha="center", va="center", rotation=90)
        ax.text(w / 2, h + 0.45, f"{w}cm", fontsize=9, ha="center", va="center")
    ax.set_xlim(-1.2, w + 1.1); ax.set_ylim(-1.0, h + 0.9); ax.set_aspect("equal"); ax.axis("off")
    fig.savefig(OUT + name, dpi=200, bbox_inches="tight", pad_inches=0.05); plt.close(fig)

# 基本＜3＞：AB=6、BC=8。PはBからCへ。△ABP
rect("j2b_rect.png", 8, 6, [(0, 6), (0, 0), (3, 0)], "P", (3, 0), (1.2, 0, 0, -0.45))
# 応用＜2＞：AB=4、BC=6。PはA→B→C→D。△APD（PがAB上）
rect("o2b_rect.png", 6, 4, [(0, 4), (0, 1.5), (6, 4)], "P", (0, 1.5), (0, -0.9, -0.4, 0), size=(2.1, 1.7))
# 宿題＜2＞：AB=4、BC=6。PはB→C→D。△ABP（PがBC上）
rect("h2b_rect.png", 6, 4, [(0, 4), (0, 0), (2.5, 0)], "P", (2.5, 0), (1.0, 0, 0, -0.45), size=(2.1, 1.7))

# 宿題＜2＞(3)：グラフをかく方眼（x：0〜12秒、y：0〜14cm²）と、その答え
def areagrid(name, lines=()):
    dia(name, 12, 14, 1, 1, [2, 4, 6, 8, 10, 12], [2, 4, 6, 8, 10, 12, 14], paths=lines, ylab="(cm²)", xlab="(秒)", size=(3.0, 3.0))
areagrid("h2b_grid.png")
areagrid("h2b_graph_ans.png", [([(0, 0), (6, 12), (10, 12)], {})])
