# Interfaz grafica

blankBoard0="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""
print("Tenga en cuenta las posiciones del tablero (1:9)")
print(blankBoard0)

def display_board(board):
    """
    Función que muestra La interfaz grafica
    del tablero de triki
    """
    blankBoard=blankBoard0

    for i in range(1,10):
        if (board[i] == 'O' or board[i] == 'X'):
            blankBoard = blankBoard.replace(str(i), board[i])
        else:
            blankBoard = blankBoard.replace(str(i), ' ')
    print(blankBoard)

# Escoger 'X' 'O' (Son Letras)
def player_input():
    """
    Función que define el jugador 1 o 2 que papel tendran dentro del juego si 'X' ó 'O'
    No es necesario poner Mayús.
    """
    player1 = input("Escoja con cual va a jugar  =  'X' or 'O': ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print("Has Elegido = " + player1 + ". El Player2 juega con = " + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("Has Elegido = " + player1 + ". El Player2 juega con = " + player2)
            return player1.upper(),player2
        else:
            player1 = input("Escoja con cual va a jugar (Recuerde ingresar Mayús) 'X' or 'O': ")

# Una Función que marca según la posición
def place_marker(board, marker, position):
    """
    Según la marca de 'X' ó 'O' da posición al tablero
    """
    board[position] = marker
    return board

# Chequea la posición del espacio
def space_check(board, position):
    "Chequea la posicion del tablero"
    return board[position] == '#'

def full_board_check(board):
    "Chequeo Total de la posicion del tablero"
    return len([x for x in board if x == '#']) == 1

# Función que da las posibilidades de ganar
def win_check(board, mark):
    "Establece los parametros para ganar en el Triki"
    if board[1] == board[2] == board[3] == mark:
        return True
    if board[4] == board[5] == board[6] == mark:
        return True
    if board[7] == board[8] == board[9] == mark:
        return True
    if board[1] == board[4] == board[7] == mark:
        return True
    if board[2] == board[5] == board[8] == mark:
        return True
    if board[3] == board[6] == board[9] == mark:
        return True
    if board[1] == board[5] == board[9] == mark:
        return True
    if board[3] == board[5] == board[7] == mark:
        return True
    return False


def player_choice(board):
    """
    Función para las entradas de los espacios del tablero original
    """
    choice = input("Seleccione un espacio vacío entre el 1 y el 9: ")
    while not space_check(board, int(choice)):
        choice = input("Este espacio no está libre (Escoga otro numero). Por favor, elija entre 1 y 9: ")
    return choice

def replay():
    """
    Función para repetir el juego
    """
    playAgain = input("¿Quieres volver a jugar (y/n) ? ")
    if playAgain.lower() == 'y':
        return True
    if playAgain.lower() == 'n':
        return False

if __name__ == "__main__":
    print('Bienvenido a Triki!')
    i = 1
    # Elige tu bando
    players=player_input()
    # Tablero Vacio init
    board = ['#'] * 10
    while True:
        # Configuración del juego
        game_on=full_board_check(board)
        while not game_on:
            # El jugador puede elegir dónde poner la marca
            position = player_choice(board)
            # ¿Quién juega?
            if i % 2 == 0:
                marker = players[1]
            else:
                marker = players[0]
            # Play!
            place_marker(board, marker, int(position))
            # Chequeo del Tablero
            display_board(board)
            i += 1
            if win_check(board, marker):
                print("You won !")
                break
            game_on=full_board_check(board)
        if not replay():
            break
        else:
            i = 1
            #Escoje tu bando
            players=player_input()
            # Tablero Vacio init
            board = ['#'] * 10
