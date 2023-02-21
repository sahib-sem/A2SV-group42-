# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        h1=l1
        h2=l2
        h3=None
        carryon=0
        while h1 is not None and h2 is not None:
            num1=h1.val

            num2=h2.val


            sum=num1+num2
            if carryon:
                sum+=carryon
                carryon=0
            if sum>9:
                carryon=1
                sum%=10
            
            new_node=ListNode(sum)
            if h3:
                h3.next=new_node
                h3=h3.next
                print(h3)
            else:
                h3=new_node
                dummy=h3

            h1=h1.next
            h2=h2.next
        while h1 is not None:
            num=h1.val
            if carryon:
                num+=1
                if num>9:
                    carryon=1
                    num%=10
                else:carryon=0
            new_node=ListNode(num)
            h3.next=new_node
            h3=h3.next
            h1=h1.next
        while h2 is not None:
            num2=h2.val
            if carryon:
                num2+=1
                if num2>9:
                    carryon=1
                    num2%=10
                else:
                    carryon=0
            new_node=ListNode(num2)
            h3.next=new_node
            h3=h3.next
            h2=h2.next
        if carryon:
            new_node=ListNode(1)
            h3.next=new_node
        
        return dummy

            

            

        