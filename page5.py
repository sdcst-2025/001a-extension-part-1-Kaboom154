#page 5 - leave the building
from rich import print
from os import system
def page5():
    system("clear||cls")

    print('''
    [red]You have left the building.[/red]

    To start again, press 1''')

    choice = input()
    if choice == "1":
        import start
    else:
        import page5