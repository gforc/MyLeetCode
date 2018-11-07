class sulotion:
        
    def maxArea(self,height):
        
        maxArea = 0  
        if len(height) == 1 :
            return height[0]
        if len(height) == 0 :
            return maxArea         
        for i in range(len(height)-1): 
            for j in range(i,len(height)): 
                maxArea = max(maxArea, min(height[i],height[j]) * (j-i))                  
        print(maxArea)   
        return maxArea     
        
            
           
        
 
if __name__ == '__main__' :
    
    height = [1,8,6,7,5,4,8,3,6]
    sulotion().maxArea(height)
