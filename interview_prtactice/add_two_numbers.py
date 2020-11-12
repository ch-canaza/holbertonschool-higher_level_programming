#!/usr/bin/python3
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        l1 = [2,4,3], 
        l2 = [5,6,4]
        

class Solution:
    def addTwoNumbers(self, l1, l2):
      
        p1 = l1.next
        p2 = l2.next
        #l3 = ListNode()
        #p3 = l3
        carry = 0
        adition = 0
        while (p1 is not None or p2 is not None or carry):
            if p1 == None:
                p1 = ListNode(0)
            if p2 == ListNode(0):
                p2 = 0
            addition = p1.val + p2.val
            module = adition % 10
            carry = adition // 10
            if p1 and p2:
                p3 = ListNode()

                p3 = p3.next
            
            p1 = p1.next
            p2 = p2.next

        while l1:
            p3.next = ListNode()
            p3 = p3.next
            add1 = l1.val + carry
            carry = add1//10
            add1 =add1%10
            p3.val = add1

            l1 = l1.next

        while l2:
            p3.next = ListNode()
            p3 = p3.next
            add1 = l2.val + carry
            carry = add1//10
            add1 =add1%10
            p3.val = add1

            l2 = l2.next

        if carry != 0:
            p3.next = ListNode()
            p3 = p3.next
            p3.val = carry
            

            



    
    
        