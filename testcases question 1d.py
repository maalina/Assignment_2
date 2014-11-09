#Run 1d test cases
from synonyms import semantic_descriptor, most_similar_word

semantic_descriptor = {
    'target': {'word1': 7, 'word2': 6, 'word3': 4},
    'similar': {'word1': 10, 'word2': 5, 'word10': 8, 'word11': 3, 'word12': 1, 'word15': 1},
    # degree of similarity: 100 / sqrt(200) = 7.01
    'bad': {'word1': 5, 'word3': 4, 'word50': 2, 'word99': 5, 'word88':18},
    # degree of similarity: 35+16=51 / sqrt(394) = 2.57
    'completelydifferent': {'word10': 4, 'word16': 4, 'word5': 1},  # similarity: 0
    'zero': {},  # similarity: 0
    'closebutnotquite': {'word1': 7, 'word2': 5, 'word3': 5, 'word10': 10},  # degree of similarity: 99 / sqrt(199) = 7.02
    'alsoclose': {'word1': 4, 'word2': 6, 'word3': 9, 'word15': 9},  # degree of similarity: 100 / sqrt(214) = 6.84
    'alsosimilar': {'word2': 10, 'word3': 10}}  # degree of similarity: 100 / sqrt(200) = 7.07


#normal case 
assert most_similar_word('target', ['bad'], semantic_descriptor) == 'bad'
assert most_similar_word('target', ['similar', 'bad', 'completelydifferent'], semantic_descriptor) == 'similar'
assert most_similar_word('target', ['closebutnotquite', 'bad', 'completelydifferent'],
                         semantic_descriptor) == 'closebutnotquite'
assert most_similar_word('target', ['alsoclose', 'zero', 'similar'], semantic_descriptor) == 'similar'

#edge case: ties
assert most_similar_word('target', ['alsosimilar', 'zero', 'closebutnotquite', 'similar'],
                         semantic_descriptor) == 'alsosimilar'
assert most_similar_word('target', ['similar', 'zero', 'closebutnotquite', 'alsosimilar'],
                         semantic_descriptor) == 'similar'

#error cases: zeros
assert most_similar_word('target', ['zero'], semantic_descriptor) == 'zero'
assert most_similar_word('target', ['completelydifferent', 'zero'], semantic_descriptor) == 'completelydifferent'

