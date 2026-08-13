class Solution:
    def findMin(self, nums:list[int]) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def lower_bound(self, nums:list[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        if left <= len(nums) - 1 and nums[left] == target:
            return left
        return -1
    
    
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        i = self.findMin(nums)
        if target > nums[-1]:
            return self.lower_bound(nums, 0, i - 1, target)
        else:
            return self.lower_bound(nums, i, n - 1, target)