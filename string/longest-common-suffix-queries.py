from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.best_index = -1
        self.best_length = float('inf')
class Solution:
    def stringIndices(self, wordsContainer: List[str], wordsQuery: List[str]) -> List[int]:
        root = TrieNode()
        min_len = float('inf')
        min_idx = 0
        for i, word in enumerate(wordsContainer):
            if len(word) < min_len:
                min_len = len(word)
                min_idx = i
        for i, word in enumerate(wordsContainer):
            node = root
            rev_word = word[::-1]
            for ch in rev_word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if len(word) < node.best_length:
                    node.best_length = len(word)
                    node.best_index = i
        ans = []
        for word in wordsQuery:
            node = root
            res = min_idx
            for ch in word[::-1]:
                if ch not in node.children:
                    break
                node = node.children[ch]
                res = node.best_index
            ans.append(res)
        return ans