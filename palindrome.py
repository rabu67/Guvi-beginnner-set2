x=int(input("enter a number"))
temp=x
rev=0
while(x>0):
  dig=x%10
  rev=rev*10+dig
  x=x//10
if(rev==temp):
  print("yes")
else:
  print("no")
