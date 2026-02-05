class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, determine if they are isomorphic.

        Two strings s and t are isomorphic if the characters in s can be replaced to get t.

        All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

        for ref:
        class Solution:
            def isIsomorphic(self, s: str, t: str) -> bool:
                md = {}
                td = {}
                for i in range(len(s)):
                    if s[i] not in md and t[i] not in td:
                        md[s[i]] = t[i]
                        td[t[i]] = s[i]
                    elif s[i] in md and t[i] in td:
                        if md[s[i]] != t[i] or td[t[i]] != s[i]:
                            return False
                    else:
                        return False

                return True
        """
        def repetition(s):
          letter_len = 0
          letter = s[0]
          idx = 0
          while idx < len(s):
            if letter == s[idx]:
              letter_len += 1
              idx += 1
              continue
            break
          return letter_len

        lenght = len(s)
        idx = 0
        cache_letters = []

        while idx < lenght:
          base_len = repetition(s[idx:])
          secondary_len = repetition(t[idx:])
          if base_len != secondary_len:
            return False
          
          cached_s = None
          cached_t = None
          for cache_item in cache_letters:
            if cache_item[0] == s[idx]:
              cached_s = cache_item[1]
              break
          for cache_item in cache_letters:
            if cache_item[1] == t[idx]:
              cached_t = cache_item[0]
              break
            
          if cached_s and cached_s != t[idx] or cached_t and cached_t != s[idx]:
            return False
          cache_letters.append(s[idx]+t[idx])

          idx += base_len
        
        return True
