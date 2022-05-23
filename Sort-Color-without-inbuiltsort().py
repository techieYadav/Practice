#THREE POINTER
#TC: O(n)   SC=O(1)
class Solution:
    def sortColors(self, nums):
        beg, mid, end = 0, 0, len(nums) - 1
        
        while mid <= end:
            if nums[mid] == 0:
                nums[beg], nums[mid] = nums[mid], nums[beg]
                mid += 1
                beg += 1
            elif nums[mid] == 2:
                nums[mid], nums[end] = nums[end], nums[mid]
                end -= 1
            else:  #nums[mid] == 1:
                mid += 1

#Using Swap
class Solution:
def sortColors(self, nums: List[int]) -> None:

    for i in range(len(nums)):
        min = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min]:
                min = j
        nums[i], nums[min] = nums[min], nums[i]
    return nums
  
 
# count sort    
def sortColors1(self, nums):
    c0 = c1 = c2 = 0
    for num in nums:
        if num == 0:
            c0 += 1
        elif num == 1:
            c1 += 1
        else:
            c2 += 1
    nums[:c0] = [0] * c0
    nums[c0:c0+c1] = [1] * c1
    nums[c0+c1:] = [2] * c2
   
  
  
# one pass 
def sortColors(self, nums):
    # zero and r record the position of "0" and "2" respectively
    l, r, zero = 0, len(nums)-1, 0
    while l <= r:
        if nums[l] == 0:
            nums[l], nums[zero] = nums[zero], nums[l]
            l += 1; zero += 1
        elif nums[l] == 2:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        else:
            l += 1





 #USING SELECTION SORT
# TC: O(N^2)
  class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        j=0
        k=0
        m=0
        for i in range(n):
            while(j<n and nums[j]!=k):
                j+=1
            if j<n:
                if nums[i]==0:
                    j+=1
                else:
                    nums[i],nums[j]=nums[j],nums[i]
                    j+=1
            else:
                if m==0:
                    k=1
                    j=i
                    m=1
                    while(j<n and nums[j]!=k):
                        j+=1
                if j<n:
                    if nums[i]==1:
                        j+=1
                    else:
                        nums[i],nums[j]=nums[j],nums[i]
                        j+=1
        return nums
