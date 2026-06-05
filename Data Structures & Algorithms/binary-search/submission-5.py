class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target == nums[0]:
            return 0
        elif target != nums[0] and len(nums) == 1:
            return -1
        l=0
        r=len(nums)-1
        while l <= r:
            new_len = l+r
            if target < nums[new_len//2]:
                r = new_len//2 - 1
            elif target > nums[new_len//2]:
                l = new_len//2 + 1
            elif target == nums[new_len//2]:
                return new_len//2
        return -1