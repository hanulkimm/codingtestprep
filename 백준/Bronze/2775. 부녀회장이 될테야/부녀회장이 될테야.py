t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    ppl = [x for x in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            ppl[j] += ppl[j-1]
    print(ppl[-1])
