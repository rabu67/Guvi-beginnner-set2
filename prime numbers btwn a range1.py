x=int(input("enter a starting number"))
y=int(input("enter a ending number"))
for num in range(x,y+1):
    if num > 0:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
