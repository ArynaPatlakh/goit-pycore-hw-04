from pathlib import Path 
import sys 

from colorama import Fore, init


def create_markup(path: Path, char=" "):

    for el in sorted(path.iterdir()):

        if el.is_dir():
            print(Fore.BLUE + f"{char}{el.name}/")
            create_markup(el, f"{char + "   "}")
        else:
            print(Fore.GREEN + f"{char}{el.name}")


def main():

    init(autoreset=True)

    if len(sys.argv) < 2:
        print("Please insert path")
        return 

    p = Path(sys.argv[1]).resolve()

    if not p.exists():
        print("Path does not exist")
        return

    if not p.is_dir():
        print("This is not directory")
        return

    print(Fore.BLUE + f"{p.name}/")
    create_markup(p)


if __name__ == "__main__":
    main()
