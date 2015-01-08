#!/usr/bin/python
"""
Restore IP Addresses

Given a string containing only digits, restore it by returning all 
possible valid IP address combinations.

For example:
Given "25525511135",

return ["255.255.11.135", "255.255.111.35"]. (Order does not matter) 
"""
class Solution:
    # @param s, a string
    # @return a list of strings
    def restoreIpAddresses(self, s):
        self.res = []
        self.getIP(s,'',0)
        return self.res

    def getIP(self, s, currIP, currIndex):
        if currIndex == 3:
            if len(s) > 0:
                if str(int(s))==s and int(s)<=255:
                    self.res.append(currIP+s)
            return
        for i in xrange(1,4):
            if len(s)>=i and str(int(s[0:i]))==s[0:i] and int(s[0:i])<=255:
                self.getIP(s[i:],currIP+s[0:i]+'.',currIndex+1)  
        
if __name__=="__main__":
    s = "25525511135"#"459022042"#"0279245587303"
    print Solution().restoreIpAddresses(s)

'''
Using DFS. str(int(s))==s just for get rid of the leading 0, 
because  "0X" or "00X" is not valid.
'''
