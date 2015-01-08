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
        palindrome = s[0]
        for i in range(len(s)):
            # get longest palindrome with center of i
            temp = self.getlongestpalindrome(s, i, i)
            if len(temp) > len(palindrome): palindrome = temp
            # get longest palindrome with center of i, i+1
            temp = self.getlongestpalindrome(s, i, i + 1)
            if len(temp) > len(palindrome): palindrome = temp
        return palindrome
        
    # Given a center, either one letter or two letter, 
    # Find longest palindrome
    def getlongestpalindrome(self, s, l, r):
        while l>= 0 and r<len(s) and s[l]==s[r]: l,r=l-1,r+1
        return s[l+1 : r]
        
if __name__=="__main__":
    #s = 'abccb'
    # s1="nypdmqqgauepeyfvwcdpbmmaxfwxmmtswfuwldtvqcisywalfnvovuordczxlyzqmslxil\
    # pnenbuwbcpebneovitwkkswsijajnkwkfbxnulmwotgrmpklntfyjavccbrgwqynryeoswmhsq\
    # zcwnudkuvfkikjxjkjpghsytjfkpvkjpvblamdeegeohospporbtorkbuggbawgodhxpscfksj\
    # birxvjyjapwwushmnqsxktnslvonlwvuseinrmwvfqjgzpkwcqfzfdbbmcngmsoeegudwjvldq\
    # maomwbqvijesnpxiqvtfeiqebrfjhtvjdwkopyfzaslewdjnkmalvfinbuouwcgnfecjtdzwyc\
    # xrynxepbcsroyzrsgiiuaszvatwyuxinwhni"
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
    print Solution().longestPalindrome(s2)

"""
This is a simple alogritm, get longest palindrome with center of i or i + 1.
Time O(n^2), Space O(1).
Reference: http://www.programcreek.com/2013/12/leetcode-solution-of-longest-palindromic-substring-java/
"""

