class PrefixNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_last = False

# good task, learned about trie itself, and how its being saving numbers
class PrefixTree:
    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = PrefixNode()
            curr = curr.children[index]
        curr.is_last = True

    def search(self, word) -> bool:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return curr.is_last

    def startsWith(self, prefix) -> bool:
        curr = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                return False
            curr = curr.children[index]
        return True

            

