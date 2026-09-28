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