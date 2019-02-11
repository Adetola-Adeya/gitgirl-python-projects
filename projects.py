# gitgirl-python-projects
questions: 
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.  How does an even / odd number react differently when divided by 2?
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

answers

name = input("What is your name:")
age = int(input("How old are you:"))
yearwhen_hundred = int(2019 - age) + 100
print ("%s will be a hundred years old in the year %s" % (name, yearwhen_hundred))

#start new question

number = input("Give a number:")
if int(number) % 2 == 0:
    print ("This number is Even")
else:
    print ("This number is Odd")

#start new question

a_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
new_list = []
for x in a_list:
  if x % 2 == 0:
    new_list.append(x)
print(new_list)
