#!/usr/bin/python

"""
Word Ladder II

Given two words (start and end), and a dictionary, find all shortest 
transformation sequence(s) from start to end, such that:

Only one letter can be changed at a time
Each intermediate word must exist in the dictionary
For example,

Given:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
All words have the same length.
All words contain only lowercase alphabetic characters.
"""

class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        #self.mp, self.res, self.path = {}, [], [] 
        self.letters = list(map(chr,xrange(97,123)))
        self.wordlen = len(start) ; dict.add(end)
        curr, next, mp = set([start]), set(), {}
        while curr:
            self.subDict(curr,next,dict,mp)
            if end in next: return self.buildpath(mp,start,end) #['hey']#
            for w in next: dict.remove(w)
            curr = set(next)
            next.clear()
        return []

    def subDict(self, curr, next, dict, mp): # bfs
        for word in curr:
            for i in xrange(self.wordlen):
                #s = word
                for j in self.letters:
                    s = word[:i]+j+word[i+1:]
                    if s in dict:
                        next.add(s)
                        if s not in mp: mp[s]=[]
                        mp[s].append(word)

    def dfs(self, res, path, mp, start, s):
        path.append(s)
        if start == s: 
            path.reverse()
            res.append(list(path))
            path.reverse()
        else:
            for key in mp:
                self.dfs(res,path,mp,start,key)
        path.pop()

    def buildpath(self, mp, start, end):
        res, path = [], []
        self.dfs(res,path,mp,start,end)
        return res

if __name__=="__main__":
    start, end = "hit", "cog"
    dic = set(["hot","dot","dog","lot","log"])
    print Solution().findLadders(start, end, dic)

"""
Using Breath First Search. 
For each words in the BFS queue, we still need to use the previous way to 
generate the valid words in the dicts (from 1st to last, change every char 
from 'a' to 'z' ).
Duplicates is permitted within a level. e.g.,
hem -> hex -> tex -> ted
hem->  tem -> tex -> ted,  are all valid paths.
Draw this into a tree structure:
        hem
       /   \
     hex    tem
      |      |
     tex    tex
      |      |
     ted    ted
A solution is to erase all the words in the previous level, 
instead of erasing words for each word in the level.
Use a map to store and retrieve the paths, stores all the previous strings 
for current string. Retrieval of the path will need recursion (DFS).
"""

