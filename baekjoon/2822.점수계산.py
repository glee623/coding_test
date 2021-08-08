scores = [0] * 8
score_idx = [x + 1 for x in range(8)]

for _ in range(8):
    scores[_] = int(input())

for i in range(8):
    min_idx = i
    for j in range(i+1, 8):
        if scores[min_idx] > scores[j]:
            min_idx = j
    scores[min_idx], scores[i] = scores[i], scores[min_idx]
    score_idx[min_idx], score_idx[i] = score_idx[i], score_idx[min_idx]

print(sum(scores[-5:]))
for x in sorted(score_idx[-5:]):
    print(x, end = ' ')
