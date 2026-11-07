# 中2 第4回（11/9）総ざらい③ の図
src = open("figs.py").read()
a = src.index("# logo grayscale"); b = src.index('g.save(OUT + "logo_gray.png")')
exec(src[:a] + src[b + len('g.save(OUT + "logo_gray.png")'):])
import numpy as np

def U(deg): return np.array([np.cos(np.radians(deg)), np.sin(np.radians(deg))])
def alab(ax, v, p, q, s, r=1.3, fs=9, **kw):
    """頂点vの角（v→p と v→q の間）の内側に文字"""
    v = np.array(v, float); u1 = np.array(p) - v; u2 = np.array(q) - v
    u1 /= np.linalg.norm(u1); u2 /= np.linalg.norm(u2); m = u1 + u2; m /= np.linalg.norm(m)
    ax.text(*(v + r * m), s, fontsize=fs, ha="center", va="center", **kw)
def lines_lm(ax, y1=5, x0=-1, x1=9):
    pl(ax, (x0, y1), (x1, y1)); pl(ax, (x0, 0), (x1, 0))
    ax.text(x1 + 0.3, y1, "ℓ", fontsize=12, style="italic", va="center"); ax.text(x1 + 0.3, 0, "m", fontsize=12, style="italic", va="center", family="serif")
def fin(ax, fig, name, xl, yl):
    ax.set_xlim(*xl); ax.set_ylim(*yl); ax.set_aspect("equal"); ax.axis("off"); save(fig, name)

# 平行線と三角形：Aはℓ上、B・Cはm上。ℓの左とABの角 L、∠BAC＝T、∠ACB＝x
def tripar(name, L, Tt, size=(2.6, 2.0)):
    fig, ax = plt.subplots(figsize=size); lines_lm(ax)
    A = np.array([4.0, 5.0]); R = 180 - L - Tt
    B = A + 5 / np.sin(np.radians(L)) * U(180 + L); C = A + 5 / np.sin(np.radians(R)) * U(-R)
    pl(ax, A, B, 1.2); pl(ax, A, C, 1.2)
    for p in (A, B, C): ax.plot(*p, "ko", ms=3)
    ax.text(A[0], A[1] + 0.5, "A", fontsize=11, ha="center", family="serif")
    ax.text(B[0] - 0.1, B[1] - 0.7, "B", fontsize=11, ha="center", family="serif"); ax.text(C[0] + 0.1, C[1] - 0.7, "C", fontsize=11, ha="center", family="serif")
    amark(ax, A, (-1, 5), B, 0.9); alab(ax, A, (-1, 5), B, f"{L}°", 1.7)
    amark(ax, A, B, C, 0.7); alab(ax, A, B, C, f"{Tt}°", 1.5)
    amark(ax, C, A, (0, 0), 0.8); alab(ax, C, A, (0, 0), "$x$", 1.4, fs=12)
    fin(ax, fig, name, (-1.4, 10.0), (-1.4, 6.2))
tripar("j4_tripar.png", 50, 70); tripar("h4_tripar.png", 55, 60)

# くの字：ℓで角a、mで角b（どちらも右側）、点Pの角x
def kuno(name, a_, b_, ans=False, size=(2.6, 2.0)):
    fig, ax = plt.subplots(figsize=size); lines_lm(ax)
    A, B = np.array([1.0, 5.0]), np.array([1.0, 0.0])
    t = 5 / (np.tan(np.radians(a_)) + np.tan(np.radians(b_)))
    P = np.array([1 + t, 5 - t * np.tan(np.radians(a_))])
    pl(ax, A, P, 1.2); pl(ax, P, B, 1.2); ax.plot(*P, "ko", ms=3)
    amark(ax, A, (9, 5), P, 1.1); alab(ax, A, (9, 5), P, f"{a_}°", 1.9)
    amark(ax, B, (9, 0), P, 1.1); alab(ax, B, (9, 0), P, f"{b_}°", 1.9)
    amark(ax, P, A, B, 0.7)
    if not ans: alab(ax, P, A, B, "$x$", 1.2, fs=12)
    ax.text(P[0] + 0.35, P[1] + 0.45, "P", fontsize=11, ha="left", va="center", family="serif")
    if ans:
        pl(ax, (P[0] - 4.0, P[1]), (P[0] + 2.4, P[1]), 1.0, "--")
        ax.text(P[0] + 2.7, P[1], "n", fontsize=11, style="italic", va="center", family="serif")
        alab(ax, P, A, (P[0] - 3, P[1]), f"{a_}°", 1.6, fs=8); alab(ax, P, B, (P[0] - 3, P[1]), f"{b_}°", 1.6, fs=8)
    fin(ax, fig, name, (-1.4, 10.0), (-1.2, 6.2))
kuno("j4_kuno.png", 35, 45); kuno("h4_kuno.png", 25, 50); kuno("h4_kuno_ans.png", 25, 50, ans=True)

# W字（折れ線2回）：Aで a（ℓの右）、P、Q、Bで d（mの左）。P＝a+c、Q＝c+d
def wfig(name, a_, c_, d_, show, ans=False, size=(2.6, 2.4)):
    H = 6.0; fig, ax = plt.subplots(figsize=size); lines_lm(ax, H, -1, 9)
    A = np.array([1.5, H]); L1, L2 = 4.0, 3.0
    P = A + L1 * U(-a_); Q = P + L2 * U(180 + c_)
    L3 = Q[1] / np.sin(np.radians(d_)); B = Q + L3 * U(-d_)
    pl(ax, A, P, 1.2); pl(ax, P, Q, 1.2); pl(ax, Q, B, 1.2)
    for p in (P, Q): ax.plot(*p, "ko", ms=3)
    vals = {"A": f"{a_}°", "P": f"{a_ + c_}°", "Q": f"{c_ + d_}°", "B": f"{d_}°"}
    vals[show] = "$x$"
    amark(ax, A, (9, H), P, 1.0); alab(ax, A, (9, H), P, vals["A"], 1.8, fs=9 if show != "A" else 12)
    amark(ax, P, A, Q, 0.7); alab(ax, P, A, Q, vals["P"], 1.4, fs=9 if show != "P" else 12)
    amark(ax, Q, P, B, 0.7); alab(ax, Q, P, B, vals["Q"], 1.4, fs=9 if show != "Q" else 12)
    amark(ax, B, (-1, 0), Q, 1.0); alab(ax, B, (-1, 0), Q, vals["B"], 1.8, fs=9 if show != "B" else 12)
    ax.text(P[0] + 0.3, P[1] + 0.35, "P", fontsize=10, ha="left", family="serif"); ax.text(Q[0] - 0.35, Q[1] + 0.2, "Q", fontsize=10, ha="right", family="serif")
    if ans:
        for p in (P, Q): pl(ax, (p[0] - 3.2, p[1]), (p[0] + 3.4, p[1]), 1.0, "--")
    fin(ax, fig, name, (-1.4, 10.0), (-1.0, H + 1.0))
wfig("o4_w.png", 30, 30, 40, "P"); wfig("o4_w_ans.png", 30, 30, 40, "P", ans=True)
wfig("h4_w.png", 35, 55, 25, "P"); wfig("h4_w_ans.png", 35, 55, 25, "P", ans=True)

# 三角形の外角
def ext(name, Bd, Cd, size=(2.4, 1.6)):
    fig, ax = plt.subplots(figsize=size)
    B, C = np.array([0.0, 0]), np.array([6.0, 0])
    t = 6 * np.sin(np.radians(Cd)) / np.sin(np.radians(180 - Bd - Cd)); A = B + t * U(Bd)
    pl(ax, B, (9.0, 0), 1.3); pl(ax, B, A, 1.3); pl(ax, A, C, 1.3)
    for s_, p, o in (("A", A, (0, 0.5)), ("B", B, (-0.4, -0.45)), ("C", C, (0, -0.55))): ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=11, ha="center", va="center", family="serif")
    amark(ax, A, B, C, 0.7); alab(ax, A, B, C, f"{180 - Bd - Cd}°", 1.4)
    amark(ax, B, C, A, 0.9); alab(ax, B, C, A, f"{Bd}°", 1.6)
    amark(ax, C, (9, 0), A, 0.7); alab(ax, C, (9, 0), A, "$x$", 1.2, fs=12)
    fin(ax, fig, name, (-1.0, 9.4), (-1.0, A[1] + 1.0))
ext("j4_ext.png", 67, 65)

# ブーメラン（へこんだ四角形）：∠A＝70、∠ABD＝25、∠ACD＝30、∠BDC＝x
def boom(name, ans=False, size=(2.4, 2.2)):
    fig, ax = plt.subplots(figsize=size)
    B, C = np.array([0.0, 0]), np.array([8.0, 0]); A = np.array([4.0, 4 * np.tan(np.radians(55))])
    # D：Bから30°、Cから155°の半直線の交点
    t = 8 * np.sin(np.radians(25)) / np.sin(np.radians(180 - 30 - 25)); D = B + t * U(30)
    pl(ax, A, B, 1.3); pl(ax, A, C, 1.3); pl(ax, B, D, 1.3); pl(ax, D, C, 1.3)
    for s_, p, o in (("A", A, (0, 0.5)), ("B", B, (-0.45, -0.3)), ("C", C, (0.45, -0.3)), ("D", D, (0, 0.55))): ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=11, ha="center", va="center", family="serif")
    amark(ax, A, B, C, 0.8); alab(ax, A, B, C, "70°", 1.6)
    amark(ax, B, A, D, 1.3); alab(ax, B, A, D, "25°", 2.2)
    amark(ax, C, A, D, 1.3); alab(ax, C, A, D, "30°", 2.2)
    amark(ax, D, B, C, 0.6); ax.text(D[0], D[1] - 1.05, "$x$", fontsize=12, ha="center", va="center")
    if ans:
        E = D + 2.6 * U(30)
        pl(ax, D, E, 1.0, "--"); ax.plot(*E, "ko", ms=3); ax.text(E[0] + 0.45, E[1] + 0.1, "E", fontsize=10, ha="center", family="serif")
    fin(ax, fig, name, (-1.0, 9.0), (-1.0, A[1] + 1.0))
boom("h4_boom.png"); boom("h4_boom_ans.png", ans=True)

# 星形
def star(name, vals, ans=False, size=(2.4, 2.4)):
    fig, ax = plt.subplots(figsize=size)
    T = [4 * U(90 + 72 * k) for k in range(5)]
    for k in range(5): pl(ax, T[k], T[(k + 2) % 5], 1.3)
    nm = ["A", "B", "C", "D", "E"]
    for k in range(5):
        p, q = T[(k + 2) % 5], T[(k + 3) % 5]
        amark(ax, T[k], p, q, 0.9)
        alab(ax, T[k], p, q, vals[k], 1.8, fs=12 if "x" in vals[k] or "$" in vals[k] else 9)
        ax.text(*(T[k] * 1.13), nm[k], fontsize=11, ha="center", va="center", family="serif")
    if ans:
        def X(p1, p2, p3, p4):
            d1, d2 = p2 - p1, p4 - p3; c2 = lambda u, v: u[0] * v[1] - u[1] * v[0]; s = c2(p3 - p1, d2) / c2(d1, d2); return p1 + s * d1
        Pp = X(T[0], T[2], T[1], T[4]); Qq = X(T[0], T[3], T[1], T[4])
        ax.add_patch(Polygon([T[0], Pp, Qq], closed=True, color="#cfcfcf", zorder=0))
        ax.text(Pp[0] - 0.5, Pp[1] + 0.3, "F", fontsize=10, ha="center", family="serif"); ax.text(Qq[0] + 0.5, Qq[1] + 0.3, "G", fontsize=10, ha="center", family="serif")
    fin(ax, fig, name, (-5.2, 5.2), (-4.6, 5.2))
star("o4_star.png", ["$x$", "32°", "38°", "40°", "35°"])
star("h4_star.png", ["$a$", "$b$", "$c$", "$d$", "$e$"]); star("h4_star_ans.png", ["$a$", "$b$", "$c$", "$d$", "$e$"], ans=True)

# 折り返し：長方形ABCD（A左上）。EFで折ってDがD'、CがC'に
def fold(name, ang, mark, ans=False, size=(2.8, 2.2)):
    fig, ax = plt.subplots(figsize=size)
    W, H = 10.0, 6.0; A, B, C, D = np.array([0, H]), np.array([0.0, 0]), np.array([W, 0]), np.array([W, H])
    k = (180 - ang) / 2  # ∠DEF
    E = np.array([5.0, H]); F = np.array([5 + H / np.tan(np.radians(k)), 0])
    u = (F - E) / np.linalg.norm(F - E)
    def refl(p): v = p - E; pr = np.dot(v, u) * u; return E + 2 * pr - v
    D2, C2 = refl(D), refl(C)
    ax.plot([E[0], A[0], B[0], F[0]], [E[1], A[1], B[1], F[1]], "k", lw=1.4)
    ax.plot([E[0], D[0], C[0], F[0]], [E[1], D[1], C[1], F[1]], "k", lw=1.0, ls=":")
    ax.plot([E[0], D2[0], C2[0], F[0], E[0]], [E[1], D2[1], C2[1], F[1], E[1]], "k", lw=1.4)
    for s_, p, o in (("A", A, (-0.4, 0.4)), ("B", B, (-0.4, -0.4)), ("C", C, (0.4, -0.4)), ("D", D, (0.4, 0.4)), ("E", E, (0, 0.5)), ("F", F, (0.35, 0.45)),
                     ("D'", D2, (-0.45, -0.35)), ("C'", C2, (0.1, -0.6))):
        ax.text(p[0] + o[0], p[1] + o[1], s_, fontsize=10, ha="center", va="center", family="serif")
    amark(ax, E, A, D2, 0.9); alab(ax, E, A, D2, f"{ang}°", 1.7)
    if mark == "EFC'":
        amark(ax, F, E, C2, 0.8); alab(ax, F, E, C2, "$x$", 1.4, fs=12)
    else:  # ∠BFC'
        amark(ax, F, B, C2, 0.8); alab(ax, F, B, C2, "$x$", 1.4, fs=12)
    if ans:
        amark(ax, E, D, F, 0.7, 2); amark(ax, E, F, D2, 0.75, 2); amark(ax, F, B, E, 0.75, 2)
    fin(ax, fig, name, (-1.0, 11.0), (min(C2[1], 0) - 1.0, H + 1.0))
fold("o4_fold.png", 50, "EFC'"); fold("h4_fold.png", 40, "BFC'"); fold("h4_fold_ans.png", 40, "BFC'", ans=True)

# 動く点：AB=6、BC=10。PはB→C→D→A。△ABP（PがBC上）
rect("o4_rect.png", 10, 6, [(0, 6), (0, 0), (4, 0)], (4, 0), (0, -0.8), ((-0.4, -1.5), (1.1, -1.5)), size=(2.6, 1.9))
# 宿題：1辺4cmの正方形。PはA→B→C→D。△APD（PがAB上）
rect("h4_sq.png", 4, 4, [(0, 4), (0, 1.8), (4, 4)], (0, 1.8), (-0.5, 0), ((-1.0, 0.6), (-1.0, -0.8)), size=(1.9, 1.9))
areagrid("h4_graph_ans.png", [([(0, 0), (4, 8), (8, 8), (12, 0)], {})])

# 宿題：2直線と三角形 ℓ: y=x+1、m: y=−2x+10。A(3,4)、B(−1,0)、C(5,0)
T5 = dict(xlim=(-3.4, 7.6), ylim=(-1.5, 7.4), L1=(1, 1, "ℓ"), L2=(-2, 10, "m"), A=(3, 4), B=(-1, 0), C=(5, 0), size=(3.0, 2.4))
trifig("h4_tri.png", **T5)
def ex5(f):
    f.seg(3, 4, 1.85, -0.6, ls="-.", lw=1.2); f.dot((2, 0), "s", 3)
    f.seg(-1, 0, 5.5, 2.6, ls=":", lw=1.3); f.dot((4, 2), "s", 3)
    f.text("M", (2, 0), [(0.0, -0.6), (0.5, -0.6)], size=10); f.text("N", (4, 2), [(0.5, 0.4), (0.6, -0.2)], size=10)
trifig("h4_tri_ans.png", **T5, extra=ex5, shade=True)
speed("h4_speed.png", "家", "図書館", "10km", "時速4km", "時速12km", r"$\frac{x}{4}$", r"$\frac{y}{12}$", "1時間30分", split=4.5)

# 南第二中用：ダイヤグラム（姉 家→図書館 2000m 分速100m。妹は10分後に図書館を出て分速150mで家へ）
dia("h4m_dia.png", 20, 2000, 1, 200, [5, 10, 15, 20], [400, 800, 1200, 1600, 2000],
    paths=[([(0, 0), (20, 2000)], {})], places=[(2000, "図書館"), (0, "家")], labels=[("姉", (16, 1600), [(-0.9, 0.5), (-0.8, 0.7)])])
def cr(f, sx, sy):
    f.seg(10 * sx, 2000 * sy, 20 * sx, 500 * sy, lw=1.8, ls="--")
    f.seg(14 * sx, 0, 14 * sx, 1400 * sy, ls=":", lw=1); f.seg(0, 1400 * sy, 14 * sx, 1400 * sy, ls=":", lw=1); f.dot((14 * sx, 1400 * sy))
dia("h4m_dia_ans.png", 20, 2000, 1, 200, [5, 10, 15, 20], [400, 800, 1200, 1600, 2000],
    paths=[([(0, 0), (20, 2000)], {})], places=[(2000, "図書館"), (0, "家")], extra=cr,
    labels=[("姉", (17, 1700), [(-0.9, 0.5)]), ("妹", (18, 800), [(0.6, 0.5)])])
