




class Solution:
    
    def removeElement(self,nums,val):
        
        if len(nums) == 0:
            return 0
        
        count = 0
        for i in range(len(nums)):
            
            if nums[i] != val:
                count +=1
                
                
        return count
    
    
    
if __name__ == '__main__':
    
    print(Solution().removeElement([2,3,3,1,2], 3))
