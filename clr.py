from colorama import Fore, Back, Style, init
init(autoreset=True)
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print('back to normal now')
