# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwo(self, l1, l2):
            d = ListNode()
            tail = d
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next   
                tail = tail.next           
            if l1:
                tail.next = l1
            if l2:
                tail.next = l2
            return d.next    
        if not lists:
            return None
        while len(lists) > 1:
            merged = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    mer = mergeTwo('',lists[i], lists[i + 1])
                    merged.append(mer)
                else:
                    merged.append(lists[i])
            lists = merged        
        return lists[0]            
        