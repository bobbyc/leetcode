# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        v1 = v2 = 0
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next

            carry, val = divmod(v1+v2+carry, 10)
            #print(div, carry)
            print(val)

            n.next = ListNode(val)
            n = n.next
            v1 = v2 = 0
        return root.next

def main():
    # Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    a = ListNode(5)
    #a.next = ListNode(4)
    #a.next.next = ListNode(3)

    b = ListNode(5)
    #b.next = ListNode(6)
    #b.next.next = ListNode(4)

    s = Solution()
    answer = s.addTwoNumbers(a,b)

if __name__ == '__main__':
    main()
