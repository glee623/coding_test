N, M = map(int, input().split())
row_min = []

for i in range(N):
    row = list(map(int, input().split()))
    row_min.append(min(row))

print(max(row_min))

#쉽게 풀었다. 3m 4s

#책에 나와있는 append를 쓰지 않는방법. 굳이 값들을 다 저장해놓고 쓸필요 x
result = 0
for i in range(N):
    row = list(map(int, input().split()))
    row_min = min(row)
    result = max(result, row_min)
    #작은 값들을 result에 저장하고 새로운 row_min 과 비교하고
    #result에 max값을 저장할거니깐, 작은값 0을 미리 저장해놓기