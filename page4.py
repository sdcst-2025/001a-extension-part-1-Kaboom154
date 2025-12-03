#page 4 - 
from rich import print
from os import system
system("clear||cls")

print("""
[blue]You have turned around on the spot.[/blue]
You may walk forwards to exit the building, or turn around again to continue on your journey.
[yellow]Where do you want to go next?[/yellow]
1 - Walk forwards to exit the building
2 - Turn around """)

choice = input()
if choice == '1':
    import page5
elif choice == '2':
    import start
else:
    import page4