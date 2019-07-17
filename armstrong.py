b,c=map(int,input().split())
for i in range(b+1,c):
  sum=0
  a=i
  while a>0:
    s=a%10
    sum=sum+s**3
    a=a//10
    if (sum==i):
      print(i,end=" ")
