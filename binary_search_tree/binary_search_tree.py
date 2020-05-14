"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = self
        def find_node(node):
            if value < node.value:
                if node.left is None:
                    node.left = BSTNode(value)
                    # if value has been assigned, end recursion
                    return True
                else:
                    return find_node(node.left)
            else:
                if node.right is None:
                    node.right = BSTNode(value)
                    return True
                else:
                    return find_node(node.right)
        return find_node(node)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target to self, which is the root
        # Return false when we know we need to go right or left based on comparison to the node, but that node does not have a corresponding child on that side.  Ex if target is 5, current node is 4 but it does not have a self.right
        if target == self.value:
            return True
        if target < self.value:
            # go left if possible and restart comparison, otherwise return false
            if not self.left:
                return False
            return self.left.contains(target)
        else:
            # target must be greater than self because function would have already returned True if equal or False if less than
            # go right if possible and restart comparision, otherwise return false
            if not self.right:
                return False
            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # if there is no self.right, return the current value
        # if there is a self.right, go to that node and check again until there is no self.right, then return the current value as above.
        while self.right is not None:
            self = self.right
        return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # call the fn on the value at this node 
        fn(self.value)

        # pass this function to the left child 
        if self.left:
            self.left.for_each(fn)
        # pass this function to the right child 
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


# from collections import deque

# class BSTNode:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

#     # Insert the given value into the tree
#     def insert(self, value):
#         # check if the incoming value is less than the current node's value 
#         if value < self.value:
#             # we know we need to go left 
#             # how do we know when we need to recurse again, 
#             # or when to stop? 
#             if not self.left:
#                 # we can park our value here 
#                 self.left = BSTNode(value)
#             else:
#                 # we can't park here 
#                 # keep searching 
#                 self.left.insert(value)
#         else:
#             # we know we need to go right 
#             if not self.right:
#                 self.right = BSTNode(value)
#             else:
#                 self.right.insert(value)

#     # Return True if the tree contains the value
#     # False if it does not
#     def contains(self, target):
#         # when we start searching, self will be the root
#         # compare the target against self
#         # 
#         # Criteria for returning False: we know we need to go in one direction
#         # but there's nothing in the left or right direction 
#         if target == self.value:
#             return True
#         if target < self.value:
#             # go left if left is a BSTNode
#             if not self.left:
#                 return False
#             return self.left.contains(target)
#         else:
#             # go right if right is a BSTNode
#             if not self.right:
#                 return False
#             return self.right.contains(target)

#     # Return the maximum value found in the tree
#     def get_max(self):
#         # we'll keep going right until there are no more nodes on the right side 
#         if not self.right:
#             return self.value
#         # otherwise, keep going right 
#         return self.right.get_max()

#     def iterative_get_max(self):
#         current_max = self.value 

#         current = self
#         # traverse our structure
#         while current is not None:
#             if current.value > current_max:
#                 current_max = current.value
#             # update our current_max variable if we see a larger value 
#             current = current.right

#         return current_max

#     # Call the function `fn` on the value of each node
#     # Do we expect a return from the for_each function? No 
#     def for_each(self, fn):
#         # call the fn on the value at this node 
#         fn(self.value)

#         # pass this function to the left child 
#         if self.left:
#             self.left.for_each(fn)
#         # pass this function to the right child 
#         if self.right:
#             self.right.for_each(fn)
        

#     def iterative_for_each(self, fn):
#         stack = [] 

#         # add the root node
#         stack.append(self)

#         # loop so long as the stack still has elements 
#         while len(stack) > 0:
#             current = stack.pop()
#             if current.right:
#                 stack.append(current.right)
#             if current.left:
#                 stack.append(current.left)

#             fn(current.value)

#     # Depth-First traversal 
#     # LIFO ordering of the tree elements 

#     def breadth_first_for_each(self, fn):
#         queue = deque()

#         # add the root node
#         queue.append(self)

#         # loop so long as the stack still has elements 
#         while len(queue) > 0:
#             current = queue.popleft()
#             if current.left:
#                 queue.append(current.left)
#             if current.right:
#                 queue.append(current.right)

#             fn(current.value)


# import random

# v1 = random.randint(1, 101)
# v2 = random.randint(1, 101)
# v3 = random.randint(1, 101)
# v4 = random.randint(1, 101)
# v5 = random.randint(1, 101)

# bst = BSTNode(5)

# bst.insert(v1)
# bst.insert(v2)
# bst.insert(v3)
# bst.insert(v4)
# bst.insert(v5)

# bst.for_each(lambda v: print(v))