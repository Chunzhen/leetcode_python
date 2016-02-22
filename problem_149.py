#! /usr/bin/env python
# -*- coding:utf-8 -*-

class Point(object):
	def __init__(self,a=0,b=0):
		self.x=a
		self.y=b

class Solution(object):
	def maxPoints(self,points):
		"""
		:type points:List[Point]
		:rtype: int
		"""	
		l=len(points)
		if l==0:
			return 0
		elif l==1:
			return 1
		d={}
		for i in range(l):
			for j in range(i+1,l):
				a,b=self.find_a_b(points[i],points[j])
				line=str(a)+','+str(b)
				temp=d.get(line,set())
				temp.add(points[i])
				temp.add(points[j])
				d[line]=temp

		return max(len(x) for x in d.values())


	def find_a_b(self,points1,points2):
		x1=float(points1.x)
		y1=float(points1.y)
		x2=float(points2.x)
		y2=float(points2.y)
		if x2-x1==0:
			return x1,None
			
		a=(y2-y1)/(x2-x1)
		b=(y1*x2-y2*x1)/(x2-x1)
		if a==0:
			a=0.0
		if b==0:
			b=0.0

		return a,b
		


def  main():
	s=Solution()
	l=[[0,-12],[5,2],[2,5],[0,-5],[1,5],[2,-2],[5,-4],[3,4],[-2,4],[-1,4],[0,-5],[0,-8],[-2,-1],[0,-11],[0,-9]]
	points=[]
	for v in l:
		points.append(Point(v[0],v[1]))
	print s.maxPoints(points)

if __name__ == '__main__':
	main()