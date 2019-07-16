from itertools import combinations
i,n=map(int,input().split())
m=len(str(i))
str_1 = list(combinations(str(i),m-n))
str_1 = sorted(str_1)
print(*str_1[0],sep='')
