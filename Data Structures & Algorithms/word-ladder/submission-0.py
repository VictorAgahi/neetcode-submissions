from collections import defaultdict, deque


class Solution:                
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        EDGE CASE: endWord not in wordList => instant return 0
        """
        isFound = False
        adjDico = defaultdict(list)
        for word in wordList:
            if word == endWord:
                isFound = True
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i + 1 :]
                adjDico[pattern].append(word)
        
        count_word = float('inf')
        if isFound == False:
            return 0
        queue = deque()
        queue.append((beginWord, 1))
        visited = {beginWord}
        while queue:
            current_word, score = queue.popleft()
            if current_word == endWord:
                return score

            for i in range(len(current_word)):
                pattern = current_word[:i] + "*" + current_word[i + 1 :]
                if pattern in adjDico:
                    for word in adjDico[pattern]:
                        if word not in visited:
                            visited.add(word)
                            queue.append((word, score + 1))
        return 0
            
            

        
