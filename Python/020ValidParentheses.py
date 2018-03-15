

class Solution:
    
    def isValid(self,s):
        
        containning_dict = {')':'(', ']':'[', '}':'{'}
        closeBracket = [')',']','}']
        strs = []
        if len(s) == 0 :
            return True
        
        for i in range(len(s)):
            strs.append(s[i])
            if strs[-1] in closeBracket:
                if len(strs) == 1:
                    return False
                
                elif containning_dict[strs[-1]] == strs[-2]:
                    strs.pop()
                    strs.pop()
                    
                elif containning_dict[strs[-1]] != strs[-2]:

                    return False             
            
        if len(strs) != 0:
            return False
        
        else :
            return True        


         
      
if __name__ == '__main__' :
    
    print(Solution().isValid("([])"))
    
    
    
    
