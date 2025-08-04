import collections
import heapq


class Node:
    def __init__(self, symbol=None, frequency=0, left=None, right=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.frequency < other.frequency


def build_huffman_tree(text):
    # Counting the frequencies of symbols in the text
    frequencies = collections.Counter(text)

    # Create nodes for each character
    priority_queue = [Node(symbol=s, frequency=f) for s, f in frequencies.items()]
    heapq.heapify(priority_queue)

    # Construction of a code tree
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = Node(
            frequency=left.frequency + right.frequency, left=left, right=right
        )
        heapq.heappush(priority_queue, merged_node)

    return priority_queue[0]


def build_huffman_codes(node, current_code="", codes={}):
    # Recursive construction of codes for each character
    if node.symbol is not None:
        codes[node.symbol] = current_code
    if node.left is not None:
        build_huffman_codes(node.left, current_code + "0", codes)
    if node.right is not None:
        build_huffman_codes(node.right, current_code + "1", codes)


def huffman_encoding(text):
    # Construction of a code tree
    root = build_huffman_tree(text)

    # Construction of codes for each character
    codes = {}
    build_huffman_codes(root, "", codes)

    # Text encoding by received codes
    encoded_text = "".join(codes[char] for char in text)

    return encoded_text, codes


if __name__ == "__main__":
    # Usage example
    text_example = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
    encoded_text, huffman_codes = huffman_encoding(text_example)

    huffman_codes = dict(sorted(huffman_codes.items()))

    print("Coding scheme:")
    for symbol, code in huffman_codes.items():
        print(f"'{symbol}': {code}")

    print("Encoded text:", encoded_text)
