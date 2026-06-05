class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        elif target != nums[0] and len(nums) == 1:
            return -1
        l=0
        r=len(nums)
        while l < r:
            new_len = l+r
            if target < nums[new_len//2]:
                r = new_len//2 - 1
            elif target > nums[new_len//2]:
                l = new_len//2 + 1
            elif target == nums[new_len//2]:
                return new_len//2
        if l < len(nums) and nums[l] == target:
            return l
        elif r >= 0 and r < len(nums) and nums[r] == target:
            return r
        else:
            return -1