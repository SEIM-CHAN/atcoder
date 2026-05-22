# 1 以上N 以下の整数のうち、10 進法での各桁の和がA 以上B 以下であるものの総和を求めてください。

N, A, B = map(int, input().split())
# 20 2 5
# 1~Nまでの数列を用意
# forで取り出して、各桁の和を算出
# A以上B以下であれば空の配列にappend

nums = [i + 1 for i in range(N)]
sumlist = []
for num in nums:
    num_sum = sum(list(map(int, str(num))))
    print(num_sum)
    if num_sum >= A or num_sum < B:
        sumlist.append(num_sum)

result = sum(sumlist)
print(result)
