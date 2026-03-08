class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        """
        Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.
        
        class Solution:
            def searchInsert(self, nums: List[int], target: int) -> int:
                st = 0
                dr = len(nums) - 1
                while st <= dr:
                    mid = (st + dr) // 2
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        dr = mid - 1
                    else:
                        st = mid + 1

                return st
        """
        if not len(nums):
          return 0
        if len(nums) == 1:
          return 0 if nums[0] >= target else 1

        middle = len(nums) // 2
        if nums[middle] == target:
          return middle
        if nums[middle] > target:
          return self.searchInsert(nums[:middle], target)
        return middle + 1 + self.searchInsert(nums[middle+1:], target)
