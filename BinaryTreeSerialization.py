"""
A script to serialize and deserialize Binary Trees in Python
"""


class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'Node({})'.format(self.val)


"""
My BT
          1
         / \
        3   4
       /   / \
      6   7   8
"""




def serialize_bt(bt):
    components = []

    def incorporate(bt, components):
        components.append(str(bt.val))
        if bt.left:
            components.append('L')
            incorporate(bt.left, components)
        if bt.right:
            components.append('R')
            incorporate(bt.right, components)
        components.append('U')
        return ''.join(components)

    incorporate(bt, components)
    components.pop()
    return ''.join(components)


def deserialize(string):
    chars = ''
    nodes = []
    next_child = None
    for i, char in enumerate(string):
        if char not in ('L', 'R', 'U'):
            chars += char
        else:
            if not nodes:
                nodes.append(Node(int(chars)))
            elif next_child == 'left':
                nodes[-1].left = Node(int(chars))
                nodes.append(nodes[-1].left)
            elif next_child == 'right':
                nodes[-1].right = Node(int(chars))
                nodes.append(nodes[-1].right)
            elif next_child == 'up':
                nodes.pop()
            if char == 'L':
                next_child = 'left'
            elif char == 'R':
                next_child = 'right'
            elif char == 'U':
                next_child = 'up'
            chars = ''
    return nodes[0]


def deserialize_recursive(string):
    list_ = []
    chars = ''
    for char in string:
        if char in ('L', 'R', 'U'):
            if chars:
                list_.append(int(chars))
                chars = ''
            list_.append(char)
        else:
            chars += char
    list_.reverse()

    nodes = [Node(list_.pop())]  # The root node

    def rebuild():
        val = list_.pop()
        if val == 'L':
            nodes[-1].left = Node(list_.pop())
            nodes.append(nodes[-1].left)
        if val == 'R':
            nodes[-1].right = Node(list_.pop())
            nodes.append(nodes[-1].right)
        if val == 'U':
            nodes.pop()
        if list_:
            rebuild()

    rebuild()
    return nodes[0]


BT = Node(1)
BT.left = Node(3)
BT.left.left = Node(6)
BT.right = Node(4)
BT.right.left = Node(7)
BT.right.right = Node(8)

print(serialize_bt(BT))
