
a = 19
b = 5

print(f"a = {a}, b = {b}")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Floating-Point Division: {a / b}")
print(f"Integer Division: {a // b}")
print(f"Modulus: {a % b}")
print(f"Exponentiation: {a ^ b}")

result1 = 3 + 7 * 5
result2 = (3 + 7) * 5
result3 = 20 % 3 + 7 * 2

print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}")

inches = int(input("Enter the number of inches: "))
feet = inches // 10
remaining_inches = inches % 10

print(f"{inches} inches is equal to {feet} feet and {remaining_inches} inches.")
