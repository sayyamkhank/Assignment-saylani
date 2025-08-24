"""Write a program that accepts a list from user and print the alternate element of list."""
list1 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    list1.append(element)
print("Alternate elements of the list are:")
for i in range(0, n, 2):
    print(list1[i])

""""Write a program that accepts a list from user. Your program should reverse the content of list and
display it. Do not use reverse() method."""
list1 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = input("Enter element {}: ".format(i + 1))
    list1.append(element)
print("Reversed list is:")
for i in range(n - 1, -1, -1):
    print(list1[i])

    """Find and display the largest number of a list without using built-in function max(). Your program
should ask the user to input values in list from keyboard."""
list1 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    list1.append(element)
largest = list1[0]
for i in range(1, n):
    if list1[i] > largest:
        largest = list1[i]
print("Largest element in the list is:", largest)

""". Write a program that rotates the element of a list so that the element at the first index moves to the
second index, the element in the second index moves to the third index, etc., and the element in the last
index moves to the first index."""
list1 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input("Enter element {}: ".format(i + 1)))
    list1.append(element)
if n > 0:
    first_element = list1[0]
    for i in range(1, n):
        list1[i - 1] = list1[i]
    list1[n - 1] = first_element
print("List after rotation:")
for i in range(n):
    print(list1[i])

""". Write a program that input a string and ask user to delete a given word from a string."""
string = input("Enter a string: ")
word_to_delete = input("Enter the word to delete: ")
words = string.split()
if word_to_delete in words:
    words.remove(word_to_delete)
    print("String after deletion:")
    print(" ".join(words))
else:
    print("Word not found in the string.")

""". Write a program that reads a string from the user containing a date in the form mm/dd/yyyy. It
should print the date in the form March 12, 2021"""

date_string = input("Enter a date (mm/dd/yyyy): ")
month, day, year = date_string.split("/")
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
if 1 <= int(month) <= 12 and 1 <= int(day) <= 31 and 1900 <= int(year) <= 2100:
    print("{} {}, {}".format(months[int(month) - 1], day, year))
else:
    print("Invalid date format.")

"""Write a program with a function that accepts a string from keyboard and create a new string after
converting character of each word capitalized. For instance, if the sentence is "stop and smell the roses."
the output should be "Stop And Smell The Roses"""

def capitalize_words(sentence):
    words = sentence.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

"""Find the sum of each row of matrix of size m x n. For example for the following matrix output will be
like this :
Sum of row 1 = 32
Sum of row 2 = 31
Sum of row 3 = 63"""

def sum_of_rows(matrix):
    for i, row in enumerate(matrix):
        print("Sum of row {} = {}".format(i + 1, sum(row)))

"""Write a program to add two matrices of size n x m"""
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result

"""Write a program to multiply two matrices"""
def multiply_matrices(matrix1, matrix2):
    if not matrix1 or not matrix2 or len(matrix1[0]) != len(matrix2):
        raise ValueError("Incompatible matrix dimensions")

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            element = sum(matrix1[i][k] * matrix2[k][j] for k in range(len(matrix2)))
            row.append(element)
        result.append(row)
    return result