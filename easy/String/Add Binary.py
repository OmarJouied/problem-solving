class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        Given two binary strings a and b, return their sum as a binary string.
        """
        end_a = len(a) - 1
        end_b = len(b) - 1

        result = ""
        rest = ""

        while end_b >= 0 or end_a >= 0:
          a_part = a[end_a] if end_a >= 0 else "0"
          b_part = b[end_b] if end_b >= 0 else "0"

          if a_part == b_part:
            if rest:
              result = "1" + result
            else:
              result = "0" + result
            
            if a_part == "1":
              rest = "1"
            else:
              rest = ""
          else:
            if rest:
              result = "0" + result
            else:
              result = "1" + result
            
          end_a -= 1
          end_b -= 1
        
        return rest + result
