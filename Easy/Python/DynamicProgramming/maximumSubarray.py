# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104




class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize current_sum and max_sum to the first element of the array
        current_sum = max_sum = nums[0]
        
        # Traverse through the array starting from the second element
        for num in nums[1:]:
            # Either add the current number to the existing subarray or start a new subarray
            current_sum = max(num, current_sum + num)
            
            # Update max_sum to be the maximum of current_sum and max_sum
            max_sum = max(max_sum, current_sum)
        
        return max_sum