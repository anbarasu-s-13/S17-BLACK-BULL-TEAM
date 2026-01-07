a=[]
b=[]
c=[]
count=1
while True:
    s=str(input("Enter your name and dept:"))
    if((s)=='0'):
        break
    if(s[-3:]=="ECE" or s[-3:]=="ece"):
        a.append(s)
    elif(s[-3:]=="CSE" or s[-3:]=="cse"):
        b.append(s)
    elif(s[-3:]=="EEE" or s[-3:]=="eee"):
        c.append(s)


for i in range(len(a)):
    print("Seat",count,"-",a[i])
    count+=1
    for j in range(i,i+1):
       print("Seat",count,"-",b[j])
       count+=1 
       for k in range(i,i+1):
           print("Seat",count,"-",c[k])
           count+=1