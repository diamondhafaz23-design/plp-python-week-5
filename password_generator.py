import random
import string

# 1 & 2. The Password Generator Function
def make_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ""
    for i in range(length):
        password += random.choice(characters)
    return password

# 3. Create and Print the Passwords
p1 = make_password()
p2 = make_password(12)

print("Password:", p1)
print("Length:", len(p1))
print("Password:", p2)
print("Length:", len(p2))
