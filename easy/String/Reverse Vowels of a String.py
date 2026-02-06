class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Given a string s, reverse only all the vowels in the string and return it.

        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

        for ref:
        class Solution:
          def reverseVowels(self, s: str) -> str:
              vowels = ["a", "e", "i", "o", "u"]
              n = len(s)
              r = n - 1
              for l in range(n):
                  if s[l].lower() in vowels:
                      while s[r].lower() not in vowels:
                          r -= 1

                      s += s[r]
                      r -= 1
                  else:
                      s += s[l]
              
              return s[n:]
        """
        def is_vowels(char: str) -> bool:
          return char == "a" or char == "A" or char == "e" or char == "E" or char == "i" or char == "I" or char == "o" or char == "O" or char == "u" or char == "U"

        start = 0
        end = len(s) - 1

        while start < end:
          if is_vowels(s[start]) and is_vowels(s[end]):
            tmp = s[start]
            s = s[:start] + s[end] + s[start + 1:]
            s = s[:end] + tmp + s[end + 1:]

            start += 1
            end -= 1
          
          if not is_vowels(s[start]):
            start += 1

          if not is_vowels(s[end]):
            end -= 1
        
        return s
