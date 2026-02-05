class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

        For example:

        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
        ...
        """
        result = ""
        while columnNumber > 0:
          letter_index = columnNumber % 26
          columnNumber //= 26

          if not letter_index:
            columnNumber -= 1

          if letter_index == 0:
            result = "Z" + result
          elif letter_index == 1:
            result = "A" + result
          elif letter_index == 2:
            result = "B" + result
          elif letter_index == 3:
            result = "C" + result
          elif letter_index == 4:
            result = "D" + result
          elif letter_index == 5:
            result = "E" + result
          elif letter_index == 6:
            result = "F" + result
          elif letter_index == 7:
            result = "G" + result
          elif letter_index == 8:
            result = "H" + result
          elif letter_index == 9:
            result = "I" + result
          elif letter_index == 10:
            result = "J" + result
          elif letter_index == 11:
            result = "K" + result
          elif letter_index == 12:
            result = "L" + result
          elif letter_index == 13:
            result = "M" + result
          elif letter_index == 14:
            result = "N" + result
          elif letter_index == 15:
            result = "O" + result
          elif letter_index == 16:
            result = "P" + result
          elif letter_index == 17:
            result = "Q" + result
          elif letter_index == 18:
            result = "R" + result
          elif letter_index == 19:
            result = "S" + result
          elif letter_index == 20:
            result = "T" + result
          elif letter_index == 21:
            result = "U" + result
          elif letter_index == 22:
            result = "V" + result
          elif letter_index == 23:
            result = "W" + result
          elif letter_index == 24:
            result = "X" + result
          elif letter_index == 25:
            result = "Y" + result

        return result
