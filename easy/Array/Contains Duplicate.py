class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        """
        Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
        """
        count_hash = {}
        for num in nums:
          count_hash[num] = count_hash.get(num, 0) + 1
        for item in count_hash:
          if count_hash[item] > 1:
            return True
        
        return False
