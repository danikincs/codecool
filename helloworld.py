
import sys
i="World"

for arg in sys.argv:
    if arg != ("helloworld.py"):
        i=arg

print ("Hello",(i),"!")
