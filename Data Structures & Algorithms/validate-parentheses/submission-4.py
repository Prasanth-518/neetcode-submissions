class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        validator=[]
        for ele in s:
            if ele == '(' or ele == '{' or ele == '[':
                validator.append(ele)
            elif len(validator) == 0:
                return False
            elif ele == ")" and validator.pop() != "(" :
                return False
            elif ele == "}" and validator.pop() != "{" :
                return False
            elif ele == "]" and validator.pop() != "[" :
                return False
        if len(validator) == 0:
            return True
        else:
            return False