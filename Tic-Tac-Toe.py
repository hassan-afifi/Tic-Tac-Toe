def PrintBoard():
    for i in range(2):
        for j in range(2):
            print(board[i][j], end="|")
        print(board[i][2], end="")
        print()
        print("———|———|———")
    for j in range(2):
        print(board[2][j], end="|")
    print(board[2][2])
def CheckWinner(ch):
    if board[0][0] == ch and board[0][1] == ch and board[0][2] == ch:
        return True
    elif board[1][0] == ch and board[1][1] == ch and board[1][2] == ch:
        return True
    elif board[2][0] == ch and board[2][1] == ch and board[2][2] == ch:
        return True
    elif board[0][0] == ch and board[1][0] == ch and board[2][0] == ch:
        return True
    elif board[0][1] == ch and board[1][1] == ch and board[2][1] == ch:
        return True
    elif board[0][2] == ch and board[1][2] == ch and board[2][2] == ch:
        return True
    elif board[0][0] == ch and board[1][1] == ch and board[2][2] == ch:
        return True
    elif board[0][2] == ch and board[1][1] == ch and board[2][0] == ch:
        return True
    else:
        return False
repeat = 'Y'
Details = open("Files/Details.txt", 'r')
X = Details.read()
if X != "":
    print("1. New Game")
    print("2. Continue Game")
    Game = input()
    while Game != "1" and Game != "2":
        print("Invalid input, try again")
        print("1. New Game")
        print("2. Continue Game")
        Game = input()
if X == "" or Game == "1":
    Details = open("Files/Details.txt", 'w')
    p1 = input("Enter the name of player one: ")
    p1char = input("Choose a character for player one: ")
    while len(p1char) != 1:
        print("Invalid input! Character must be a single digit, try again")
        p1char = input("Choose a character for player one: ")
    p2 = input("Enter the name of player two: ")
    p2char = input("Choose a character for player two: ")
    if p1 == p2:
        p1 = p1 + "(1)"
        p2 = p2 + "(2)"
    while len(p2char) != 1 or p2char == p1char:
        print("Invalid input! Character must be unique an must be a single digit, try again")
        p2char = input("Choose a character for player two: ")
    print(p1, file = Details)
    print(p2, file = Details)
    print(p1char, file = Details)
    print(p2char, file = Details)
    Board = open("Files/Board.txt", 'w')
    Board.close()
    XO = open("Files/XO.txt", 'w')
    XO.close()
    turn = 1
    count = 0
    Score = open("Files/Score.txt", 'w')
    Score.close()
    cont = False
    p1score = 0
    p2score = 0
    draw = 0
    game = 1
    Score = open("Files/Score.txt", 'w')
    print(p2score, file = Score)
    print(p2score, file = Score)
    print(draw, file = Score)
    print(game, file = Score)
    Score.close()
    XO = open("Files/XO.txt", 'w')
    print(0, file = XO)
    print(1, file = XO)
    XO.close()
else:
    Details.seek(0)
    p1 = Details.readline()
    p1 = p1.strip()
    p2 = Details.readline()
    p2 = p2.strip()
    p1char = Details.readline()
    p1char = p1char.strip()
    p2char = Details.readline()
    p2char = p2char.strip()
    XO = open("Files/XO.txt", 'r')
    count = XO.readline()
    count = int(count.strip())
    turn = XO.readline()
    turn = int(turn.strip())
    XO.close()
    Score = open("Files/Score.txt", 'r')
    p1score = Score.readline()
    p1score = int(p1score.strip())
    p2score = Score.readline()
    p2score = int(p2score.strip())
    draw = Score.readline()
    draw = int(draw.strip())
    game = Score.readline()
    game = int(game.strip())
    Score.close()
    cont = True
    rep = True
Details.close()
while repeat == 'Y' or repeat == 'y':
    board = [["   " for i in range(3)] for j in range(3)]
    Board = open("Files/Board.txt", 'r')
    Y = Board.read()
    if Y == "":
        print("""
 7 | 8 | 9
———|———|———
 4 | 5 | 6
———|———|———
 1 | 2 | 3
        """)
    else:
        Board.seek(0)
        for i in range(3):
            for j in range(3):
                board[i][j] = Board.readline()[:3]
        PrintBoard()
        Board.close()
    while CheckWinner(" "+p1char+" ") == False and CheckWinner(" "+p2char+" ") == False and count < 9:
        rep = False
        if turn == 1:
            if game % 2 == 1:
                print(p1, "'s turn", sep="")
            else:
                print(p2, "'s turn", sep="")
        elif turn == 2:
            if game % 2 == 1:
                print(p2, "'s turn", sep="")
            else:
                print(p1, "'s turn", sep="")
        valid = False
        while not valid:
            valid = True
            flag = False
            while not flag:
                flag = True
                try:
                    try:
                        loc = int(eval(input("Choose a location: ")))
                    except SyntaxError:
                        print("Invalid input, try again")
                        flag = False
                except NameError:
                    print("Invalid input, try again")
                    flag = False
            if 6 < loc < 10:
                row = 0
                col = loc - 7
            elif 3 < loc < 7:
                row = 1
                col = loc - 4
            elif 0 < loc < 4:
                row = 2
                col = loc - 1
            else:
                print("Invalid location, try again")
                valid = False
            if valid == True and board[row][col] != "   ":
                print("Location already occupied, try again")
                valid = False
        if turn == 1:
            if game % 2 == 1:
                board[row][col] = " "+p1char+" "
                turn = 2
            else:
                board[row][col] = " "+p2char+" "
                turn = 2
        else:
            if game % 2 ==1:
                board[row][col] = " "+p2char+" "
                turn = 1
            else:
                board[row][col] = " "+p1char+" "
                turn = 1
        count = count + 1
        PrintBoard()
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
        game = game + 1
        if CheckWinner(" "+p1char+" "):
            print(p1, "won!")
            p1score = p1score + 1
        elif CheckWinner(" "+p2char+" "):
            print(p2, "won!")
            p2score = p2score + 1
        else:
            print("Draw!")
            draw = draw + 1
    Score = open("Files/Score.txt", 'w')
    print(p1score, file=Score)
    print(p2score, file=Score)
    print(draw, file=Score)
    print(game, file=Score)
    Score.close()
    print(p1, ": ", p1score, sep="")
    print(p2, ": ", p2score, sep="")
    print("Draw: ", draw, sep="")
    print("Do you want to play again? (Y/N)")
    repeat = input()
    while repeat != 'Y' and repeat != 'y' and repeat != 'N' and repeat != 'n':
        print("Invalid answer, try again")
        print("Do you want to play again? (Y/N)")
        repeat = input()
    cont = False
    turn = 1
    count = 0
    Board = open("Files/Board.txt", 'w')
    Board.close()
XO = open("Files/XO.txt", 'w')
XO.close()
Score = open("Files/Score.txt", 'w')
Score.close()
Details = open("Files/Details.txt", 'w')
Details.close()
