class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
        """
        length = len(s)

        start = 0
        end = length - 1
        while start < length:

          if s[start] < "0" or s[start] > "9" and s[start] < "A" or s[start] > "Z" and s[start] < "a" or s[start] > "z":
            start += 1
            continue
          if s[end] < "0" or s[end] > "9" and s[end] < "A" or s[end] > "Z" and s[end] < "a" or s[end] > "z":
            end -= 1
            continue
          if s[end].upper() != s[start].upper():
            return False
          
          start += 1
          end -= 1

        return True
