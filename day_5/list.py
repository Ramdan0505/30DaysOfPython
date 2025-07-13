# Day 5 of 30 Days of Python 

# Exercise Level 1
# Declare a empty list
empty_list = []

# Declare a list with more than 5 items
fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape', 'honeydew']

# Find the length of the list
print(len(fruits)) # Output: 8

# Get the first item, the middle item and the last item of the list
first_item = fruits[0]

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['John Doe', 30, 5.9, 'Single', '123 Main Street']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print(len(it_companies)) # Output: 7

# Print the first, middle and last company
print(it_companies[0]) # First company: Facebook
print(it_companies[len(it_companies) // 2]) # Middle company: IBM
print(it_companies[-1]) # Last company: Amazon

# Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies) # Output: ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Add an IT company to it_companies
it_companies.append('Tesla')
print(it_companies) # Output: ['Meta', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Tesla']

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies) // 2, 'Nvidia')
print(it_companies) # Output: ['Meta', 'Google', 'Nvidia', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Tesla']

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper() # Change 'Google' to 'GOOGLE'
print(it_companies) # Output: ['Meta', 'GOOGLE', 'Nvidia', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon', 'Tesla']

# Join the it_companies with a string '#;  '
joined_companies = '#; '.join(it_companies)
print(joined_companies) # Output: Meta#; GOOGLE#; Nvidia#; Microsoft#; Apple#; IBM#; Oracle#; Amazon#; Tesla

# Check if a certain company exists in the it_companies list.
company_to_check = 'Google'
it_companies_exists = company_to_check in it_companies
print(f"Does {company_to_check} exist in the list? {it_companies_exists}") 

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]
print(first_three_companies) 

# Slice out the last 3 companies from the list
last_three_companies = it_companies[:-3]
print(last_three_companies)

# Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2 
middle_company = it_companies[middle_index]
print(middle_company)

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle IT company or companies from the list
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# Join the following lists:
"""front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
 back_end = ['Node','Express', 'MongoDB']"""""

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Redux') + 2, 'SQL')
print(full_stack)

# Excerise 2 
# The following is a list of 10 students ages: 
# ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f"min age: {ages[0]}, max age: {ages[-1]}")

# Add the min age and the max age again to the list
ages.append(ages[0])
ages.append(ages[-1])
print(ages)

# Find the median age (one middle item or two middle items divided by two)
median_index = len(ages) // 2
median_age = (ages[median_index] + ages[median_index - 1]) / 2
print(f"median age: {median_age}")

# Find the average age (sum of all items divided by their number )
average_age = sum(ages) / len(ages)
print(f"average age: {average_age}")

# Find the range of the ages (max minus min)
age_range = ages[-1] - ages[0]
print(f"age range: {age_range}")

# Compare the value of (min - average) and (max - average), use abs() method
min_minus_average = abs(ages[0]) - average_age
max_minus_average = abs(ages[-1]) - average_age
print(f"min - average: {min_minus_average}, max - average: {max_minus_average} ")

# Find the middle country(ies) in the countries list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
middle_index = len(countries) // 2
print(countries[middle_index])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
length = len(countries)
half = (length + 1) // 2
first_half = countries[:half]
second_half = countries[half:]
print(first_half)
print(second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
first_three_countries = countries[:3]
scandic_countries = countries[3:]
print(first_three_countries)
print(scandic_countries)
