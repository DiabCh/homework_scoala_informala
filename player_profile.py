import getpass
from pathlib import Path
import json


def verify_account(username, password):
    if username["password"] == password:
        print("Authentication successful!")
        return True
    else:
        print("Incorrect password, please try again")
        return False


def login():
    username = get_useraccount()
    while username is None:

        choice = int(input("Account does not exist, "
                           "try again or register "
                            "account\n1.Try again "
                            "\n2.Register new account\n"))
        if choice == 1:
            username = get_useraccount()
        elif choice == 2:
            register()
            break

    password = getpass.getpass(prompt="Please introduce password: ")
    while not verify_account(username, password):
        password = getpass.getpass(prompt="Please introduce password: ")


def get_useraccount():
    directory = "saved_data"
    p = Path() / directory
    with open(p / "Saved Data.json", "r") as file:
        username = input("Insert username: ").lower()
        saved_data = json.loads(file.read())
        search_account = [x for x in saved_data if
                          x["username"] == username]
        try:
            search_account = search_account[0]
        except:
            search_account = None

        finally:
            return search_account


def register(player_password=True, player_password_confirm=False):
    dir_name = "saved_data"
    p = Path() / dir_name
    p.mkdir(exist_ok=True)

    with open(p / "Saved Data.json", "r") as file:
        registered_accounts = file.read()
        registered_accounts = json.loads(registered_accounts)

    player_first_name = input("Insert first name: ")
    player_last_name = input("Insert last name: ")
    player_username = input("Insert username: ").lower()
    while player_password != player_password_confirm:
        player_password = getpass.getpass(prompt="Insert password: ").lower()
        player_password_confirm = \
            getpass.getpass(prompt="Confirm password: ").lower()
        if player_password != player_password_confirm:
            print("The passwords do not match, please try again!")
    player_profile = {
        "password": player_password,
        "fname": player_first_name,
        "lname": player_last_name,
        "username": player_username,
        "games_played_1": 0,
        "games_won_1": 0,
        "games_played_3": 0,
        "games_won_3": 0,
        "games_played_5": 0,
        "games_won_5": 0

    }

    registered_accounts.append(player_profile)
    with open(p / "Saved Data.json", "w") as file:
        to_dump = json.dumps(registered_accounts)
        file.write(to_dump)
    print("Account created successfully!: ")
