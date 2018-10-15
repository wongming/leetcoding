# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        top_node = None
        last_node = None
        while l1 or l2:
            if l1 == None:
                val = l2.val
                l2 = l2.next
            elif l2 == None:
                val = l1.val
                l1 = l1.next
            elif l1.val < l2.val:
                val = l1.val
                l1 = l1.next
            else:
                val = l2.val
                l2 = l2.next
            if last_node == None:
                top_node = ListNode(val)
                last_node = top_node
            else:
                last_node.next = ListNode(val)
                last_node = last_node.next
        return top_node
