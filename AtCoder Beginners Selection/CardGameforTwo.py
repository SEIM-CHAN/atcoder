"""
N枚のカードがあります.
i枚目のカードには,ai​という数が書かれています.
AliceとBobは,これらのカードを使ってゲームを行います.
ゲームでは,AliceとBobが交互に1枚ずつカードを取っていきます.
Aliceが先にカードを取ります.
2人がすべてのカードを取ったときゲームは終了し,取ったカードの数の合計がその人の得点になります.
2人とも自分の得点を最大化するように最適な戦略を取った時,AliceはBobより何点多く取るか求めてください.
"""

N = int(input())
A = list(map(int, input().split()))

Alice = 0
Bob = 0

for i in range(N):
    if i % 2 != 0:
        m = max(A)
        Alice = Alice + m
        A.remove(m)
    elif i % 2 == 0:
        m = max(A)
        Bob = Bob + m
        A.remove(m)

print(Bob - Alice)
