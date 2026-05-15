# 黒板にN 個の正の整数 A1,...,AN が書かれています．

# すぬけ君は，黒板に書かれている整数がすべて偶数であるとき，次の操作を行うことができます．
# 黒板に書かれている整数すべてを，2 で割ったものに置き換える．
# すぬけ君は最大で何回操作を行うことができるかを求めてください．

N = int(input())
A = list(map(int, input().split()))

print(A)

sum = 0
AA = []
for i in A:
    Anum = i / 2
    if Anum % 2 == 0:
        AA.append(Anum)
    elif Anum % 2 != 0:
        break
    sum += 1
    
print(sum)
print(AA)

# まだ途中