import unittest
from ds_toolkit.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        """Initialize a new Trie for each test."""
        self.trie = Trie()

    def test_insert_and_search(self):
        """Test inserting and searching for words."""
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.assertFalse(self.trie.search("appl"))
        self.assertFalse(self.trie.search("banana"))

    def test_starts_with(self):
        """Test checking for words starting with a prefix."""
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.starts_with("app"))
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertFalse(self.trie.starts_with("ban"))

    def test_delete(self):
        """Test deleting words from the Trie."""
        self.trie.insert("apple")
        self.trie.insert("app")
        self.assertTrue(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.trie.delete("apple")
        self.assertFalse(self.trie.search("apple"))
        self.assertTrue(self.trie.search("app"))
        self.trie.delete("app")
        self.assertFalse(self.trie.search("app"))

    def test_delete_non_existent_word(self):
        """Test deleting a non-existent word."""
        self.trie.insert("apple")
        self.trie.delete("banana")
        self.assertTrue(self.trie.search("apple"))

    def test_to_list(self):
        """Test converting the Trie to a list of words."""
        words = ["apple", "app", "banana", "bat", "batman"]
        for word in words:
            self.trie.insert(word)
        trie_list = self.trie.to_list()
        self.assertEqual(sorted(trie_list), sorted(words))

    def test_empty_trie(self):
        """Test operations on an empty Trie."""
        self.assertFalse(self.trie.search("apple"))
        self.assertFalse(self.trie.starts_with("app"))
        self.assertEqual(self.trie.to_list(), [])

    def test_starts_with_edge_cases(self):
        """Test starts_with method on edge cases."""
        self.trie.insert("apple")
        self.assertTrue(self.trie.starts_with("a"))
        self.assertTrue(self.trie.starts_with("ap"))
        self.assertTrue(self.trie.starts_with("app"))
        self.assertFalse(self.trie.starts_with("appl"))
        self.assertFalse(self.trie.starts_with("banana"))


if __name__ == "__main__":
    unittest.main()
