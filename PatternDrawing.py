from colorama import Fore


# 🖼️ Python Pattern Drawing Project
print(Fore.CYAN + "🌟 Welcome to the Python Pattern Drawing Program!")
exit_program = False

while True:
    # Display a menu to the user
    print(Fore.GREEN + "Choose a pattern type:")
    print("1. Right-angled Triangle")
    print("2. Square with Hollow Center")
    print("3. Diamond")
    print("4. Left-angled Triangle")
    print("5. Hollow Square")
    print("6. Pyramid")
    print("7. Reverse Pyramid")
    print("8. Rectangle with Hollow Center")
    print("9. Christmas Tree")
    print("10. Sandglass watch")
    print("11. Exit Program!")

    # Get the user's choice
    choice = int(input("Enter the number corresponding to your choice: "))

    # Get dimensions based on choice or terminate program
    if choice in [1, 3, 4, 6, 7, 10]:
        rows = int(input(Fore.BLUE + "Enter the number of rows: "))
    elif choice in [2, 5]:
        size = int(input(Fore.BLUE + "Enter the size of the square: "))
    elif choice == 8:
        width = int(input(Fore.BLUE + "Enter the width of the rectangle: "))
        height = int(input(Fore.BLUE + "Enter the height of the rectangle: "))
    elif choice == 9:
        height = int(input(Fore.BLUE + "Enter the height of the tree:"))
    elif choice == 11:
        print("Good bye!")
        break
    else:
        print("Invalid input! Please enter valid number from menu above!")
        continue

    # Generate the selected pattern
    pattern = ""

    if choice == 1: # Right-angled Triangle
        for i in range(1, rows + 1):
            pattern += i * "*" + "\n"


    elif choice == 2: # Square with Hollow Center
        star = "*"
        space = " "

        for i in range(1, size + 1):
            if i == 1 or i == size:
                pattern += size * star + "\n"
            else:
                pattern += star + (size - 2) * space + star + "\n"

    elif choice == 3: # Diamond
        for row in range(1, rows):
            pattern += (rows - row) * " " + "*" + (row - 1) * " *" + "\n"

        for row in range(rows, 0, - 1):
            pattern += (rows - row) * " " + "*" + (row - 1) * " *" + "\n"


    elif choice == 4: # Left-angled Triangle
        for i in range(rows, 0, -1):
            pattern += i * "*" + "\n"

    elif choice == 5: # Hollow Square
        star = "*"
        space = " "

        for i in range(1, size + 1):
            if i == 1 or i == size:
                pattern += size * star + "\n"
            else:
                pattern += star + (size - 2) * space + star + "\n"

    elif choice == 6: # Pyramid
        stars = 1
        spaces = ((rows * 2) - 1) // 2
        for i in range(1, rows + 1):
            pattern += spaces * " " + stars * "*" + spaces * " " + "\n"
            spaces -= 1
            stars += 2


    elif choice == 7: # Reverse Pyramid
        stars = (rows * 2) - 1
        spaces = 0
        for i in range(rows, 0, -1):
            pattern += spaces * " " + stars * "*" + spaces * " " + "\n"
            spaces += 1
            stars -= 2


    elif choice == 8: # Rectangle with Hollow Center
        for i in range(1, height + 1):
            if i == 1 or i == height:
                pattern += width * "*" + "\n"
            else:
                pattern += "*" + (width - 2) * " " + "*" + "\n"

    elif choice == 9: # Christmas tree
        pattern += (height + 1) * " " + "|" + "\n"
        for row in range(1, height):
            pattern += (height - row) * " " + row * "*" + " | " + row * "*" + "\n"

    elif choice == 10: # Sunglass watch
        stars = (rows * 2) - 1
        spaces = 0
        for i in range(rows, 0, -1):
            pattern += spaces * " " + stars * "*" + "\n"
            spaces += 1
            stars -= 2

        stars = 1
        spaces = ((rows * 2) - 1) // 2
        for i in range(1, rows + 1):
            pattern += spaces * " " + stars * "*" + "\n"
            spaces -= 1
            stars += 2

    print(Fore.RED + pattern)

    # Allow the user to save pattern in file
    save_file_prompt = input(Fore.MAGENTA + "Do you want to save the pattern to a file?")
    if save_file_prompt.lower() == "yes":
        with open("python_patterns.txt", "w") as file:
            file.write(pattern)

        print(Fore.MAGENTA + "Pattern successfully added to Python file")

    # Allow the user to restart or exit
    while True:
        new_choice = input(Fore.YELLOW + "Do you want to try again? (Yes or No)")
        if new_choice.lower() == "no":
            exit_program = True
            print("Good bye!")
            break
        elif new_choice.lower() == "yes":
            break
        else:
            print("Please enter valid answer!")
            continue

    if exit_program:
        break

