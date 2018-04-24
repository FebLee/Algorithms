# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Palindrom:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        first = head
        #second = self.reverse_list(head)
        while first:
            print("first", first.val)
         #   print("second", second.val)
          #  if first.val != second.val:
          #      return False
            first = first.next
          #  second = second.next
            print("first", first.val)
         #   print("second", second.val)
            print()
        return True
    
    def reverse_list(self, head):
        pre = None
        while head:
            current = head
            head = head.next
            current.next = pre
            pre = current
        return pre
if __name__ =='__main__':
    x1 = ListNode(1)
    x2 = ListNode(1)
    x3 = ListNode(2)
    x4 = ListNode(1)
    x1.next = x2
    x2.next = x3
    x3.next = x4

    pali = Palindrom()

    is_pali = pali.isPalindrome(x1)
    print(is_pali)
    
