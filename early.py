from playsound import playsound
from time import sleep
from colorama import init, Fore, Back, Style
init(autoreset=True)

while True:

    wizard = Fore.BLUE + Style.BRIGHT + "Wizard"
    elf = Fore.MAGENTA + Style.BRIGHT + "Elf"
    human = Fore.YELLOW + Style.BRIGHT + "Human"
    orc = Fore.RED + Style.BRIGHT + "Orc"

    wizard_hp = 70
    elf_hp = 100
    human_hp = 150
    orc_hp = 125

    wizard_damage = 150
    elf_damage = 100
    human_damage = 20
    orc_damage = 115

    dragon_hp = 300
    dragon_damage = 50

    print(f"1) {Fore.BLUE}{Style.BRIGHT}Wizard")
    print(f"2) {Fore.MAGENTA}{Style.BRIGHT}Elf")
    print(f"3) {Fore.YELLOW}{Style.BRIGHT}Human")
    print(f"4) {Fore.RED}{Style.BRIGHT}Orc")
    print(f"5) {Fore.CYAN}{Style.BRIGHT}Exit")
    choice = input("Choose your character: ").lower()
    if choice == "1" or choice == "wizard":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
    elif choice == "2" or choice == "elf":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
    elif choice == "3" or choice == "human":
        character = human
        my_hp = human_hp
        my_damage = human_damage
    elif choice == "4" or choice == "orc":
        character = orc
        my_hp = orc_hp
        my_damage = orc_damage
    elif choice == "5" or choice == "exit":
        print("Exiting the game.")
        exit()
    else:
        print("Unknown character")
        continue

    print(f"\nYou have chosen the character: {character}")
    print(f"{Fore.CYAN}{Style.BRIGHT}Health: {my_hp}")
    print(f"{Fore.CYAN}{Style.BRIGHT}Damage: {my_damage}\n")
    sleep(3)

    while True:
        dragon_hp = dragon_hp - my_damage
        print(f"The {character}{Fore.RESET}{Style.NORMAL} damaged the {Fore.GREEN}{Style.BRIGHT}Dragon{Fore.RESET}{Style.NORMAL}!")
        print(
            f"The {Fore.GREEN}{Style.BRIGHT}Dragon{Fore.RESET}{Style.NORMAL}'s hitpoints are now: {dragon_hp} \n")
        sleep(2.5)
        if dragon_hp <= 0:
            print(
                f"The {Fore.GREEN}{Style.BRIGHT}Dragon {Fore.RESET}{Style.NORMAL}has lost the battle.")
            playsound('./sounds/winning.mp3')

            sleep(2)
            break

        my_hp = my_hp - dragon_damage
        print(
            f"The {Fore.GREEN}{Style.BRIGHT}Dragon {Fore.RESET}{Style.NORMAL}strikes back at the {character}")
        print(
            f"The {character}{Fore.RESET}{Style.NORMAL}'s hitpoints are now: {my_hp}\n")
        sleep(2.5)
        if my_hp <= 0:
            print(
                f"The {character}{Fore.RESET}{Style.NORMAL} has lost the battle.\n")
            playsound('./sounds/loosing.wav')
            sleep(2)
            break

    repeat = input("Do you want to play again? ").lower()
    if repeat == "y" or repeat == "yes":
        continue
    else:
        print("Exiting the game.")
        break
