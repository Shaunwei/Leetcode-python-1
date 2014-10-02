#!/usr/bin/python

# Simplify Path

#Given an absolute path for a file (Unix-style), simplify it.

#For example,
#path = "/home/", => "/home"
#path = "/a/./b/../../c/", => "/c"
#click to show corner cases.

#Corner Cases:
#Did you consider the case where path = "/../"?
#In this case, you should return "/".
#Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
#In this case, you should ignore redundant slashes and return "/home/foo".

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        stack = ['/']
        for i in path.strip('/').split('/'):
            if i=='.' or i=='': continue
            if i == '..':
                if len(stack) > 1: stack.pop()
            else:
                stack.append(i+'/')
        return ''.join(stack).rstrip('/') if len(stack) > 1 else ''.join(stack)

if __name__=="__main__":
    path1 = '/home/'
    path2 = '/a/./b/../../c/'
    path3 = '/../'
    path4 = '/home//foo/'
    print Solution().simplifyPath(path4)

'''
(1) Use a stack to store the path.
(2) Use a int flag to store the '/' pair
(3) First remove the "//" in the path.
(4) meets ".", do nothing, meets ".." pop stack if not empty, other strings push into stack.
'''
