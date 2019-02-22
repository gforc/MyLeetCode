

class Solution(object):
    def plusOne(self, digits):

        result = [0] + digits       
        result[-1] = result[-1] + 1 
        for i in range(len(result)-1,0,-1):
            if result[i] > 9 :
                result[i] =0
                result[i-1] = result[i-1] +1 

        if result[0] == 0:
            return result[1:]
        else:
            return result

class solution1(): ## this method is better
    
    def plusOne(self,digits):
        
        i = len(digits)-1  
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i-=1
                print('!!!!!!! = %s' % digits)
            
            else:
                digits[i] +=1
                print('@@@@@@@ = %s' % digits)
                return digits
            
        result = [1] + digits      
        print(result)
        return result
        
if __name__ == "__main__":
    print (Solution().plusOne([9, 9, 9, 9]))
