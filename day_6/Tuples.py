# Day 6 of 30 days of Python

# create an empty tuple
my_tuple = ()
print(my_tuple)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
my_tuple = ('Hala', 'Hola', 'Khalid')
print(my_tuple)

# Join brothers and sisters tuples and assign it to siblings
siblings = my_tuple + ('Hala', 'Hola', 'Khalid')
print(siblings)

# How many siblings do you have?
print(len(siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = siblings + ('John Doe', 'Jane Doe')
print(family_members)

# Excercise Level 2
# Unpack siblings and parents from family_members
