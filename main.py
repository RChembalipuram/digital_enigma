from os import system
from tabulate import tabulate
from time import sleep
from funcs import encoder, decoder, bombe

def sleep_clear(message, time):
	print(message)
	sleep(time)
	system("cls")

def main() -> None:
    while True:
        match input(f"What would you like to do?\n{tabulate([['Encode',1], ['Decode',2], ['Bombe (enigma cracker)', 3],['Exit',4]], headers=['Activity','Key'], tablefmt='double_grid')}\n\n").strip():
            case "1":
                sleep_clear("Encode selected",1.5)
                encoder()
            case "2":
                sleep_clear("Decode selected",1.5)
                decoder()
            case "3":
                sleep_clear("Bombe selected",1.5)
                bombe()
            case "4":
                break
            case _:
                sleep_clear("Invalid input, please try again",1.5)

if __name__ == "__main__":
    main()