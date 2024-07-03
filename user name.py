def main():
    print("Welcome to the User Information Form")
    
    # Get user input
    name = input("Enter your name: ")
    email = input("Enter your email address: ")
    phone_number = input("Enter your phone number: ")
    address = input("Enter your address: ")
    
    # Print the entered information
    print("\nUser Information:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone Number: {phone_number}")
    print(f"Address: {address}")
    
if __name__ == "__main__":
    main()
