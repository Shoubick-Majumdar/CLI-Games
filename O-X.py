import numpy as np
from os import system
from random import randint

inp_arr = np.zeros(9, dtype='i2')  # 'i2' represents int4

val_loc = [1,5,9]


def grid():
    ct = 0
    for i in range(11):
        for j in range(11):
            
            if j == 3 or j == 7:
                print("|", end='')
            
            elif  i == 3 or i == 7:
                print("__", end='')

            elif i in val_loc and j in val_loc:
                
                if inp_arr[ct] == 1:
                    print('X', end=' ')
                elif inp_arr[ct] == 2:
                    print('O', end=' ')
                else:
                    print("  ", end="")
                ct += 1

            else:
                print("  ", end='')
        print()
    print()

def check():
    arr = inp_arr.reshape(3,3)

    if (arr[0][0] == arr[1][1] == arr[2][2]) or (arr[0][2] == arr[1][1] == arr[2][0]):
        return arr[1][1]

    for j in range(3):
        if (arr[0][j] == arr[1][j] == arr[2][j]):
            return arr[0][j]

    for i in range(3):
        if (arr[i][0] == arr[i][1] == arr[i][2]):
            return arr[i][0]
    
    return 0

def inp(player):
    global inp_arr

    if (player % 2 == 0):
        pos = int(input("Enter position (1-9): "))
    else:
        pos = randint(1,9)
    
    if not(inp_arr[pos-1]):
        if(player % 2 == 0):
            inp_arr[pos-1] = 1
        else:
            inp_arr[pos-1] = 2
    else:
        if (player % 2 == 0):
            print("position already filled")
            system('pause')
        return True
    return False

def mainloop():
    turn = 0
    while turn < 9:

        system('cls')
        grid()

        if(inp(turn)):
            continue
        res = check()

        if res:
            system('cls')
            grid()
            
            if res == 1:
                print("Player Wins")
            elif res == 2:
                print("Cpu Wins")
            
            return
        turn += 1

    grid()
    print("It's a Draw ")

if __name__ == "__main__":
    mainloop()