a,b=list(map(int,input().split()))
c,d=list(map(int,input().split()))
e,f=list(map(int,input().split()))
if a==b or c==d or e==f or a==c==f or b==d==e:
    print('yes')
else:
    print('no')
