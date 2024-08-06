def insecure_xss(user_input):
    # Vulnerable to XSS
    print(f"Hello, {user_input}!")

user_input = input("Enter your name: ")
insecure_xss(user_input)
