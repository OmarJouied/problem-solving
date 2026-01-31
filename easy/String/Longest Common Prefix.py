class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        """
        Function to find the longest common prefix string amongst an array of strings.
        
        :param strs: list of words
        :type strs: list[str]
        :return: the longest common prefix string
        :rtype: str
        """
        longest = ""
        base_word = strs[0]

        idx = 0
        while idx < len(base_word):
          
          for word in strs[1:]:
            if idx >= len(word) or base_word[idx] != word[idx]:
              return longest
            
          longest += base_word[idx]

          idx += 1
        
        return longest
