for i in range(int(input())):
    x,y = map(int,input().split())
    x += y
    if(x>=7):
        print("Yes")
    else:
        print("No")