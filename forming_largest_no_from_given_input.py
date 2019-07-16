x=int(input())
y=input("")
z=list(y.split(" "))
z.sort(reverse=True)
y=list(map(int,z))
if sum(y)==0:
  print("0")
else:
  a="".join(z)
  print(a)
