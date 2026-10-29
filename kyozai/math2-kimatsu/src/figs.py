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
def trifig(name, xlim, ylim, L1, L2, A, B, C, size, extra=None, shade=False):
    f = Fig(size, xlim, ylim)
    x0, x1 = xlim[0] + 0.3, xlim[1] - 0.6
    y0, y1 = ylim[0] + 0.2, ylim[1] - 0.6
    if shade: f.ax.add_patch(Polygon([A, B, C], closed=True, color="#cfcfcf", zorder=0))
    f.arrow(xlim[0] + 0.2, 0, xlim[1] - 0.3, 0); f.arrow(0, ylim[0] + 0.1, 0, ylim[1] - 0.2)
    e1 = f.line(L1[0], L1[1], x0, x1, y0, y1); e2 = f.line(L2[0], L2[1], x0, x1, y0, y1)
    if extra: extra(f)
    for p in (A, B, C): f.dot(p)
    pts = around(0.8, 16, np.pi / 16)
    f.text("A", A, pts); f.text("B", B, pts); f.text("C", C, pts)
    for (s, e) in ((L1[2], e1), (L2[2], e2)):
        ex, ey = (e[2], e[3]) if e[3] > e[1] else (e[0], e[1])
        f.text(s, (ex, ey), around(0.6, 12), size=13, style="italic", family=("IPAGothic" if s == "ℓ" else "serif"), r=0.4)
    f.text("x", (xlim[1] - 0.3, 0), [(0.1, -0.55), (0.1, 0.55)], size=13, style="italic")
    f.text("y", (0, ylim[1] - 0.2), [(0.5, -0.1), (-0.5, -0.1)], size=13, style="italic")
    f.text("O", (0, 0), [(-0.45, -0.55), (0.45, -0.55), (-0.5, 0.5)], size=11, r=0.3)
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
fig, ax = plt.subplots(figsize=(5.2, 1.3))
ax.plot([0, 10], [0, 0], "k", lw=1.6)
for x in (0, 7.5, 10): ax.plot([x, x], [-0.15, 0.15], "k", lw=1.4)
ax.text(-0.3, -0.55, "家", fontsize=10); ax.text(9.6, -0.55, "公園", fontsize=10)
ax.annotate("", xy=(0, 0.55), xytext=(7.5, 0.55), arrowprops=dict(arrowstyle="<->", lw=1))
ax.annotate("", xy=(7.5, 0.55), xytext=(10, 0.55), arrowprops=dict(arrowstyle="<->", lw=1))
ax.text(2.0, 0.7, "自転車　時速12km　x km", fontsize=9)
ax.text(7.6, 0.7, "歩き 時速4km y km", fontsize=8)
ax.annotate("", xy=(0, -0.85), xytext=(10, -0.85), arrowprops=dict(arrowstyle="<->", lw=1))
ax.text(3.6, -1.3, "全部で14km　／　1時間30分", fontsize=9)
ax.set_xlim(-0.8, 10.8); ax.set_ylim(-1.5, 1.1); ax.axis("off")
fig.savefig(OUT + "h_speed.png", dpi=200, bbox_inches="tight", pad_inches=0.05); plt.close(fig)
