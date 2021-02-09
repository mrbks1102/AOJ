x1, y1, x2, y2 = map(float, input().split())
# 三平方の定理より式変換したらp1,p2の距離を求められる。
print(((x2-x1)**2+(y2-y1)**2)**0.5)
