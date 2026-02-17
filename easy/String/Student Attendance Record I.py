class Solution:
    def checkRecord(self, s: str) -> bool:
      """
      You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

      'A': Absent.
      'L': Late.
      'P': Present.
      The student is eligible for an attendance award if they meet both of the following criteria:

      The student was absent () for strictly fewer than 2 days total.'A'
      The student was never late () for 3 or more consecutive days.'L'
      Return true if the student is eligible for an attendance award, or false otherwise.

      for ref:
      Java
      class Solution {
      public boolean checkRecord(String s) {
          int countA = 0, countL = 0;

          for (char ch : s.toCharArray()) {
              if (ch != 'L') countL = 0;
              if (ch == 'L') countL++;
              if (ch == 'A') countA++;
              if (countA == 2 || countL == 3) return false;
          }

          return true;
      }
  }
      """
      count_A = 0
      count_L = 0
      for char in s:
        if char == "L":
          count_L += 1
          if count_L == 3:
            return False
          continue

        count_L = 0
        if char == "A":
          count_A += 1
          if count_A == 2:
            return False
      return True
