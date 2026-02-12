class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        """
        You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

        We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

        Return the reformatted license key.

        for ref:
        class Solution:
            def licenseKeyFormatting(self, s: str, k: int) -> str:
                ans = ""
                counter = 0
                for i in range(len(s) - 1, -1, -1):
                    if s[i] == '-':
                        continue
                    if counter == k:
                        ans = '-' + ans
                        counter = 0
                    ans = s[i].capitalize() + ans
                    counter += 1
                return ans
        """
        result = ""

        counter = 0
        for i in range(len(s) - 1, -1, -1):
          if s[i] == "-":
            continue
          if counter == k and i >= 0:
            counter = 0
            result = "-" + result
          if ord(s[i]) >= 97:
            result = chr(ord(s[i]) - 32)  + result
          else:
            result = s[i] + result
          counter += 1

        return result
