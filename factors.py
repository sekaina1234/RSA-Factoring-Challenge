#!/usr/bin/python3
import sys

def factorize_number(n):
    factors = []
    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def factorize_file(filename):
    with open(filename, 'r') as file:
        numbers = file.read().splitlines()
        for number in numbers:
            n = int(number)
            factors = factorize_number(n)
            if len(factors) > 1:
                print(f"{n}={factors[0]}*{factors[1]}")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: factors <file>")
    else:
        factorize_file(sys.argv[1])
