import random
import os
import time
from functions import color_ai, color_user, hands
from functions import rpstonr
from functions import bye
from functions import intro
from colors import bcolors
wincount=0
aiwincount=0
tiecount=0
total=0
while True:
    os.system('cls') 
    ai =random.randint(1, 3)
    # 1 = rock
    # 2 = paper
    # 3 = scissors
    user=4
    while user==4:
        user_input=intro(wincount,aiwincount,tiecount,total)
        user=rpstonr(user_input)
    if ai ==user:
        tiecount=tiecount+1
        res=3
    elif user == 1 and ai == 3:
        wincount=wincount+1   
        res=1
    elif user == 3 and ai == 1:
        aiwincount=aiwincount+1  
        res=2    
    elif ai<user:
        wincount=wincount+1   
        res=1   
    elif user<ai:
        aiwincount=aiwincount+1  
        res=2
    total=tiecount+aiwincount+wincount
    color_user(res)
    print("U picked:")
    hands(user)
    color_ai(res)
    print("Ai picked:")
    hands(ai)
    time.sleep(1)