
class Solution:

    def longestCommonPrefix(self, strs):

        if not strs :
            return ""
        
        else :
            result = ""
            for i in range(len(strs[0])):              
                for item in strs[1:]:                 
                    if i >= len(item) or strs[0][i] != item[i] :                    
                        if i == 0 :
                            return ""
                        else :
                            return strs[0][:i]
               
            return strs[0]
            

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(['aa','ab']))
    print(Solution().longestCommonPrefix(['da','ab']))
    print(Solution().longestCommonPrefix(['c','c']))
    print(Solution().longestCommonPrefix(['w']))
