import os
from datetime import date

#functions
def mainMenu():
    print (":::Main menu:::")
    print ("[1]Regsiter aa new user")
    print ("[2]List all users")
    print ("[3]Search user")
    print ("[4]Delete user")
    print ("[5]Update user")
    print ("[6]Show active uses")
    print ("[7]Show inactive users")
    print ("[8]Exit")

ids=[]    
firtsnames=[]
lastnames=[]
mobile_phones=[]
emails=[]
statuses=[]
genders=[]

ages=[]
salarys=[]

created_at=[]

#Main

while True:
    os.system('clear')
    mainMenu()
    opt=input("Press any option [1-8]: ")

    match opt:
        case '1':
            os.system('clear')
            print("::: Register form :::")

            while True:
                id=input("ident number: ")
                count = 0
                i=0
                while i < len(ids):
                    if id == ids[i]:
                        print("identification number already exists! \n try again:::")
                        count += 1
                        break
                    i += 1
                if count == 0:
                    break

            firtsname=input("Firstname: ")
            lastname=input("Lastname: ")

            while True:
                mobile_phone=input("Mobile Phone: ")
                count = 0
                i=0
                while i < len(mobile_phones):
                    if mobile_phone == mobile_phones[i]:
                        print("Number Phone already exists! \n try again:::")
                        count += 1
                        break
                    i += 1
                if count == 0:
                    break

            email=input("E-mail: ")
            gender=input("Gender [M/F/O]: ")

            age=input("age: ")
            salary=input("salary: ")

            ids.append(id)
            firtsnames.append(firtsname)
            lastnames.append(lastname)
            mobile_phones.append(mobile_phone)
            emails.append(email)
            statuses.append(True)
            genders.append(gender)

            ages.append(age)
            salarys.append(salary)

            created_at.append(date.today())
            print("User has been created successfully !!")
            any_key = input("Press any key to back to main menu")

       
        case '2':
            while True:
                os.system('clear')
                print(":::List all registered users:::")
                print("[1]. Sort in ascending order by identification")
                print("[2]. Sort in descending order by identification")
                print("[3]. Sort in ascending order by lastname")
                print("[4]. Sort in descending order by lastname")
                print("[5]. Exit")

                option = input("Press any option [1-5]: ")

                if option == '5':
                    break

                if option not in ['1', '2', '3', '4']:
                    input("Invalid option. Press Enter to try again...")
                    continue

                if len(ids) == 0:
                    input("There are no registered users yet. Press Enter...")
                    continue

                # Create a list of indexes to preserve the relationship
                # between all the user data lists.
                indexes = list(range(len(ids)))

                if option == '1':
                    indexes.sort(key=lambda i: ids[i])
                elif option == '2':
                    indexes.sort(key=lambda i: ids[i], reverse=True)
                elif option == '3':
                    indexes.sort(key=lambda i: lastnames[i].lower())
                elif option == '4':
                    indexes.sort(
                        key=lambda i: lastnames[i].lower(),
                        reverse=True
                    )

                print()
                print('-' * 163)
                print(
                    f"| {'id':<15} | {'Firsname':<15} | "
                    f"{'Lastname':<15} | {'Mobile Phone':<15} | "
                    f"{'Emails':<15} | {'Genders':<15} | "
                    f"{'Ages':<15} | {'Salarys':<15} | "
                    f"{'Created':<15} |"
                )
                print('-' * 163)

                for i in indexes:
                    print(
                        f"| {ids[i]:<15} | "
                        f"{firtsnames[i]:<15} | "
                        f"{lastnames[i]:<15} | "
                        f"{mobile_phones[i]:<15} | "
                        f"{emails[i]:<15} | "
                        f"{genders[i]:<15} | "
                        f"{ages[i]:<15} | "
                        f"{salarys[i]:<15} | "
                        f"{created_at[i]!s:<15} |"
                    )
                    print('-' * 163)

                input("Press Enter to continue...")

        case '3':
            os.system('clear')
            print("Search User ::: \n")

            id_user = input("Enter identification number to Search: ")
            i = 0
            j = 0
            while i < len(ids):
                if id_user == ids[i]:
                    j = 1
                    break
                i += 1

            if j > 0:
                print(f"Ident user: {ids[i]}")
                print(f"Fullname: {firtsnames[i]} {lastnames[i]}")
                print(f"Mobile phone: {mobile_phones[i]}")
                print(f"Email: {emails[i]}")
                print(f"Gender: {genders[i]}")
                print(f"Age: {ages[i]}")
                print(f"Salary: {salarys[i]}")
                print(f"Status: {'Active' if statuses[i] else 'Inactive'}")
                print(f"Created at: {created_at[i]}")
            else:
                print("Identification Number not found")

            key = input("Press any key to back to main menu: ")
        
        case '8':
            any_key=input("bye bye. press any key... ")
            break

        case _:
            any_key=input("Invalid option. press any key to try again")