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


'''
10m16s

책 뒤쪽 내용을 보니 수열관련 내용이 있다. 수열 측면에서 보면 맞을지도
좀 더 많은 test case가 필요할 것 같다.

파이썬에서는, 몫을 나타내기 위해 int(a / b) or a//b 를 사용한다
'''
