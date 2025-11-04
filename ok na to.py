print("===========================================================")
print("PYTHON INTERACTIVE TUTORIAL")
print("===========================================================")

print("PRELIM LESSON")
print("[1] Introduction")
print("[2] What is programming")
print("[3] Python Print Syntax")
print("[4] Python Comments")
print("[5] Variable and Data Types")
print("[6] Arithmetic Operators")

print("MIDTERM LESSON")
print("[7] Input functions")
print("[8] f-string")
print("[9] Conditional Statement")

print("FINAL LESSON")
print("[10] Looping")

chose = int(input("Enter your choice(0-10)"))

if chose == 1:
    print("Introduction")
    print("Python is a high-level, general-purpose programming language known for its readability and versatility. ")
    print("What is Python?")
    print("Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.")
    input("\nPress Enter to return to the menu...")
elif chose == 2:
    print("What is programming")
    print(
        "Programming is the process of writing instructions, or code, that tell a computer what to do to solve a problem or perform a specific task.")
    input("\nPress Enter to return to the menu...")

elif chose == 3:
    print("Python Print Syntax")
    print("Hello, World!")
    input("\nPress Enter to return to the menu...")
elif chose == 4:
    print("Python Comments")
    print("# This is a single-line comment.")
    print("Hello, World!")
    input("\nPress Enter to return to the menu...")
elif chose == 5:
    print("Variable and Data Types")
    print("Integer (int): Whole numbers, positive or negative.")
    print("my_integer = 10")
    print("my_string = Hello, Python!")
    print("Float (float): Numbers with a decimal point.")
    print("my_float = 3. 14")
    print("bool: Represents truth values, either True or False.")
    print("my_boolean = True")
    print("complex: Numbers with a real and imaginary part.")
    print("(e.g., 1 + 2j)")
    input("\nPress Enter to return to the menu...")

elif chose == 6:
    print("Arithmetic Operators")
    print("x = 7")
    print("y = 3")
    print("sum_result = x + y")
    print("difference_result = x - y")
    print("product_result = x * y")
    print("floor_division_result = x // y")
    input("\nPress Enter to return to the menu...")
elif chose == 7:
    print("Input functions")
    print("name = input('Please enter your name':")
    print(f"Hello, (name)!")
    input("\nPress Enter to return to the menu...")
elif chose == 8:
    print("f-string")
    print("name = 'Alice'")
    print("age = 30")
    print("print(f'My name is {name} and I am {age} years old.')")
    input("\nPress Enter to return to the menu...")

elif chose == 9:
    print("Conditional Statement")
    print("Example:")
    print("age = 18")
    print("if age >= 18:")
    print("    print('You are an adult.')")
    print("else:")
    print("    print('You are a minor.')")

    age = int(input("Enter your age: "))
    if age >= 18:
        print("You are an adult.")
    else:
        print("You are a minor.")
    input("\nPress Enter to return to the menu...")

elif chose == 10:
    print("Looping")
    print("Example of a for loop:")
    print("for i in range(5):")
    print("    print(i)")
    print("Example of a while loop:")
    print("count = 0")
    print("while count < 5:")
    print("    print(count)")
    print("    count += 1")

    print("Counting from 0 to 4 using a for loop:")
    for i in range(5):
        print(i)
    print("Counting from 0 to 4 using a while loop:")
    count = 0
    while count < 5:
        print(count)
        count += 1
        input("\nPress Enter to return to the menu...")


else:
    print("Invalid choice! Please enter a number between 0 and 10.")