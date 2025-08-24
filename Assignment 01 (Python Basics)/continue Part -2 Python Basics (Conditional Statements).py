##A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

classes_held = int(input("Enter the number of classes held: "))
classes_attended = int(input("Enter the number of classes attended: "))

attendance_percentage = (classes_attended / classes_held) * 100
print("Percentage of classes attended:", attendance_percentage)

if attendance_percentage < 75:
    print("The student is not allowed to sit in the exam.")
else:
    print("The student is allowed to sit in the exam.")

##Modify the above question to allow student to sit if he/she has medical cause. Ask user if he/she has medical cause or not ( 'Y' or 'N' ) and print accordingly.

medical_cause = input("Does the student have a medical cause? (Y/N): ")

if medical_cause.upper() == 'Y':
    print("The student is allowed to sit in the exam.")

##Write a program to check if a year is leap year or not.
##If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

##Ask user to enter age, gender ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.
#if employee is a male and age is in between 20 to 40 then he may work in anywhere
#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#And any other input of age should print "ERROR"

age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ")
marital_status = input("Enter marital status (Y/N): ")

if gender.upper() == 'F':
    print("Place of service: Urban Areas")
elif gender.upper() == 'M':
    if 20 <= age <= 40:
        print("Place of service: Anywhere")
    elif 40 < age <= 60:
        print("Place of service: Urban Areas")
    else:
        print("ERROR")

 ##Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : Unit Price
#uptp 100 units no charge Next 200 units Rs 5 per unit After 200 units Rs 10 per unit (For example if input unit is 350 than total bill amount is Rs.3500 (For example if input unit is 97 than total bill amount is Rs.0 (For example if input unit is 150 than total bill amount is Rs.750

units = int(input("Enter the number of units consumed: "))
if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + (units - 300) * 10
print("Total bill amount is Rs.", bill)

##Take input of age of 3 people by user and determine oldest and youngest among them.

age1 = int(input("Enter age of person 1: "))
age2 = int(input("Enter age of person 2: "))
age3 = int(input("Enter age of person 3: "))

oldest = max(age1, age2, age3)
youngest = min(age1, age2, age3)

print("Oldest person is:", oldest)
print("Youngest person is:", youngest)