#!/usr/bin/python

# Scramble String

#Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

#Below is one possible representation of s1 = "great":

#    great
#   /    \
#  gr    eat
# / \    /  \
#g   r  e   at
#           / \
#          a   t
#To scramble the string, we may choose any non-leaf node and swap its two children.

#For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

#    rgeat
#   /    \
#  rg    eat
# / \    /  \
#r   g  e   at
#           / \
#          a   t
#We say that "rgeat" is a scrambled string of "great".

#Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

#    rgtae
#   /    \
#  rg    tae
# / \    /  \
#r   g  ta  e
#       / \
#      t   a
#We say that "rgtae" is a scrambled string of "great".

#Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
        if len(s1) != len(s2): return False
        slen = len(s1)
        arr = [0 for i in xrange(26)]	
        for i in xrange(slen):
            arr[ord(s1[i])-ord('a')] += 1 
        for i in xrange(slen):
            arr[ord(s2[i])-ord('a')] -= 1
        for i in xrange(26):
            if arr[i] != 0: return False
        for i in xrange(1,slen):
            result = self.isScramble(s1[0:i],s2[0:i]) and self.isScramble(s1[i:],s2[i:]) 
            result = result or (self.isScramble(s1[0:i],s2[slen-i:]) and self.isScramble(s1[i:],s2[0:slen-i]))	    
            if result==True: return True
        return False

if __name__=="__main__":
    s1 = "great"
    s2 = "rgtae"#"rgeat" #
    print Solution().isScramble(s1,s2)

"""
Using recursive with condition cut out.
The idea is split s1 into s11, s12, so as s2 into s21, s22.
It is true when s21 is the scramble of s11 and s22 is the scramble of s12.
Also it is true when s22 is the scramble of s11 and s21 is the scramble of s12. 
"""

