


class Solution:
    
    
    def generate(self,numRows):
        
        result = [[1]]
        
        if numRows == 0:
            return 0
        elif numRows == 1:
            return result
        
        
        for i in range (1,numRows):
            middle = []
            for j in range(i+1):
                 
                if j < 1 or j == i :
                    middle.append(1)
                    
                else :
                    middle.append(result[i-1][j-1] + result[i-1][j])
                    
            result.append(middle)

        return result


if __name__ == '__main__':
    
    print(Solution().generate(5))
