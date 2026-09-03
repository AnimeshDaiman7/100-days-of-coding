from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):

        words = set(wordList)

        if endWord not in words:
            return []

        parents = defaultdict(list)
        queue = deque([beginWord])
        visited = {beginWord}
        found = False

        while queue and not found:

            level_visited = set()

            for _ in range(len(queue)):

                word = queue.popleft()

                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        next_word = word[:i] + ch + word[i + 1:]

                        if next_word not in words:
                            continue

                        if next_word not in visited:
                            if next_word not in level_visited:
                                level_visited.add(next_word)
                                queue.append(next_word)

                            parents[next_word].append(word)

                            if next_word == endWord:
                                found = True

                        elif next_word in level_visited:
                            parents[next_word].append(word)

            visited.update(level_visited)

        result = []
        path = [endWord]

        def backtrack(word):
            if word == beginWord:
                result.append(path[::-1])
                return

            for parent in parents[word]:
                path.append(parent)
                backtrack(parent)
                path.pop()

        if found:
            backtrack(endWord)

        return result
