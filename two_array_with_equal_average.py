x = int(input())
y = list(map(int, input().split()))
z = int(len(y)/2)
if sum(y[:z])//len(y[:z]) == sum(y[z:])//len(y[z:]):
    print('yes')
else:
    print('no')
