class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict = dict({})
        # t_dict = dict({})
        anagram=True
        for ele in s:
            if ele in s_dict:
                s_dict[ele]+=1
            else:
                s_dict[ele]=1
        for ele in t:
            if ele in s_dict:
                s_dict[ele]-=1
            else:
                return False
        for k,v in s_dict.items():
            if v != 0:
                return False
        return True
        