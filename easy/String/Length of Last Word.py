class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        idx = 0

        while idx < length:
          
          if s[idx] != " ":
            result = 0
            while idx < length and s[idx] != " ":
              result += 1
              idx += 1

          idx += 1

        return result
