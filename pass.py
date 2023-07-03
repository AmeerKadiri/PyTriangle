def main():
    username = input("Set your username: ")
    password = input("Set your password: ")
    print("Username and password set successfully!")

    print("Sign in")
    sign_in_username = input("Username: ")
    sign_in_password = input("Password: ")

    # Check if the entered credentials match the set credentials
    if sign_in_username == username and sign_in_password == password:
        print("Sign in successful! Welcome, " + username + "!")
    else:
        print("Invalid username or password. Sign in failed.")


if __name__ == "__main__":
    main()