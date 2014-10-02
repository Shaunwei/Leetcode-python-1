#!/usr/bin/python

# Word Break II 

# Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

# Return all such possible sentences.

# For example, given
# s = "catsanddog",
# dict = ["cat", "cats", "and", "sand", "dog"].

# A solution is ["cats and dog", "cat sand dog"].  

# Very pythonic version solution
# from __future__ import print_function
import functools
 
def memoize(obj):
    cache = obj.cache = {}
 
    @functools.wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return memoizer
 
 
class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
 
        # lazy way for the cache decorator
        @memoize
        def _wordBreak(s):
            # print(s)
            results = []
            for word in dict:
                if s == word:
                    results.append(word)
                elif s.startswith(word):
                    # print('got', word)
                    for result in _wordBreak(s[len(word):]):
                        results.append(word+' '+result)
 
            return results
 
        return _wordBreak(s)
 
 
if __name__ == '__main__':
    s = "catsanddog"
    dict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, dict))
 
    s = 'aaaaaaa'
    dict = ["aaaa", "aaa"]
    print(Solution().wordBreak(s, dict))
    s='aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    dict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    print(Solution().wordBreak(s, dict))
