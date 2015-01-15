#!/usr/bin/python

"""
Compare Version Numbers 

Compare two version numbers version1 and version1.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and 
the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth 
second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 13.37
"""

class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        if not version1 or not version2: return 0
        stra, strb = version1.split('.'), version2.split('.')
        i, lena, lenb = 0, len(stra), len(strb)
        while i < lena or i < lenb:
            s1 = int(stra[i]) if i<lena else 0
            s2 = int(strb[i]) if i<lenb else 0
            if s1 > s2: return 1
            elif s1 < s2: return -1
            else: i += 1
        return 0

if __name__=="__main__":
    a = "1.11.1"
    b = "1.2.1"
    print Solution().compareVersion(a,b)

