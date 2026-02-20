class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
      """
      Given two arrays of strings list1 and list2, find the common strings with the least index sum.

      A common string is a string that appeared in both list1 and list2.

      A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

      Return all the common strings with the least index sum. Return the answer in any order.

      for ref:
      class Solution:
        def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
            index_map = {word: i for i, word in enumerate(list1)}
            
            min_sum = float('inf')
            result = []
            
            for j, word in enumerate(list2):
                if word in index_map:
                    index_sum = index_map[word] + j
                    
                    if index_sum < min_sum:
                        min_sum = index_sum
                        result = [word]
                    elif index_sum == min_sum:
                        result.append(word)
            
            return result
      """
      word_hash = {}
      for i in range(len(list1)):
        word_hash[list1[i]] = i

      min = 1998
      result = []
      for i in range(len(list2)):
        idx = word_hash.get(list2[i], -1)
        if idx > -1:
          if idx + i < min:
            result = [list2[i]]
            min = idx + i
          elif idx + i == min:
            result.append(list2[i])

      return result
