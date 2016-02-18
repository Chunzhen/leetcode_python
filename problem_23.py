#! /usr/bin/env python
# -*- coding:utf-8 -*-
class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None


class Solution(object):
	def mergeKLists(self,lists):
		"""
		:type lists: List[ListNode]
		:rtype: ListNode
		"""
		n=len(lists)
		if n<1:
			return None
		elif n==1:
			return lists[0]
		mid=n//2
		L=self.mergeKLists(lists[:mid])
		R=self.mergeKLists(lists[mid:])
		return self.mergeTwoLists(L,R)

	def mergeTwoLists(self,l1,l2):
		"""
		:type l1: ListNode
		:type l2: ListNode
		:rtype: ListNode
		"""
		if not l1:
			return l2
		if not l2:
			return l1

		l=None
		r=None
		while l1 and l2:
			next=None
			if l1.val<l2.val:
				next=ListNode(l1.val)
				l1=l1.next
			else:
				next=ListNode(l2.val)
				l2=l2.next
			if l:
				l.next=next
				l=next
			else:
				l=next
				r=l

		if l1:
			l.next=l1
		if l2:
			l.next=l2

		return r
		

def print_list(l):
	while l:
		print l.val
		l=l.next

def  main():
	s=Solution()
	l1=ListNode(1)
	l2=ListNode(2)
	l3=ListNode(3)
	l4=ListNode(4)
	l5=ListNode(5)

	l1.next=l2
	l2.next=l3
	#l3.next=l4
	l4.next=l5

	lists=[l1,l4,l3]
	ll=s.mergeKLists(lists)

	print_list(ll)

if __name__ == '__main__':
	main()