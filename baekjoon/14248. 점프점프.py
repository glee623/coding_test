import collections

def bfs(now, dis):  # 현재 있는 돌의 위치, 갈수 있는 거리
    global cnt

    que = collections.deque()  # que 선언
    que.append((now, dis))  # 돌 인덱스, 거리
    visited[now] = 1  # 현재 있는 돌, 방문 flag

    while que:
        now, dis = que.pop()
        for i in range(2):
            dis *= -1
            if -1 < now + dis < n and visited[now + dis] == 0:
                visited[now + dis] = 1
                que.append((now + dis, Ai[now + dis]))
                cnt += 1


n = int(input())  # 스톤 개수
Ai = list(map(int, input().split()))  # 스톤에서 갈수 있는 거리
s = int(input())  # 현재 있는 돌의 위치

visited = [0] * n
cnt = 1
bfs(s - 1, Ai[s - 1])
print(cnt)