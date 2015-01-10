#!/usr/bin/python

# Valid Palindrome

# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# For example,
# "A man, a plan, a canal: Panama" is a palindrome.
# "race a car" is not a palindrome.

# Note:
# Have you consider that the string might be empty? This is a good question to ask during an interview.

# For the purpose of this problem, we define empty string as valid palindrome. 


class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        strarr = []
        for c in s.lower():
            if '0' <= c <= '9' or 'a' <= c <= 'z':
                strarr.append(c)
        return strarr == strarr[::-1]

if __name__=="__main__":
    string1 = "A man, a plan, a canal: Panama"
    string2 = "race a car"
    print "\"%s\""%string1
    print Solution().isPalindrome(string1)
    print "\"%s\""%string2
    print Solution().isPalindrome(string2)
