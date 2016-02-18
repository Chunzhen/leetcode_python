#! /usr/bin/env python
# -*- coding:utf-8 -*-
class ListNode(object):
	def __init__(self,x):
		self.val=x
		self.next=None


class Solution(object):
	def reverseKGroup(self,head,k):
		"""
		:type head: ListNode
		:type k: int 
		:rtype: ListNode
		"""
		pre=None
		current=head
		i=0
		temp=head
		while(i<k and temp):
			temp=temp.next
		if i<k:
			return head

		temp=current
		while(i<k and temp):
			temp=temp.next
		if i<k:
			break
		current2=temp

		while current and current.next:
			next1=current.next
			next2=next1.next

			if pre:
				pre.next=next1
				
			next1.next=current
			current.next=next2

			pre=current
			current=next2
		return head

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
	l3.next=l4
	l4.next=l5

	#print_list(l1)
	ll=s.swapPairs(None)

	print_list(ll)

if __name__ == '__main__':
	main()