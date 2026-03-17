class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
      """
      Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

      for ref:
      def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for _ in range(1, rowIndex + 1):
          row.append(1)
          for i in range(len(row) - 2, 0, -1):
            row[i] = row[i] + row[i - 1]

        return row

      def getRow(self, rowIndex):
        row = [1]

        for _ in range(rowIndex):
          row = [left + right for left, right in zip([0]+row, row+[0])]

        return row

      def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(1, rowIndex + 1):
          next_element = row[i - 1] * (rowIndex - i + 1) // i
          row.append(next_element)

        return row
      """
      res = [1] * (rowIndex + 1)
      for i in range(1, rowIndex + 1):
        for j in range(i // 2, 0, -1):
          if res[j] == 1:
            res[j] = res[~j] = res[j - 1] * 2
          else:
            res[j] = res[~j] = res[j] + res[j - 1]

      return res
