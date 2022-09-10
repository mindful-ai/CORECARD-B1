info = "pass$$$123&*^"
h = hash(info)
print(h)

password = input("Your password: ")
if(h == hash(password)):
    print("You are logged in")
else:
    print("Invalid password")

# --------------------------------------------------------------

import hashlib

h = hashlib.new('sha256')
h.update(info.encode())
print(h.hexdigest())