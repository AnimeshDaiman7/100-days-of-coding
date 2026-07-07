class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        index = {value: i for i, value in enumerate(inorder)}
        pre = 0

        def build(left, right):
            nonlocal pre

            if left > right:
                return None

            root_val = preorder[pre]
            pre += 1

            root = TreeNode(root_val)

            mid = index[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)
