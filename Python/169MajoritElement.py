'''
Created on 2017年9月14日

@author: evan
this script is done
'''
import collections 
class solution():

    def majorityElement(self,nums):       
        dict = collections.defaultdict(int)
        
        for i in range(len(nums)):
            dict[nums[i]] += 1
         
        for item in dict:
            if dict[item] > len(nums)/2:
                 return item   
        
if __name__ =='__main__':
    nums = [2,2,1,1,1,2,2]
    print(solution().majorityElement1(nums) )
                
