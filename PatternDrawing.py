# 🖼️ Python Pattern Drawing Project
print("🌟 Welcome to the Python Pattern Drawing Program!")
while True:

    print("Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")
    print("9. Exit Program!")

    choice = int(input("Enter the number corresponding to your choice: "))

    if choice in [1, 3, 4, 6, 7]:
        rows = int(input("Enter the number of rows: "))
    elif choice in [2, 5]:
        size = int(input("Enter the size of the square: "))
    elif choice == 8:
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
    elif choice == 9:
        print("Good bye!")
        break
    else:
        print("Invalid input! Please enter valid number from menu above!")
        continue

    if choice == 1:
        for i in range(1, rows + 1):
            print(i * "*")

    elif choice == 2:
        star = "*"
        space = " "

        for i in range(1, size + 1):
            if i == 1 or i == size:
                print(size * star)
            else:
                print(star + (size - 2) * space + star)

    elif choice == 3:
        star = "*"
        space = " "

        half_size = size // 2

        for i in range(1, size + 1, 2):
            stars_count = 1 * i
            space_count = (size - stars_count) // 2

            print(space * space_count + star * stars_count + space * space_count)

        for j in range(size - 2, 0, -2):
            stars_count = 1 * j
            space_count = (size - stars_count) // 2

            print(space * space_count + star * stars_count + space * space_count)

    elif choice == 4:
        for i in range(rows, 0, -1):
            print(i * "*")

    elif choice == 5:
        star = "*"
        space = " "

        for i in range(1, size + 1):
            if i == 1 or i == size:
                print(size * star)
            else:
                print(star + (size - 2) * space + star)

    elif choice == 6:
        stars = 1
        spaces = ((rows * 2) - 1) // 2
        for i in range(1, rows + 1):
            print(spaces * " " + stars * "*" + spaces * " ")
            spaces -= 1
            stars += 2


    elif choice == 7:
        stars = (rows * 2) - 1
        spaces = 0
        for i in range(rows, 0, -1):
            print(spaces * " " + stars * "*" + spaces * " ")
            spaces += 1
            stars -= 2


    elif choice == 8:
        for i in range(1, height + 1):
            if i == 1 or i == height:
                print(width * "*")
            else:
                print("*" + (width - 2) * " " + "*")



    new_choice = input("Do you want to try again? (Yes or No)")
    if new_choice == "No":
        print("Good bye!")
        break
    elif new_choice != "Yes":
        new_choice = input("Do you want to try again? (Yes or No)")