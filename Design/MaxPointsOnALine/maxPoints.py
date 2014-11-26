#!/usr/bin/python

# Max Points on a Line

# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        # Line formula: 
        #y=((y2-y1)/(x2-x1))*x+(x2*y1-x1*y2)/(x2-x1)
        if len(points)<3:
             return len(points)
        maxpoints = 0
        for i in range(len(points)):
             sl = {}
             duplicate = 1
             for j in range(len(points)):
                 if points[i].x==points[j].x and points[i].y==points[j].y and i!=j:
                     duplicate += 1
                 elif i!=j:
                     if points[i].x==points[j].x:
                         sl['v'] = sl.get('v',0) + 1
                     elif points[i].y==points[j].y:
                         sl['h'] = sl.get('h',0) + 1
                     else:
                         slope = float(points[i].y-points[j].y)/(points[i].x-points[j].x)
                         sl[slope] = sl.get(slope,0) + 1
             if len(sl)>0:
                 maxpoints = max(maxpoints,max(sl.values())+duplicate)
             else:
                 maxpoints = max(maxpoints,duplicate)
        return maxpoints

def printPoints(points):
    for i in points:
        print "(%d,%d), "%(i.x,i.y),

if __name__=="__main__":
    sol = Solution()
    p1 = Point()
    p2 = Point(-1,-1)
    p3 = Point(2,2)
    p4 = Point(1,-1)
    p5 = Point(1,1)
    points0 = [p1]
    points1 = []
    points2 = [p1,p1]
    points3 = [p1,p2,p3]
    points4 = [p1,p4,p2]
    points5 = [p1,p5,p1]
    printPoints(points0)
    print sol.maxPoints(points0) # 1
    printPoints(points1)
    print sol.maxPoints(points1) # 0
    printPoints(points2)
    print sol.maxPoints(points2) # 2
    printPoints(points3) 
    print sol.maxPoints(points3) # 3
    printPoints(points4)
    print sol.maxPoints(points4) # 2
    printPoints(points5)
    print sol.maxPoints(points5) # 3
