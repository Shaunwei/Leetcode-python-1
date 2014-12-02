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
        def buildpath(path, word):
            if len(prevMap[word])==0:
                path.append(word); currPath=path[:]
                currPath.reverse(); result.append(currPath)
                path.pop();
                return
            path.append(word)
            for iter in prevMap[word]:
                buildpath(path, iter)
            path.pop()
        
        result=[]
        prevMap={}
        length=len(start)
        dict.add(start)
        for i in dict:
            prevMap[i]=[]
        candidates=[set(),set()]; current=0; previous=1
        candidates[current].add(start)
        while True:
            current, previous=previous, current
            for i in candidates[previous]: dict.remove(i)
            candidates[current].clear()
            for word in candidates[previous]:
                for i in range(length):
                    part1=word[:i]; part2=word[i+1:]
                    for j in 'abcdefghijklmnopqrstuvwxyz':
                        if word[i]!=j:
                            nextword=part1+j+part2
                            if nextword in dict:
                                prevMap[nextword].append(word)
                                candidates[current].add(nextword)
            if len(candidates[current])==0: return result
            if end in candidates[current]: break
        buildpath([], end)
        return result

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