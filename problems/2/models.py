class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def of(nums: list[int]) -> ListNode | None:
        curr = None
        prev = None
        for num in reversed(nums):
            curr = ListNode(num, prev)
            prev = curr
        return curr