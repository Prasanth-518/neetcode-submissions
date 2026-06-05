class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1=dict({})
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict1:
                return [dict1[diff], i]
            elif diff not in dict1:
                dict1[nums[i]] = i
        