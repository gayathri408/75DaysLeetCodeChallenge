class Solution(object):
    def isAnagram(self, s, t):
        m=len(s)
        n=len(t)
        if len(s)!=len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False

        