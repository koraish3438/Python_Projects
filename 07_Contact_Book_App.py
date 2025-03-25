contacts = {}

while True:
    print("\nContact Book App")
    print("1. Create contact")
    print("2. View contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search contact")
    print("6. Count contact")
    print("7. Exit")

    choice = input("\nEnter what do you want : ")

    if choice == "1":
        name = input("Enter your name : ")
        if name in contacts:
            print(f"Contact name {name} already exists!")
        else:
            age = input("Enter age : ")
            email = input("Enter email : ")
            mobile = input("Enter mobile Number : ")
            contacts[name] = {'age':int(age), 'email':email, 'mobile':mobile}
            print(f"Contact name {name} has been created successfully!")

    elif choice == "2":
        name = input("Enter contact name to view : ")
        if name in contacts:
            contact = contacts[name]
            print(f"Name : {name}, Age : {contact['age']}, Email : {contact['email']}, Mobile Number : {contact['mobile']}")
        else:
            print("Contact not found!")

    elif choice == "3":
        name = input("Enter contact name to update : ")
        if name in contacts:
            age = input("Enter updated age : ")
            email = input("Enter updated email : ")
            mobile = input("Enter updated mobile Number : ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
        else:
            print("Contact not found!")

    elif choice == "4":
        name = input("Enter contact name to delete : ")
        if name in contacts:
            del contacts[name]
            print(f"Contact name {name} has been deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == "5":
        search_name = input("Enter contact name to search : ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() in name.lower():
                print(f"Found -- Name : {name}, Age : {contact['age']}, Email : {contact['email']}, Mobile Number : {contact['mobile']}")
                found = True
        if not found:
            print("No contact found is that name!")

    elif choice == "6":
        print(f"Total contact in your contact book is : {len(contacts)}")

    elif choice == "7":
        print("Exit.. close the contact book..")
        break
    else:
        print("Invalid input!")