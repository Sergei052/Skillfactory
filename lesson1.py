board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
players_1 = "x"
def print_board():
    """Выводит поле в кансоль"""
    print("\n  0  1   2")
    for i, row in enumerate(board):
        print(i," | ".join(row))
        if i<2:
            print("---------")
    print()
def check_win():
    """Возвращает символ победителя (X или O) , если победителя нет возвращант None"""
    #Проверка строк и столбцов
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2] != " ":
            return board[i][0]
        if board[0][i]==board[1][i]==board[2][i] != " ":
            return board[0][i]
    #Проверка диагоналей
    if board[0][0]==board[1][1]==board[2][2] != " ":
        return board[0][0]
    if board[0][2]==board[1][1]==board[2][0] != " ":
        return board[0][2]
    return None
def is_full():
    """Проверяет есть ли ничья"""
    for row in board:
        if " "in row:
            return False
        return True
def make_m(row,col):
    """Делает ход игрок"""
    if board[row][col]==" ":
        board[row][col]= players_1
        return True
    return False
def switch_pl():
    global players_1
    if players_1 == "x":
        players_1 = "o"
    else:
        players_1 = "x"
while True:
    print_board()
    print(f"Делает ход игрок {players_1}")
    while True:
        try:
            row=(int(input("Введите строку, число (0,1,2): ")))
            col=(int(input("Введите столбец, число(0,1,2): ")))
            if row not in range(3) or col not in range(3):
                print("Неверно! Введите число строго от (0,1,2):")
                continue
            if not make_m(row,col):
                print("Клетка занята,выберите другую цифру")
                continue
            break
        except ValueError:
            print("Введите целые числа от (0,1,2)")

    winner = check_win()
    if winner:
        print_board()
        print(f"Поздравляем победителя{winner}")
        break
    if is_full():
        print_board()
        print("Поздравляем у вас ничья!")
        break
switch_pl()



















































