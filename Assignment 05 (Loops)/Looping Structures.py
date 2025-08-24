"""1. Write a Python program to print the numbers from 1 to 10 using a for loop."""

for i in range(1, 11):
    print(i)

"""2. Write a Python program to print the numbers from 20 to 1 using a while loop."""

i = 20
while i > 0:
    print(i)
    i -= 1

""" 3. Write a program to print even numbers from 1 to 10."""

for i in range(1, 11):
    if i % 2 == 0:
        print(i)

"""4. Write a program that prompts the user to enter a number n and prints all the
numbers from 1 to n"""

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

"""5. Write a program that prompts the user to enter a number n, and then prints all the
odd numbers between 1 and n. """

n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

"""6. Write a program that prints 'Happy Birthday!' five times on screen. """

for i in range(5):
    print("Happy Birthday!")

"""7. Write a program that takes a number n as input from the user and generates the first
n terms of the series formed by squaring the natural numbers.
Sample output
Enter a number: 6
The first 6 terms of the series are:
1 4 9 16 25 36 """

n = int(input("Enter a number: "))
print("The first", n, "terms of the series are:")
for i in range(1, n + 1):
    print(i * i, end=" ")

"""8. Write a program that prompts the user to input a number and prints its multiplication
table. """

n = int(input("Enter a number: "))
print("Multiplication table for", n)
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

""" 9. Write a Python program to print the first 8 terms of an arithmetic progression starting
with 3 and having a common difference of 4.
The program should output the following sequence:
3 7 11 15 19 23 27 31"""

n = 8
a = 3
d = 4
for i in range(n):
    print(a + i * d, end=" ")

"""10. Write a Python program to print the first 6 terms of a geometric sequence starting
with 2 and having a common ratio of 3.
The program should output the following sequence:
2 6 18 54 162 486"""

n = 6
a = 2
r = 3
for i in range(n):
    print(a * (r ** i), end=" ")

"""11. Write a program that asks the user for a positive integer value. The program should
calculate the sum of all the integers from 1 up to the number entered. For example, if
the user enters 20, the loop will find the sum of 1, 2, 3, 4, ... 20. """

n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    total += i
print("The sum of all integers from 1 to", n, "is:", total)

"""12. write a program that takes a positive integer N as input and calculates the sum of
the reciprocals of all numbers from 1 up to N. The program should display the final sum.
Output of the program should be like:
Enter a positive integer: 5
The sum of reciprocals from 1 to 5 is: 2.28"""

n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    total += 1 / i
print("The sum of reciprocals from 1 to", n, "is:", total)

"""13. Write a program that prompts the user to enter a number and repeats this process 5
times. The program should accumulate the numbers entered and then display the final
running total.
Sample Output:
Enter a number: 10
Enter a number: 15
Enter a number: 35
Enter a number: 40
Enter a number: 50
The final running total is: 150"""

n = 5
total = 0
for i in range(n):
    num = int(input("Enter a number: "))
    total += num
print("The final running total is:", total)

"""14. Write a program that prompts the user to enter a positive integer and calculates its
factorial. The factorial of a positive integer 'n' is denoted as 'n!' and is calculated by
multiplying all the integers from 1 to 'n' together. For example, the factorial of 5
(denoted as 5!) is calculated as 1 x 2 x 3 x 4 x 5.
The program should display the factorial value if the input is a positive number, or
display a message stating that the factorial does not exist for negative numbers.
Additionally, for an input of zero, the program should output that the factorial of 0 is 1."""

n = int(input("Enter a positive integer: "))
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("The factorial of", n, "is:", factorial)

"""15. Write a Python program that prompts the user to enter a base number and an
exponent, and then calculates the power of the base to the exponent. The program
should not use the exponentiation operator (**) or the math.pow() function. The
program should handle both positive and negative exponents"""

base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

if exponent == 0:
    result = 1
else:
    result = 1
    for i in range(abs(exponent)):
        result *= base

if exponent < 0:
    result = 1 / result

print("The result of", base, "raised to the power of", exponent, "is:", result)
