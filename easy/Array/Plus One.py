class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
      """
      You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

      Increment the large integer by one and return the resulting array of digits.
      
      for ref:
      class Solution:
        def plusOne(self, digits):
            n = len(digits)
            for i in range(n - 1, -1, -1):
                if digits[i] < 9:
                    digits[i] += 1
                    return digits
                digits[i] = 0
            return [1] + digits
      """
      added = 1
      for i in range(len(digits) - 1, -1, -1):
        digits[i] = (digits[i] + added) % 10
        if digits[i]:
          added = 0
      
      return ([1] if added else []) + digits
