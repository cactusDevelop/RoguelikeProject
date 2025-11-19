
import os, sys, time, msvcrt


def clear_console():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def quick_print(txt: tuple):
    for _ in txt:
        print(_, end="")
        wait_input()

def slow_print(txt: tuple, delay: float):
    for l in txt:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(delay)
        #Ajouter un sfx ?
    print()

def solid_input(conf, to_display):
    to_display()
    action_input = input(" > ").strip()

    while not conf(action_input):
        clear_console()
        to_display()
        print("\033[3m\nValeur invalide...\033[0m")
        action_input = input(" > ").strip()

    return action_input.lower()

def get_width():
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80
    return columns

def wait_input():
    if os.name == "nt":
        try:
            while True:
                if msvcrt.kbhit():
                    key = msvcrt.getch()
                    if key in (b'\r',b'\n'):
                        break
        except ImportError:
            input()

    else:
        input() # Je prends pas le risque sur Linux/IOS
    print()