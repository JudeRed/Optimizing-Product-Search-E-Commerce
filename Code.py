# Hash Map for Product Search
class ProductSearch:
    def __init__(self):
        self.products = {}

    def add_product(self, sku, product_name):
        self.products[sku] = product_name

    def search_by_sku(self, sku):
        return self.products.get(sku, 'Product not found')

    def search_by_keyword(self, keyword):
        results = []
        for sku, name in self.products.items():
            if keyword.lower() in name.lower():
                results.append((sku, name))
        return results

# Trie for Autocomplete
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_product(self, product_name):
        node = self.root
        for char in product_name:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return self._get_all_words_with_prefix(node, prefix)

    def _get_all_words_with_prefix(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, next_node in node.children.items():
            results.extend(self._get_all_words_with_prefix(next_node, prefix + char))
        return results
