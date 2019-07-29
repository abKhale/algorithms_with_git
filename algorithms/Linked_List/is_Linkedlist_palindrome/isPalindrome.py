import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
	def __init__(self, node_data):
		self.data = node_data
		self.next = None

	def __repr__(self):
		return "{} -> {}".format(self.data, self.next)

class SinglyLinkedList:
	def __init__(self):
		self.head = None
		self.tail = None

	def insert_node(self, node_data):
		node = SinglyLinkedListNode(node_data)

		if not self.head:
			self.head = node
		else:
			self.tail.next = node
		self.tail = node

'''checks if given linked list is Palindrome or not by RECURSIVE way.'''

def isPalindrome(head):
	if (head is None) or (head.next is None):
		return True #LinkedList is Palindrome if it is null or has only head node

	slow, cur = head, head

	while (cur.next.next != None): 
		cur = cur.next   # move cur pointer to 2nd last element

	if slow.data == cur.next.data:    # if 1st and last node are equal -> continue and 
		cur.next = None				  # delete last node as we don't need it anymore
		if slow.next != None:		  
			slow = slow.next          # move slow pointer to next node
		return isPalindrome(slow)     # call function recursively to check if slow node is equivalent to current last node

	return False					  # if slow node and current last node aren't equal then return false




def main():
	t=int(input())
    for cases in range(t):
        size = int(input())
        a = LinkedList() # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        if isPalindrome(a.head):
            print(1)
        else:
            print(0)

if __name__ == '__main__':
	main()