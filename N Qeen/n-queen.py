import matplotlib.pyplot as plt

def N_Queens(board, queens, success, row):
    Cell = [True] * (queens + 1)
    placeable_cell = [Cell[:] for _ in range(queens + 1)]

    for i in range(1, queens + 1):
        for j in range(1, queens + 1):
            if board[i][j] == 1:
                
                for k in range(1, queens + 1):
                    placeable_cell[i][k] = False
                    placeable_cell[k][j] = False

                diagonal_i, diagonal_j = i, j
                while True:
                    diagonal_i += 1
                    diagonal_j += 1
                    if diagonal_i <= queens and diagonal_j <= queens:
                        placeable_cell[diagonal_i][diagonal_j] = False
                    else:
                        break

                diagonal_i, diagonal_j = i, j
                while True:
                    diagonal_i -= 1
                    diagonal_j -= 1
                    if diagonal_i >= 1 and diagonal_j >= 1:
                        placeable_cell[diagonal_i][diagonal_j] = False
                    else:
                        break

                diagonal_i, diagonal_j = i, j
                while True:
                    diagonal_i += 1
                    diagonal_j -= 1
                    if diagonal_i <= queens and diagonal_j >= 1:
                        placeable_cell[diagonal_i][diagonal_j] = False
                    else:
                        break

                diagonal_i, diagonal_j = i, j
                while True:
                    diagonal_i -= 1
                    diagonal_j += 1
                    if diagonal_i >= 1 and diagonal_j <= queens:
                        placeable_cell[diagonal_i][diagonal_j] = False
                    else:
                        break

    for i in range(1, queens + 1):
        if placeable_cell[row][i]:
            board[row][i] = 1
        else:
            continue

        if row == queens:
            success[0] = True
            break

        N_Queens(board, queens, success, row + 1)

        if not success[0]:
            board[row][i] = 0
        else:
            break

Queens = int(input("Enter number of queens: "))

Cell = [0] * (Queens + 1)
Board = [Cell[:] for _ in range(Queens + 1)]

Success = [False]
N_Queens(Board, Queens, Success, 1)



# for i in range(1, Queens + 1):
#     for j in range(1, Queens + 1):
#         if Board[i][j] == 0:
#             print("+", end=" ")
#         else:
#             print("Q",end=" ")
#     print()



def draw_chess_board(board):
    n = len(board) - 1  # because board is 1-based indexing
    plt.figure(figsize=(n, n))
    
    # Draw the squares
    for i in range(1, n+1):
        for j in range(1, n+1):
            color = 'white' if (i+j)%2==0 else 'gray'
            plt.fill([j-1, j, j, j-1], [n-i, n-i, n-i+1, n-i+1], color=color)
            # Draw a queen if present
            if board[i][j] == 1:
                plt.text(j-0.5, n-i+0.5, '♕', ha='center', va='center', fontsize=30, color='red')
    
    # Hide axes
    plt.xlim(0, n)
    plt.ylim(0, n)
    plt.axis('off')
    plt.show()

draw_chess_board(Board)