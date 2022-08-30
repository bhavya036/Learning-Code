a = int(input("Enter the needed rows :"))

for i in range (a):
    for j in range(i+1):
        if (j%2 != 0):
            print('0', end = " ")
        else:
                print('1', end = " ")
        #print("",end=" ")
        
    print()