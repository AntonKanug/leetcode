# https://leetcode.com/problems/word-search/submissions/

class Solution:
    board = []
    word = ''
    w,h=0,0

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.w,self.h = len(self.board), len(self.board[0])
        
        for i in range(self.w):
            for j in range(self.h):
                if self.dfs(i,j,0): return True
        return False
    
    # return 
    def dfs(self,i,j,word):
        if word == len(self.word): return True
        if not self.board[i][j] or self.board[i][j] != self.word[word]: return False
        
        temp = str(self.board[i][j])
        self.board[i][j] = 0
        
        for x,y in [[0,1],[1,0],[0,-1],[-1,0]]:
            x1,y1 = x+i,y+j
            if not(0<=x1<self.w and 0<=y1<self.h): continue
            if self.dfs(x1,y1,word+1): return True
            
        self.board[i][j] = temp
            
        return False or word+1 == len(self.word)
    