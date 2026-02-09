class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        """
        Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

        for ref:
        class Solution:
          def addStrings(self, num1: str, num2: str) -> str:
              # APPROACH
              '''
              start MSB -> LSB (run loop back)
              total -> num + carry
              write -> total % 10
              carry -> total // 10
              carry = 0
              ord('7') = 55
              ord('0') = 48
              ord('7') - ord('0') = 7
              '''
              i = len(num1)-1
              j = len(num2)-1

              carry = 0
              
              result = []
              while i >= 0 or j >= 0:
                  total = carry
                  if i >= 0:
                      total += ord(num1[i]) - ord('0')
                      i -= 1
                  if j >= 0:
                      total += ord(num2[j]) - ord('0')
                      j -= 1
              
                  base = total % 10
                  result.append(str(base))
                  carry = total // 10
              
              if carry:
                  result.append(str(carry))

              return ''.join(result[::-1])
        """
        result = ""

        l1 = len(num1) - 1
        l2 = len(num2) - 1
        rest = 0
        while l1 >= 0 or l2 >= 0:
          d = (ord(num1[l1]) if l1 >= 0 else ord("0")) + (ord(num2[l2]) if l2 >= 0 else ord("0")) - 2 * ord("0") + rest
          result = chr(d % 10 + ord("0")) + result
          rest = 1 if d >= 10 else 0
          l1 -= 1
          l2 -= 1
        return ("1" if rest else "") + result
  
solution = Solution().addStrings("9", "9")
print(solution)