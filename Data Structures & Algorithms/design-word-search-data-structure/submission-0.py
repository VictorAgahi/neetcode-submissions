class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False        

    def addWord(self, word: str) -> None:
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = WordDictionary()
            curr = curr.children[char]
        curr.is_end = True

    
    def search_rec(self, node, word, index):
        if index == len(word):
            return node.is_end
        char = word[index]
        if char == '.':
            for key in node.children.keys():
                if self.search_rec(node.children[key], word, index + 1):
                    return True
            return False
        else:
            if char not in node.children:
                return False
            return self.search_rec(node.children[char], word, index + 1)
            
    
    
    def search(self, word: str) -> bool:
        curr = self
        return self.search_rec(curr, word, 0)
