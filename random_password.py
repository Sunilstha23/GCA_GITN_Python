import random
import string
users = {
    "harry": 6,
    "rob": 7,
    "bob": 6,
    "Jane": 8
}
passwords = {}
letter = []
letter = list(string.ascii_lowercase + string.digits)
print(letter)
for username, length in users.items():
    password = []
    for _ in range(0, length):
        password.append(random.choice(letter))
    passwords[username] = "".join(password)

    print(users)
    print(passwords)
