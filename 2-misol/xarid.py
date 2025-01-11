
def save_shopping_list():

    with open("shopping_list.txt", "a") as file:  
        while True:
            product = input("Mahsulot nomini kiriting (yoki chiqish uchun '0' yozing): ")
            if product.lower() == "0":
                break
            file.write(product + "\n")
            print(f"{product} ro'yxatga qo'shildi.\n")


def read_shopping_list():
    
    try:
        with open("shopping_list.txt", "r") as file:
            print("\nXaridlar ro'yxati:")
            items = file.readlines()
            for item in items:
                print(item.strip())
    except FileNotFoundError:
        print("Hali hech qanday xaridlar ro'yxati saqlanmagan.")


print("Xaridlar ro'yxatini yaratish dasturi.")
save_shopping_list()
read_shopping_list()