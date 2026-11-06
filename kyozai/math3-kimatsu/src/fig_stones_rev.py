# 宿題 碁石：同じ形をさかさまにしてくっつける図（1〜4番目）
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = ["IPAGothic"]
fig, ax = plt.subplots(figsize=(6.0, 2.0))
x0 = 0.0
for n in (1, 2, 3, 4):
    for i in range(1, n + 1):          # 上から i 行目：黒 i 個、白 n+1-i 個
        y = n - i
        sh = 0.5 * y                    # 上の行ほど右へずらす
        for j in range(n + 1):
            black = j < i
            ax.add_patch(plt.Circle((x0 + sh + j, y), 0.36, fc="k" if black else "w", ec="k", lw=1.3))
    w = n + 0.5 * (n - 1)
    ax.text(x0 + w / 2, -1.15, f"{n}番目", ha="center", va="center", fontsize=11)
    x0 += w + 2.2
ax.set_xlim(-0.6, x0 - 1.6); ax.set_ylim(-1.6, 3.6); ax.set_aspect(1); ax.axis("off")
fig.savefig("img/h4_stones_rev.png", dpi=300, bbox_inches="tight", pad_inches=0.05)
