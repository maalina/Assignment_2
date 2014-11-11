# encoding=utf-8
# CSC 180 Assignment 2
# Christopher Chu, Alina Ma
# Result for question 1e: 72.5% correct once the algorithm was trained was
# Swann's Way.

def get_sentence_lists(text):
    """
    Break a string into sentences, which are broken into words.
    :param text:    The string to be broken up
    :return:    A list of lists of strings. The second level of lists
    corresponds to the sentences.
    """
    if text == "":
        return [[]]

    import string

    res = []
    blank = []  # accumulates the list corresponding to the current sentence.
    cur_word = ""

    # Split text along every character
    for ch in text + ".":  # ensure that our sentence always has a trailing
        # period
        if ch in ",-:;()\"\' \t\n" + string.whitespace:  # if we hit a word
        # break
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
    Return the text contained in the file filename as a string.
    :param filename:    a string containing the name of a file relative to
    the current directory
    :return:    the contents of the file as a single string.
    """
    text = open(filename, encoding="utf8").read()
    return text


def get_sentence_lists_from_files(filenames):
    """
    Question 1b. Combine the text from each of the files into a list of
    lists in the same format as question 1a.
    :param filenames:   The filenames (relative to the current directory) as
    string
    :return:    a list of list of strings, where the lists group together the
    words from that sentence.
    """
    starter = []
    for i in filenames:
        starter.extend(get_sentence_lists(get_text(i)))
    return starter


def build_semantic_descriptors(sentences):
    """
    Given a list of list of strings representing sentences, return a
    dictionary with semantic descriptors of each word.
    The semantic descriptor represents how many times the subject word and
    the other word appear in the same sentence as
    each other.

    :param sentences:   a list of list of strings, where the lists group
    together the words from that sentence.
                        (typically the output of get_sentence_lists or
                        get_sentence_lists_from_files)
    :return:    a dictionary with each word that appears in sentences as
    keys. The value is another dictionary with words as keys and values as
    the number of times the first and second keys appear in the same sentence
    """

    dictionary_count = {}

    sentences = [set(s) for s in sentences]  # convert all sentences to a set.

    # Make a list that contains all of the words.
    for sentence in sentences:
        for word in sentence:
            if word not in dictionary_count:
                dictionary_count[word] = {}

    # Populate aforementioned list.
    for word in dictionary_count:
        for sentence in sentences:
            if word in sentence:
                for new_word in sentence:
                    if (new_word != word) and (
                                new_word not in dictionary_count[word]):
                        dictionary_count[word][new_word] = 1
                    elif new_word in dictionary_count[word]:
                        dictionary_count[word][new_word] += 1
    return dictionary_count


def calculating_similarity(word, choice, semantic_descriptor):
    """
    Return the cosine similarity between two words, word and choice by
    looking through their dictionaries in semantic_descriptor
    :param word: a single word, the original question-word
    :param choice: a single word, one of the answer options given
    :param semantic_descriptor: a dictionary of semantic descriptors of words
    found in that document
    :return: the cosine similarity between two words. If there are no overlaps,
    return -1.
    """
    if word not in semantic_descriptor or choice not in semantic_descriptor:
        return -1

    word_dictionary = semantic_descriptor[word]
    choice_dictionary = semantic_descriptor[choice]
    if choice_dictionary == {}:
        similarity = -1.0
        return similarity
    top = 0
    bottom1 = 0
    bottom2 = 0
    for first_word, first_number in word_dictionary.items():
        for second_word, second_number in choice_dictionary.items():
            if first_word == second_word:
                top += first_number * second_number
    for bottom_word1, bottom_number1 in word_dictionary.items():
        bottom1 += bottom_number1 ** 2
    for bottom_word2, bottom_number2 in choice_dictionary.items():
        bottom2 += bottom_number2 ** 2
    bottom = (bottom1 * bottom2) ** 0.5
    similarity = top / bottom
    return similarity  # returns the cosine similarity value between 2 words,
    # word and choice


def most_similar_word(word, choices, semantic_descriptors):
    """
    From the words in choices, return the most similar one to word, given the
    dictionary semantic_descriptors

    :param word: a single word, the original question word we are finding a
    most similar word to
    :param choices: a list of words, from which we find the most similar word
    to word
    :param semantic_descriptors: a dictionary of semantic descriptors of
    words found in that document
    """
    max_similarity = -2.0
    for choice in choices:
        option = choice
        similarity = calculating_similarity(word, choice, semantic_descriptors)
        if similarity > max_similarity:
            max_similarity = similarity
            closest = option
    return closest


def run_similarity_test(filename, semantic_descriptors):
    """
    Return the percentage that most_similar_word guessed the most similar
    word correctly, based on the semantic descriptors
    :param filename: the name of a file, as a string which contains the
    questions,
    1st word as the question word, 2nd word as the correct answer, and the
    3rd and 4th word as word options
    :param semantic_descriptors: a semantic descriptor build based on an
    external document text.
    :return: as a float the percentage of the tests the algorithm got right
    """
    total_runs = 0
    correct = 0
    text = open(filename, encoding="utf8")

    for line in text:
        first, second, third, fourth = line.split()
        choices = [third, fourth]
        if most_similar_word(first, choices, semantic_descriptors) == second:
            total_runs += 1
            correct += 1
        else:
            total_runs += 1
    return correct / total_runs * 100


def testing_everything():
    """
    Test question 1e, i.e. how well the algorithm performs against a synonym
    questions given the corpora Warandpeace.txt and Swannsway.txt
    :return: as a float what percentage of the tests the algorithm got right
    """
    sentences = get_sentence_lists_from_files(
        ["Warandpeace.txt", "Swannsway.txt"])
    print("got files")
    descriptors = build_semantic_descriptors(sentences)
    print('descriptors built')
    percentage = run_similarity_test("test.txt", descriptors)
    print("similarity test run")
    return percentage

# import time
# t = time.time()
# print(testing_everything())
# print (time.time() - t)


if __name__ == '__main__':
    # ## QUESTION B ###
    assert get_sentence_lists(
        "Hello, Jack. How is it going? Not bad; pretty good, actually... Very "
        "very good, in fact.") == [['hello', 'jack'],
                                   ['how', 'is', 'it', 'going'],
                                   ['not', 'bad', 'pretty', 'good', 'actually'],
                                   ['very', 'very', 'good', 'in', 'fact']]

    assert get_sentence_lists(
        "Including exclamation marks would be intelligent!! What about "
        "\"quotes\"") == [['including', 'exclamation', 'marks', 'would', 'be',
                           'intelligent'], ['what', 'about', 'quotes']]

    assert get_sentence_lists(
        "This line has no trailing period. Although the case wasn't defined, "
        "let's see what happens") == [
               ['this', 'line', 'has', 'no', 'trailing', 'period'],
               ['although', 'the', 'case', 'wasn', 't', 'defined', 'let', 's',
                'see', 'what', 'happens']]

    assert get_sentence_lists("PUNCTUATION IS FUN--so we should; "
                              "improperly-punctuate:this?sentence") == [
               ['punctuation', 'is', 'fun', 'so', 'we', 'should', 'improperly',
                'punctuate', 'this'], ['sentence']]

    assert get_sentence_lists("") == [[]]
    print("Question A tested successfully")

    # ## QUESTION B ###
    assert get_sentence_lists_from_files(
        ["testcases question 1b file.txt"]) == [['hello', 'jack'],
                                                ['how', 'is', 'it', 'going'],
                                                ['not', 'bad', 'pretty', 'good',
                                                 'actually'],
                                                ['very', 'very', 'good', 'in',
                                                 'fact']]

    assert get_sentence_lists_from_files(["testcases question 1b file2.txt",
                                          "testcases question 1b file.txt"]) \
           == [
               ['including', 'exclamation', 'marks', 'would', 'be',
                'intelligent'], ['what', 'about', 'quotes'], ['hello', 'jack'],
               ['how', 'is', 'it', 'going'],
               ['not', 'bad', 'pretty', 'good', 'actually'],
               ['very', 'very', 'good', 'in', 'fact']]
    print("Question B tested successfully")

    ### QUESTION C ###
    assert (build_semantic_descriptors(
        [['hello', 'jack'], ['jack', 'is', 'good'],
         ['jack', 'is', 'not', 'bad'],
         ['jack', 'is', 'very', 'very', 'good', 'in', 'fact']]) == {
                'jack': {'in': 1, 'not': 1, 'hello': 1, 'bad': 1, 'fact': 1,
                         'very': 1, 'is': 3, 'good': 2},
                'in': {'jack': 1, 'fact': 1, 'very': 1, 'is': 1, 'good': 1},
                'not': {'bad': 1, 'jack': 1, 'is': 1}, 'hello': {'jack': 1},
                'bad': {'jack': 1, 'is': 1, 'not': 1},
                'fact': {'jack': 1, 'in': 1, 'very': 1, 'is': 1, 'good': 1},
                'very': {'jack': 1, 'in': 1, 'fact': 1, 'is': 1, 'good': 1},
                'is': {'jack': 3, 'in': 1, 'not': 1, 'bad': 1, 'fact': 1,
                       'very': 1, 'good': 2},
                'good': {'jack': 2, 'in': 1, 'fact': 1, 'very': 1, 'is': 2}})

    i_am_a_sick_man_sentence = build_semantic_descriptors(
        [['i', 'am', 'a', 'sick', 'man'], ['i', 'am', 'a', 'spiteful', 'man'],
         ['i', 'am', 'an', 'unattractive', 'man'],
         ['i', 'believe', 'my', 'liver', 'is', 'diseased'],
         ['however', 'i', 'know', 'nothing', 'at', 'all', 'about', 'my',
          'disease', 'and', 'do', 'not', 'know', 'for', 'certain', 'what',
          'ails', 'me']])

    assert i_am_a_sick_man_sentence['man'] == {"i": 3, "am": 3, "a": 2,
                                               "sick": 1, "spiteful": 1,
                                               "an": 1, "unattractive": 1}
    assert i_am_a_sick_man_sentence['liver'] == {"i": 1, "believe": 1, "my": 1,
                                                 "is": 1, "diseased": 1}
    print("Question C tested successfully")

    semantic_descriptor = {'target': {'word1': 7, 'word2': 6, 'word3': 4},
                           'similar': {'word1': 10, 'word2': 5, 'word10': 8,
                                       'word11': 3, 'word12': 1, 'word15': 1},
                           # degree of similarity: 100 / sqrt(200) = 7.01
                           'bad': {'word1': 5, 'word3': 4, 'word50': 2,
                                   'word99': 5, 'word88': 18},
                           # degree of similarity: 35+16=51 / sqrt(394) = 2.57
                           'completelydifferent': {'word10': 4, 'word16': 4,
                                                   'word5': 1},  # similarity: 0
                           'zero': {},  # similarity: 0
                           'closebutnotquite': {'word1': 7, 'word2': 5,
                                                'word3': 5, 'word10': 10},
                           # degree of similarity: 99 / sqrt(199) = 7.02
                           'alsoclose': {'word1': 4, 'word2': 6, 'word3': 9,
                                         'word15': 9},
                           # degree of similarity: 100 / sqrt(214) = 6.84
                           'alsosimilar': {'word2': 10,
                                           'word3': 10}}  # degree of
    # similarity: 100 / sqrt(200) = 7.07


    #normal cases
    assert most_similar_word('target', ['bad'], semantic_descriptor) == 'bad'
    assert most_similar_word('target',
                             ['similar', 'bad', 'completelydifferent'],
                             semantic_descriptor) == 'similar'
    assert most_similar_word('target',
                             ['closebutnotquite', 'bad', 'completelydifferent'],
                             semantic_descriptor) == 'closebutnotquite'
    assert most_similar_word('target', ['alsoclose', 'zero', 'similar'],
                             semantic_descriptor) == 'similar'

    #edge cases: ties
    assert most_similar_word('target',
                             ['alsosimilar', 'zero', 'closebutnotquite',
                              'similar'], semantic_descriptor) == 'alsosimilar'
    assert most_similar_word('target', ['similar', 'zero', 'closebutnotquite',
                                        'alsosimilar'],
                             semantic_descriptor) == 'similar'

    #error cases: zeros
    assert most_similar_word('target', ['zero'], semantic_descriptor) == 'zero'
    assert most_similar_word('target', ['completelydifferent', 'zero'],
                             semantic_descriptor) == 'completelydifferent'
    print("Question D tested successfully")

    # Question e uses the different functions together, so it is our
    # integrated test.