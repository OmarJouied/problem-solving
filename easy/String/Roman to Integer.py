class Solution:
    def romanToInt(self, s: str) -> int:
        """
        function that Given a roman numeral, and convert it to an integer.
        
        :param s: A roman numeral
        :type s: str
        :return: converted to an integer.
        :rtype: int
        """
        result = 0
        prev_char = ""

        for char in s:
          if char == "I":
            result += 1
          elif char == "V":
            if prev_char == "I":
                result += 3
            else:
              result += 5
          elif char == "X":
            if prev_char == "I":
                result += 8
            else:
              result += 10
          elif char == "L":
            if prev_char == "X":
                result += 30
            else:
              result += 50
          elif char == "C":
            if prev_char == "X":
                result += 80
            else:
              result += 100
          elif char == "D":
            if prev_char == "C":
                result += 300
            else:
              result += 500
          elif char == "M":
            if prev_char == "C":
                result += 800
            else:
              result += 1000
          prev_char = char

        return result
