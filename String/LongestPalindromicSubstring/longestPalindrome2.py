#!/usr/bin/python

"""
Longest Palindromic Substring

Given a string S, find the longest palindromic substring in S. 
You may assume that the maximum length of S is 1000, and there 
exists one unique longest palindromic substring.
"""



class Solution:
    # @return a string
    def longestPalindrome(self, s):
        slen = len(s)
        subP = [[False for i in xrange(slen)] for j in xrange(slen)]
        maxlen = start = end = 0
        for j in xrange(slen):
            for i in xrange(j):
                subP[i][j] = s[i]==s[j] and (j==i+1 or subP[i+1][j-1]) 
                if subP[i][j] and maxlen<j-i+1:
                    maxlen, start, end = j-i+1, i, j
            subP[j][j] = True
        return s[start:end+1]
        
if __name__=="__main__":
    #s = 'abccb'
    s1="nypdmqqgauepeyfvwcdpbmmaxfwxmmtswfuwldtvqcisywalfnvovuordczxlyzqmslxil\
    pnenbuwbcpebneovitwkkswsijajnkwkfbxnulmwotgrmpklntfyjavccbrgwqynryeoswmhsq\
    zcwnudkuvfkikjxjkjpghsytjfkpvkjpvblamdeegeohospporbtorkbuggbawgodhxpscfksj\
    birxvjyjapwwushmnqsxktnslvonlwvuseinrmwvfqjgzpkwcqfzfdbbmcngmsoeegudwjvldq\
    maomwbqvijesnpxiqvtfeiqebrfjhtvjdwkopyfzaslewdjnkmalvfinbuouwcgnfecjtdzwyc\
    xrynxepbcsroyzrsgiiuaszvatwyuxinwhni"
    s2="civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedca\
    nlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaport\
    ionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnatio\
    nmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersenseweca\
    nnotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivingandd\
    eadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTghew\
    orldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhatth\
    eydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhicht\
    heywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedto\
    thegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevoti\
    ontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyre\
    solvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanew\
    birthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotper\
    ishfromtheearth"
    print Solution().longestPalindrome(s1)
    print Solution().longestPalindrome(s2)

"""
This is a DP problem. According to http://leetcode.com/2011/11/longest-palindromic-substring-part-i.html
table[i][j] saves if the string start from i ends at j is the Palindromic string.

Initial state:
table[i][i] =  true.
table[i][i+1] = (s[i]==s[i+1]);

State Change:
if s[i]==s[j], table[i][j]=table[i+1][j-1];

More idea detail:
define a relation,
P[i,j] = string area [i,j] whether is palindrome.

look at an example: S="abccb",
  S   = a  b  c  c  b
Index = 0  1  2  3  4

P[0,0] = true  //each char is a palindrome
P[0,1] = S[0]==S[1],   P[1,1] = true 
P[0,2] = S[0]==S[2] && P[1,1], P[1,2] = S[1]==S[2] , P[2,2] = true
P[0,3] = S[0]==S[3] && P[1,2], P[1,3] = S[1]==S[3] && P[2,2] ,P[2,3]= S[2]==S[3], P[3,3] = true       
...
so we can find the rule as follow:

P[i,j] = true  if i == j
       = S[i]==S[j]   if j == i+1
       = S[i]==S[j] && P[i+1][j-1]  if j > i+1

This version is TLE(Time Limit Exceeded)

Manacher’s algorithm:
http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
"""

