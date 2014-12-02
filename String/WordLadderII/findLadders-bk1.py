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
    def findLadders(self, start, end, dic):
        stack, cur, found = [{start:[]}], {}, False
        while stack and not found:
            for word in stack[-1]:
                for i in xrange(len(word)):
                    s = word
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        s = s[:i]+j+s[i+1:]
                        if s == end:
                            found = True
                            if s not in cur: cur[s]=[]
                            cur[s].append(word)
                        elif s in dic:
                            if s not in cur: cur[s]=[]
                            cur[s].append(word)
            stack.append(dict(cur))
            for w in cur: 
                if w in dic: dic.remove(w)
            cur = {}
        print stack
        res, tmp = [], []
        if found: self.dfs(res,tmp,stack,len(stack)-1,end)
        return res

    def dfs(self, res, tmp, stack, l, cur):
        if l == -1:
            t = tmp; t.reverse(); res.append(t)
        else:
            tmp.append(cur)
            for i in xrange(len(stack[l][cur])):
                self.dfs(res,tmp,stack,l-1,stack[l][cur][i])
            tmp.pop()

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