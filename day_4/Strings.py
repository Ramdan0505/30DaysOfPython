#Day 4 of 30 days of Python
# Strings

# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.\
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
full_string = str1 + ' ' + str2 + ' ' + str3 + ' ' + str4 
print(full_string)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
str5 = 'Coding'
str6 = 'For'
str7 = 'All'
full_string2 = str5 + ' ' + str6 + ' ' + str7
print(full_string2)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding for All"

# Print the variable company using print().
print(company) 

# Print the length of the company string using len() method and print().
print(len(company))

# Change all the characters to uppercase letters using upper() method.
print(company.upper())

# Change all the characters to lowercase letters using lower() method.
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[0:6]) # 'Coding'

# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.find('Coding')) # It returns the index of the first occurrence of 'Coding', which is 0.

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Python'))

# Change Python for Everyone to Python for All using the replace method or other methods.
new_company = "python for Everyone"
print(new_company.replace('Everyone', 'All'))

# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(' ')) # ['Coding', 'for', 'All']

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
tech_companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(tech_companies.split(', ')) # ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# What is the character at index 0 in the string Coding For All.
print(company[0]) # 'C' 

# What is the last index of the string Coding For All.
print(company[-1]) # 'l'

# What character is at index 10 in "Coding For All" string.
print(company[10]) # 'A'

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
python_words = "Python For Everyone".split(' ')
python_acronym = ''.join([word[0] for word in python_words])
print(python_acronym)  # 'PFE'

# Create an acronym or an abbreviation for the name 'Coding For All'.
coding_words = "Coding For All".split(' ')
coding_acronym = ''.join([word[0] for word in coding_words])
print(coding_acronym)  # 'CFA'
# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C')) # 0

# Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('f')) # 7

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l')) # 14

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because')) # 30

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence.rindex('because')) # 38

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
start_index = sentence.find('because')
end_index = sentence.rindex('because') + len('because')
sliced_phrase = sentence[start_index:end_index]
print(sliced_phrase) # 'because because because'

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = sentence.find('because')
print(first_occurrence) # 30

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = sentence[first_occurrence:sentence.rindex('because') + len('because')]

# Does ''Coding For All' start with a substring Coding?
print(company.startswith('Coding')) # True

# Does 'Coding For All' end with a substring coding?
print(company.endswith('coding')) # False

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
trailing_spaces = '   Coding For All    '
print(trailing_spaces.strip()) # 'Coding For All'

# Which one of the following variables return True when we use the method isidentifier(): 30DaysOfPython, thirty_days_of_python
print('30DaysOfPython'.isidentifier()) # False
print('thirty_days_of_python'.isidentifier()) # True

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(libraries)) # 'Django # Flask # Bottle # Pyramid # Falcon'

# Use the new line escape sequence to separate the following sentences. "I am enjoying this challenge." "I just wonder what is next."
print("I am enjoying this challenge.\nI just wounder what is next.")

# Use a tab escape sequence to write the following lines.
""""Name      Age     Country   City
Asabeneh  250     Finland   Helsinki"""
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki")

# Use the string formatting method to display the following:
""""radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square."""
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

# Make the following using string formatting methods:
"""""8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144"""
a = 8
b = 6
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b} = {a ** b}")
