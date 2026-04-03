class Solution:
    def majorityElement(self, nums: list[int]) -> int:
      """
      Given an array nums of size n, return the majority element.

      The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

      for ref:
        def majorityElement(self, nums: List[int]) -> int:
            res = majority = 0
            
            for n in nums:
              if majority == 0:
                res = n
              
              majority += 1 if n == res else -1
            
            return res
      """
      # sort array
      def sort(nums: list[int]) -> list[int]:
        if len(nums) == 1:
          return nums
        left = sort(nums[:len(nums) // 2])
        right = sort(nums[len(nums) // 2:])
        i = j = 0
        res = [0] * len(nums)
        while i < len(left) and j < len(right):
          if left[i] < right[j]:
            res[i + j] = left[i]
            i += 1
          else:
            res[i + j] = right[j]
            j += 1
        left = left[i:] if i < len(left) else right[j:]
        i += j
        for num in left:
          res[i] = num
          i += 1
        return res
      
      nums = sort(nums)
      return nums[len(nums) // 2]
