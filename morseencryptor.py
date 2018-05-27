from pygame import *
from time import sleep

dictonary={ " " : " ","a" : ".-", "b" : "-...","c" : "-.-.","d" : "-..","e" : ".","f" : "..-.",
"g" : "--.","h" : "....","i" : "..","j" : ".---","k" : "-.-","l" : ".-..","m" : "--","n" : "-.",
"o" : "---","p" : ".--.","q" : "--.-","r" : ".-.","s" : "...","t" : "-","u" : "..-","v" : "...-",
"w" : ".--","x" : "-..-","y" : "-.--","z" : "--..", "1" : ".----","2" : "..---","3" : "...--",
"4" : "....-","5" : ".....","6" : "-....","7" : "--...","8" : "---..","9" : "----.","0" : "-----",
"." : ".-.-.-","," : "--..--","?" : "..--..","!" : "-.-.--"}


try:
    print "Type ctrl+c to quit"
    while True:
        init()
        on=image.load("on.png")
        off=image.load("off.png")
        sentence=raw_input(": ")
        sentence=sentence.lower()
        res=[325,450]
        window=display.set_mode(res)
        window.blit(off,(0,0))
        display.flip()
        for i in sentence:
            print dictonary[i]," ",
            for j in dictonary[i]:
                if j==".":
                    mixer.music.load("short.ogg")
                    mixer.music.play(1)
                    window.blit(on,(0,0))
                    display.flip()                   
                    sleep(0.1)   
                if j=="-":
                    mixer.music.load("long.ogg")
                    mixer.music.play(1)
                    window.blit(on,(0,0))
                    display.flip()  
                    sleep(0.5)
                if j==" ":
                    sleep(0.5)
                window.fill((0,0,0))
                window.blit(off,(65,35))
                display.flip() 
                sleep(0.4)        
        print 
        sleep(1)
        quit()
except KeyboardInterrupt:
    print (" \nGood bye")