# Python3 Program to print binary tree in 2D
COUNT = [10]

# Binary Tree Node
""" utility that allocates a newNode
with the given key """
class Node:

	# Construct to create a newNode
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

# Function to print binary tree in 2D
# It does reverse inorder traversal
def print2DUtil(root, space) :

	# Base case
	if (root == None) :
		return

	# Increase distance between levels
	space += COUNT[0]

	# Process right child first
	print2DUtil(root.right, space)

	# Print current node after space
	# count
	print()
	for i in range(COUNT[0], space):
		print(end = " ")
	print(root.data)

	# Process left child
	print2DUtil(root.left, space)

# Wrapper over print2DUtil()
def print2D(root) :
	
	# space=[0]
	# Pass initial space count as 0
	print2DUtil(root, 0)

# Driver Code
if __name__ == '__main__':

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
print2D(root)



