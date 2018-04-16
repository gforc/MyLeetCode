






class Solution:
    
    def threeSumCloset(self,nums,target):
        diff_min = float("inf")
        result = []
        
        nums.sort()
        
        for i in range(len(nums)-2):
            
            for j in range(i+1,len(nums)-1):
                
                for n in range(j+1,len(nums)):
                    diff = nums[i]+nums[j]+nums[n] - target
                    
                    if diff_min > abs(diff):
                        diff_min = abs(diff)
                        result = [nums[i],nums[j],nums[n]]
                    
        return result           
                    
if __name__ == '__main__':
    
    print(Solution().threeSumCloset([-1, 2, 1, -4], 1))              
