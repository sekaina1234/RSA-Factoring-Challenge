#!/usr/bin/python3
import sys

def factorize(number):
    factors = []
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
            factors.append(i)
    if number > 1:
        factors.append(number)
    return factors

def main():
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        return

    filename = sys.argv[1]
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                factors = factorize(number)
                p = factors[0]
                q = number // p
                print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except ValueError:
        print("Invalid number in the file.")

if __name__ == "__main__":
    main()
