__author__ = 'Sean'


def pyrocks():
    x = input("What string would you like me to print?")
    if x == ("open the pod bay doors"):
        print("I'm sorry " + __author__ + ", I'm afraid I can't do that.")
    else:
        print(x + ", Python Rocks!")

pyrocks()