import heapq
from collections import defaultdict

def huffman_encoding(text):
    if not text:
        return "", {}
    
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    
    heap = [[freq, [char, ""]] for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

    huffman_codes = {pair[0]: pair[1] for pair in heap[0][1:]}
    encoded_text = "".join(huffman_codes[char] for char in text)

    return encoded_text, huffman_codes

def huffman_decoding(encoded_text, huffman_codes):
    """Decodes Huffman encoded text using the generated codes."""
    reverse_codes = {code: char for char, code in huffman_codes.items()}
    decoded_text = ""
    current_code = ""
    for bit in encoded_text:
        current_code += bit
        if current_code in reverse_codes:
            decoded_text += reverse_codes[current_code]
            current_code = ""
    return decoded_text

if __name__ == "_main_":
    text = "this is an example of huffman encoding"
    print(f"Original text: {text}\n")

    encoded_text, huffman_codes = huffman_encoding(text)
    print(f"Encoded text: {encoded_text}\n")
    print(f"Huffman codes: {huffman_codes}\n")

    decoded_text = huffman_decoding(encoded_text, huffman_codes)
    print(f"Decoded text: {decoded_text}")