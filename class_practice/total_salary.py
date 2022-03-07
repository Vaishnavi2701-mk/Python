basic_pay=float(input("Enter the basic pay \n"))
print("---------------------------------------------")

print("\n     # Net Salary of an Employee #\n")

print("---------------------------------------------")

print("Basic salary of an employee     |",basic_pay)

HRA=0.1*basic_pay
print("---------------------------------------------")
print("HRA of Basic pay of an employee |",HRA)
print("---------------------------------------------")

TA=0.5*basic_pay 

print("TA on the Basic pay             |",TA)
print("---------------------------------------------")
Total_salary=basic_pay+HRA+TA

Tax=0.2*Total_salary
print("Tax payable                     |",Tax)
print("---------------------------------------------")

Net_salary=Total_salary-Tax
print("Net salary                      |",Net_salary)
print("---------------------------------------------")
