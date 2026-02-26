class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
        Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

        Substrings that occur multiple times are counted the number of times they occur.

        class Solution:
            def countBinarySubstrings(self, s: str) -> int:
                prev = 0
                cur = 1
                cnt = 0

                for i in range(1, len(s)):
                    if s[i] == s[i-1]:
                        cur += 1
                    else:
                        cnt += min(cur, prev)
                        prev = cur
                        cur = 1

                return cnt + min(cur, prev)
        """
        result = 0
        base_stack = [s[0]]
        complement_stack = []
        i = 1
        end = len(s)
        while i < end:
          while i < end and base_stack[0] == s[i]:
            base_stack.append(s[i])
            i += 1
            
          while i < end and base_stack and base_stack[0] != s[i]:
            base_stack.pop()
            complement_stack.append(s[i])
            i += 1
            result += 1

          base_stack = complement_stack
          complement_stack = []

        return result
