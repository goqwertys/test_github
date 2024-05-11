"""
Hello World
"""

from src.hello_world import greetings, text_reverse


def main():
    name = input("What is your name?\n")
    greetings(name)
    # Turning to TWIN PEAKS MODE
    print("Welcome to Twin Peaks")
    greetings(text_reverse(name))
    print("main fixes")
    print("some changes")



if __name__ == "__main__":
    main()
