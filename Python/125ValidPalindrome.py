

class Solution:
    
    def isPalindrome(self,s):
        
        result = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isnumeric():
                if s[i].isupper() :
                    result += s[i].lower()               
                else :                   
                    result += s[i]

        if len(result) <=1 :
            return 'true'
        
        for i in range(len(result)//2):
            if result[i] != result[-(i+1)]:
                return 'false'
        
        
        return 'true'
        
        
if __name__ == '__main__':
    
    print(Solution().isPalindrome('A man, a plan, a canal: Panama'))
    print(Solution().isPalindrome('0P'))
