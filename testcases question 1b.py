from sentences import *

assert get_sentence_lists_from_files(["testcases question 1b file"]) == [['hello', 'jack'],
                                                                         ['how', 'is', 'it', 'going'],
                                                                         ['not', 'bad', 'pretty', 'good', 'actually'],
                                                                         ['very', 'very', 'good', 'in', 'fact']]

assert get_sentence_lists_from_files(["testcases question 1b file2", "testcases question 1b file"]) == [
    ['including', 'exclamation', 'marks', 'would', 'be', 'intelligent'],
    ['what', 'about', 'quotes'],
    ['hello', 'jack'],
    ['how', 'is', 'it', 'going'],
    ['not', 'bad', 'pretty', 'good', 'actually'],
    ['very', 'very', 'good', 'in', 'fact']]

