class Solution:
    def convertToBase7(self, num: int) -> str:
        """
        Given an integer num, return a string of its base 7 representation.
        """
        base = ["0","1","2","3","4","5","6"]
        result = ""
        is_neg = False
        if num < 0:
          is_neg = True
          num *= -1
        elif not num:
          result = "0"
        while num:
          result = base[num % 7] + result
          num //= 7
        return ("-" if is_neg else "") + result
