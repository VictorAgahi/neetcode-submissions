class Trie:
    def __init__(self):
        self.children = {}
        self.word = None
    def add_word(self, word):
        curr = self
        for char in word:
            if char not in curr.children:
                curr.children[char] = Trie()
            curr = curr.children[char]
        curr.word = word

class Solution:

  def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    trie = Trie()
    for word in words:
      trie.add_word(word)

    rows, cols = len(board), len(board[0])
    visited = set()
    res = []

    def dfs(x, y, node):
      if x < 0 or x >= rows or y < 0 or y >= cols or (x, y) in visited:
        return
      if board[x][y] not in node.children:
        return

      next_node = node.children[board[x][y]]
      if next_node.word:
        res.append(next_node.word)
        next_node.word = None

      visited.add((x, y))
      dfs(x - 1, y, next_node)
      dfs(x + 1, y, next_node)
      dfs(x, y + 1, next_node)
      dfs(x, y - 1, next_node)
      visited.remove((x, y))

    for x in range(rows):
      for y in range(cols):
        dfs(x, y, trie)
    return res