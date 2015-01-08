#!/usr/bin/python

"""
Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

For example,
Given board =
[
  ["ABCE"],
  ["SFCS"],
  ["ADEE"]
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if board[i][j] == word[0]:
                    if self.dfs(board, i, j, word[1:]): return True
        return False
         
    def dfs(self, board, r, c, word):
        if len(word) == 0: return True
        if r > 0 and board[r-1][c] == word[0]: # Up
            ch, board[r][c] = board[r][c], '#'
            if self.dfs(board, r-1, c, word[1:]): return True
            board[r][c] = ch
        if r < len(board)-1 and board[r+1][c] == word[0]: # Down
            ch, board[r][c] = board[r][c], '#'
            if self.dfs(board, r+1, c, word[1:]): return True
            board[r][c] = ch
        if c > 0 and board[r][c-1] == word[0]: # Left
            ch, board[r][c] = board[r][c], '#'
            if self.dfs(board, r, c-1, word[1:]): return True
            board[r][c] = ch    
        if c < len(board[0])-1 and board[r][c+1] == word[0]: # Right
            ch, board[r][c] = board[r][c], '#'
            if self.dfs(board, r, c+1, word[1:]): return True
            board[r][c] = ch    
        return False

if __name__=="__main__":
    board = [['A','B','C','E'],['S','F','C','S'],['A','D','E','E']]
    word = 'ABCB'
    print Solution().exist(board, word)

"""
Use DFS. Don't make a new board or other large 
variables to record state, or it's easy to TLE.
"""

