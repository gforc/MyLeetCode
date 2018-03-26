






class Solution:
    
    def getRow(self,rowIndex):
        
        
        result = [[1]]
        if rowIndex == 0 :
            return result
        
        
        for i in range(1,rowIndex+1):
            middle = []
            for j in range(i+1) :
                
                if j == 0 or j == i :
                    middle.append(1)
                    
                else :
                    middle.append(result[i-1][j-1] + result[i-1][j])
                    
             
             
            result.append(middle)
            
            
        return result[-1]  
    
    
    
if __name__ == '__main__':
    print(Solution().getRow(1))
