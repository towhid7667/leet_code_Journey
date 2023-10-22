class TrieNode:
    def __init__(self):
        self.child = {}
        self.ending = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.child:
                curr.child[w] = TrieNode()
            curr = curr.child[w]
        curr.ending = True 

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.child.values():
                        if dfs(i+1, child):
                            return True
                    return False
                else:
                  
                    if c not in cur.child:
                        return False
                    cur = cur.child[c]
            return cur.ending 
        return dfs(0, self.root)                     




        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)