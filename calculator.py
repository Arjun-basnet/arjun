# Program make a simple calculator that can add, subtract, multiply and divide using functions and interest calculator.

def add(x, y):
   return x + y
def subtract(x, y):
   return x - y
def multiply(x, y):
   return x * y
def divide(x, y):
   return x / y
def interest(p,t,r):
    return p*t*r/100
print("Please Select what operation do you want make?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user
choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("Invalid input")

print("Now calculate the Interest")

principal = int(input("Enter the principal amount:"))
time = int(input("Enter the time:"))
rate = int(input("Enter the rate:"))

print(principal,"*",time,"*",rate,"/",100,"=",interest(principal,time,rate))