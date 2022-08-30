a = int(input("Enter the needed rows :"))

for i in range (a):  # For print reversing pattern take (a+1,0,-1) 
    for j in range(i+1): # for print reversing pattern take (0,i-1)
        print(j+1,end=" ") #for print* just replace j+1 by "*"
        
    print()
