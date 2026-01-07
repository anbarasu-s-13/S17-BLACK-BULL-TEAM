s=str(input("Enter your password:"))
while(len(s)<8):
    if(len(s)>=8):
        break
    else:
        s=str(input("Enter your password again:"))
up=0
low=0
num=0
sp=0
for i in s:
    if(i.isupper()):
        up=1
    elif(i.islower()):
        low=1
    elif(i.isnumeric()):
        num=1
    elif(i.isascii()) :
         sp=1
    else:
        continue
sum=0
sum=up+low+num+sp
if(sum<3):
    print("password strength: weak")
elif(sum==3):
    print("password strength:medium")
else:
    print("password strength: strong")