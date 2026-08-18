from collections import Counter

class Solution:
    def findSubstring(self, s, words):

        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        word_freq = Counter(words)
        result = []

        for offset in range(word_len):

            left = offset
            count = 0
            current = {}

            for right in range(offset, len(s) - word_len + 1, word_len):

                word = s[right:right + word_len]

                if word not in word_freq:
                    current.clear()
                    count = 0
                    left = right + word_len
                    continue

                current[word] = current.get(word, 0) + 1
                count += 1

                while current[word] > word_freq[word]:

                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

                if count == word_count:

                    result.append(left)

                    left_word = s[left:left + word_len]
                    current[left_word] -= 1
                    left += word_len
                    count -= 1

        return result
