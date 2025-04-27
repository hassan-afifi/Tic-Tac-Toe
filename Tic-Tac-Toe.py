def printBoard():
    for i in range(2):
        for j in range(2):
            print(" " + board[i][j] + " ", end="|")
        print(" " + board[i][2] + " ", end="")
        print()
        print("———|———|———")
    for j in range(2):
        print(" " + board[2][j] + " ", end="|")
    print(" " + board[2][2] + " ")
    print()

def checkWinner(ch):
    return (board[0][0] == ch and board[0][1] == ch and board[0][2] == ch) or (board[1][0] == ch and board[1][1] == ch and board[1][2] == ch) or (board[2][0] == ch and board[2][1] == ch and board[2][2] == ch) or (board[0][0] == ch and board[1][0] == ch and board[2][0] == ch) or (board[0][1] == ch and board[1][1] == ch and board[2][1] == ch) or (board[0][2] == ch and board[1][2] == ch and board[2][2] == ch) or (board[0][0] == ch and board[1][1] == ch and board[2][2] == ch) or (board[0][2] == ch and board[1][1] == ch and board[2][0] == ch)

def minimax(depth, isMax, count):
    if checkWinner(p2char):
        return 1
    elif checkWinner(p1char):
        return -1
    elif count == 9:
        return 0
    if isMax:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = p2char
                    score = minimax(depth + 1, False, count + 1)
                    board[i][j] = " "
                    if score > best:
                        best = score
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = p1char
                    score = minimax(depth + 1, True, count + 1)
                    board[i][j] = " "
                    if score < best:
                        best = score
        return best

def aiPlay(count):
    best = -1000
    move = (-1, -1) # Using a tuple for move because it is immutable, ordered, allows duplication, and represents (row, col) clearly.
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = p2char
                score = minimax(0, False , count + 1)
                board[i][j] = " "
                if score > best:
                    move = (i, j)
                    best = score
    board[move[0]][move[1]] = p2char              
        
repeat = 'Y'
Details = open("Files/Details.txt", 'r')
data = Details.read()
if data != "":
    print("1. New Game")
    print("2. Continue Game")
    game = input("Enter your choice: ")
    print()
    while game != "1" and game != "2":
        print("Invalid input, try again")
        print("1. New Game")
        print("2. Continue Game")
        game = input("Enter your choice: ")
        print()
if data == "" or game == "1":
    Details = open("Files/Details.txt", 'w')
    print("1. SinglePlayer")
    print("2. Multiplayer")
    mode = input("Enter your choice: ")
    print()
    while mode != "1" and mode != "2":
        print("Invalid input, try again")
        print("1. SinglePlayer")
        print("2. Multiplayer")
        mode = input("Enter your choice: ")
        print()
    if mode == "1":
        p1 = "You"
        p1char = input("Choose your character: ")
        print()
        while len(p1char) != 1:
            print("Invalid input! Character must be a single digit, try again")
            p1char = input("Choose your character: ")
            print()
        p2 = "AI"
        if p1char == 'X' or p1char == 'x':
            p2char = "O"
        else:
            p2char = "X"
    else:
        p1 = input("Enter the name of player one: ")
        p1char = input("Choose a character for player one: ")
        print()
        while len(p1char) != 1:
            print("Invalid input! Character must be a single digit, try again")
            p1char = input("Choose a character for player one: ")
            print()
        p2 = input("Enter the name of player two: ")
        p2char = input("Choose a character for player two: ")
        print()
        if p1 == p2:
            p1 = p1 + "(1)"
            p2 = p2 + "(2)"
        while len(p2char) != 1 or p2char == p1char:
            print("Invalid input! Character must be unique an must be a single digit, try again")
            p2char = input("Choose a character for player two: ")
            print()
    print(mode, file = Details)
    print(p1, file = Details)
    print(p2, file = Details)
    print(p1char, file = Details)
    print(p2char, file = Details)
    Board = open("Files/Board.txt", 'w')
    Board.close()
    XO = open("Files/XO.txt", 'w')
    XO.close()
    turn = True
    count = 0
    Score = open("Files/Score.txt", 'w')
    Score.close()
    cont = False
    p1score = 0
    p2score = 0
    draw = 0
    round = 1
    Score = open("Files/Score.txt", 'w')
    print(p1score, file = Score)
    print(p2score, file = Score)
    print(draw, file = Score)
    print(round, file = Score)
    Score.close()
    XO = open("Files/XO.txt", 'w')
    print(count, file = XO)
    print(turn, file = XO)
    XO.close()
else:
    Details.seek(0)
    mode = Details.readline().strip()
    p1 = Details.readline().strip()
    p2 = Details.readline().strip()
    p1char = Details.readline().strip()
    p2char = Details.readline().strip()
    XO = open("Files/XO.txt", 'r')
    count = int(XO.readline().strip())
    turn = eval(XO.readline().strip())
    XO.close()
    Score = open("Files/Score.txt", 'r')
    p1score = int(Score.readline().strip())
    p2score = int(Score.readline().strip())
    draw = int(Score.readline().strip())
    round = int(Score.readline().strip())
    Score.close()
    cont = True
    rep = True
Details.close()
while repeat == 'Y' or repeat == 'y':
    board = [[" " for i in range(3)] for j in range(3)] # Using a 2D list for the board because it is mutable, ordered, allows duplication, and maps naturally to a 3x3 grid.
    Board = open("Files/Board.txt", 'r')
    Y = Board.read()
    if Y == "":
        print(""" 7 | 8 | 9
———|———|———
 4 | 5 | 6
———|———|———
 1 | 2 | 3
        """)
    else:
        Board.seek(0)
        for i in range(3):
            for j in range(3):
                board[i][j] = Board.readline()[:1]
        printBoard()
        Board.close()
    while not checkWinner(p1char) and not checkWinner(p2char) and count < 9:
        rep = False
        if mode == "1" and turn:
            print("Your turn")
        elif mode == "2" and (round % 2 == 1) == turn:
            print(p1 + "'s turn")
        else:
            print(p2 + "'s turn")
        if mode == "2" or turn:
            valid = False
            while not valid:
                valid = True
                flag = False
                while not flag:
                    flag = True
                    try:
                        loc = int(input("Choose a location: "))
                        print()
                    except:
                        print("Invalid input, try again")
                        flag = False
                if loc in (7, 8, 9):
                    row = 0
                    col = loc - 7
                elif loc in (4, 5, 6):
                    row = 1
                    col = loc - 4
                elif loc in (1, 2, 3):
                    row = 2
                    col = loc - 1
                else:
                    print("Invalid location, try again")
                    valid = False
                if valid == True and board[row][col] != " ":
                    print("Location already occupied, try again")
                    valid = False
            if (mode == "1" and turn) or (mode == "2" and ((round % 2 == 1) == turn)):
                board[row][col] = p1char
            else:
                board[row][col] = p2char
        else:
            print("AI played: ")
            print()
            aiPlay(count)
        turn = not turn
        count = count + 1
        printBoard()
        Board = open("Files/Board.txt", 'w')
        for k in range(3):
            for l in range(3):
                print(board[k][l], file = Board)
        Board.close()
        XO = open("Files/XO.txt", 'w')
        print(count, file = XO)
        print(turn, file = XO)
        XO.close()
    if not rep:
        round = round + 1
        if checkWinner(p1char):
            print(p1 + " won!")
            print()
            p1score = p1score + 1
        elif checkWinner(p2char):
            if mode == "1":
                print("You lost!")
                print()
            else:
                print(p2 + " won!")
                print()
            p2score = p2score + 1
        else:
            print("Draw!")
            print()
            draw = draw + 1
    Score = open("Files/Score.txt", 'w')
    print(p1score, file = Score)
    print(p2score, file = Score)
    print(draw, file = Score)
    print(round, file = Score)
    Score.close()
    print("Score:")
    if mode == "1":
        print("Wins: " + str(p1score))
        print("Losses: " + str(p2score))
    else:
        print(p1 + ": " + str(p1score))
        print(p2 + ": " + str(p2score))
    print("Draws: " + str(draw))
    print()
    repeat = input("Do you want to play again? (Y/N): ")
    print()
    while repeat != 'Y' and repeat != 'y' and repeat != 'N' and repeat != 'n':
        print("Invalid answer, try again")
        repeat = input("Do you want to play again? (Y/N): ")
        print()
    cont = False
    turn = True
    count = 0
    XO = open("Files/XO.txt", 'w')
    print(count, file = XO)
    print(turn, file = XO)
    XO.close()
    Board = open("Files/Board.txt", 'w')
    Board.close()
XO = open("Files/XO.txt", 'w')
XO.close()
Score = open("Files/Score.txt", 'w')
Score.close()
Details = open("Files/Details.txt", 'w')
Details.close()