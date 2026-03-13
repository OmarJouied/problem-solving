class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
      """
      Given an integer numRows, return the first numRows of Pascal's triangle.

      class Solution:
          def generate(self, numRows: int) -> List[List[int]]:
              
              res = []

              for i in range(numRows):
                  row = [1] * (i + 1)

                  for j in range(1, i):
                      row[j] = res[i-1][j-1] + res[i-1][j]
              
                  res.append(row)
              
              return res
      """
      result = []
      for i in range(numRows):
        arr = []
        for j in range(i + 1):
          if j == 0 or j == i:
            arr.append(1)
          else:
            arr.append(result[i-1][j-1] + result[i-1][j])
        result.append(arr)
      return result
