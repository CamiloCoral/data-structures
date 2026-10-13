planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
gravity = [3.7, 8.8, 9.8, 3.7, 24.7, 10.4, 8.6, 11.1]
#print(type(gravity)) #Class List
print(planets)
print(len(planets))

i = 0

print("_" * 40)
print("| Planet name{:<15} | Gravity{:<10} |")
print("_" * 40)

while i < len(planets):
    print(f"| {planets[i]:<15} | {gravity[i]:<10} |")
    print("_" * 40)
    i += 1