import math
# this is my first python program 
# this is a comment 
# this is a another comment 

"""This is a multiline comment you
write multiple lines of text in here"""

# Day 1 - 30 days of python programming

# first we have the operators and the print function

print( 1 + 1) # addition
print( 1 - 1) # subtraction
print( 1 * 2) # multiplication
print( 4 / 2) # division
print( 4 % 2) # modulus 
print( 2 ** 2) # exponentiation 
print( 3 // 2) # floor division

# now we have Strings 

print("Ramadan Ramadan") # this is a string 
print("Ramadan family") # this is another string
print("united states of america") # this is a string with spaces
print("I love 30 days of python programming") # this is a string with numbers

# now we have data types 

print(type(10)) # int 
print(type(9.8)) # float
print(type(3.14)) # float 
print(type(4 - 4j)) # complex number 
print(type(['Ramadan', 'python', 'Ramadan'])) # list  
print(type({'Ramadan', 'python', 'Ramadan'})) # set
print(type(('Ramadan', 'python', 'Ramadan'))) # tuple

# different examples of data types
print(type('hello')) # string 
print(type(True)) # boolean
print(type(False)) # boolean 
print(type(None)) # NoneType 
print(type(10 + 5j)) # complex number 
print(type(3.14)) # float
print(type(100)) # int 
print(type([1, 2, 3, 4, 5])) # list 
print(type((1, 2, 3, 4, 5))) # tuple 
print(type({1 , 2, 3, 4, 5})) # set  
print(type({'name': 'Ramadan', 'age': 20})) # dictionary

# find Eucludean distance between (2,3) and (10,8) 
 
distance = math.sqrt((2 - 3)**2 + (10 - 8)**2)
print("Euclidean distance between (2,3) and (10,8) is:", distance) 