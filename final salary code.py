print("SALARY PROGRAM")
name= str(input("Enter name of employee:"))
basic=float(input("Enter Basic Salary :"))
da=float(basic*0.9)
hra=float(basic*0.1)

netpay=float(basic+da+hra)

if netpay>100000 :
 tax=float(basic*0.05)
else:
     tax=float(basic*0.02)
     
final=netpay-tax

print("\n\n")
print("S A L A R Y D E T A I L E D B R E A K U P ")
print("==============================================")
print(" NAME OF EMPLOYEE : ",name)
print(" BASIC SALARY : ",basic)
print(" DEARNESS ALLOW. : ",da)
print(" HOUSE RENT ALLOW.: ",hra)
print(" TAX : ",tax)
print("==============================================")
print(" NET SALARY PAY : ",final)
