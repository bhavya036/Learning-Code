print("==============================")
print("==============================")
print("Average Marks OF Student pgm")
print("==============================")
print("==============================")

Math = int(input("Enter the Math Marks :"))
Science = int(input("Enter theScience Marks :"))
Chemistry = int(input("Enter the Chemistry Marks :"))
Computer = int(input("Enter the Computer Marks :"))
Sst = int(input("Enter the Sst Marks :"))

avg = (Math + Science + Chemistry + Computer + Sst) / 5

if avg in range (90,100):
    print("Awsome You have Achieved A+ :)")

elif avg in range (80,89):
    print("Very Good You have Achieved A :)")
    
elif avg in range (70,79):
        print("Good You have Achieved B+ :)")
        
elif avg in range (60,69):
    print("Best You have Achieved B :)")
    
elif avg in range (50,59):
    print("Work More You have Achieved C :)")
    
elif avg in range (35,49):
    print("You nedd to do more hard work you passed with D grade :)")
    
else:
        print("sorry You have not cleared this examination :( ")
        
    

