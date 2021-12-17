# Interfaz grafica
def display_board(board):
    """
    Función que muestra La interfaz grafica
    del tablero de triki
    """
    blankBoard="""
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
    """
    player1 = input("Escoja con cual va a jugar (Recuerde ingresar Mayús) =  'X' or 'O' ")
    while True:
        if player1.upper() == 'X':
            player2='O'
            print("Has Elegido =" + player1 + ". El Jugador 2 Jugará con =" + player2)
            return player1.upper(),player2
        elif player1.upper() == 'O':
            player2='X'
            print("Has Elegido =" + player1 + ". El Jugador 2 Jugará con =" + player2)
            return player1.upper(),player2
        else:
            player1 = input("Escoja con cual va a jugar (Recuerde ingresar Mayús) =  'X' or 'O' ")

def place_marker(board, marker, position):
    board[position] = marker
    return board
