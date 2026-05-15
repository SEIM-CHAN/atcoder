a = int(input())
b, c = map(int, input().split())
s = input()

# print(a+b+c, s) ←これだと間違い
print("{} {}".format(a+b+c, s))