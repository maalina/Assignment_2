semantic_descriptor = {
    'target': {'word1': 7, 'word2': 6, 'word3': 4},
    'similar': {'word1': 10, 'word2': 5, 'word10': 8, 'word11': 3, 'word12': 1, 'word15': 1},
    # degree of similarity: 100 / sqrt(200)
    'bad': {'word1': 5, 'word3': 4},  # degree of similarity: 35+16=51 / sqrt(39)
    'completelydifferent': {'word10': 4, 'word16': 4, 'word5': 1},  # similarity: 0
    'zero': {},  # similarity: 0
    'closebutnotquite': {'word1': 7, 'word2': 5, 'word3': 5, 'word10': 10},  # degree of similarity: 99 / sqrt(199)
    'alsoclose': {'word1': 4, 'word2': 6, 'word3': 9, 'word15': 9},  # degree of similarity: 100 / sqrt(214)
    'alsosimilar': {'word2': 10, 'word3': 10}}  # degree of similarity: 100 / sqrt(200)

word_dictionary = semantic_descriptor["target"]
for word, number in word_dictionary.items():
    print (word, number)