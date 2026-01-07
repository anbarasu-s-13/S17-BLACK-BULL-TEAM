a=float(input("Enter your total number of classes:")) 
b=float(input("Enter your number of classes attended:"))
cal = ((b/a)*100) #calculating the percentage
print("Attendence percentage:",cal,"%")
if(float(cal)>=75):
    print("status: ELIGIBLE")
else:
    print("status: NOT ELIGIBLE")
    re=75-float(cal) #REMAINING PERCENTAGE
    d=float((re/100)*a) #NO. OF CLASSES TO ATTEND
    print("Additional classes required:",d)