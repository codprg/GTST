def check_number():
    try:
        number = float(input("Enter a number: "))
        if number.is_integer():
            if number % 2 == 0:
                print("This number is Even")
            else:
                print("This number is Odd")
        else:
            print("Please enter a whole number only.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

check_number()
