
def save_contacts_to_file():
    
    with open("contacts.txt", "a") as file:  # "a" rejimi qo'shish uchun ishlatiladi
        while True:
            name = input("Dustingizni ismini kiriting (yoki chiqish uchun '0' bosing): ")
            if name.lower() == "0":
                break
            phone = input(f"{name}ning telefon raqamini kiriting: ")
            file.write(f"{name}: {phone}\n")
            print(f"{name}ning telefon raqami saqlandi.\n")


def read_contacts_from_file():
    
    try:
        with open("contacts.txt", "r") as file:
            print("\nFayldagi kontaktlar:")
            contacts = file.readlines()
            for contact in contacts:
                print(contact.strip())
    except FileNotFoundError:
        print("Hali hech qanday kontakt saqlanmagan.")


print("Telefon raqamlarini saqlash dasturi.")
save_contacts_to_file()
read_contacts_from_file()