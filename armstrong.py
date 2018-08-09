number=int(input("enter a number"))
sum=0
temp=0
num=number
while(num!=0):
  temp=num%10
  sum=sum+temp*temp*temp
  num=num//10
if(sum==number):
  print("yes!,Armstrong Number")
else:
  print("No!,its not a Armstrong Number")
