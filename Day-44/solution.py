from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        ans = []
        queue = deque([root])

        while queue:

            size = len(queue)

            for i in range(size):

                node = queue.popleft()

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

                if i == size - 1:
                    ans.append(node.val)

        return ans
