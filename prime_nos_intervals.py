a,b=input().split()
a=int(a)
b=int(b)
for i in range(a+1,b):
	count=0
	for x in range(1,i+1):
		if(i%x==0):
			count+=1
	if(count==2):
		print(i,end=' ')
