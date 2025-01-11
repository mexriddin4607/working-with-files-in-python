
def save_grades():
    
    with open("grades.txt", "a") as file:  
        while True:
            name = input("Talabaning ismini kiriting (yoki chiqish uchun 'exit' yozing): ")
            if name.lower() == "exit":
                break
            try:
                grade = float(input(f"{name}ning bahosini kiriting: "))
                file.write(f"{name}: {grade}\n")
                print(f"{name}ning bahosi saqlandi.\n")
            except ValueError:
                print("Noto'g'ri baho kiritildi. Iltimos, qaytadan urinib ko'ring.\n")


def calculate_average_grade():
    
    try:
        with open("grades.txt", "r") as file:
            grades = []
            for line in file:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    try:
                        grade = float(parts[1].strip())
                        grades.append(grade)
                    except ValueError:
                        pass  

            if grades:
                average = sum(grades) / len(grades)
                print(f"\nUmumiy o'rtacha baho: {average:.2f}")
            else:
                print("\nFaylda baholar mavjud emas.")
    except FileNotFoundError:
        print("Hali hech qanday baho saqlanmagan.")


print("Baholarni saqlash va hisoblash dasturi.")
save_grades()
calculate_average_grade()