from rich import print
from os import system
import page1
import page2
import page3
import page4
import start
def start1():
    system("clear||cls")


    print("[yellow] Where do you want to go next?")
    print("1 - Turn left")
    print("2 - Turn right")
    print("3 - Keep walking forwards")
    print("4 - Turn around")

    choice = input()
    if choice == "1":
        page1.page1()
    elif choice == "2":
        page2.page2()
    elif choice == "3":
        page3.page3()
    elif choice == "4":
        page4.page4()
    else:
        start.start1()
start.start1()