class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
        
        for ref:
        class Solution:
            def firstUniqChar(self, s: str) -> int:
                al = 'abcdefghijklmnopqrstuvwxyz'
                dt = []
                for i in al:
                    x = s.find(i)
                    y = s.rfind(i)
                    if x != -1 and x == y:
                        dt.append(x)
                if len(dt) == 0:
                    return -1
                return min(dt)
        """
        indeces = {}
        letters = ""

        length = len(s)
        idx = 0
        while idx < length:
          if s[idx] not in letters:
            letters += s[idx]
            indeces[s[idx]] = idx
          else:
            indeces[s[idx]] = -1
          idx += 1

        for l in letters:
          if indeces[l] > -1:
            return indeces[l]
        
        return -1
