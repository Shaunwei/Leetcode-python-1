#!/usr/bin/python

"""
Word Ladder

Given two words (start and end), and a dictionary, find the length of shortest 
transformation sequence from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return an integer
    def ladderLength(self, start, end, dict):
        if self.valid(start,end): return 2
        self.letters = list(map(chr,xrange(97,123)))
        que,rque,mark,rmark,lev,rlev=[(start,1)],[(end,1)],{},{},1,1
        for st in dict: mark[st], rmark[st] = False, False;
        while que and rque:
            if len(que) < len(rque):
                while que and que[0][1]==lev:
                    ldic = self.subDict(que[0][0],dict)
                    for st in ldic:
                        if mark[st]==False:
                            mark[st] = True
                            if rmark[st]: return que[0][1]+rque[-1][1]
                            que.append((st,lev+1))
                    que.pop(0)
                lev += 1
            else:
                while rque and rque[0][1]==rlev:
                    rdic = self.subDict(rque[0][0],dict)
                    for st in rdic:
                        if rmark[st]==False:
                            rmark[st] = True
                            if mark[st]: return rque[0][1]+que[-1][1]
                            rque.append((st,rlev+1))
                    rque.pop(0)
                rlev += 1
        return 0

    def subDict(self, st, dict):
        res = []
        for i in xrange(len(st)):
            s = st
            for j in self.letters:
                if s[i] != j:
                    s = s[:i]+j+s[i+1:]
                    if s in dict and s not in res:
                        res.append(s)
        return res

    def valid(self, st1, st2):
        flag = False
        for i in xrange(len(st1)):
            if st1[i] != st2[i]:
                if flag == True: return False
                else: flag = True
        return True 

if __name__=="__main__":
    start, end = 'hit', 'cog' #'a','c' # 
    dic = set(["hot","dot","dog","lot","log"])
    #dic = set(['a','b','c'])
    print Solution().ladderLength(start, end, dic)

"""
Double breadth first search.
Search from both direction. Every time, we search one level from 
the start and one level from the end, the stop condition is found 
one node which has been marked by the other direction.

          O (start)   |
      /   |   \       |
     O    O    O      |
    / \  / \  / \     v
    O  O @ O  O  O   ---
    \ /  \ /  \ /     ^
     O    O    O      |
      \   |   /       |
          O (end)     |
"""

