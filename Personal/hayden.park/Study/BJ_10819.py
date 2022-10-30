# |A0 - A1| + |A1 - A2| + ... + |A(n-2) - A(n-1)| 의 최대값
# 1. 내장 모듈 이용하기
# from itertools import permutations

# 2. 직접 순열 함수 만들기 (perm)
def func_sum(n, numlist):
    sum = 0
    for i in range(n):
        if i >= n-1:
            break
        else:
            sum = sum + abs(numlist[i]-numlist[i+1])
    return sum

def perm(lst,n):
    ret = []
    if n > len(lst): return ret
    if n==1:
        for i in lst:
            ret.append([i])
    elif n>1:
        for i in range(len(lst)):
            temp = [i for i in lst] 
            temp.remove(lst[i])
            for p in perm(temp, n-1):
                ret.append([lst[i]]+p)
    return ret

n = int(input())
numlist = list(map(int, input().split()))
allcase = perm(numlist,n)
answer = 0
for i in allcase:
    max = func_sum(n,i)
    if max >= answer:
        answer = max
    
print(answer)

# 다른사람 정답 : 
# n = int(input().strip())
# case = sorted([int(v) for v in input().strip().split()])
# case.sort()
# def abs_sum(arr):
#     return sum([abs(arr[i] - arr[i+1]) for i in range(len(arr) - 1)])
# asc = [case[i // 2] if i % 2 == 0 else case[(i // 2 + 1) * (-1)] for i in range(len(case))]
# desc = [case[i // 2] if i % 2 == 1 else case[(i // 2 + 1) * (-1)] for i in range(len(case))]
# print(max([abs_sum([asc[-1]] + asc[:-1]), abs_sum([desc[-1]] + desc[:-1])]))