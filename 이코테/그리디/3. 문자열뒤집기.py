lst = list(map(int, input()))
n = len(lst)
match = lst[0]
ans = 0
i = 1
while i < n:
    if lst[i] != match:
        if i==n-1:
            ans += 1
            break
        else:
            for j in range(i+1, n):
                if lst[j] == match or j == n-1:
                    ans += 1
                    i = j+1
                    break
    else:
        i += 1
print(ans)

# 제공된 코드 참고
lst = list(map(int, input()))
n = len(lst)
match = lst[0]
ans = 0
for i in range(n-1):
    if lst[i]!=lst[i+1] and lst[i+1]!=match:
        ans +=1
print(ans)