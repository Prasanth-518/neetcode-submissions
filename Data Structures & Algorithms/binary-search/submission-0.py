class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        elif target != nums[0] and len(nums) == 1:
            return -1
        if target >= nums[len(nums)//2]:
            i = len(nums)//2
            while i < len(nums):
                if nums[i] == target:
                    return i
                i+=1
        else:
            i = 0
            while i < len(nums)//2:
                if nums[i] == target:
                    return i
                i+=1
        return -1
        