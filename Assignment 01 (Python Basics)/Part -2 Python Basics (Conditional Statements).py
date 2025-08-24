##A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.
salary = float(input("Enter your salary:"))
year_of_service = int(input("Enter your year of service:"))

if year_of_service > 5:
    bonus = salary * 0.05
    print("Your net bonus amount is:", bonus)
else:
    print("You are not eligible for a bonus.")

 ##Write a program to check whether a person is eligible for voting or not. (accept age from user) if age is greater than 17 eligible otherwise not eligible
age = int(input("Enter your age:"))
if age > 17:
    print("You are eligible for voting.")
else:
    print("You are not eligible for voting.")
    
##Write a program to check whether a number entered by user is even or odd.
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")

##Write a program to check whether a number is divisible by 7 or not. Show Answer
number = int(input("Enter a number:"))
if number % 7 == 0:
    print("The number is divisible by 7.")
else:
    print("The number is not divisible by 7.")

##Write a program to display "Hello" if a number entered by user is a multiple of five , otherwise print "Bye".
num = int(input("Enter a number:"))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")

##Write a program to display the last digit of a number.
num = int(input("Enter a number:"))
last_digit = num % 10
print("The last digit is:", last_digit)

##Take values of length and breadth of a rectangle from user and print if it is square or rectangle.
length = float(input("Enter the length of the rectangle:"))
breadth = float(input("Enter the breadth of the rectangle:"))
if length == breadth:
    print("The shape is a square.")
else:
    print("The shape is a rectangle.")

    ##Take two int values from user and print greatest among them.
num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))
if num1 > num2:
    print("The greatest number is:", num1)
else:
    print("The greatest number is:", num2)

##A shop will give discount of 10% if the cost of purchased quantity is more than 1000. Ask user for quantity Suppose, one unit will cost 100. Judge and print total cost for user.
quantity = int(input("Enter the quantity of items purchased:"))
cost_per_unit = 100
total_cost = quantity * cost_per_unit
if total_cost > 1000:
    total_cost *= 0.9  # Apply 10% discount
print("The total cost is:", total_cost)

##A school has following rules for grading system:
#a. Below 25 - F

#b. 25 to 45 - E

#c. 45 to 50 - D

#d. 50 to 60 - C

#e. 60 to 80 - B

#f. Above 80 - A

#Ask user to enter marks and print the corresponding grade.

marks = int(input("Enter your marks:"))
if marks < 25:
    print("Your grade is: F")
elif marks < 45:
    print("Your grade is: E")
elif marks < 50:
    print("Your grade is: D")
elif marks < 60:
    print("Your grade is: C")
elif marks < 80:
    print("Your grade is: B")
else:
    print("Your grade is: A")
