"""黒線のキャラクターPNG（背景透明）を、コッピーの線の色に塗り替える。

使い方: python3 recolor.py 入力.png 出力.png [色コード]
色コードを省くと、やさしいブルー #6F96D1 になる。
"""
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
hexcolor = (sys.argv[3] if len(sys.argv) > 3 else "#6F96D1").lstrip("#")
r, g, b = (int(hexcolor[i:i + 2], 16) for i in (0, 2, 4))

im = Image.open(src).convert("RGBA")
px = im.load()
for y in range(im.height):
    for x in range(im.width):
        a = px[x, y][3]
        if a:
            px[x, y] = (r, g, b, a)
im.save(dst)
