class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        """
        Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

        If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

        for ref:
        class Solution(object):
          def reverseStr(self, s, k):
              i = 0

              while i < len(s):
                  s = s[:i] + s[i:i+k][::-1] + s[i+k:]
                  i = i + 2*k

              return s
        """
        def reverse(s: str) -> str:
          l = len(s)
          for i in range(l // 2):
            tmp = s[i]
            s = s[:i] + s[l - 1 - i] + s[i+1:]
            s = s[:l - 1 - i] + tmp + s[l - i:]
          return s
        l = len(s)
        i = 0
        while i < l:
          s = s[:i] + reverse(s[i:k + i]) + s[k + i:]
          i += 2 * k
        return s
