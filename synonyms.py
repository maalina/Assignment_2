# encoding=utf-8

the_prince = open("text.txt", encoding="utf-8").read()


def get_sentence_lists(text):
    """
    Breaks a string into sentences, which are broken into words.
    :param text:    The string to be broken up
    :return:    A list of lists of strings. The second level of lists corresponds to the sentences.
    """
    if text == "":
        return [[]]

    res = []
    blank = []  # accumulates the list corresponding to the current sentence.
    cur_word = ""

    # Split text along every character
    for ch in text + ".":  # ensure that our sentence always has a trailing period
        if ch in ",-:;()\"\' \t\n":  # if we hit a word break
            if cur_word != "":
                blank.append(cur_word.lower())
            cur_word = ""
        elif ch in ".?!":
            if cur_word != "":
                blank.append(cur_word.lower())
            if blank != []:
                res.append(blank)
            blank = []
            cur_word = ""
        else:
            cur_word += ch

    return res


def get_text(filename):
    """
    Returns the text contained in the file filename as a string.
    :param filename:    a string containing the name of a file relative to the current directory
    :return:    the contents of the file as a single string.
    """
    text = open(filename).read()
    return text


def get_sentence_lists_from_files(filenames):
    """
    Question 1b. Combines the text from each of the files into a list of lists in the same format as question 1a.
    :param filenames:   The filenames (relative to the current directory) as  string
    :return:    a list of list of strings, where the lists group together the words from that sentence.
    """
    starter = []
    for i in (filenames):
        starter.extend(get_sentence_lists(get_text(i)))
    return starter


def build_semantic_descriptors(sentences):
    """
    Given a list of list of strings representing sentences, returns a dictionary with semantic descriptors of each word.
    The semantic descriptor represents how many times the subject word and the other word appear in the same sentence as
    each other.

    :param sentences:   a list of list of strings, where the lists group together the words from that sentence.
                        (typically the output of get_sentence_lists or get_sentence_lists_from_files)
    :return:    a dictionary with each word that appears in sentences as keys. The value is another dictionary with words as keys and values as the number of times the first and second keys appear in the same sentence
    """

    dictionary_count = {}

    for sentence in sentences:  # looking at one sentence/list
        for word in sentence:  #looking at each word in the sentence/list
            if word not in dictionary_count:
                dictionary_count[word] = {}
    print (dictionary_count)
    for word in dictionary_count:  #looking at each new/inserted word in the dict
        print (word)
        for sentence in sentences:  #looking at one sentence/list
            print(sentence)
            copy_sentence = []
            for checking_word in sentence:
                if checking_word not in copy_sentence:
                    copy_sentence.append(checking_word)
             #now every copy_sentence has unique words
            print(sentence)
            print(copy_sentence)
            if word not in copy_sentence:
                for new_word in copy_sentence:
                    if new_word in dictionary_count[word]:
                        dictionary_count[word][new_word] += 0 #does not update dict for it, since it does not appear, so 0
            else:
                for new_word in copy_sentence:  #looking at each word in the sentence
                    print (new_word)
                    if (new_word != word) and (new_word not in dictionary_count[word]): #create a new dict for it, appears so 1
                        dictionary_count[word][new_word] = 1
                        print(dictionary_count)
                    elif new_word in dictionary_count[word]: #updates existing dict, adds 1, since it appears
                        dictionary_count[word][new_word] += 1
                        print(dictionary_count)
    return dictionary_count


def calculating_similarity(word, choice, semantic_descriptor):
    word_dictionary = semantic_descriptor[word]
    choice_dictionary = semantic_descriptor[choice]
    top = 0
    bottom1 = 0
    bottom2 = 0
    for i in word_dictionary:
        for j in choice_dictionary:
            if i == j:
                top += i[0] * j[0]
    for i in word_dictionary:
        bottom1 += i[0] ** 2
    for j in choice_dictionary:
        bottom2 += j[0] ** 2
    bottom = (bottom1 * bottom2) ** 0.5
    similarity = top / bottom
    return similarity #returns the cosine similarity value between 2 words, word and choice


'''Part (d) most_similar_word(word, choices, semantic_descriptors)
This function takes in a string word, a list of strings choices, and a dictionary semantic_descriptors
which is built according to the requirements for build_semantic_descriptors, and returns the element
of choices which has the largest semantic similarity to word, with the semantic similarity computed using
the data in semantic_descriptors. If the semantic similarity between two words cannot be computed, it
is considered to be −1. In case of a tie between several elements in choices, the one with the smallest index
in choices should be returned (e.g., if there is a tie between choices[5] and choices[7], choices [7] is returned'''

semantic_descriptor = {
    'target': {'word1': 7, 'word2': 6, 'word3': 4},
    'similar': {'word1': 10, 'word2': 5, 'word10': 8, 'word11': 3, 'word12': 1, 'word15': 1},
    # degree of similarity: 100 / sqrt(200)
    'bad': {'word1': 5, 'word3': 4},  # degree of similarity: 35+16=51 / sqrt(39)
    'completelydifferent': {'word10': 4, 'word16': 4, 'word5': 1},  # similarity: 0
    'zero': {},  # similarity: 0
    'closebutnotquite': {'word1': 7, 'word2': 5, 'word3': 5, 'word10': 10},  # degree of similarity: 99 / sqrt(199)
    'alsoclose': {'word1': 4, 'word2': 6, 'word3': 9, 'word15': 9},  # degree of similarity: 100 / sqrt(214)
    'alsosimilar': {'word2': 10, 'word3': 10}}  # degr

def most_similar_word(word, choices, semantic_descriptors):
    max_similarity = 0
    for choice in choices:
        similarity = calculating_similarity(word, choice)
        if similarity > max_similarity:
            max_similarity = similarity
            closest = choice
    print(closest)
    return(closest)

