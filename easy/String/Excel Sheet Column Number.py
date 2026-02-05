class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
      """
      Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

      For example:

      A -> 1
      B -> 2
      C -> 3
      ...
      Z -> 26
      AA -> 27
      AB -> 28 
      ...

      as ref:
      class Solution:
        def titleToNumber(self, columnTitle: str) -> int:
            result = 0

            for x in columnTitle:
                result = result * 26 + (ord(x)-ord('A')+1)
            return result
      """
      result = 0

      length = len(columnTitle) - 1
      idx = length
      while idx >= 0:
        coef = 26 ** (length - idx)

        if columnTitle[idx] == "A":
          result += coef
        elif columnTitle[idx] == "B":
          result += coef * 2
        elif columnTitle[idx] == "C":
          result += coef * 3
        elif columnTitle[idx] == "D":
          result += coef * 4
        elif columnTitle[idx] == "E":
          result += coef * 5
        elif columnTitle[idx] == "F":
          result += coef * 6
        elif columnTitle[idx] == "G":
          result += coef * 7
        elif columnTitle[idx] == "H":
          result += coef * 8
        elif columnTitle[idx] == "I":
          result += coef * 9
        elif columnTitle[idx] == "J":
          result += coef * 10
        elif columnTitle[idx] == "K":
          result += coef * 11
        elif columnTitle[idx] == "L":
          result += coef * 12
        elif columnTitle[idx] == "M":
          result += coef * 13
        elif columnTitle[idx] == "N":
          result += coef * 14
        elif columnTitle[idx] == "O":
          result += coef * 15
        elif columnTitle[idx] == "P":
          result += coef * 16
        elif columnTitle[idx] == "Q":
          result += coef * 17
        elif columnTitle[idx] == "R":
          result += coef * 18
        elif columnTitle[idx] == "S":
          result += coef * 19
        elif columnTitle[idx] == "T":
          result += coef * 20
        elif columnTitle[idx] == "U":
          result += coef * 21
        elif columnTitle[idx] == "V":
          result += coef * 22
        elif columnTitle[idx] == "W":
          result += coef * 23
        elif columnTitle[idx] == "X":
          result += coef * 24
        elif columnTitle[idx] == "Y":
          result += coef * 25
        elif columnTitle[idx] == "Z":
          result += coef * 26

        idx -= 1

      return result
