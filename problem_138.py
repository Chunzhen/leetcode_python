#! /usr/bin/env python
# -*- coding:utf-8 -*-

class RandomListNode(object):
	def __init__(self,x):
		self.label=x
		self.next=None
		self.random=None

class Solution(object):
	def copyRandomList(self,head):
		"""
		:type head: RandomListNode
		:rtype: RandomListNode
		"""
		current=head
		if not current:
			return None
		d={}
		l=[]
		i=0
		while current:
			label=current.label
			l.append(RandomListNode(label))

			d[current]=i
			current=current.next
			i+=1

		current=head
		i=0
		while current:
			random=current.random
			if random!=None:
				index=d.get(random)
				l[i].random=l[index]
			current=current.next
			i+=1

		for i in range(len(l)-1):
			l[i].next=l[i+1]

		return l[0]


def print_rlist(current):
	while current:
		random=current.random
		r=-1
		if random:
			r=random.label

		print current.label,' ',r
		current=current.next

def  main():
	s=Solution()

	r1=RandomListNode(1)
	r2=RandomListNode(2)
	r3=RandomListNode(3)
	r4=RandomListNode(4)
	r5=RandomListNode(5)
	r6=RandomListNode(6)

	r1.next=r2
	r2.next=r3
	r3.next=r4
	r4.next=r5
	r5.next=r6

	r1.random=r5
	r4.random=r3

	r=s.copyRandomList(r1)
	print_rlist(r)

if __name__ == '__main__':
	main()