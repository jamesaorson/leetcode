from models import ListNode
from typing import Optional

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        if l1 is None:
            print('l1 is None')
            return l2 if l2 else None
        if l2 is None:
            print('l2 is None')
            return l1 if l1 else None
        curr_1 = l1
        curr_2 = l2
        result_head = None
        result_prev = None
        result_curr = None
        while curr_1 is not None and curr_2 is not None:
            if result_curr is None:
                result_head = ListNode()
                result_curr = result_head
            else:
                result_curr = ListNode()
            if carry > 0:
                val = 1
                carry = 0
            else:
                val = 0
            val += (curr_1.val + curr_2.val)
            if val >= 10:
                val -= 10
                carry = 1
            result_curr.val = val
            if result_prev is not None:
                result_prev.next = result_curr
            result_prev = result_curr
            curr_1, curr_2 = curr_1.next, curr_2.next
        if curr_1 is not None:
            # add remaining digits
            while curr_1 is not None:
                result_curr = ListNode()
                if carry > 0:
                    val = 1
                    carry = 0
                else:
                    val = 0
                val += curr_1.val
                if val >= 10:
                    val -= 10
                    carry = 1
                result_curr.val = val
                if result_prev is not None:
                    result_prev.next = result_curr
                result_prev = result_curr
                curr_1 = curr_1.next
        elif curr_2 is not None:
            while curr_2 is not None:
                result_curr = ListNode()
                if carry > 0:
                    val = 1
                    carry = 0
                else:
                    val = 0
                val += curr_2.val
                if val >= 10:
                    val -= 10
                    carry = 1
                result_curr.val = val
                if result_prev is not None:
                    result_prev.next = result_curr
                result_prev = result_curr
                curr_2 = curr_2.next
        if carry > 0:
            result_curr.next = ListNode(carry, None)
        return result_head
