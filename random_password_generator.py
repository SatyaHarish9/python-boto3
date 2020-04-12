from random import choice

pass_length = 8
valid_chars_for_password="qwertyuiopasdfghjklzxcvbnm"
password = []

for each in range(pass_length):
    password.append(choice(valid_chars_for_password))

random_password = "".join(password)
print(random_password)