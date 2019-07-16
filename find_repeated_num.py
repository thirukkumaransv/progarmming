q=int(input())
num2=list(map(int,input().split()))
list1=[]
for i in num2:
    if num2.count(i)>1:
        if str(i) not in list1:
            list1.append(str(i))
if len(list1)==0:
    print("unique")
else:
    num2.sort()
    print(" ".join(list1))
