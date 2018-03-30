class Solution:
    def preProcess(self,s):
        
        result = ''
        for i in range(len(s)):
            
            result += '#'
            result += s[i]
            
        return result+'#'
    
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) ==1 :
            return s
        s = self.preProcess(s)
        print(s)
        result = ''
        for i in range(len(s)):
            

            m = 1
            n = 1
            middle_result = s[i]
          
            while i-m >= 0 and i+n < len(s):
#                print(s[i])
                if s[i+n] == s[i-m]:
                    middle_result = s[i-m:i+n+1]
                      
                else :
                    
                    if len(result) <= len(middle_result):
                        result = middle_result
                    
                    break
     
                n+=1
                m+=1
            
            if len(result) <= len(middle_result):
                result = middle_result       
                
        result = result[1:-1].split('#')
                    
                
        return ''.join(result)
        
        
