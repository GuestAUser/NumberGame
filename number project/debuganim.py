import random
from os import system
from termcolor import colored
from time import sleep

def textanimation(packed):
    x_frame = 0
    y_pushtimes = len(packed)
    format_packed =  str(packed)
    color_sets = [] #future feature?
    border = "------------------------------------------------------------------------------"
    while x_frame != 18: #18 frames for cycle
        system('clear')
        x_frame += 1
        print(colored("CONGRATS!".center(80), 'red' , attrs=['bold']))
        print(border)
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'green', attrs=['bold'])) #frame set buffer -> {1}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'red', attrs=['bold'])) #frame set buffer -> {2}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'cyan', attrs=['bold'])) #frame set buffer -> {3}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'yellow', attrs=['bold'])) #frame set buffer -> {4}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'grey', attrs=['bold'])) #frame set buffer -> {5}
        print(colored(format_packed.center(y_pushtimes*int(x_frame)), 'white', attrs=['bold'])) #frame set buffer -> {6}
        print(border)
        sleep(0.25) #time to reset loop{animation};
