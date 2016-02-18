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
		pre1=None
		current1=head
		i=0
		temp=head
		while(i<k-1 and temp):
			temp=temp.next
			i+=1

		if i<k-1 or k<2 or not temp:
			return head
		head=temp

		while(self.isNext(current1,k)):
			i=k-1
			next_current1=None
			next_pre1=None
			while(i>2):
				j=i
				temp=current1
				pre2=None
				while(j>0):
					pre2=temp
					temp=temp.next
					j-=1

				current2=temp
				if i==k-1:
					next_current1=current2.next
					next_pre1=current1
					print "bingo:",print_list(next_current1)

				next1=current1.next
				next2=current2.next

				if pre1:
					pre1.next=current2
				current2.next=next1
				pre2.next=current1
				current1.next=next2

				pre1=current2
				current1=next1
				i-=2

			if i==1:
				current2=current1.next
				next2=current2.next

				if pre1:
					pre1.next=current2
				current2.next=current1
				current1.next=next2

				if k==2:
					pre1=current1
					next_current1=current1.next
					if pre1:
						print "  ",pre1.val

			elif i==2:
				current2=current1.next.next
				next1=current1.next
				next2=current2.next
				if pre1:
					pre1.next=current2
				current2.next=next1
				next1.next=current1
				current1.next=next2
				if k==3:
					pre1=current1
					next_current1=current1.next

			print_list(head)

			current1=next_current1
			if k>3:
				pre1=next_pre1
 
		return head
	def isNext(self,head,k):
		i=0
		temp=head
		while(i<k-1 and temp):
			temp=temp.next
			i+=1
		if i<k-1 or not temp:
			return False
		else:
			return True

def print_list(l):
	while l:
		print l.val
		l=l.next

	print ""

def  main():
	s=Solution()
	l1=ListNode(1)
	l2=ListNode(7)
	l3=ListNode(3)
	l4=ListNode(2)
	l5=ListNode(7)
	l6=ListNode(1)
	l7=ListNode(2)
	l8=ListNode(3)
	l9=ListNode(4)

	l1.next=l2
	l2.next=l3
	l3.next=l4
	l4.next=l5
	l5.next=l6
	l6.next=l7
	l7.next=l8
	l8.next=l9

	#print_list(l1)
	ll=s.reverseKGroup(l1,3)
	print ""
	print_list(ll)

if __name__ == '__main__':
	main()