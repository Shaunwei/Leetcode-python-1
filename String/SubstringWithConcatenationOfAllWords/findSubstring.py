#!/usr/bin/python

"""
Substring with Concatenation of All Words

You are given a string, S, and a list of words, L, that are all of the same length. Find all starting indices of substring(s) in S that is a concatenation of each word in L exactly once and without any intervening characters.

For example, given:
S: "barfoothefoobarman"
L: ["foo", "bar"]

You should return the indices: [0,9].
(order does not matter).
"""

class Solution:
    # @param S, a string
    # @param L, a list of string
    # @return a list of integer
    def findSubstring(self, S, L):
        slen, llen, wlen = len(S), len(L), len(L[0])
        result = []
        for i in xrange(slen-wlen*llen+1):
            slist = [S[j:j+wlen] for j in xrange(i,i+wlen*llen,wlen)]
            found = True;
            for word in L:
                if word in slist: slist.remove(word)
                else: found = False; break
            if found: result.append(i)
        return result      

if __name__=="__main__":
    #S,L = 'barfoothefoobarman',["foo", "bar"]
    S="lingmindraboofooowingdingbarrwingmonkeypoundcake"
    L=["fooo","barr","wing","ding","wing"]
    print Solution().findSubstring(S,L)
 
"""
Say in L there are m strings with length n. 
What string is required to match in S?     A length of m*n string start with each position in S.
What is a match?  In the m*n long string, every string in L appear only once.

So the algorithm is:
Scan every m*n long string start from each position in S, see if all the strings in L have been appeared only once using Map data structure. If so, store the starting position.
"""

