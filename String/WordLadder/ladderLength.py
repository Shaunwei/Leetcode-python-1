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
        dict.add(end)
        queue,letters=[(start, 1)],list(map(chr,xrange(97,123)))
        while queue:
            curr = queue.pop(0)
            currWord, currLen = curr[0], curr[1]
            if currWord == end: return currLen
            for i in xrange(len(start)):
                for j in letters:
                    if currWord[i] != j:
                        nextWord = currWord[:i]+j+currWord[i+1:]
                        if nextWord in dict:
                            queue.append((nextWord,currLen+1))
                            dict.remove(nextWord)
        return 0

if __name__=="__main__":
    start, end = 'hit', 'cog'
    dic = set(["hot","dot","dog","lot","log"])
    print Solution().ladderLength(start, end, dic)

"""
Using Breath First Search. 
A tree breadth first search guarantees the optimal solution.
"""

