def maxDepth(root):
  max_depth = 0

  if root is None:
      return max_depth

  left_depth = maxDepth(root.left)
  right_depth = maxDepth(root.right)
  max_depth = max(left_depth, right_depth) + 1
  return max_depth

maxDepth(root)