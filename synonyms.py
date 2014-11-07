# encoding=utf-8

text = open("text.txt", encoding="utf-8").read()


def get_sentence_lists(text):
    text = text.split()
    rec = []
    blank = []
    for i in text:
        if i == i.strip(".?!"):
            blank.append((i.strip(",-:;--!()?\"\'")).lower())
        else:
            blank.append((i.strip(".?!")).lower())
            rec.append(blank)
            blank = []
    return rec


def get_text(filename):
    global text
    text = open('%r').read().split() % (filename)
    return text


def get_sentence_lists_from_files(filenames):
    for i in (filenames):
        get_text(i)
        print(get_sentence_lists(text))


def build_semantic_descriptors(sentences):
    dictionary_count = {}

    for sentence in sentences:  # looking at one sentence/list
        for word in sentence:  #looking at each word in the sentence/list
            if word not in dictionary_count:
                dictionary_count[word] = {}
            else:
                pass
    for word in dictionary_count:  # each new/inserted word in the dict
        for sentence in sentences:  #looking at one sentence/list
            for new_word in sentence:  #looking at each word in the secntence
                if (new_word != word) and (new_word not in dictionary_count[
                    word]):  #not sure about first past since new_word is a word and word is a dictionary, but make sure we're comparing words, not using the same ones...?
                    word[new_word] = 1
                elif new_word in dictionary_count[word]:
                    word[new_word] += 1
    return dictionary_count


print(get_sentence_lists(text))

'''Part (b) get_sentence_lists_from_files(filenames)
This function takes in a list of strings filenames, each one the name of a text file, and returns the list of
every sentence contained in all the text files in filenames, in order.'''


def get_sentence_lists_from_files(filenames):
    for i in (filenames):
        get_text(i)
        print(get_sentence_lists(text))


def build_semantic_descriptors(sentences):
    dictionary_count = {}

    for sentence in sentences:  # looking at one sentence/list
        for word in sentence:  #looking at each word in the sentence/list
            if word not in dictionary_count:
                dictionary_count[word] = {}
            else:
                pass
    for word in dictionary_count:  # each new/inserted word in the dict
        for sentence in sentences:  #looking at one sentence/list
            for new_word in sentence:  #looking at each word in the secntence
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