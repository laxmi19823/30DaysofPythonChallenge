def isnum(value):
    try:
        num = int(value)
        if num < 0:
            print("Please enter a non-negative integer.")
            return None
        return num
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return None

def fiboSeries():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def mainFun():
    user_num = input("Enter a number to generate Fibonacci Series: ")
    checknum = isnum(user_num)

    if checknum is None:
        return

    count = 0
    for i in fiboSeries():
        if count < checknum:
            print(i)
            count += 1
        else:
            break

# Call the main function
mainFun()

