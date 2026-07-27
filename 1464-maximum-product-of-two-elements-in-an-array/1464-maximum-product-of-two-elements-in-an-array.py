class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_val = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    current_product = (nums[i] - 1) * (nums[j] - 1)
                    if current_product > max_val:
                        max_val = current_product
                        
        return max_val