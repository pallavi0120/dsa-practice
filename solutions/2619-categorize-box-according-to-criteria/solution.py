class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky=0
        heavy=0
        volume=length*width*height
        if length>=10**4 or width>=10**4 or height>=10**4 or volume>=10**9:
            bulky+=1
        if mass>=100:
            heavy+=1
        if bulky==1 and heavy==1:
            return "Both"
        elif bulky!=1 and heavy!=1:
            return "Neither"
        elif bulky==1 and heavy!=1:
            return "Bulky"
        else:
            return "Heavy"        
