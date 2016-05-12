import sys

def argument(list):
    i = "World"
    for arg in list:
        if arg != ("helloworld2.py"):
            i=arg
    return i



print ("Hello",argument(sys.argv),"!")
