#!/usr/bin/python
"""
Word Break II 

Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"]. ".  
"""
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        n = len(s)
        A = [None] * n
        i = n-1
        while i >= 0:  # work break part 
            if s[i:n] in dict:
                A[i] = [n]  
            else:
                A[i] = []
            for j in xrange(i+1, n): 
                if A[j] and s[i:j] in dict:
                    A[i].append(j)
            i -= 1
        res, path_list = [], [[0]]  
        while path_list:
            new_list = []
            for path in path_list:
                if path[-1] == n: 
                    temp = [s[path[i]:path[i+1]] for i in xrange(len(path)-1)]
                    res.append(" ".join(temp))
                else:  
                    for j in A[path[-1]]:
                        new_list.append(path+[j])
            path_list = new_list
        return res

if __name__=="__main__":
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, dict))

"""
This problem is some extension of the word break problem, so the solution is 
based on the discussion in Word Break.

We also use DP to solve the problem. In this solution, A[i] is not a boolean any more, 
but a list of all possible value of j>i such that s[i..j-1] is a word and A[j]==True. 
The pseudo-code for computing the array is similar to that in Word Break with a few modifications

WORD-BREAK(string s, dictionary d):
  let A[0..n-1] be a new array
  for i = n-1 to 0
    if A[i..n-1] is a word in d
      A[i] = [n]
    else
      A[i] = [] // Empty set
      for j = i+1 to n-1
        if A[j] == True and s[i..j-1] is a word in d
            insert j to A[i]
  return A
The next step is to print all possible sentences with breaks. In another word, we need to 
find all valid sequences of breaks. Before doing this, lets review the meaning of A[i]. 
A[i] dentoes the next valid break after setting a break before s[i]. That is, we cannot 
set a break after we setting a break before s[i] if A[i] is []; otherwise A[i] is a list 
of all valid breaks after setting break before s[i].

A valid sequence of breaks should be in the form of (0, b1, ..., bm, n). We can solve all 
possible sequences by using BFS which starts from A[0] which contains valid values of the 
first break and find all valid paths (a path ends with "n") and print the sentences with the breaks of the path.

The path is at most of length |s|=n, and for each break there are at most |d| possible choices, 
so the BFS could terminate in O(|d|^|n|) time. 
"""