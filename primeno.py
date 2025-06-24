#checking divisibility up to the square root of the number.#
import math

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= int(math.sqrt(n)):
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()


