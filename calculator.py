with open("history.txt", "a") as file:
    while True:
        print("Smart Calculator")
        print(1, ". Addition")
        print(2, ". Subtraction")
        print(3, ". Multiplication")
        print(4, ". Division")
        print(5, ". Modulus")
        print(6, ". Exponentiation")
        print(7, ". View History")
        print(8, ". Clear History")
        print(9, ". Exit")
        choice=int(input("Enter your choice (1-9): "))
        if choice > 9 or choice < 1:
            print("Invalid choice. Please try again.")
            continue

        if choice == 9:
            print("Thanks for using my Smart Calculator ;) ")
            break

        if choice == 7:
            with open("history.txt", "r") as history_file:
                history = history_file.read()

            print("History:")
            if history == "":
                print("No history found.")
            else:
                print(history)
            continue

        if choice == 8:
            with open("history.txt", "w") as history_file:
                pass
            print("History cleared.")
            continue

        if choice in range(1, 6):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == 1:
                result = num1 + num2
                file.write(str(num1) + " + " + str(num2)+ "\n")

            elif choice == 2:
                result = num1 - num2
                file.write(str(num1) + " - " + str(num2)+ "\n")

            elif choice == 3:
                result = num1 * num2
                file.write(str(num1) + " * " + str(num2)+ "\n")

            elif choice == 4:
                if num2 != 0:
                    result = num1 / num2
                    file.write(str(num1) + " / " + str(num2)+ "\n")
                else:
                    print("Error: Division by zero is not allowed.")
                    continue

            elif choice == 5:
                if num2 != 0:
                    result = num1 % num2
                    file.write(str(num1) + " % " + str(num2)+ "\n")
                else:
                    print("Error: Division by zero is not allowed.")
                    continue

        if choice == 6:
            base = int(input("Enter the base number: "))
            exponent = int(input("Enter the exponent: "))
            result = base ** exponent
            file.write(str(base) + " ^ " + str(exponent))

        file.write("=" + str(result) + "\n")
        file.flush()
        print("Result:", result)