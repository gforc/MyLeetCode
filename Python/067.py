'''
Created on Feb 22, 2019

@author: evanli
'''

class solution():
    
    def addBinary(self,a,b):
        cvs = 0
        result = ''
        middle = 0
        for i in range(1,max(len(a)+1,len(b)+1)):
            
            if i-1 < len(a) :
                
                middle += int(a[-i]) 
            if i-1 < len(b):
                middle +=  int(b[-i]) 
                
            if middle == 3:
                cvs = 1 
                result+='1'
                
            elif middle ==2:
                cvs = 1
                result+='0'
            else:
                cvs=0
                result+=str(middle)
            
            
            middle = 0
            middle+=cvs
            
        
        if cvs == 1:
            result+=str(cvs) 
        print(result[::-1])
    
    
if __name__ =='__main__':
    
    a = '1010'
    b = '1011'
    solution().addBinary(a, b)
