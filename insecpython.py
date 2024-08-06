# Insecure Python code example
import os

def unsafe_function(user_input):
    # This function is vulnerable to command injection
    os.system(f"echo {user_input}")

def main():
    user_input = input("Enter something: ")
    unsafe_function(user_input)

if __name__ == "__main__":
    main()
