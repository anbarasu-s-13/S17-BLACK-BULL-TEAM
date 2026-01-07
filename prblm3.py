av=2
i=1
while(av>=0):
    s=str(input("ALLOCATE:"))
    av-=1
    if(av<0):
        print("Available Rooms :0")
        print("No Rooms Available")
        break
    
    print("Room Allocated to",s,": Room",i)
    i+=1
    

