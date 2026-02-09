class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Docstring for longestPalindrome
        
        :param self: Description
        :param s: Description
        :type s: str
        :return: Description
        :rtype: int
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
