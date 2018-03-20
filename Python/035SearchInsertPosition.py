



class Solution:
    
    def searchInsert(self,nums,target):
        
        if not nums:
            return 0
        
        for i in range(len(nums)-1):
            
            if nums[i] < target :
                if nums[i+1] > target :
                    return i+1
                
            elif nums[i] >= target:
                return i
            
        
        if nums[0] >= target:   # 当只有一个元素
            return 0
        elif nums[-1] == target :   #当最后一个元素等于target
            return len(nums)-1
        else :
            return len(nums)
    
    
if __name__ == '__main__':
    
    print(Solution().searchInsert([1,3,5,6], 5))
    print(Solution().searchInsert([1,3,5,6], 2))
    print(Solution().searchInsert([1,3,5,6], 7))
    print(Solution().searchInsert([1,3,5,6], 0))

                
