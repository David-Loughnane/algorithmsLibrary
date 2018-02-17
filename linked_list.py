"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current = self.head
        for i in range(position - 1):
            if current is None:
                return None
            else:
                current = current.next
        return current

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            first = self.head
            for i in range(position - 2):
                first = first.next
            new_element.next = first.next
            first.next = new_element

    def delete(self, value):
        """Delete the first node with a given value."""
        previous = self.head
        if previous.value == value:
            self.head = previous.next
        current = previous.next

        if current.value == value:
            previous.next = current.next
        else:
            current = current.next


# Test cases
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)


assert ll.head.next.next.value == 3

assert ll.get_position(3).value == 3

ll.insert(e4, 3)
assert ll.get_position(3).value == 4

ll.delete(1)
assert ll.get_position(1).value == 2
assert ll.get_position(2).value == 4
assert ll.get_position(3).value == 3
