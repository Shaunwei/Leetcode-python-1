#!/usr/bin/python

"""
Anagrams 

Given an array of strings, return all groups of strings that are anagrams.

Note: All inputs will be in lower-case.
"""

class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def anagrams(self, strs):
        strdict = {}
        for s in strs:
            key = ''.join(sorted(s))
            strdict[key] = [s] if key not in strdict else strdict[key]+[s]
        anag = []
        for key in strdict:
            if len(strdict[key]) > 1:b[
                anag += strdict[key]
        print strdict
        return anag

if __name__=="__main__":
    s = ['tac','cat','act','dog']
    print Solution().anagrams(s)

