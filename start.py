
from rich import print
from os import system
system("clear||cls")


print("[yellow] Where do you want to go next?")
print("1 - Turn left")
print("2 - Turn right")
print("3 - Keep walking forwards")
print("4 - Turn around")

choice = input()
if choice == "1":
    import page1
elif choice == "2":
    import page2
elif choice == "3":
    import page3
elif choice == "4":
    print('p4')
    import page4
    del page4
else:
    import start