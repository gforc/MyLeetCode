'''
Created on Feb 23, 2019

@author: evan
'''


class solution():
    def twoSum(self,numbers,target):
        start = 0
        end = len(numbers)-1
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end-=1
            elif sum < target:
                start+=1
            
            else :
                return [start+1,end+1]
        


        
if __name__ == '__main__':
    numbers = [2,7,11,15]
    target = 9
    print(solution().twoSum(numbers, target))
