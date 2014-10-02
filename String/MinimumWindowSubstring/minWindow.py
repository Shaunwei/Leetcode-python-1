#!/usr/bin/python

# Minimum Window Substring 

#Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

#For example,
#S = "ADOBECODEBANC"
#T = "ABC"
#Minimum window is "BANC".

#Note:
#If there is no such window in S that covers all characters in T, return the emtpy string "".

#If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

class Solution:
    # @return a string
    def minWindow(self, S, T):
        if len(S) == 0: return ''
        if len(S) < len(T): return ''
        appearCount = [0 for i in xrange(256)]
        expectCount = [0 for i in xrange(256)]
        for i in xrange(len(T)):
            expectCount[ord(T[i])] += 1
        minV, minStart = 10**10, 0
        winStart = appeared = 0
        for winEnd in xrange(len(S)):
            # this char is a part of T
            if expectCount[ord(S[winEnd])] > 0:
                appearCount[ord(S[winEnd])] += 1
                if appearCount[ord(S[winEnd])] <= expectCount[ord(S[winEnd])]:
                    appeared += 1
            if appeared == len(T):
                while appearCount[ord(S[winStart])] > expectCount[ord(S[winStart])] or expectCount[ord(S[winStart])] == 0:
                    appearCount[ord(S[winStart])] -= 1
                    winStart += 1
                if minV > winEnd - winStart + 1:
                    minV = winEnd - winStart + 1
                    minStart = winStart
        if minV == 10**10: return ''
        return S[minStart:minStart+minV]

if __name__=="__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    print Solution().minWindow(S,T)

'''
The idea is like this:
   We have two pointers, p and q.  S[p:q] stores the string covers all the chars in T. We want minimum p:q.
   Start from the whole S, p=0, q=S.size()-1,  if it cannot cover T, return "";
   Fix p, try to move q close to p, but keep the requirement S[p:q] covers T.
   Find the shortest p:q, here exactly is 1:q, where S[1:q] covers T.
   Move p and q dynamically:
        if  S[p] is irrelevant char, p++;
        if  S[p] is char in T, must move q to left until find S[q]==S[p] to keep the requirement, or q is last.
            When move q to left, if S[q] is in T, store the S[q] occurrence.
   Every move, compare the length p:q store the minimum length and position.
'''
