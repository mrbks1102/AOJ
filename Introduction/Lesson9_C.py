n = int(input())
tarou = 0
hanako = 0

for i in range(n):
    a, b = map(str, input().split())
    if a == b:
        tarou += 1
        hanako += 1
    else:
      # 辞書順は不等号で求めることができる。
        if a < b:
            hanako += 3
        else:
            tarou += 3

print(tarou, hanako)
