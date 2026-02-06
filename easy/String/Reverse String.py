class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        function that reverses a string. The input string is given as an array of characters s.

        You must do this by modifying the input array in-place with O(1) extra memory.
        """
        idx = 0
        while idx < len(s) // 2:
          tmp_str = s[idx]
          s[idx] = s[len(s) - idx - 1]
          s[len(s) - idx - 1] = tmp_str
          idx += 1
