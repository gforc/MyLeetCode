
'''
Created on Mar 14, 2018

@author: mli
'''


class Solution:
   
    def isPalindrome(self,x):
        
        if x < 0 :
            x = -1 * x    # 认为负数也是回文
        elif x == 0 :
            return True
        
        x = str(x)    # int 转换为 str
           
        for i in range(len(x)//2):    ## // 为取整，/ 返回float
            
            if x[i] != x[-(1+i)] :
                return False
            
        return True       

        
         
if __name__ == '__main__':
    
    print(Solution().isPalindrome(1234))
    print(Solution().isPalindrome(1234321))
    print(Solution().isPalindrome(12034))

 
     
