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
    for word in dictionary_count:  # each new/inserted word in the dict
        for sentence in sentences:  #looking at one sentence/list
            for new_word in sentence:  #looking at each word in the sentence
                if (new_word != word) and (new_word not in dictionary_count[
                    word]):  #not sure about first past since new_word is a word and word is a dictionary, but make sure we're comparing words, not using the same ones...?
                    word[new_word] = 1
                elif new_word in dictionary_count[word]:
                    word[new_word] += 1
    return dictionary_count


def calculating_similarity(word, choice):
    top = 0
    bottom1 = 0
    bottom2 = 0
    for i in word:
        for j in choice:
            if i == j:
                top += i[0] * j[0]
    for i in word:
        bottom1 += i[0] ** 2
    for i in choice:
        bottom2 += j[0] ** 2
    bottom = (bottom1 + bottom2) ** 0.5
    similarity = top / bottom
    return similarity


'''Part (d) most_similar_word(word, choices, semantic_descriptors)
This function takes in a string word, a list of strings choices, and a dictionary semantic_descriptors
which is built according to the requirements for build_semantic_descriptors, and returns the element
of choices which has the largest semantic similarity to word, with the semantic similarity computed using
the data in semantic_descriptors. If the semantic similarity between two words cannot be computed, it
is considered to be −1. In case of a tie between several elements in choices, the one with the smallest index
in choices should be reutrned (e.g., if there is a tie between choices[5] and choices[7], choices [7] is returned'''


def most_similar_word(word, choices, semantic_descriptors):
    pass