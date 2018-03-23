

# not verify pass in LeetCode




from _string import formatter_field_name_split




class TreeNode:
    def __init__(self,x):
        
        self.val = x 
        self.leftNode = None
        self.rightNode= None
    
    
class Solution:
    
    def __init__ (self):
        
        self.result = []    
    
    def isSameTree(self,p,q):
        
        self.formate(p) 
        result_p = self.result
        self.result = []
        self.formate(p)
        if result_p == self.result:
            return True
        else :
            return False
        
        
    def formate(self,n):
        
        if n != None:
            self.result.append(n.var)
        
            self.formate(n.leftNode)
            self.formate(n.rightNode)

            
  
