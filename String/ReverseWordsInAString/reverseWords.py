#!/usr/bin/python
"""
Reverse Words in a String

Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the"
"""
class Solution:

    def reverseWords(self, s):
	return ' '.join(list(reversed(s.split())))

if __name__=="__main__":
    string = "the sky is blue"
    sol = Solution()
    print sol.reverseWords(string)
