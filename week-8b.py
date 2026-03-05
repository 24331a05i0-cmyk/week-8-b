n=int(input("enter how many values: "))
result=[]
for i in range(1,n+1):
   num=int(input("enter tuple values:"))
   tup=(num,num**2)
   result.append(tup)
print(result)
