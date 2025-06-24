try:
    with open("numbers.txt", "r") as file:
        total = 0
        for line in file:
            try:
                number = int(line.strip())
                total += number
            except ValueError:
                print(f"Invalid data: '{line.strip()}' is not a number.")
except FileNotFoundError:
    print("Error: The file 'numbers.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Program execution completed.")
