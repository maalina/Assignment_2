# encoding=utf-8

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
    text = open(filename, encoding="utf8").read()
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

    sentences = [set(s) for s in sentences]  # convert all sentences to a set.

    for sentence in sentences:  # looking at one sentence/list
        for word in sentence:  #looking at each word in the sentence/list
            if word not in dictionary_count:
                dictionary_count[word] = {}
    for word in dictionary_count:  #looking at each new/inserted word in the dict
        for sentence in sentences:  #looking at one sentence/list
            if word in sentence:
                for new_word in sentence:  #looking at each word in the sentence
                    if (new_word != word) and (new_word not in dictionary_count[word]): #create a new dict for it, appears so 1
                        dictionary_count[word][new_word] = 1
                    elif new_word in dictionary_count[word]: #updates existing dict, adds 1, since it appears
                        dictionary_count[word][new_word] += 1
    return dictionary_count

def calculating_similarity(word, choice, semantic_descriptor):
    """
    Return the cosine similarity between two words, word and choice by looking through their dictionaries in semantic_descriptor
    :param word: a single word, the original question-word
    :param choice: a single word, one of the answer options given
    :param semantic_descriptor: a dictionary of semantic descriptors of words found in that document
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
    return similarity  # returns the cosine similarity value between 2 words, word and choice

def most_similar_word(word, choices, semantic_descriptors):
    """
    From the words in choices, return the most similar one to word, given the dictionary semantic_descriptors

    :param word: a single word, the original question word we are finding a most similar word to
    :param choices: a list of words, from which we find the most similar word to word
    :param semantic_descriptors: a dictionary of semantic descriptors of words found in that document
    """
    max_similarity = -2.0
    for choice in choices:
        option = choice
        similarity = calculating_similarity(word, choice, semantic_descriptors)
        if similarity > max_similarity:
            max_similarity = similarity
            closest = option
    return closest #for the error cases, why is closest referenced before assignment as a local var

def run_similarity_test(filename, semantic_descriptors):
    """
    Return the percentage that most_similar_word guessed the most similar word correctly, based on the semantic descriptors
    :param filename: the name of a file, which contains the questions, 1st word as the question word, 2nd word as the correct answer, and the 3rd and 4th word as word options
    :param semantic_descriptors: a semantic descriptor build based on an external document text
    """
    total_runs = 0
    correct = 0
    text = open(filename, encoding="utf8")

    for line in text:  # looking at the first four words
        first, second, third, fourth = line.split()
        choices = [third, fourth]
        if most_similar_word(first, choices, semantic_descriptors) == second:
            total_runs += 1
            correct += 1
        else:
            total_runs +=1
    return correct / total_runs * 100

def testing_everything():
    sentences = get_sentence_lists_from_files(["Warandpeace.txt", "Swansway.txt"])
    print ("got files")
    descriptors = build_semantic_descriptors(sentences)
    print ('descriptors built')
    percentage = run_similarity_test("test.txt", descriptors)
    print ("similarity test run")
    return percentage

print(testing_everything())