class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        This function finds the index of the first occurrence of a string in other.
        
        :param haystack: The finding string
        :type haystack: str
        :param needle: The string searched for.
        :type needle: str
        :return: The first index of occurrence.
        :rtype: int
        """
        haystack_len = len(haystack)
        needle_len = len(needle)

        if haystack == needle or needle_len == 0:
          return 0
        if haystack_len == 0 or haystack_len < needle_len:
          return -1
        
        for idx in range(0, haystack_len - needle_len + 1):
          if haystack[idx : idx + needle_len] == needle:
            return idx
        
        return -1
