#!/usr/bin/python

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        arr_s=list(s)
        arr_t=list(t)
        dict_s=dict()
        dict_t=dict()

        for i in range(len(arr_s)):
            if arr_s[i] in dict_s:
                dict_s[arr_s[i]]+=1
            else:
                dict_s[arr_s[i]]=1

        for i in range(len(arr_t)):
            if arr_t[i] in dict_t:
                dict_t[arr_t[i]]+=1
            else:
                dict_t[arr_t[i]]=1


        if dict_s == dict_t: 
            return True
        else:
            return False


s="rat"
t="car"
a=Solution()
print a.isAnagram(s,t)
