class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        Given a pattern and a string s, find if s follows the same pattern.

        Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

        Each letter in pattern maps to exactly one unique word in s.
        Each unique word in s maps to exactly one letter in pattern.
        No two letters map to the same word, and no two words map to the same letter.
        """
        def get_words(s: str) -> list[str]:
          result = []
          idx = 0
          word = ""
          while idx < len(s):
            if s[idx] != " ":
              word += s[idx]
            else:
              result.append(word)
              word = ""
            idx += 1
          
          result.append(word)

          return result

        words = get_words(s)
        
        if len(pattern) != len(words):
          return False

        char_pairs = {}
        word_pairs = {}
        idx = 0
        while idx < len(pattern):
          if not pattern[idx] in char_pairs and not words[idx] in word_pairs:
            char_pairs[pattern[idx]] = words[idx]
            word_pairs[words[idx]] = pattern[idx]
          elif pattern[idx] in char_pairs and words[idx] in word_pairs:
            if char_pairs[pattern[idx]] != words[idx] or word_pairs[words[idx]] != pattern[idx]:
              return False
          else:
            return False
          idx += 1
        return True
