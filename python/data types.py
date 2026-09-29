<<<<<<< HEAD
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



=======
print("Hello. Welcome to data structures class")

number1 = 10
print(f"Var number1 is: {type(number1)}")

gravity = 9.8
print(f"Var gravity is: {type(gravity)}")

numberx = 8j
print(f"Var numberx is: {type(numberx)}")

my_name = "Camilo"
fullname = "Camilo Coral"

"Hello, hows it going?"

personal_info = [
    "Camilo",
    "Coral",
    25,
    True,
    "pasto",
    ["juli", 10]
]

print(type(personal_info))

print(f"Father age: {personal_info[2]}")
print(f"Father city: {personal_info[4]}")

print(f"Daughter name: {personal_info[5][0]}")
print(f"Daughter age: {personal_info[5][1]}")

new_age = input("please, type new father age: ")
personal_info[2] = new_age

personal_info.append("Malala")

user_data = ("Benazir", "Bhutto", 25, "Pakistan")
print(user_data)
print(user_data[0])

new_age = 40

countries_info = {
    "country_name": "colombia",
    "capital": "bogota",
    "abbrev": "co",
    "code": 57
}

print(countries_info["country_name"])
>>>>>>> ec375a70a141b3d71bdc7c4a39047b83277581ec
