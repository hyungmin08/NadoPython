n = int(input())
numlist = list(map(int, input().split()))

sum = 0
for i in range(n):
    sum = sum + abs(numlist[i]-numlist[i+1])
    if i >= n-1:
        break
print(sum)

