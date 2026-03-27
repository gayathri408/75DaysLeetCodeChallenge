class Solution(object):
    def lengthOfLongestSubstring(self, s):
        n=len(s)
        l=[]
        max_len=0
        for i in range(n):
            if s[i] in l:
                while s[i] in l:
                    l.pop(0)   
            l.append(s[i])
            max_len=max(max_len,len(l))
        return max_len


            