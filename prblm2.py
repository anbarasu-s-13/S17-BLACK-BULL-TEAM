a=int(input("Enter your total number of classes:")) 
b=int(input("Enter your number of classes attended:"))
cal = ((b/a)*100) #calculating the percentage
print("Attendence percentage:",cal)
if(int(cal)>=75):
    print("status: ELIGIBLE")
else:
    print("status: NOT ELIGIBLE")
    re=75-int(cal) #REMAINING PERCENTAGE
    d=int((re/100)*a) #NO. OF CLASSES TO ATTEND
    print("Additional classes required:",d)