#!/usr/bin/python

'''
Surrounded Regions  

Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
'''

class Solution:
    # @param board, a 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        if not board: return board
        row, col, queue = len(board), len(board[0]), []
        visited = [[False for j in xrange(col)] for i in xrange(row)]
        for i in xrange(col):
            if board[0][i] == 'O': queue.append((0,i))
            if board[row-1][i] == 'O': queue.append((row-1,i))
        for i in xrange(row):
            if board[i][0] == 'O': queue.append((i,0))
            if board[i][col-1] == 'O': queue.append((i,col-1))
        while queue:
            idO = queue.pop(0)
            board[idO[0]][idO[1]] = '$'
            visited[idO[0]][idO[1]] = True                          #up check
            if idO[0]-1>=0 and board[idO[0]-1][idO[1]]=='O' and not visited[idO[0]-1][idO[1]]:
                queue.append((idO[0]-1,idO[1]))                     #down check
            if idO[0]+1<row and board[idO[0]+1] [idO[1]]=='O' and not visited[idO[0]+1][idO[1]]:
                queue.append((idO[0]+1,idO[1]))                     #left check
            if idO[1]-1>=0 and board[idO[0]][idO[1]-1]=='O' and not visited[idO[0]][idO[1]-1]: 
                queue.append((idO[0],idO[1]-1))                     #right check
            if idO[1]+1<col and board[idO[0]][idO[1]+1]=='O' and not visited[idO[0]][idO[1]+1]: 
                queue.append((idO[0],idO[1]+1))
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == 'O': board[i][j] = 'X'
                if board[i][j] == '$': board[i][j] = 'O'

if __name__=='__main__':
    #A = [['X','X','X','X'],['X','O','O','X'],['X','X','O','X'],['X','O','X','X']]
    A = [['X','O','X','O','X','O'],['O','X','O','X','O','X'],['X','O','X','O','X','O'],['O','X','O','X','O','X']]
    Solution().solve(A)
    print A
   
'''
Search is a way to solve this problem!
If 'O' in the four sides of baord, they won't be surround by 'X'; so we can start from those 'O', and using BFS to get all the conjoint 'O', then repalce then to '$'. After that, just repalce all rest 'O' to 'X', then replace all '$' back to 'O'. 
'''

