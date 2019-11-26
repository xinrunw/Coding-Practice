# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = max(nums)
        curr = 0
        for elem in nums:
            if elem < 0:
                if curr + elem > 0:
                    curr += elem
                else:
                    curr = 0
            else:
                curr += elem;
                if curr_max < curr:
                    curr_max = curr;
        return curr_max

