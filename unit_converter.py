def temperature_converter():
    try:
        choice = input("Choose an option:\n1. Celsius to Fahrenheit\n2. Fahrenheit to Celsius\n")
        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def length_converter():
    try:
        choice = input("Choose an option:\n1. Meters to Feet\n2. Feet to Meters\n")
        if choice == '1':
            meters = float(input("Enter length in meters: "))
            feet = meters * 3.28084
            print(f"{meters} meters is equal to {feet} feet")
        elif choice == '2':
            feet = float(input("Enter length in feet: "))
            meters = feet / 3.28084
            print(f"{feet} feet is equal to {meters} meters")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def weight_converter():
    try:
        choice = input("Choose an option:\n1. Kilograms to Pounds\n2. Pounds to Kilograms\n")
        if choice == '1':
            kilograms = float(input("Enter weight in kilograms: "))
            pounds = kilograms * 2.20462
            print(f"{kilograms} kilograms is equal to {pounds} pounds")
        elif choice == '2':
            pounds = float(input("Enter weight in pounds: "))
            kilograms = pounds / 2.20462
            print(f"{pounds} pounds is equal to {kilograms} kilograms")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

while True:
    print("Unit Converter Menu:")
    print("1. Temperature Converter")
    print("2. Length Converter")
    print("3. Weight Converter")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        temperature_converter()
    elif choice == '2':
        length_converter()
    elif choice == '3':
        weight_converter()
    elif choice == '4':
        print("Thank You")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
