
import getpass

def print_username(name):
    print(f"Hello {name}!")

def print_introduce(name):
    print(f"My name is {name}.")

if __name__ == "__main__":
    cmd = input("Type your command (1: name, 2: introduce) >>> ")
    uname = getpass.getuser()
    if cmd == "1":
        print_username(uname)
    elif cmd == "2":
        print_introduce(uname)
