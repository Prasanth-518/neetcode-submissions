class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        duplicate = False
        for ele in nums:
            if not(ele in num_set):
                num_set.add(ele)
            else:
                duplicate = True
                break
        return duplicate