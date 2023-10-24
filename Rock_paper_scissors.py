#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
print("\n\t\t\tROCK-PAPER-SCISSOR")
print("\t\t\t-------------------\n")
print("---INSTRUCTIONS---")
print("-------------------\n")
print("0 for rock(🪨 ) \t 1 for paper(📜 )\t2 for scissor(✂️ ):")
c=1
while(c!=0):
    a=int(input('\nEnter a number....\n'))
    if a>=3 or a<0:
        print("Enter a valid number.....!You lose")
    else:
        lis=["🪨","📜","✂️"]
        b=random.randint(0,2)
        print("user choice:",lis[a])
        print("system choice:",lis[b])
        if a==b:
            print("----------\nDraw...!----------n")
        elif b==0:
            if a==1:
                print("------------------\nYou win....✨🤩!\n------------------")
            else:
                print("------------------\nYou lose....🤞🤞!\n------------------")
        elif b==1:
            if a==0:
                print("------------------\nYou lose....🤞🤞!\n------------------")
            else:
                print("------------------\nYou win....✨🤩!\n------------------")
        elif b==2:
            if a==0:
                print("------------------\nYou win....✨🤩!\n------------------")
            else:
                print("------------------\nYou lose....🤞🤞!\n------------------")
        c=int(input("\nDo you want to play again press '1' or else to terminate Game press '0':"))

