import random
from os import system
from termcolor import colored
from time import sleep

def textanimation(packed):
    x_frame = 0
    y_pushtimes = len(packed)
    format_packed =  str(packed)
    color_sets = [] #future feature?
    while x_frame != 18: #18 frames for cycle
        system('clear')
        x_frame += 1
        #print("framecount -> " + str(x_frame) + "\n") #debug status [frames display]
        #print("y_pustimesvar: " + str(y_pushtimes) + "| To add to Xframes-> " + str(x_frame)) #debug status [push]
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'green', attrs=['bold'])) #frame set buffer -> {1}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'red', attrs=['bold'])) #frame set buffer -> {2}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'cyan', attrs=['bold'])) #frame set buffer -> {3}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'yellow', attrs=['bold'])) #frame set buffer -> {4}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'grey', attrs=['bold'])) #frame set buffer -> {5}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'white', attrs=['bold'])) #frame set buffer -> {6}
        sleep(0.25) #time to reset loop{animation};

#ideia space

What_to_do = '''

1 - find a way to alternate colors givin in the range of color_sets -> []
2 - maybe add multi threading?
3 - will multi threading ruin my animation speed, because of the faster "render" of the animation?
4 - do a revert animation?

'''
