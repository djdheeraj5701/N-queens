import sys
from PIL import Image
sys.stdout = open('output.txt', 'w')


board=[]
count=0
def display_board(board):
    global count
    count+=1
    for i in range(n):
        print(''.join(board[i]))
    print()

    # center placing at 150,150 ->300 450... 1050
    chessboard_img = Image.open('chessboard.jpg')
    queen_img = Image.open('queen.png').resize((100, 100))
    for i in range(n):
        for j in range(n):
            if board[i][j]=='Q':
                chessboard_img.paste(queen_img,(135*j+22,135*i+22))
    chessboard_img.save('output_imgs/'+str(count)+'.png')


# constraints of the CSP in this function
def canplace(i,j,currboard):
    for k in range(n):
        if currboard[i][k]=='Q':
            return False
        if currboard[k][j]=='Q':
            return False
        if 0<=i+k<n and 0<=j+k<n and currboard[i+k][j+k]=='Q':
            return False
        if 0<=i+k<n and 0<=j-k<n and currboard[i+k][j-k]=='Q':
            return False
        if 0<=i-k<n and 0<=j+k<n and currboard[i-k][j+k]=='Q':
            return False
        if 0<=i-k<n and 0<=j-k<n and currboard[i-k][j-k]=='Q':
            return False
    return True

def generate_chessboard(i,j,q,currboard):
    if j==n:
        # bound to give no solution coz in this row no queen placed
        return
    if i==n:
        if q==n:  # although redundant to check but still performed
            display_board(currboard)
        return
    # branch at the most 2 times
    if canplace(i,j,currboard):
        currboard[i][j]='Q'
        generate_chessboard(i+1,0,q+1,currboard.copy())
        currboard[i][j]='.'
    # kind of backtrack as we explore other option
    generate_chessboard(i, j+1, q, currboard.copy())

n=8
for i in range(n):
    board.append(['.' for i in range(n)])
generate_chessboard(0,0,0,board.copy())
print(count)
