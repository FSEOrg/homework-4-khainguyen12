class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        sort 2 string, roi compare 2 string do, khac nhau = False
        2 string len khac nhau -> False
        '''
        if len(s) != len(t):
            return False
        
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        if sorted_s != sorted_t:
            return False
        return True    