class Solution:
    def toLowerCase(self, s: str) -> str:
      """
      Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
      """
      result = ""
      for char in s:
        if 65 <= ord(char) <= 90:
          char = chr(ord(char) + 32)
        result += char
      return result
