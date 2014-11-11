from synonyms import get_sentence_lists_from_files

assert get_sentence_lists_from_files(["testcases_question_1b_file.txt"]) == [['hello', 'jack'],
                                                                         ['how', 'is', 'it', 'going'],
                                                                         ['not', 'bad', 'pretty', 'good', 'actually'],
                                                                         ['very', 'very', 'good', 'in', 'fact']]

assert get_sentence_lists_from_files(["testcases_question_1b_file2.txt", "testcases_question_1b_file.txt"]) == [
    ['including', 'exclamation', 'marks', 'would', 'be', 'intelligent'],
    ['what', 'about', 'quotes'],
    ['hello', 'jack'],
    ['how', 'is', 'it', 'going'],
    ['not', 'bad', 'pretty', 'good', 'actually'],
    ['very', 'very', 'good', 'in', 'fact']]

