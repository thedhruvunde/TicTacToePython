def display(r1, r2, r3):
    print(r1)
    print(r2)
    print(r3)
def indexWriter(r1, r2, r3, index, pn):
    index = index.split(',')
    for _ in range(0, 2):
        index[_] = int(index[_])

    if pn == 1:
        if index[0] == 1:
            if index[1] == 1:
                r1[0] = 'X'
            elif index[1] == 2:
                r2[0] = 'X'
            elif index[1] == 3:
                r3[0] = 'X'
        elif index[0] == 2:
            if index[1] == 1:
                r1[1] = 'X'
            elif index[1] == 2:
                r2[1] = 'X'
            elif index[1] == 3:
                r3[1] = 'X'
        elif index[0] == 3:
            if index[1] == 1:
                r1[2] = 'X'
            elif index[1] == 2:
                r2[2] = 'X'
            elif index[1] == 3:
                r3[2] = 'X'

    if pn == 2:
        if index[0] == 1:
            if index[1] == 1:
                r1[0] = 'O'
            elif index[1] == 2:
                r2[0] = 'O'
            elif index[1] == 3:
                r3[0] = 'O'
        elif index[0] == 2:
            if index[1] == 1:
                r1[1] = 'O'
            elif index[1] == 2:
                r2[1] = 'O'
            elif index[1] == 3:
                r3[1] = 'O'
        elif index[0] == 3:
            if index[1] == 1:
                r1[2] = 'O'
            elif index[1] == 2:
                r2[2] = 'O'
            elif index[1] == 3:
                r3[2] = 'O'
    display(r1, r2, r3)
def winCheck(r1, r2, r3):
    win = False
    if (r1[0] == 'X' and r2[0] == 'X' and r3[0] == 'X' or r1[1] == 'X' and r2[1] == 'X' and r3[1] == 'X' or r1[2] == 'X' and r2[2] == 'X' and r3[2] == 'X'):
        print("Player1 Wins!!!")
        win = True

    elif (r1[0] == 'X' and r1[1] == 'X' and r1[2] == 'X' or r2[0] == 'X' and r2[1] == 'X' and r2[2] == 'X' or r3[0] == 'X' and r3[1] == 'X' and r3[2] == 'X'):
        print("Player1 Wins!!!")
        win = True

    elif (r1[0] == 'X' and r2[1] == 'X' and r3[2] == 'X' or r1[2] == 'X' and r2[1] == 'X' and r3[0] == 'X'):
        print("Player1 Wins!!!")
        win = True

    elif (r1[0] == 'O' and r2[0] == 'O' and r3[0] == 'O' or r1[1] == 'O' and r2[1] == 'O' and r3[1] == 'O' or r1[2] == 'O' and r2[2] == 'O' and r3[2] == 'O'):
        print("Player2 Wins!!!")
        win = True

    elif (r1[0] == 'O' and r1[1] == 'O' and r1[2] == 'O' or r2[0] == 'O' and r2[1] == 'O' and r2[2] == 'O' or r3[0] == 'O' and r3[1] == 'O' and r3[2] == 'O'):
        print("Player2 Wins!!!")
        win = True

    elif (r1[0] == 'O' and r2[1] == 'O' and r3[2] == 'O' or r1[2] == 'O' and r2[1] == 'O' and r3[0] == 'O'):
        print("Player2 Wins!!!")
        win = True
    
    return win

r1 = [' ', ' ', ' ']
r2 = [' ', ' ', ' ']
r3 = [' ', ' ', ' ']
display(r1, r2, r3)

while True:
    win = winCheck(r1, r2, r3)
    if win == True:
        break
    index = input("Player1 type your index: ")
    pn = 1
    indexWriter(r1, r2, r3, index, pn)
    win = winCheck(r1, r2, r3)
    if win == True:
        break
    index = input("Player2 type your index: ")
    pn = 2
    indexWriter(r1, r2, r3, index, pn)
    winCheck(r1, r2, r3)