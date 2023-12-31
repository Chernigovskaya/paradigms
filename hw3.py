board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
game_is_on = True


def draw_bord():
    for i in range(3):
        print(board[i * 3], board[1 + i * 3], board[2 + i * 3])


def game_step(index, char):
    if index > 9 or index < 1 or board[index - 1] in ('X', 'O'):
        return False
    board[index - 1] = char
    return True


def wining():
    win = False

    win_combination = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8),  (0, 4, 8), (2, 4, 6)
    )

    for pos in win_combination:
        if board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X', 'O'):
            win = board[pos[0]]

    return win


def start_game():
    current_player = 'X'
    step = 1
    draw_bord()
    while step <= 9 and wining() == False:
        index = input(f'Ходит игрок {current_player}. Введите номер ячейки: ')
        if index == '0':
            break
        if game_step(int(index), current_player):
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'
            draw_bord()
            step += 1
        else:
            print('Введите другую ячейку')
    print(f'Выиграл игрок: {wining()}')


print('Для выхода нажмите 0')
start_game()
