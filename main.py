import math

# Function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

# Given string
string = "34157219834157"

# Convert the string to a list of integers
digits = [int(digit) for digit in string]

# Find p and q
p, q = None, None

# Iterate through the string to find p and q
for i in range(len(digits) - 1):
    for j in range(i + 1, len(digits)):
        num = int("".join(map(str, digits[i:j + 1])))
        if is_prime(num):
            if p is None:
                p = num
            else:
                q = num

            # Check if there is no prime number between p and q
            if is_prime(num + 2):
                break

# Output the results
if p is not None and q is not None:
    with open("./prime_numbers.txt", "w") as f:
        f.write(f"p: {p}\nq: {q}")
        print(f"{p}, {q}")
else:
    print("Prime numbers p and q not found in the given string.")
