class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
      if root is None:
        return True
      return self.checkSym(root.left, root.right)
      
    def checkSym(self, left, right) -> bool:
      if left is None and right is None:
        return True
      elif left is None or right is None:
        return False
      if left.val == right.val:
        return self.checkSym(left.left, right.right) and self.checkSym(left.right, right.left)
      return False