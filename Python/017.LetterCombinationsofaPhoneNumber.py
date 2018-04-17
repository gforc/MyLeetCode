



class Solution:
    
    def __init__(self):
        
        self.numMap =["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
    def twoCombinations(self,str1,str2):
        
        result = []
        if str1 == '' and str2 == '':
            return ''
        
        elif str1 == '' and str2 != '':
            return str2
            
        elif str1 != '' and str2 == '':
            return str1
        
        else :

            for i in range(len(str1)):
                
                for j in range(len(str2)):            
                    result.append(str1[i] + str2[j])         
        
        return result                   

    
    
    def letterCombinations(self,digits):
        
        if len(digits) == 1 :
            return self.numMap[int(digits)]
        
        if len(digits) >= 2 :        
            result = self.twoCombinations(self.numMap[int(digits[0])],self.numMap[int(digits[1])])

            if len(digits) ==2 :
                return result
            
            else :
                for i in range(2,len(digits)):
                    result = self.twoCombinations(result,self.numMap[int(digits[i])])
        
                return result
        
               
        
if __name__ =='__main__':
    print(Solution().letterCombinations('0234'))       
