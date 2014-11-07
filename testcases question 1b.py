from synonyms import get_sentence_lists_from_files

assert get_sentence_lists_from_files(["testcases question 1b file.txt"]) == [['hello', 'jack'],
                                                                         ['how', 'is', 'it', 'going'],
                                                                         ['not', 'bad', 'pretty', 'good', 'actually'],
                                                                         ['very', 'very', 'good', 'in', 'fact']]

assert get_sentence_lists_from_files(["testcases question 1b file2.txt", "testcases question 1b file.txt"]) == [
    ['including', 'exclamation', 'marks', 'would', 'be', 'intelligent'],
    ['what', 'about', 'quotes'],
    ['hello', 'jack'],
    ['how', 'is', 'it', 'going'],
    ['not', 'bad', 'pretty', 'good', 'actually'],
    ['very', 'very', 'good', 'in', 'fact']]

