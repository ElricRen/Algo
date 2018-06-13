# Node data structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def merge(self, head1, head2):
        """
        Merge two already sorted linked list.
        Use an empty head to point to the head of result.
        :param head1: head of linked list1
        :param head2: head of linked list2
        :return: the head of merged linked list
        """
        curr = empty_head = Node(None)

        while head1 and head2:
            if head1.data < head2.data:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next

        if head1:
            curr.next = head1
        else:
            curr.next = head2

        return empty_head.next


# Simple test case
if __name__ == '__main__':
    h1 = Node(1)
    h1.next = Node(2)
    h2 = Node(1)
    h2.next = Node(1)
    h = Solution().merge(h1, h2)
    while h:
        print(h.data)
        h = h.next