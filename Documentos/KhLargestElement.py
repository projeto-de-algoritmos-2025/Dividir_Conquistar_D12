import random

class Solution:
    def findKthLargest(self, nums, k):
        k_index = len(nums) - k
        
        left, right = 0, len(nums) - 1
        
        while True:
            if left == right:
                return nums[left]
            pivot_index = random.randint(left, right)
            pivot = nums[pivot_index]
            
            lt = left     
            i = left      
            gt = right    

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[gt], nums[i] = nums[i], nums[gt]
                    gt -= 1
                else:  
                    i += 1
            
            if k_index < lt:
                right = lt - 1
            elif k_index > gt:
                left = gt + 1
            else:
              
                return pivot