# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        res = None      
        c = None
        first_node = True
        l1 = list1
        l2 = list2
        while l1 is not None  and l1.val is not None \
            and l2 is not None and l2.val is not None:
            if l1.val <= l2.val:
                if first_node:
                    res = ListNode()
                    c = res
                    c.val = l1.val                    
                else:
                    c.next = ListNode() 
                    c = c.next
                    c.val = l1.val
                l1 = l1.next
            else:
                if first_node:
                    res = ListNode()
                    c = res
                    c.val = l2.val                    
                else:
                    c.next = ListNode() 
                    c = c.next
                    c.val = l2.val
                l2 = l2.next
            first_node = False
        
        while l1 is not None and l1.val is not None:
            if first_node:
                res = ListNode()
                c = res
                c.val = l1.val                    
            else:
                c.next = ListNode() 
                c = c.next
                c.val = l1.val
            l1 = l1.next
            first_node = False

        
        while l2 is not None and l2.val is not None:
            if first_node:
                res = ListNode()
                c = res
                c.val = l2.val                    
            else:
                c.next = ListNode() 
                c = c.next
                c.val = l2.val
            l2 = l2.next
            first_node = False
        
        return res
    
def print_list_node(l:ListNode):
    c = l
    while c is not None and c.val is not None:
        print(c.val)
        c = c.next

def main():
    s = Solution()

    # list1 = ListNode(1, ListNode(2, ListNode(4)))
    # list2 = ListNode(1, ListNode(3, ListNode(4)))
    # res = s.mergeTwoLists(list1=list1, list2=list2)
    # print_list_node(res)

    # l1 = ListNode(-9, ListNode(3)) # [-9,3]
    # l2 = ListNode(5, ListNode(7)) # [5,7]
    # res = s.mergeTwoLists(l1, l2)
    # print_list_node(res)

    l1 = None
    l2 = ListNode()
    res = s.mergeTwoLists(l1, l2)
    print_list_node(res)

    
if __name__ == '__main__':
    main()
        