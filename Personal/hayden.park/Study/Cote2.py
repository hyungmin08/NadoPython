import os

def solution(cost, x):
    count = 0
    for _ in range(len(cost)):
        if x >= cost[-1]:
            count = count + 2**(len(cost)-1)
            print("value=",len(cost)-1)
            print("count=",count)
            x = x - cost[-1]
            cost.pop()
        else:
            cost.pop()
    return count % (10**9+7)

    
cost_count = int(input().strip())
cost = []

for _ in range(cost_count):
    cost_item = int(input().strip())
    cost.append(cost_item)
x = int(input().strip())


result = solution(cost, x)

print(result)
