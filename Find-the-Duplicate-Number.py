#Time Complexity: O(nlogn)
#Space Complexity: O(logn) or O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                return i
 

#Time Complexity: O(n)
#Space Complexity: O(n) 
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
            
            
            
#Time Complexity: O(n)
#Space Complexity: O(1)            
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
