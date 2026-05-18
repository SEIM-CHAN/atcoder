# 黒板にN 個の正の整数 A1,...,AN が書かれています．

# すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．
# 黒板に書かれている整数すべてを，2 で割ったものに置き換える．
# すぬけ君は最大で何回操作を行うことができるかを求めてください．

N = int(input())
A = list(map(int, input().split()))

count = 0

while all(x % 2 == 0 for x in A):
    A = [x // 2 for x in A]
    count += 1

print(count)