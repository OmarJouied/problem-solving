class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
      """
      Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

      You may assume that each input would have exactly one solution, and you may not use the same element twice.      
      """
      num_hash = {}
      for i in range(len(nums)):
        if (target - nums[i]) in num_hash:
          return [num_hash[target - nums[i]], i]
        num_hash[nums[i]] = i
