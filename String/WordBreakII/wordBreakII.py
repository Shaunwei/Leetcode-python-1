#!/usr/bin/python

# Word Break II 

# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"]. ".  

class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        """
        We solve this problem using DP
        Define a boolean array A[0..n-1], where
        A[i] = True, means s[i..n-1] can be segmented into words
        ------------------------------------
        The recursive formula is:
        A[i] = True, if there exists j>i (s[i..n-1] = s[i..j-1] + s[j..n-1])
                   such that s[i..j-1] is a word and A[j] = True
        or A[i] = True, if s[i..n-1] is a word
        ------------------------------------
        We fill A-table from i=n-1 to n
        """
        n = len(s)
        A = [False for i in range(n)]
        i = n-1
        while i >= 0:
            if s[i:n] in dict:
                A[i] = True
            else:
                for j in xrange(i+1, n):
                    if A[j] and s[i:j] in dict:
                        A[i] = True
                        break
            i -= 1
        return A[0]

    # the same DP method but in reverse way
    def wordBreak2(self, s, dict):
        segment = [True]
        for i in range(len(s)):
            segment.append(False)
            for j in range(i,-1,-1):
                if segment[j] and s[j:i+1] in dict:
                    segment[i+1] = True
                    break 
        return segment[len(s)]

if __name__=="__main__":
    string = "a"#"leetcode"
    dicts = []#["leet","code"] 
    sol = Solution()
    print sol.wordBreak(string,dicts)
