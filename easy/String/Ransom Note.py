class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

        Each letter in magazine can only be used once in ransomNote.

        for ref:
        class Solution:
          def canConstruct(self, ransomNote: str, magazine: str) -> bool:
            maga_hash = {}

            for c in magazine:
              maga_hash[c] = 1 + maga_hash.get(c, 0)

            for c in ransomNote:
              if c not in maga_hash or maga_hash[c] <= 0:
                return False
              maga_hash[c] -= 1
            
            return True
        """
        if len(ransomNote) > len(magazine):
          return False
        count_hash = {}
        for letter in magazine:
          count_hash[letter] = count_hash.get(letter, 0) + 1
        for letter in ransomNote:
          count_hash[letter] = count_hash.get(letter, 0) - 1
          if count_hash[letter] < 0:
            return False
        return True
