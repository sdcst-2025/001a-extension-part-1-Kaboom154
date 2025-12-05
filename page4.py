from rich import print
from os import system
import start
import page4
import page5
def page4():
    system("clear||cls")

    print("""
    [blue]You have turned around on the spot.[/blue]
    You may walk forwards to exit the building, or turn around again to continue on your journey.
    [yellow]Where do you want to go next?[/yellow]
    1 - Walk forwards to exit the building
    2 - Turn around """)

    choice = input()
    if choice == '1':
        page5.page5()
    elif choice == '2':
        start.start1()
    else:
        page4.page4()