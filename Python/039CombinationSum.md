

```

class Solution:
    
    def combination(self,candiates,target):
        
        result = []
        self.combinationHelper([], target, sorted(candiates), result,0)
        
        print(result)
        return result
        
        
  
    
    def combinationHelper(self, middle_result, target, candiates, result,start):
        
        if target == 0:
            result.append(middle_result)
            return
        
        for i in range(start, len(candiates)):
            
            if target < candiates[i]:                
                return
            
            self.combinationHelper(middle_result+[candiates[i]], target-candiates[i], candiates, result, start)
            start+=1
           


        

if __name__ == '__main__':
    
    candiates = [2,3,6,7]
    target = 7
    Solution().combination(candiates, target)
    

```
