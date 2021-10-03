N, K = map(int, input().split())

cnt = 0
while(N != 1):
    if N % K == 0:
        N /= K
        cnt += 1
    else:
        N -= 1
        cnt += 1
print(cnt)

#쉽게 풀었다. 2m 5s
#근데,,, 제대로 푼게 맞나