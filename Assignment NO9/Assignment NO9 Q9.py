contacts = {}

name = input("Enter Name: ")
phone = input("Enter Phone Number: ")
email = input("Enter Email: ")

contacts[name] = {
    "phone": phone,
    "email": email
}

search_name = input("Search Contact Name: ")

result = contacts.get(search_name)

if result:
    print("Contact Found:")
    print(result)
else:
    print("Contact Not Found")

print("\nAll Contacts:")
for name, details in contacts.items():
    print(name, ":", details)