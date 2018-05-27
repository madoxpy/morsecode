from time import sleep
import sys

dictonary={".-" : "a","-..." : "b","-.-." : "c","-.." : "d",
"." : "e","..-." : "f","--." : "g","...." : "h",
".." : "i",".---" : "j","-.-" : "k",".-.." : "l",
"--" : "m","-." : "n","---" : "o",".--." : "p",
"--.-" : "q",".-." : "r","..." : "s","-" : "t",
"..-" : "u","...-" : "v",".--" : "w","-..-" : "x",
"-.--" : "y","--.." : "z",".----" : "1","..---" : "2",
"...--" : "3","....-" : "4","....." : "5","-...." : "6",
"--..." : "7","---.." : "8","----." : "9","-----" : "0",
".-.-.-" : ".","--..--" : "0","..--.." : "?","-.-.--" : "!"}


try:
    print "Type ctrl+c to quit"
    while True:
        try:
            sentence=raw_input(": ")
            words=sentence.split("  ")
            for word in words:
                chars = word.split()
                for char in chars:
                    sys.stdout.write(dictonary[char])
                print " ",
                
            print
        except KeyError:
            print "One of the key is not in the dictionary. Try again."
except KeyboardInterrupt:
    print (" \nGood bye")
