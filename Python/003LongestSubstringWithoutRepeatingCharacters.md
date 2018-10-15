
```
dict = {}  
class Solution:  
    def lengthOfLongestSubString(self,s):  
        i = 1  
        for chr in s :  
            print(chr)  
            if not dict.__contains__(chr) :                
                dict[chr] = i  
                i += 1   
        
        result=[]  
        for key in dict:  
            result.insert(dict[key],key)                
        
        return(''.join(result))  

    
aa = Solution()      
aa.lengthOfLongestSubString('abcabvdabcdef')  
```
