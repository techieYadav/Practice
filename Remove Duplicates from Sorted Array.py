https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Solution:

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for i in range(1,len(nums)):
            if nums[i]!=nums[r-1]:
                nums[l]=nums[i]
                l+=1
        return l
        
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=list(set(nums))
        l.sort()
        for i in range(len(nums)):
            if i<len(l):
                nums[i]=l[i]
            else:
                nums[i]='_'
        return len(l)
        
        
