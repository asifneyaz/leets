"""

                              1

                    4

          8

                    13

5

          4

                              2

                    11

                              7


Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Example 3:

Input: root = [1,2], targetSum = 0
Output: false

"""


#define a node object and thus build a binary tree first
class Node(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        if root == None:
            return False
        else:
            current = root
            s = []
            s.append(current)
            s.append(current.val)

            while s != []:
                pathsum = s.pop()
                current = s.pop()

                if not current.left and not current.right:
                    if pathsum == sum:
                        return True
                if current.right:
                    rightpathsum = pathsum + current.right.val
                    s.append(current.right)
                    s.append(rightpathsum)
                if current.left:
                    leftpathsum = pathsum + current.left.val
                    s.append(current.left)
                    s.append(leftpathsum)
            return False
                

#builing binary tree here by adding each nodes
root = Node(5)
root.left = Node(4)
root.right = Node(8)
root.left.left = Node(11)
root.left.right = None
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right.left = Node(13)
root.right.left.left = None
root.right.left.right =None
root.right.right = Node(4)
root.right.right.left = None
root.right.right.right = Node(1)            

#driver function
sol = Solution().hasPathSum(root, 22)
print(sol)