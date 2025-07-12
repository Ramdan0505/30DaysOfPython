import math
# This is Day 3 of 30 days of Python programming challenge

#Excercise: Operators
int_age = 20
float_height = 5.3
complex_number = 2 + 3j 
user_base = float(input("Enter base: "))
user_height = float(input('Enter height: ')) 
user_area_of_triangle = 0.5 * float(user_base) * user_height
print('Area of triangle:', user_area_of_triangle)

# Area of triangle using user input
user_side_a = float(input('Enter side a: '))
user_side_b = float(input('Enter side b: '))
user_side_c = float(input('Enter side c: '))
user_perimeter_of_triangle = user_side_a + user_side_b + user_side_c
print('Perimeter of triangle:' , user_perimeter_of_triangle)

# Area of rectangle using user input
user_length = float(input('Enter length: '))
user_length = float(input('Enter length: '))
user_area_of_rectangle = user_length * user_length
print('Area of rectangle:', user_area_of_rectangle)

# perimeter of rectangle using user input 
user_length = float(input('Enter length: '))
user_width = float(input('Enter width: '))
user_perimeter_of_triangle = 2 * (user_length + user_width)
print('Perimeter of rectangle:', user_perimeter_of_triangle)

# radius of a circle using user input
pi = 3.14
radius = float(input('Enter radius: '))
area = pi * radius ** 2
print('Area of circle:', area)

# circumference of a circle using user input
pi = 3.14
user_r = float(input('Enter_radius: '))
user_circumference_of_circle = 2 * pi * user_r
print('Circumference of circle:.', user_circumference_of_circle)

# Calculate the slope 
slope = 2
y_intercept = -2
x_intercept = -y_intercept / slope 

# calculate m = (y2 - y1) / (x2 - x1)
y2 = 10
y1 = 2
x2 = 6
x1 = 2
m = (y2 - y1) / (x2 - x1)
print('slope:', m)

# Calculate Euclidean distance
euclidean_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('Euclidean distance:', euclidean_distance)

# Calculate y = x^2 + 6x + 9 and find the value to make y and x equal 0
x = -3
y = x ** 2 + 6 * x + 9
print('y = x^2 + 6x + 9:', y)

# find the length of 'python' and 'dragon' and make a false comparison statement
python_length = len('python')
dragon_length = len('dragon')
comparison = python_length > dragon_length
print('Is python length greater than dragon length?', comparison)

# Check if 'on' is found in both 'python' and 'dragon'
python_contains_on = 'on' in 'python'
dragon_contains_on = 'on' in 'dragon'
print('Does python contain "on"?', python_contains_on)
print('Does dragon contain "on"?', dragon_contains_on)

# I hope this course is not full of jargon use in operator to check if jargon is in the sectence
jargon = 'jargon'
sentence = 'I hope this course is not full of jargon'
jargon_in_sentence = jargon in sentence
print('Is "jargon" in the sentence?', jargon_in_sentence)

# their is no 'on' in both python and dragon
no_on_in_both = not (python_contains_on and dragon_contains_on)
print("Is 'on' not in both python and dragon?", no_on_in_both)

# Find the length of the text python and convert the value to float and convert it to string
python_text = 'python'
python_length_float = float(len(python_text))
python_length_str = str(python_length_float)
print('Length of python as float:', python_length_float)
print('Lemgth of python as string:', python_length_str)

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = 8
is_even = number % 2 == 0
print('Is the number even?', is_even)

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
floor_divion_check = 7 // 3 == int(2.7)
print('Is floor division of 7 by 3 equal to int(2.7)?', floor_divion_check)

# Check if type of '10' is equal to type of 10
type_check = type('10') == type(10)
print('Is type of "10" equal to type of 10?', type_check)

# Check if int('9.8') is equal to 10
int_conversion_check = int(float('9.8')) == 10
print('Is int("9.8") equal to 10?', int_conversion_check)

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = float(input("Enter hours worked: "))
rate_per_hour = float(input("Enter rate per hour: "))
pay = hours * rate_per_hour
print('Pay of the person:', pay) 

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
year = float(input("Enter number of years: "))
seconds_in_a_year = 365 * 24 * 60 * 60
total_seconds = year * seconds_in_a_year
print('Total seconds a person can live:', total_seconds)

# Write a Python script that displays the following table
"""1 1 1 1 1
   2 1 2 4 8
   3 1 3 9 27
   4 1 4 16 64
   5 1 5 25 125"""

n = 1
print(n, 1, n, n**2, n**3)

n = 2
print(n , 1, n, n**2, n**3)

n = 3
print(n, 1, n, n**2, n**3)

n = 4
print(n, 1, n, n**2, n**3)

n = 5
print(n, 1, n, n**2, n**3)



