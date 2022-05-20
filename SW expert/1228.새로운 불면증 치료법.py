T = int(input())

for i in range(T):
    xN = input()
    N = int(xN)
    answer = []
    cons = 2
    cnt = 0

    while (len(answer) != 10):
        for j in list(xN):
            answer.append(j)
        answer = list(set(answer))
        xN = str(N * cnt + 2)
        cnt += 1

    print(f'#{i + 1} {N * cnt}')
