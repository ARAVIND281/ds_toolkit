class TrieNode:
    """Node class for Trie."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """Trie (Prefix Tree) implementation."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insert a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        """Search for a word in the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        """Check if there is any word in the Trie that starts with the given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def delete(self, word):
        """Delete a word from the Trie."""
        def _delete(node, word, index):
            if index == len(word):
                if not node.is_end_of_word:
                    return False
                node.is_end_of_word = False
                return len(node.children) == 0
            char = word[index]
            if char not in node.children:
                return False
            can_delete = _delete(node.children[char], word, index + 1)
            if can_delete:
                del node.children[char]
                return len(node.children) == 0
            return False

        _delete(self.root, word, 0)

    def to_list(self):
        """Convert the Trie to a list of words."""
        result = []

        def _traverse(node, prefix):
            if node.is_end_of_word:
                result.append(prefix)
            for char, child in node.children.items():
                _traverse(child, prefix + char)

        _traverse(self.root, "")
        return result
