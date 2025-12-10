class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    """
    Return True if the binary tree is height-balanced.
    """

    def check(node):
        if node is None:
            return 0, True  # height 0, balanced

        left_height, left_balanced = check(node.left)
        right_height, right_balanced = check(node.right)

        # If either subtree is unbalanced, propagate unbalanced now
        if not left_balanced or not right_balanced:
            return 0, False

        # Check height difference
        if abs(left_height - right_height) > 1:
            return 0, False

        # Height of this node
        return max(left_height, right_height) + 1, True

    _, balanced = check(root)
    return balanced
