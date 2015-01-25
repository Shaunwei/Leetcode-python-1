#!/usr/bin/python

"""
Text Justification 

Given an array of words and a length L, format the text such that each line 
has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words 
as you can in each line. Pad extra spaces ' ' when necessary so that each line 
has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, 
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is 
inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.

Corner Cases:
A line other than the last line might contain only one word. What should you do in this case?
In this case, that line should be left-justified.
"""


class Solution:
    # @param words, a list of strings
    # @param L, an integer
    # @return a list of strings
    def fullJustify(self, words, L):
        text, i = [], 0
        while i < len(words):
            start, sumwords = i, 0
            while i<len(words) and sumwords+len(words[i])<=L:
                sumwords += len(words[i]) + 1 # word plus space 
                i += 1
            end = i - 1    
            intervalCount = end - start   
            avgSp = leftSp = 0   
            if intervalCount >0:   
                avgSp = (L-sumwords + intervalCount+1) / intervalCount   
                leftSp = (L-sumwords + intervalCount+1) % intervalCount   
            line = ''      
            for j in range(start,end):
                line += words[j]   
                if i == len(words): # the last line  
                    line += ' '
                else:  
                    line += ''.join(' ' for i in xrange(avgSp)); #average space  
                    if leftSp > 0: # the extra space  
                        line += ' '   
                        leftSp -= 1 
            line += words[end] ; print len(line)  
            if len(line) < L:   
                line += ''.join(' ' for i in xrange(L-len(line)))   
            text.append(line)     
        return text   

if __name__=="__main__":
    words = [''] #["This", "is", "an", "example", "of", "text", "justification."]
    L = 2 #16
    print Solution().fullJustify(words,L)
