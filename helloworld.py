import sys #this crap just import the system stuff like exit() stb

for arg in sys.argv: #this is just a simple for ciklus, and sys.argv is a list (0:the name of the file
    print arg           #1:you write after the file stb stb) argv become as long list as long you write it
                        #after the filename in terminal





#made by the website instructions
import sys
i="World"
                    #if the program get nothing for the arg,
                    #it will change the name of the i variable to World-to print Hello World!

for arg in sys.argv:
    if arg != ("helloworld.py"):  #ha arg nem egyezik meg a névvel akkor az i változó a beirt név lesz
        i=arg                      #ha nem irsz be semmit meg fog egyezni akkor viszont az i változó World marad
                                    #és igy Hello World! lesz a kiírás
print ("Hello",(i),"!")    #if the script get an arg(the first thing in list argv)
                            #it will print Hello (name(i variable)=the name you written after the filename) !
