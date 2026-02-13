class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        """
        We define the usage of capitals in a word to be right when one of the following cases holds:

        All letters in this word are capitals, like "USA".
        All letters in this word are not capitals, like "leetcode".
        Only the first letter in this word is capital, like "Google".
        Given a string word, return true if the usage of capitals in it is right.
        """
        capital_count = 0
        for char in word:
          if ord(char) <= 90:
            capital_count += 1

        if not capital_count or capital_count == len(word) or capital_count == 1 and ord(word[0]) <= 90:
          return True
        return False
