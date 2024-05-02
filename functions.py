import msvcrt
import os
import time
from colors import bcolors

def rpstonr(x):
    if x=="q":
        bye()
        time.sleep
        quit
    elif x == "R":
        return 1
    elif x == "P":
        return 2
    elif x == "S":
        return 3
    elif x =="Q":
        os.system('cls')  
        bye()
        quit()
    else:
        print(bcolors.RED+'''     
           *#############################*
         Please use the following listed under
                  R / P / S
           *#############################*''')
        time.sleep(1)
        os.system('cls')
        return 4

def intro(x,y,z,q):
    print(bcolors.PURPLE+f'''
       *#############################*
       #* Rock ## Paper ## scissors *#
       ###############################
       #* Made by: Eric  2024-04-11 *#
       *#############################*
       {bcolors.GREEN}        wins={x}     
       {bcolors.PURPLE} *#                           #*
       {bcolors.RED}      looses={y}    
       {bcolors.PURPLE} *#                           #*
       {bcolors.YELLOW}        ties={z}     
       {bcolors.PURPLE} *#                           #*
       {bcolors.CYAN}        total={q}     
       {bcolors.PURPLE} *#############################*
        #   Pick between   R / P / S  #
        #   If u want to quit use Q   #
        #  Put ur choice down below   #
        *#############################*
          ''')
    
    pick = msvcrt.getwch().upper()
    return pick

def hands(x):
    if x==1:
        print('''
           _________
          |   |  |  \__
         /¨¨¨¨===   |  |
        /    ___/__ |__|
       |    /          |
        \_____ROCK_____/
        ''')       
    elif x==2:
        print('''
            __ __ __
           |  |  |  |__
           |¨¨|¨¨|¨¨|  |
        __ |¨¨|¨¨|¨¨|¨¨|
        \ \|  |  |  |¨¨|
        |  \__         |
        |              |
         \____PAPER____/
        ''')
    elif x==3:
        print('''
        __       __
        \  \   /  /
         \  \ /  /
          \  V  /__ __
         /¨¨¨¨===  |  |
        /    ___/__|__|
        |    /        |
        \__SCISSORS___/             
        ''')   
def bye():
    print(bcolors.RED+''' 
        __  __             _        __     __ 
       / / / /  ___       (_)  ____/ /  __(())
      / /_/ /  / _ \     / /  / __  /  / __ `/
     / __  /  /  __/    / /  / /_/ /  / /_/ / 
    /_/ /_/   \___/  __/ /   \__,_/   \__,_/  
                    /___/                     


    ''')
def color_user(x):
    if x==1:
        print(bcolors.GREEN+"")
    elif x==2:
        print(bcolors.RED+"")
    elif x==3:
        print(bcolors.YELLOW+"")
def color_ai(x):
    if x==1:
        print(bcolors.RED+"")
    elif x==2:
        print(bcolors.GREEN+"")
    elif x==3:
        print(bcolors.YELLOW+"")