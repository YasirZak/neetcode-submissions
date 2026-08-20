# Use trie for this
class TrieNode:
    def __init__(self):
        self.isEnd = False
        self.children = {}

class PrefixTree:

    def __init__(self):
        self.h = TrieNode()

    def insert(self, word: str) -> None:
        i=0
        node=self.h
        while i<len(word) and word[i] in node.children:
            node = node.children[word[i]]
            i+=1

        while i<len(word):
            child=TrieNode()
            node.children[word[i]]=child
            node=child
            i+=1

        node.isEnd=True


    def search(self, word: str) -> bool:
        i=0
        node=self.h
        while i<len(word):
            if word[i] not in node.children:
                return False
            node=node.children[word[i]]
            i+=1

        return node.isEnd
        

    def startsWith(self, prefix: str) -> bool:
        i=0
        node=self.h
        while i<len(prefix):
            if prefix[i] not in node.children:
                return False
            node=node.children[prefix[i]]
            i+=1

        return True
        
        