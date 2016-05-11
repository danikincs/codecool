#made by the website instructions
import sys
i="World"
#if the program get nothing for the arg, it will change the name of the i variable to World-to print Hello World!

for arg in sys.argv:
    if arg != ("helloworld.py"):
        i=arg

print ("Hello",(i),"!")    #if the script get a name it will print Hello (name(i variable)) !
