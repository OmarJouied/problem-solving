class Solution:
    def singleNumber(self, nums: list[int]) -> int:
      """
      Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

      You must implement a solution with a linear runtime complexity and use only constant extra space.

      for ref:
      def singleNumber(self, nums: List[int]) -> int:
          result = 0 
          for num in nums:
              result ^= num # XOR bit operation
          return result

      def singleNumber(self, nums: List[int]) -> int:
          index = 0
          while index < len(nums):
              if nums.count(nums[index]) > 1:
                  index += 1
              else:
                  return nums[index]

      Note: my solution use O(n) space, not the correct answer
      """
      res = 0
      memo = []
      for num in nums:
        if num in memo:
          res -= num
        else:
          res += num
          memo.append(num)
      return res
