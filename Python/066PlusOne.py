

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

    
if __name__ == "__main__":
    print (Solution().plusOne([9, 9, 9, 9]))
