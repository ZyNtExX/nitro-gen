try:
    import colorama
except ModuleNotFoundError as e:
    modulename = str(e).split("No module named ")[1].replace("'", "")
    input(f"Please install module with: pip install {modulename}")
    exit()

from colorama import Fore, init
from os import system as cmd
from time import sleep
import ctypes
import random
import string
import platform

ctypes.windll.kernel32.SetConsoleTitleW(
    "Discord Nitro Generator | ZyNtExX | v1.0")
init(convert=True)

nitros = open("nitros.txt", "a")


def main():

    clear_console()
    print(f"{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Discord Nitro Generator made by {Fore.WHITE}ZyNtExX{Fore.LIGHTBLACK_EX} | Licensed under {Fore.WHITE}MIT {Fore.LIGHTBLACK_EX}License | {Fore.WHITE}This tool is for educational purposes only{Fore.RESET}\n{Fore.WHITE}[ {Fore.CYAN}§ {Fore.WHITE}] {Fore.LIGHTBLACK_EX}You can follow me on Github: {Fore.WHITE}https://github.com/ZyNtExX{Fore.RESET}")
    try:
        try:
            nitroAmount = int(input(
                f"\n{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}How much codes will be generated: {Fore.WHITE}"))
        except ValueError:
            print(
                f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Amount must be {Fore.WHITE}a number")
            sleep(2)
            return main()

        nitroType = input(f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}What kind of nitro do you want ? {Fore.WHITE}classic {Fore.LIGHTBLACK_EX}or {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}? (Classic Nitro is 16chars and Boost Nitro is 24chars): {Fore.WHITE}")

        if nitroType == "boost" or nitroType == "classic":
            pass
        else:
            print(
                f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}boost {Fore.LIGHTBLACK_EX}or {Fore.WHITE}classic{Fore.RESET}")
            sleep(2)
            return main()

        nitroLink = input(
            f"{Fore.WHITE}[ {Fore.YELLOW}> {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Do you want {Fore.WHITE}https://discord.com/gifts/ {Fore.LIGHTBLACK_EX}behind the code ? ({Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no): {Fore.WHITE}")

        if nitroLink == "yes" or nitroLink == "no":
            pass
        else:
            print(
                f"{Fore.WHITE}[ {Fore.RED}! {Fore.WHITE}] {Fore.LIGHTBLACK_EX}Answer must be {Fore.WHITE}yes {Fore.LIGHTBLACK_EX}or {Fore.WHITE}no{Fore.RESET}")
            sleep(2)
            return main()
    except KeyboardInterrupt:
        clear_console()
        exit()

    gen(nitroAmount, nitroType, nitroLink)


def gen(nitroAmount, nitroType, nitroLink):

    amount = 0

    with open("nitros.txt", "w") as file:
        file.write("")

    for _ in range(nitroAmount):
        genCode = "".join(random.choice(string.digits+string.ascii_letters)
                          for _ in range(24)) if nitroType == "boost" else "".join(random.choice(string.digits+string.ascii_letters)
                                                                                   for _ in range(16))
        nitro = f"https://discord.com/gifts/{genCode}" if nitroLink == "yes" else genCode

        try:
            print(
                f"{Fore.WHITE}[ {Fore.YELLOW}- {Fore.WHITE}] {Fore.RESET}{nitro}")
            nitros.write(
                f"{nitro}\n")
            amount += 1
        except:
            break

    nitros.close()
    input(
        f"\n{Fore.WHITE}[ {Fore.GREEN}> {Fore.WHITE}] {amount} nitros have been generated. (Press any key to close the generator)")


def clear_console():
    if platform.system() == "Windows":
        cmd("cls")
    else:
        cmd("clear")


if __name__ == "__main__":
    main()
