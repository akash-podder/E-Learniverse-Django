class Node:
    def __init__(self):
        self.children = {}
        self.is_last_char = False


class Trie:
    def __init__(self):
        # initializing Trie with a root Node
        self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root

        for ch in word:
            # Check if character is already present in children
            if ch not in current.children:
                current.children[ch] = Node()

            # Move to the next level in the Trie
            current = current.children[ch]

        # Mark the end of the word
        current.is_last_char = True

    def search(self, word: str) -> bool:
        current = self.root

        for ch in word:
            # If character is not found, return False
            if ch not in current.children:
                return False
            current = current.children[ch]

        # Check if this is a valid complete word
        return current.is_last_char

    def starts_with(self, prefix: str) -> bool:
        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]

        # It's a prefix, so we return True regardless of is_last_char
        return True

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))      # True
    print(trie.search("app"))        # False
    print(trie.starts_with("app"))   # True
    trie.insert("app")
    print(trie.search("app"))        # True