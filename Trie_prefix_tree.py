class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        currentNode = self.root
        for ch in word:
            node = currentNode.children.get(ch)
            if node is None:
                node = TrieNode()
                currentNode.children[ch] = node
            currentNode = node
        currentNode.endOfString = True

    def search(self, word):
        currentNode = self.root
        for ch in word:
            node = currentNode.children.get(ch)
            if node is None:
                return False
            currentNode = node
        if not currentNode.endOfString:
            return False
        else:
            return True

    def delete(self, word):

        def delete_helper(root, the_word, index):
            ch = the_word[index]
            currentNode = root.children.get(ch)
            if not currentNode:
                return False
            if index == len(the_word) - 1:
                if len(currentNode.children) >= 1:
                    currentNode.endOfString = False
                    return False
                else:
                    root.children.pop(ch)
                    return True
            if len(currentNode.children) > 1 or currentNode.endOfString:
                delete_helper(currentNode, the_word, index + 1)
                return False
            will_delete = delete_helper(currentNode, the_word, index + 1)
            if will_delete:
                root.children.pop(ch)
                return True
            else:
                return False

        delete_helper(self.root, word, 0)
        return


my_trie = Trie()
my_trie.insert("API")
my_trie.insert("APIS")
my_trie.insert("K")
print(my_trie.search("API"))
print(my_trie.search("APIS"))
print(my_trie.search("K"))
my_trie.delete("K")
print(my_trie.search("API"))
print(my_trie.search("APIS"))
print(my_trie.search("K"))
