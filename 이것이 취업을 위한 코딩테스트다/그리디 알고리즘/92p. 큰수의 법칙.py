N, M, K = map(int, input().split())
Ns = list(map(int, input().split()))

#test case 01
# N, M, K = 5, 8, 3
# Ns = [2, 4, 5, 4, 6]

# #test case 02
# N, M, K = 5, 7, 3
# Ns = [3, 4, 3, 4, 3]

# Q. 일단, 제일 큰수와 두번째 큰수만 있으면 문제가 풀릴 것 같은데 예외는 존재하지 않는가 ?

my_list = sorted(Ns)[-2:]
answer = (my_list[1] * K * (M // K)) + (my_list[0] * (M % K))

print(answer)
