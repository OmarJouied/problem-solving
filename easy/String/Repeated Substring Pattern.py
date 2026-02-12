class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
      """
      Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

      for ref:
        class Solution:
          def repeatedSubstringPattern(self, s: str) -> bool:
              // given s, check if it can be constructed by taking a substring and appending multiple copies 
              news = s+s 
              // abaaba
              for i in range(1, len(s)): 
                  temp = news[i: i+len(s)]
                  if temp == s: 
                      return True 
              return False

        class Solution:
          def repeatedSubstringPattern(self, s: str) -> bool:
              ss = (s + s)[1:-1]
              return s in ss
        
        class Solution:
          def repeatedSubstringPattern(self, s: str) -> bool:
              n = len(s)
              for i in range(1, n // 2 + 1):
                  if n % i == 0 and s[:i] * (n // i) == s:
                      return True
              
              return False
      """
      if len(s) == 1:
        return False
      
      length = len(s)
      divisors = [1]
      for i in range(2, length // 2 + 1):
        if i not in divisors and not length % i:
          divisors.append(i)
          divisors.append(length // i)

      for div in divisors:
        base_sub = s[:div]
        for sub_len in range(div, length, div):
          if s[sub_len: sub_len + div] != base_sub:
            break
          elif sub_len + div == length:
            return True
      return False
