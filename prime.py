t=int(input(""))
if t>1:
    for i in range(2,t):
        if (t % i) == 0:
            print("no")
            break
    else:
        print("yes")

else:
    print("no")
