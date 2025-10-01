'''
While Loops
'''
password = "python123"
attempt = ""
tries = 0

while attempt __________ password and tries < __________:
    attempt = input("Enter password: ")
    tries += 1

if attempt == password:
    print("Access granted")
else:
    print("Too many attempts")