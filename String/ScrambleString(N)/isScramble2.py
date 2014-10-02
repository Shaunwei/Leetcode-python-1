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
        if len(s1): return True
        if s1 == s2: return True
        iss = [False for i in xrange(len(s1))]	
        for leni in xrange(1,len(s1)):
            levelSize = len(s1) - leni + ss1 #size at this level
            levelIndex = leni - 1
            iss[levelIndex] = [False for i in xrange(len(levelSize))]
            for indexS1 in xrange(levelSize):
            	iss[levelIndex][indexS1] = [False for i in xrange(len(levelSize))]
                for is2 in xrange(levelSize):
                    if leni == 1:
                        iss[levelIndex][indexS1][is2] = (s1[indexS1] == s2[is2])
                    else:
                        iss[levelIndex][indexS1][is2] = False
                        for seglen1 in xrange(1,count):
                            seglen2 = leni - seglen1
                            sli1 = seglen1 - 1
                            sli2 = seglen2 - 1
                            if iss[sli1][indexS1][is2] and iss[sli2][indexS1+seglen1][is2+seglen1]:
                                iss[levelIndex][indexS1][is2] = true;
                                break
                            if iss[sli1][indexS1][is2+seglen2] and iss[sli2][indexS1+seglen1][is2]:
                                iss[levelIndex][indexS1][is2] = true;
                                break
                        	
        return iss[len(s1)-1][0][0]
 
        
if __name__=="__main__":
    s1 = "great"
    s2 = "rgtae"#"rgeat" #
    print Solution().isScramble(s1,s2)

"""
Using 3D dynamic programming.
"""

