from collections import deque

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ''
        res = ''
        queue = deque()
        queue.append(root)
        while queue:
            level = len(queue)
            for i in range(level):
                node = queue.popleft()
                if not node:
                    res += ',None'
                    continue
                else:
                    res += ','+str(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
        return res[1:]

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(',')
        root = TreeNode(int(data[0]))
        queue = deque()
        queue.append(root)
        for i in range(1, len(data), 2):
            node = queue.popleft()
            if data[i] != 'None':
                left = TreeNode(int(data[i]))
                node.left = left
                queue.append(node.left)
            if i+1 < len(data) and data[i+1] != 'None':
                right = TreeNode(int(data[i+1]))
                node.right = right
                queue.append(node.right)
        return root



ser = Codec()
