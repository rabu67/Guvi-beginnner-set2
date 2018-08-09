
n1=int(input("interval1"))
n2=int(input("interval2"))


for i in range(n1,n2+1):
  num=i
  sum=0
  while num>0:
        temp=num%10
        sum=sum+temp*temp*temp
        num=num//10
  if(sum==i):
      print(i)
 
    
