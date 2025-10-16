
age = int(input("Enter age: "))
is_student = input("Is student? (True/False): ").lower() == "true"

base_price = 20
discount = 0

if age <= 10:
    discount = 2
elif age >= 30:
    discount = 3
elif is_student:
    discount = 3

final_price = base_price - discount
print(f"Your ticket price is ${final_price}.")

correct_username = "Shet"
correct_password = "ayoko"
is_2fa_enabled = True
correct_2fa_code = "012345678"

input_username = input("Enter username: ")
input_password = input("Enter password: ")

if is_2fa_enabled:
    input_2fa_code = input("Enter 2FA code: ")
    if (input_username == correct_username and
            input_password == correct_password and
            input_2fa_code == correct_2fa_code):
        print("Login successful!")
    else:
        print("Login failed!")
else:
    if (input_username == correct_username and
            input_password == correct_password):
        print("Login successful!")
    else:
        print("Login failed!")
