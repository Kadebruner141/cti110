# A project that calculates the number of pizzas and slices you need depending on number of students
#2/16/2022
#CTI-110 P1HW2 - Pizza Order
#Kade Bruner
#

#input int student
student = int(input('How many students do you want to order pizza for? '))
print()
#Set slice = student * 3
#Set pizza = slice /6
slice = student * 3
pizza = slice / 6
#Displaying the number of students
#Displaying the number of slices needed
#Displaying the number of pizzas needed
print('-----Pizza Order--------')
print('Number of Students :', student)
print('Pizza Slices Needed:', slice)
print('Pizzas Needed :', pizza)
print('-------------------------')