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

"""



class Node(object):
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None



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
                

            

sol = Solution().hasPathSum(root, 22)
print(sol)