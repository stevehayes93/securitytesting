import hashlib

def insecure_password_storage(password):
    # Insecure password storage (use bcrypt or similar in production)
    hashed = hashlib.md5(password.encode()).hexdigest()
    print(f"Stored hash: {hashed}")

user_password = input("Enter a password: ")
insecure_password_storage(user_password)
