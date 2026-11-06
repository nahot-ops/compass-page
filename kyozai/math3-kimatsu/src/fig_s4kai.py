# 中3 第4回 授業プリント②の解答解説用の図
exec(open("figs.py").read())

# ＜1＞ 5番目の図形：1辺6枚、内側は1辺4枚
def kt(name="s4k_tiles_ans.png"):
    fig, ax = plt.subplots(figsize=(2.2, 2.2)); m = 6
    for i in range(m):
        for j in range(m):
            edge = i in (0, m - 1) or j in (0, m - 1)
            ax.add_patch(Rectangle((i, j), 1, 1, facecolor="#9a9a9a" if edge else "white", edgecolor="k", lw=0.8))
    dimarc(ax, (0, m), (m, m), -1.0, "6枚", 0.8, fs=9)
    ax.annotate("", xy=(5, 3.0), xytext=(1, 3.0), arrowprops=dict(arrowstyle="<->", lw=0.9))
    ax.text(3, 3.45, "4枚", fontsize=9, ha="center", va="center", bbox=dict(fc="white", ec="none", pad=0.5))
    ax.text(3, -0.7, "5番目", fontsize=9, ha="center", va="center")
    ax.set_xlim(-0.5, 6.5); ax.set_ylim(-1.2, 8.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
kt()

# ＜2＞ 2つの場合：QがAD上（0<x≦3）と、QがDC上（3≦x≦6）
def ksq(name="s4k_sq_ans.png"):
    fig, axs = plt.subplots(1, 2, figsize=(4.4, 2.5)); s_ = 6
    for k, ax in enumerate(axs):
        if k == 0: P_, Q_ = (0, 3.6), (4.8, 6)
        else: P_, Q_ = (0, 2), (6, 4)
        ax.add_patch(Polygon([(0, 6), P_, Q_], closed=True, fill=False, hatch="////", edgecolor="k", lw=1.2))
        ax.plot([0, 0, s_, s_, 0], [s_, 0, 0, s_, s_], "k", lw=1.5)
        corners(ax, s_, s_)
        ax.plot(*P_, "ko", ms=4.5, zorder=5); ax.plot(*Q_, "ko", ms=4.5, zorder=5)
        ax.text(P_[0] + 0.5, P_[1] - 0.45, "P", fontsize=11, ha="center", va="center", family="serif")
        if k == 0:
            ax.text(Q_[0] + 0.55, Q_[1] - 0.55, "Q", fontsize=11, ha="center", va="center", family="serif")
            dimarc(ax, (0, 6), P_, 1.0, "$x$cm", 0.8, fs=9)
            dimarc(ax, (0, 6), Q_, -1.0, "$2x$cm", 1.0, fs=9)
            ax.text(3, -1.3, "0＜$x$≦3", fontsize=10, ha="center", va="center")
        else:
            ax.text(Q_[0] + 0.6, Q_[1], "Q", fontsize=11, ha="center", va="center", family="serif")
            dimarc(ax, (0, 6), P_, 1.2, "$x$cm", 1.0, fs=9)
            dimarc(ax, (0, 6), (6, 6), -1.0, "6cm", 0.9, fs=9)
            ax.text(3, -1.3, "3≦$x$≦6", fontsize=10, ha="center", va="center")
        ax.set_xlim(-2.6, s_ + 1.3); ax.set_ylim(-1.8, s_ + 2.0); ax.set_aspect("equal"); ax.axis("off")
    save(fig, name)
ksq()

# ＜3＞ 平行四辺形OACBと△PAB
def kpar(name="s4k_par_ans.png", size=(2.7, 3.1)):
    fig, ax = plt.subplots(figsize=size)
    ax.annotate("", xy=(5.6, 0), xytext=(-4.0, 0), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    ax.annotate("", xy=(0, 12.0), xytext=(0, -1.2), arrowprops=dict(arrowstyle="-|>", color="k", lw=1.1))
    xs = np.linspace(-3.6, 4.6, 300); k = xs ** 2 / 2 <= 11.0; ax.plot(xs[k], xs[k] ** 2 / 2, "k", lw=1.5)
    O, A, B, C, D, Pp = (0, 0), (-2, 2), (4, 8), (2, 10), (0, 4), (0, 20 / 3)
    ax.plot([O[0], A[0], C[0], B[0], O[0]], [O[1], A[1], C[1], B[1], O[1]], "k", lw=1.3)
    ax.plot([A[0], B[0]], [A[1], B[1]], "k--", lw=1.0)
    ax.plot([A[0], Pp[0], B[0]], [A[1], Pp[1], B[1]], "k:", lw=1.2)
    for p in (A, B, C, D, Pp): ax.plot(*p, "ko", ms=3.5, zorder=5)
    f = dict(family="serif")
    ax.text(-2.35, 2.0, "A", fontsize=11, ha="right", va="center", **f)
    ax.text(4.35, 7.8, "B", fontsize=11, ha="left", va="center", **f)
    ax.text(1.75, 10.5, "C", fontsize=11, ha="right", va="center", **f)
    ax.text(0.3, 3.55, "D", fontsize=11, ha="left", va="center", **f)
    ax.text(-0.3, 20 / 3 + 0.35, "P", fontsize=11, ha="right", va="center", **f)
    ax.text(-0.25, -0.35, "O", fontsize=10, ha="right", va="top", **f)
    ax.text(5.4, -0.8, "x", fontsize=12, style="italic", **f)
    ax.text(0.25, 11.6, "y", fontsize=12, style="italic", **f)
    ax.text(-3.9, 10.6, "$y=\\frac{1}{2}x^2$", fontsize=9)
    ax.set_xlim(-4.6, 6.0); ax.set_ylim(-1.4, 12.4); ax.set_aspect(0.55); ax.axis("off")
    save(fig, name)
kpar()
