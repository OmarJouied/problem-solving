class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

        Letters are case sensitive, for example, "Aa" is not considered a palindrome.
        """
        chars = {}
        for char in s:
          chars[char] = chars.get(char, 0) + 1

        result = 0
        has_odd = False
        for char in chars:
          if chars[char] % 2:
            result += chars[char] - 1
            has_odd = True
          else:
            result += chars[char]
        return result + 1 if has_odd else result
