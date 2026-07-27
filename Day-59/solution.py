# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):

        result = []

        def dfs(node):
            if not node:
                result.append("N")
                return

            result.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(result)

    def deserialize(self, data):

        values = data.split(",")
        self.index = 0

        def dfs():

            if values[self.index] == "N":
                self.index += 1
                return None

            node = TreeNode(int(values[self.index]))
            self.index += 1

            node.left = dfs()
            node.right = dfs()

            return node

        return dfs()
