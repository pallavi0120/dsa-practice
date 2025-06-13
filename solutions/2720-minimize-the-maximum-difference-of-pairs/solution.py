class Solution:
    def minimizeMax(self, nums: list[int], p: int) -> int:
        nums.sort()
        
        def can_form_pairs(max_diff):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= max_diff:
                    count += 1
                    i += 2  # skip both, as they form a pair
                else:
                    i += 1  # try next pair
            return count >= p
        
        # Binary search range
        left = 0
        right = nums[-1] - nums[0]
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if can_form_pairs(mid):
                result = mid
                right = mid - 1  # try to find smaller max diff
            else:
                left = mid + 1  # increase allowed diff
        return result

