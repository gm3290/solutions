class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the mergeLists function below.

def mergeLists(head1, head2):
    mergedList = SinglyLinkedList()
    while head1 and head2 is not None:
        if head1.data < head2.data:
            mergedList.insert_node(head1.data)
            head1 = head1.next
        else:
            mergedList.insert_node(head2.data)
            head2 = head2.next
    if head1 is None:
        mergedList.tail.next = head2
    else:
        mergedList.tail.next = head1

    return mergedList.head