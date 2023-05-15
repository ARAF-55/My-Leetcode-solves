class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        currentNode = self.root
        for ch in word:
            node = currentNode.children.get(ch)
            if node is None:
                node = TrieNode()
                currentNode.children[ch] = node
            currentNode = node
        currentNode.endOfString = True

    def search(self, word: str) -> bool:
        currentNode = self.root
        for ch in word:
            node = currentNode.children.get(ch)
            if node is None:
                return False
            currentNode = node
        if currentNode.endOfString:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        currentNode = self.root
        for ch in prefix:
            node = currentNode.children.get(ch)
            if node is None:
                return False
            currentNode = node
        return True
