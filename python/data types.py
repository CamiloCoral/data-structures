print("Hello. Welcome to data structures class !!!")

number1 = 10
print(f"Var number1 is: {type(number1)}")
gravity = 9.8
print(f"Var gravity is: {type(gravity)}")
numberx = 8j
print(f"Var numberx is: {type(numberx)}")

# String Data Types
my_name = "Camilo"
fullname = "Peter McDonald"
description = '''
    Hello, how's it going?
    This is amazing !!!
'''
print(f"Var my_name is: {type(my_name)}")
print(f"Var fullname is: {type(fullname)}")
print(f"Var description is: {type(description)}")
#lists
personal_info = [
'Camilo',
'Coral',
21, 
True,
'3155876117',
'Pasto',
['Juli',9]
]
print(personal_info)
# Show father age
print(f"Father age:{personal_info[2]}")
print("Father city: ",personal_info[5])
#Show daugther name and age
print(f"Daugther Name: {personal_info[6][0]}")
print(f"Daugther age: {personal_info[6][1]}")
print(type(personal_info))
#Update father age
new_age = input("Please, type the new father age:")
personal_info[2] = new_age
print(f"New Father age is:{personal_info[2]}")
# Add new information
personal_info.append('Malala')
print(personal_info)

#Tuple
User_data = ("Benazir", "Butto", 35)
print(User_data)
print(User_data[0])
new_age = 40
User_data[2] = new_age

countries_info = {
    'country_name': 'Colombia',
    'Capital': 'Bogota',
    'Abbrev': 'CO',
    "Code": 123456
}
print(countries_info[0])



