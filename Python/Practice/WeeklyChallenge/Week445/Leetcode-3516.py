class Solution(object):
    def findClosest(self, x, y, z):
        distx = abs(z - x) 
        disty = abs(z - y)

        if distx == disty:
            return 0
        
        return 1 if distx < disty else 2

        