# Basic Python
# You can print the variables to see the results
# This list is not complete, just some of the most useful
# Remember that google is a great tool



#---Interact with User---
# Output
print("I like tomato soup")

# Input
name = input("What's your name again?")



#---Defining Variables---
x = 12 #Sets x to the value 12



#---Math Operators---
# Addition
x = 6 + 3 #Sets x to value 9

# Subtraction
x = 6 - 3 #Sets x to value 3

# Multiplication
x = 6 * 3 #Sets x to value 18

# Division
x = 6 / 3 #Sets x to value 2



#---Comparative Operators---
#Note: the numbers can be replaced with variables

# Equal to
3 == 3 #True
2 == 4 #False

# Greater than
#Note: use >= for greater than or equal
5 > 3 #True
1 > 4 #False
3 > 3 #False

# Less than
#Note: use <= for less then or equal
2 < 3 #True
4 < 2 #False



#---Logical Operators---
#Note: the numbers can be replaced with variables

# True if both are true
4 > 3 and 5 == 5 #True
4 == 2 and 5 > 2 #False

# True if either is true
4 < 3 or 6 > 3 #True
2 == 3 or 5 < 1 #False

# True if false
not 2 == 3 #True
not 5 == 5 #False



#---Decide Between Options---
x = 4

# If statement
if x == 4:
    print("x is 4")

# Else statement
if x == 3:
    print("x is 3")
else:
    print("x is not 3")

# Elif statement
if x == 3:
    print("x is 3")
elif x == 4:
    print("x is 4")
else:
    print("x is not 3 nor 4")



#---Repeating an Action---
for i in range(10): #Note: this example is 0 to 10, non-inclusive of 10
    print(i)



#---Lists---
# Defining Lists
x = [2, 3, 5] #1D list
x = [[3, 5], [7, 2], [9, 4]] #2D list

# Acessing Lists
#Note: finds items in list by location, not value
x[0] #1D
x[2][1] #2D



#---Functions---
# Defining a function
def printHelloPerson(name):
    print("Hello " + name)

# Call a function
printHelloPerson("Bob")