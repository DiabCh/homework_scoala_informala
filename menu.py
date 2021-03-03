from .player_profile import login, register

def intro_graphic():
    print(
        """
        888   d8b        888                   888
        888   Y8P        888                   888
        888              888                   888
        888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.
        888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b
        888   888888     888   .d888888888     888   888  88888888888
        Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.
         "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888

Welcome to the informal log-in screen:
1.Log in
2.Register
3.Play vs Cpu
         """)


def main_menu():
    intro_graphic()
    while True:
        player_choice = int(input())
        if player_choice == 1:
            login()
        elif player_choice == 2:
            register()
        elif player_choice == 3:
            print('not implemented yet')
        else:
            print("Please pick one of the available options")

