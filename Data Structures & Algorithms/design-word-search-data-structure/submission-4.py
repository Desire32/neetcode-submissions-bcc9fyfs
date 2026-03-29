class WordNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_last = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr.children[index] is None:
                curr.children[index] = WordNode()
            curr = curr.children[index]
        curr.is_last = True

    def _match(self, node, word): # for convinience
        for i,c in enumerate(word):
            if c == ".":
                for child in node.children:
                    if child is not None and self._match(child, word[i+1:]):
                        return True
                return False
            else:
                index = ord(c) - ord('a')
                if node.children[index] is None:
                    return False
                node = node.children[index]
        return node.is_last


    def search(self, word: str) -> bool:
        return self._match(self.root, word)
