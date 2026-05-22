# あなたは、500 円玉をA 枚、100 円玉をB 枚、50 円玉をC 枚持っています。 
# これらの硬貨の中から何枚かを選び、合計金額をちょうどX 円にする方法は何通りありますか。
# 同じ種類の硬貨どうしは区別できません。
# 2 通りの硬貨の選び方は、ある種類の硬貨についてその硬貨を選ぶ枚数が異なるとき区別されます。

A = int(input()) #500yen
B = int(input()) #100yen 
C = int(input()) #50yen
X = int(input())

'''
sum = 1200
500 * 3
100 * 5
50*6

一番大きい金額の硬貨が何枚使えるかで変わる
(500*i + 100*j + 50*k) == 1200ならcount+1
'''

# 自分の答え
count = 0
for i in range(A+1):
    if 500*i > X:
        break
    elif 500*i <= X:
            for j in range(B+1):
                if 500*i + 100*j > X:
                    break
                elif 500*i + 100*j <= X:
                        for k in range(C+1):
                            if 500*i + 100*j + 50*k > X:
                                break
                            elif 500*i + 100*j + 50*k == X:
                                    count +=1

print(count)

# ほかの答え①
ans = 0 
for i in range(A+1):
    for j in range(B+1):
        for k in range(C+1):
            if 500*i + 100*j + 50*k == X:
                ans += 1

print(ans)

# ほかの答え②

                    
# 途中    
    
