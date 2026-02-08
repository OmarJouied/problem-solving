class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
      """
      Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

      A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
      
      for ref:
      class Solution:
          def isSubsequence(self, s: str, t: str) -> bool:
              sp = tp = 0

              while sp < len(s) and tp < len(t):
                  if s[sp] == t[tp]:
                      sp += 1
                  tp += 1
              
              return sp == len(s)
      """
      def index(char: str, string: str):
        for i in range(len(string)):
          if string[i] == char:
            return i
        return -1

      for i in range(len(s)):
        p = index(s[i], t)
        if p == -1:
          return False
        t = t[p + 1:]

      return True
