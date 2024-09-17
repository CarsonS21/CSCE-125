s =0
c=0
sum=0
while s != 999:
  s=int(input("enter your test score or 999 to exit: "))
  if(s >=0 and s<=100):
    sum+=s
    c+=1

av=(sum)/c
print("average = ",av)

