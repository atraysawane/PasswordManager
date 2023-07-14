import json
from getpass import getpass


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def save_data(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)


def add_password(data):
    name = input("Enter the name of the account: ")
    username = input("Enter the username: ")
    password = getpass("Enter the password: ")
    data[name] = {
        'username': username,
        'password': password
    }
    print("Password added successfully!")


def get_password(data):
    name = input("Enter the name of the account: ")
    if name in data:
        account = data[name]
        print(f"Username: {account['username']}")
        print(f"Password: {account['password']}")
    else:
        print("Account not found!")


def delete_password(data):
    name = input("Enter the name of the account: ")
    if name in data:
        del data[name]
        print("Password deleted successfully!")
    else:
        print("Account not found!")


def main():
    file_name = 'passwords.json'
    data = load_data(file_name)

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Delete Password")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_password(data)
        elif choice == '2':
            get_password(data)
        elif choice == '3':
            delete_password(data)
        elif choice == '4':
            save_data(data, file_name)
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
