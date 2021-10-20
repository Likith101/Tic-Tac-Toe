import pygame
from pygame.locals import *
import random

XO   = "X"
grid = [ [ None, None, None ,None], \
         [ None, None, None ,None], \
         [ None, None, None ,None], \
         [ None, None, None ,None] ]
winner = None
win1 = 0
win2 = 0
draw = 0
count = 0
reset = False
countstopper = False
singleplayer = False
piececount = 0
senario = 0
difficulty = False

def initBoard(ttt):
    
    global background, singleplayer, difficulty

    background.fill ((209,209,209))
    pygame.draw.line (background, (0,0,0), (150,150), (150,600), 5)
    pygame.draw.line (background, (0,0,0), (600,150), (600,600), 5)
    pygame.draw.line (background, (0,0,0), (150,150), (600,150), 5)
    pygame.draw.line (background, (0,0,0), (150,600), (600,600), 5)
    pygame.draw.line (background, (0,0,0), (300,150), (300,600), 2)
    pygame.draw.line (background, (0,0,0), (450,150), (450,600), 2)
    pygame.draw.line (background, (0,0,0), (150,300), (600,300), 2)
    pygame.draw.line (background, (0,0,0), (150,450), (600,450), 2)
    pygame.draw.line (background, (0,0,0), (700,0), (700,750), 10)
    pygame.draw.line (background, (0,0,0), (740,200), (740,500), 3)
    pygame.draw.line (background, (0,0,0), (860,200), (860,500), 3)
    pygame.draw.line (background, (0,0,0), (740,200), (860,200), 3)
    pygame.draw.line (background, (0,0,0), (740,500), (860,500), 3)
    pygame.draw.line (background, (0,0,0), (740,300), (860,300), 3)
    pygame.draw.line (background, (0,0,0), (740,400), (860,400), 3)
    pygame.draw.line (background, (0,0,0), (740,260), (860,260), 1)
    pygame.draw.line (background, (0,0,0), (740,360), (860,360), 1)
    pygame.draw.line (background, (0,0,0), (740,460), (860,460), 1)
    pygame.draw.line (background, (0,0,0), (760,575), (840,575), 4)
    pygame.draw.line (background, (0,0,0), (760,600), (840,600), 4)
    pygame.draw.line (background, (0,0,0), (760,575), (760,600), 4)
    pygame.draw.line (background, (0,0,0), (840,575), (840,600), 4)
    pygame.draw.line (background, (0,0,0), (760,625), (840,625), 4)
    pygame.draw.line (background, (0,0,0), (760,675), (840,675), 4)
    pygame.draw.line (background, (0,0,0), (760,625), (760,675), 4)
    pygame.draw.line (background, (0,0,0), (840,625), (840,675), 4)
    if (singleplayer==True):
        if (difficulty==False):
            pygame.draw.line (background, (252,255,54), (760,75), (840,75), 4)
            pygame.draw.line (background, (252,255,54), (760,100), (840,100), 4)
            pygame.draw.line (background, (252,255,54), (760,75), (760,100), 4)
            pygame.draw.line (background, (252,255,54), (840,75), (840,100), 4)
            pygame.draw.line (background, (0,0,0), (760,125), (840,125), 4)
            pygame.draw.line (background, (0,0,0), (760,150), (840,150), 4)
            pygame.draw.line (background, (0,0,0), (760,125), (760,150), 4)
            pygame.draw.line (background, (0,0,0), (840,125), (840,150), 4)
        else:
            pygame.draw.line (background, (0,0,0), (760,75), (840,75), 4)
            pygame.draw.line (background, (0,0,0), (760,100), (840,100), 4)
            pygame.draw.line (background, (0,0,0), (760,75), (760,100), 4)
            pygame.draw.line (background, (0,0,0), (840,75), (840,100), 4)
            pygame.draw.line (background, (252,255,54), (760,125), (840,125), 4)
            pygame.draw.line (background, (252,255,54), (760,150), (840,150), 4)
            pygame.draw.line (background, (252,255,54), (760,125), (760,150), 4)
            pygame.draw.line (background, (252,255,54), (840,125), (840,150), 4)
    return background

def drawStatus (board):

    global XO, winner, p1, p2, count, win1, win2, draw

    if (singleplayer==False):
        if (winner is None):
            if (count%2==0):
                if (XO=="X"):
                    x = "Player1"
                else:
                    x = "Player2"
            else:
                if (XO=="O"):
                    x = "Player1"
                else:
                    x = "Player2"
            message = x + "'s turn (" + XO + ")"

        elif (winner == 1):
            message = "Draw"

        else:
            if (count%2==0):
                if (XO=="X"):
                    x = "Player 1"
                else:
                    x = "Player 2"
            else:
                if (XO=="O"):
                    x = "Player 1"
                else:
                    x = "Player 2"
            message = x + " won! (" + winner + ")"
        p1 = "Player 1"
        p2 = "Player 2"
        but21 = "Single"
        t2 = "Multi-player"
    else:
        if (winner is None):
            if (count%2==0):
                message = "Your turn(X)"
            else:
                if (piececount==0):
                    message = "Click to  start game"
                else:
                    message = "Your turn(O)"

        elif (winner == 1):
            message = "Draw"

        else:
            if (count%2==0):
                if (winner=="X"):
                    y = 1
                else:
                    y = 0
            else:
                if (piececount%2==0):
                    y = 1
                else:
                    y = 0
            if (y==0):
                message = "You won"
            else:
                message = "You lost"
        p1 = "Player"
        p2 = "Computer"
        but21 = "Multi"
        t2 = "Single-player"
        
    but1 = "Reset"
    but22 = "Player"
    but3 = "Easy"
    but4 = "Hard"
    dr = "Draws"
    w1 = "(Wins)"
    w2 = "(Wins)"
    wi1 = str(win1)
    wi2 = str(win2)
    dra = str(draw)
    font = pygame.font.Font(None, 24)
    titlefont = pygame.font.Font(None, 45)
    text = font.render(message, 1, (0, 0, 0))
    board.fill ((209,209,209), (200,610,350,25))

    if (singleplayer==False):
        if (winner==1):
            board.blit(text, (357,620))

        else:
            board.blit(text, (310,620))

    else:
        if (piececount==0 and count%2!=0):
            board.blit(text, (300,620))
        else:
            if (winner==None):
                board.blit(text, (330,620))
            elif (winner==1):
                board.blit(text, (357,620))
            else:
                board.blit(text, (345,620))

    but1 = font.render(but1, 2, (0,0,0))
    board.fill ((250,0,0), (762,577,78,23))
    board.blit(but1, (780,582))
    p1 = font.render(p1, 2, (0,0,0))
    w1 = font.render(w1, 2, (0,0,0))
    board.fill ((209,209,209), (742,202,117,57))
    if (singleplayer==False):
        board.blit(p1, (770,210))
    else:
        board.blit(p1, (776,210))
    board.blit(w1, (776,233))
    p2 = font.render(p2, 2, (0,0,0))
    w2 = font.render(w2, 2, (0,0,0))
    board.fill ((209,209,209), (742,302,117,57))
    if (singleplayer==False):
        board.blit(p2, (770,310))
    else:
        board.blit(p2, (762,310))
    board.blit(w2, (776,333))
    dr = font.render(dr, 2, (0,0,0))
    board.fill ((209,209,209), (742,402,117,57))
    board.blit(dr, (777,423))
    wi1 = font.render(wi1, 2, (0,0,0))
    board.fill ((209,209,209), (742,262,117,38))
    board.blit(wi1, (797,273))
    wi2 = font.render(wi2, 2, (0,0,0))
    board.fill ((209,209,209), (742,362,117,38))
    board.blit(wi2, (797,373))
    dra = font.render(dra, 2, (0,0,0))
    board.fill ((209,209,209), (742,462,117,38))
    board.blit(dra, (797,473))
    but21 = font.render(but21, 3, (0,0,0))
    if (singleplayer==False):
        board.fill ((16,232,164), (762,627,78,48))
    else:
        board.fill ((83,8,196), (762,627,78,48))
    if (singleplayer==False):
        board.blit(but21, (777,635))
    else:
        board.blit(but21, (783,635))
    but22 = font.render(but22, 3, (0,0,0))
    board.blit(but22, (778,650))
    if (singleplayer==True):
        but3 = font.render(but3, 3, (0,0,0))
        board.fill ((68,179,29), (762,77,78,23))
        board.blit(but3, (783,81))
        but4 = font.render(but4, 3, (0,0,0))
        board.fill ((230,62,21), (762,127,78,23))
        board.blit(but4, (783,131))
    t2 = titlefont.render(t2, 3, (0,0,0))
    board.fill ((209,209,209), (150,635,450,115))
    board.blit(t2, (150,635))

def showBoard (ttt, board):
    
    drawStatus (board)
    ttt.blit (board, (0, 0))
    pygame.display.flip()
    
def boardPos (mouseX, mouseY):

    global reset, singleplayer, count, win1, win2, draw, difficulty

    if (mouseY<300 and mouseY>150):
        row = 0

    elif (mouseY<450 and mouseY>300):
        row = 1

    elif (mouseY<600 and mouseY>450):
        row = 2

    else:
        row = 3

    if (mouseX<300 and mouseX>150):
        col = 0

    elif (mouseX<450 and mouseX>300):
        col = 1

    elif (mouseX<600 and mouseX>450):
        col = 2

    else:
        col = 3

    if (mouseX<840 and mouseX>760 and mouseY<600 and mouseY>575):
        reset = True

    if (mouseX<840 and mouseX>760 and mouseY<675 and mouseY>625):
        if (singleplayer==False):
            singleplayer = True
        else:
            singleplayer = False
        reset = True
        count = 0
        win1 = 0
        win2 = 0
        draw = 0
    if (singleplayer==True):
        if (mouseX<840 and mouseX>760 and mouseY<100 and mouseY>75):
            difficulty = False
            reset = True
            count = 0
            win1 = 0
            win2 = 0
            draw = 0
        elif (mouseX<840 and mouseX>760 and mouseY<150 and mouseY>125): 
            difficulty = True
            reset = True
            count = 0
            win1 = 0
            win2 = 0
            draw = 0
    return (row, col)

def drawMove (board, boardRow, boardCol, Piece):

    global piececount

    piececount = piececount + 1
    centerX = ((boardCol) * 150) + 225
    centerY = ((boardRow) * 150) + 225

    if (Piece == 'O'):
        pygame.draw.circle (board, (0,0,0), (centerX, centerY), 55, 2)

    else:
        pygame.draw.line (board, (0,0,0), (centerX - 40, centerY - 40), \
                         (centerX + 40, centerY + 40), 4)
        pygame.draw.line (board, (0,0,0), (centerX + 40, centerY - 40), \
                         (centerX - 40, centerY + 40), 4)

    grid [boardRow][boardCol] = Piece
    
def clickBoard(board):

    global grid, XO, winner, count

    (mouseX, mouseY) = pygame.mouse.get_pos()
    (row, col) = boardPos (mouseX, mouseY)
    if winner==None:
        if (row == 3 or col == 3 ):
            return

        if ((grid[row][col] == "X") or (grid[row][col] == "O")):
            return

        if (singleplayer==False):
            drawMove (board, row, col, XO)
            if (XO == "X"):
                XO = "O"

            else:
                XO = "X"

        else:
            if (count%2==0):
                XO = "X"
            else:
                XO = "O"
            if (count%2==0):
                drawMove (board, row, col, XO)
                singleplay(board)

            else:
                if (piececount==0):
                    singleplay(board)
                else:
                    drawMove (board, row, col, XO)
                    singleplay(board)

    elif (winner==1):
        XO = "X"
    
def gameWon(board):

    global grid, winner, reset, ttt, running, win1, win2, count, draw, countstopper, XO, piececount

    for row in range (0, 3):
        if ((grid [row][0] == grid[row][1] == grid[row][2]) and \
           (grid [row][0] is not None)):
            winner = grid[row][0]
            pygame.draw.line (board, (250, 0, 0), (165, (row + 1)* 150 + 75), \
                              (585, (row + 1)* 150 + 75), 4)
            if (count%2==0 and countstopper==False):
                if (winner=="X"):
                    win1 = win1 + 1
                else:
                    win2 = win2 + 1
                count = count + 1
                countstopper=True
            elif (count%2==1 and countstopper==False):
                if (winner=="O"):
                    win1 = win1 + 1
                else:
                    win2 = win2 + 1
                count = count + 1
                countstopper=True
            break

    for col in range (0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and \
           (grid[0][col] is not None):
            winner = grid[0][col]
            pygame.draw.line (board, (250, 0, 0), ((col + 1)*150 + 75, 165), \
                              ((col + 1)* 150 + 75, 585), 4)
            if (count%2==0 and countstopper==False):
                if (winner=="X"):
                    win1 = win1 + 1
                else:
                    win2 = win2 + 1
                count = count + 1
                countstopper=True
            elif (count%2==1 and countstopper==False):
                if (winner=="O"):
                    win1 = win1 + 1
                else:
                    win2 = win2 + 1
                count = count + 1
                countstopper=True
            break

    if (grid[0][0] == grid[1][1] == grid[2][2]) and \
       (grid[0][0] is not None):
        winner = grid[0][0]
        pygame.draw.line (board, (250, 0, 0), (165, 165), (585, 585), 2)
        if (count%2==0 and countstopper==False):
            if (winner=="X"):
                win1 = win1 + 1
            else:
                win2 = win2 + 1
            count = count + 1
            countstopper=True
        elif (count%2==1 and countstopper==False):
            if (winner=="O"):
                win1 = win1 + 1
            else:
                win2 = win2 + 1
            count = count + 1
            countstopper=True

    if (grid[0][2] == grid[1][1] == grid[2][0]) and \
       (grid[0][2] is not None):
        winner = grid[0][2]
        pygame.draw.line (board, (250, 0, 0), (585, 165), (165, 585), 2)
        if (count%2==0 and countstopper==False):
            if (winner=="X"):
                win1 = win1 + 1
            else:
                win2 = win2 + 1
            count = count + 1
            countstopper=True
        elif (count%2==1 and countstopper==False):
            if (winner=="O"):
                win1 = win1 + 1
            else:
                win2 = win2 + 1
            count = count + 1
            countstopper=True

    if (grid[0][0] != None and grid[0][1] != None and grid[0][2] != None and \
        grid[1][0] != None and grid[1][1] != None and grid[1][2] != None and \
        grid[2][0] != None and grid[2][1] != None and grid[2][2] != None and \
        winner == None):
        winner = 1
        if (countstopper==False):
            draw = draw + 1
            count = count + 1
            countstopper=True

    if (reset == True):
        reset = False
        countstopper = False
        piececount = 0
        XO = "X"
        grid = [ [ None, None, None ,None], \
                 [ None, None, None ,None], \
                 [ None, None, None ,None], \
                 [ None, None, None ,None] ]
        winner = None
        board = initBoard (ttt)
        running = 1

def finalsteps(board):

    global count, piececount

    gameWon(board)

    if (winner==None):

        if (count%2==0 and piececount%2!=0 and piececount<9):
            filler(board)

        elif (count%2!=0 and piececount%2==0 and piececount<9):
            filler(board)

def filler(board):

    global grid, play, comp, piececount

    for i in range(0,3):

        if (grid[i][0]==comp and grid[i][1]==comp and grid[i][2]==None):
            drawMove(board, i, 2, comp)
            return

        elif (grid[i][1]==comp and grid[i][2]==comp and grid[i][0]==None):
            drawMove(board, i, 0, comp)
            return

        elif (grid[i][2]==comp and grid[i][0]==comp and grid[i][1]==None):
            drawMove(board, i, 1, comp)
            return

    for i in range(0,3):

        if (grid[0][i]==comp and grid[1][i]==comp and grid[2][i]==None):
            drawMove(board, 2, i, comp)
            return

        elif (grid[1][i]==comp and grid[2][i]==comp and grid[0][i]==None):
            drawMove(board, 0, i, comp)
            return

        elif (grid[2][i]==comp and grid[0][i]==comp and grid[1][i]==None):
            drawMove(board, 1, i, comp)
            return

    if (grid[0][0]==comp and grid[1][1]==comp and grid[2][2]==None):
        drawMove(board, 2, 2, comp)
        return

    elif (grid[1][1]==comp and grid[2][2]==comp and grid[0][0]==None):
        drawMove(board, 0, 0, comp)
        return

    elif (grid[2][2]==comp and grid[0][0]==comp and grid[1][1]==None): 
        drawMove(board, 1, 1, comp)
        return

    if (grid[0][2]==comp and grid[1][1]==comp and grid[2][0]==None):
        drawMove(board, 2, 0, comp)
        return

    elif (grid[1][1]==comp and grid[2][0]==comp and grid[0][2]==None):
        drawMove(board, 0, 2, comp)
        return

    elif (grid[2][0]==comp and grid[0][2]==comp and grid[1][1]==None): 
        drawMove(board, 1, 1, comp)
        return


    for i in range(0,3):

        if (grid[i][0]==play and grid[i][1]==play and grid[i][2]==None):
            drawMove(board, i, 2, comp)
            return

        elif (grid[i][1]==play and grid[i][2]==play and grid[i][0]==None):
            drawMove(board, i, 0, comp)
            return

        elif (grid[i][2]==play and grid[i][0]==play and grid[i][1]==None):
            drawMove(board, i, 1, comp)
            return

    for i in range(0,3):

        if (grid[0][i]==play and grid[1][i]==play and grid[2][i]==None):
            drawMove(board, 2, i, comp)
            return

        elif (grid[1][i]==play and grid[2][i]==play and grid[0][i]==None):
            drawMove(board, 0, i, comp)
            return

        elif (grid[2][i]==play and grid[0][i]==play and grid[1][i]==None):
            drawMove(board, 1, i, comp)
            return

    if (grid[0][0]==play and grid[1][1]==play and grid[2][2]==None):
        drawMove(board, 2, 2, comp)
        return

    elif (grid[1][1]==play and grid[2][2]==play and grid[0][0]==None):
        drawMove(board, 0, 0, comp)
        return

    elif (grid[2][2]==play and grid[0][0]==play and grid[1][1]==None): 
        drawMove(board, 1, 1, comp)
        return

    if (grid[0][2]==play and grid[1][1]==play and grid[2][0]==None):
        drawMove(board, 2, 0, comp)
        return

    elif (grid[1][1]==play and grid[2][0]==play and grid[0][2]==None):
        drawMove(board, 0, 2, comp)
        return

    elif (grid[2][0]==play and grid[0][2]==play and grid[1][1]==None): 
        drawMove(board, 1, 1, comp)
        return

    randomplay(board)

def randomplay(board):

    global grid, comp 

    a=True
    while (a==True):
        p=random.randint(1,9)
        if (p==1 and grid[0][0]==None):
            drawMove(board, 0, 0, comp)
            a=False

        elif (p==2 and grid[0][1]==None):
            drawMove(board, 0, 1, comp)
            a=False

        elif (p==3 and grid[0][2]==None):
            drawMove(board, 0, 2, comp)
            a=False 

        elif (p==4 and grid[1][0]==None):
            drawMove(board, 1, 0, comp)
            a=False

        elif (p==5 and grid[1][1]==None):
            drawMove(board, 1, 1, comp)
            a=False

        elif (p==6 and grid[1][2]==None):
            drawMove(board, 1, 2, comp)
            a=False

        elif (p==7 and grid[2][0]==None):
            drawMove(board, 2, 0, comp)
            a=False

        elif (p==8 and grid[2][1]==None):
            drawMove(board, 2, 1, comp)
            a=False

        elif (p==9 and grid[2][2]==None):
            drawMove(board, 2, 2, comp)
            a=False
        p=p+1


def singleplay(board):

    global grid, senario, play, comp, piececount, difficulty

    if (count%2==0):
        play = "X"
        comp = "O"
    else:
        play = "O"
        comp = "X"

    if (difficulty==False):
        finalsteps(board)

    else:
        if (piececount==0):

            drawMove(board, 1, 1, comp)

        elif (piececount==1):

            if (grid[1][1]==play):
                drawMove(board, 0, 0, comp)
                senario = 1
            elif (grid[0][0]==play):
                drawMove(board, 1, 1, comp)
                senario = 2
            elif (grid[0][1]==play):
                drawMove(board, 1, 1, comp)
                senario = 3
            elif (grid[0][2]==play):
                drawMove(board, 1, 1, comp)
                senario = 4
            elif (grid[1][0]==play):
                drawMove(board, 1, 1, comp)
                senario = 5
            elif (grid[1][2]==play):
                drawMove(board, 1, 1, comp)
                senario = 6
            elif (grid[2][0]==play):
                drawMove(board, 1, 1, comp)
                senario = 7
            elif (grid[2][1]==play):
                drawMove(board, 1, 1, comp)
                senario = 8
            elif (grid[2][2]==play):
                drawMove(board, 1, 1, comp)
                senario = 9

        elif (piececount==2):

            if (grid[0][0]==play):
                drawMove(board, 2, 2, comp)
                senario = 100
            elif (grid[0][1]==play):
                drawMove(board, 2, 2, comp)
                senario = 0
            elif (grid[0][2]==play):
                drawMove(board, 2, 0, comp)
                senario = 101
            elif (grid[1][0]==play):
                drawMove(board, 2, 2, comp)
                senario = 0
            elif (grid[1][2]==play):
                drawMove(board, 0, 0, comp)
                senario = 0
            elif (grid[2][0]==play):
                drawMove(board, 0, 2, comp)
                senario = 102
            elif (grid[2][1]==play):
                drawMove(board, 0, 0, comp)
                senario = 0
            elif (grid[2][2]==play):
                drawMove(board, 0, 0, comp)

        elif (piececount==3):

            if (senario==1):
                if (grid[0][1]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[0][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][1]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][2]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0

            elif (senario==2):
                if (grid[0][1]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[0][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][2]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0
                elif (grid[2][1]==play):
                    drawMove(board, 2, 0, comp)
                    senario = 0
                elif (grid[2][2]==play):
                    drawMove(board, 0, 1, comp)
                    senario = 0

            elif (senario==3):
                if (grid[0][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[0][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][0]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0
                elif (grid[1][2]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0
                elif (grid[2][0]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0
                elif (grid[2][2]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0
                elif (grid[2][1]==play):
                    drawMove(board, 2, 0, comp)
                    senario = 0

            elif (senario==4):
                if (grid[0][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[0][1]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][0]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0
                elif (grid[2][0]==play):
                    drawMove(board, 1, 0, comp)
                    senario = 0
                elif (grid[2][1]==play):
                    drawMove(board, 2, 2, comp)
                    senario = 0

            elif (senario==5):
                if (grid[0][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[0][1]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0
                elif (grid[2][1]==play):
                    drawMove(board, 2, 0, comp)
                    senario = 0
                elif (grid[0][2]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0
                elif (grid[2][2]==play):
                    drawMove(board, 2, 0, comp)
                    senario = 0
                elif (grid[1][2]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0

            elif (senario==6):
                if (grid[0][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[0][1]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0
                elif (grid[2][1]==play):
                    drawMove(board, 2, 2, comp)
                    senario = 0
                elif (grid[0][0]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0
                elif (grid[2][0]==play):
                    drawMove(board, 2, 2, comp)
                    senario = 0
                elif (grid[1][0]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0

            elif (senario==7):
                if (grid[0][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][1]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[0][1]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0
                elif (grid[1][2]==play):
                    drawMove(board, 2, 2, comp)
                    senario = 0
                elif (grid[0][2]==play):
                    drawMove(board, 0, 1, comp)
                    senario = 0

            elif (senario==8):
                if (grid[2][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][0]==play):
                    drawMove(board, 2, 0, comp)
                    senario = 0
                elif (grid[1][2]==play):
                    drawMove(board, 2, 2, comp)
                    senario = 0
                elif (grid[0][0]==play):
                    drawMove(board, 2, 0, comp)
                    senario = 0
                elif (grid[0][2]==play):
                    drawMove(board, 2, 2, comp)
                    senario = 0
                elif (grid[0][1]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0

            elif (senario==9):
                if (grid[0][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][0]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[1][2]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[2][1]==play):
                    finalsteps(board)
                    senario = 0
                elif (grid[0][0]==play):
                    drawMove(board, 0, 1, comp)
                    senario = 0
                elif (grid[0][1]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0
                elif (grid[1][0]==play):
                    drawMove(board, 2, 0, comp)
                    senario = 0

        elif (piececount==4):

            if (senario==100):
                if (grid[2][1]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0
                elif (grid[1][2]==play):
                    drawMove(board, 2, 0, comp)
                    senario = 0
                else:
                    senario = 0

            elif (senario==101):
                if (grid[1][0]==play):
                    drawMove(board, 2, 2, comp)
                    senario = 0
                elif (grid[2][1]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0
                else:
                    senario = 0

            elif (senario==102):
                if (grid[0][1]==play):
                    drawMove(board, 2, 2, comp)
                    senario = 0
                elif (grid[1][2]==play):
                    drawMove(board, 0, 0, comp)
                    senario = 0
                else:
                    senario = 0

            elif (senario==103):
                if (grid[1][0]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0
                elif (grid[0][1]==play):
                    drawMove(board, 0, 2, comp)
                    senario = 0
                else:
                    senario = 0


        if (senario==0):
            finalsteps(board)



pygame.init()
ttt = pygame.display.set_mode ((900, 750))
pygame.display.set_caption ('Tic-Tac-Toe')
background = pygame.Surface (ttt.get_size())
background = background.convert()
board = initBoard (ttt)
running = 1

while (running == 1):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickBoard(board)
        gameWon (board)
        showBoard (ttt, board)