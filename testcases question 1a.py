from synonyms import *
#print(get_sentence_lists("Hello, Jack. How is it going? Not bad; pretty good, actually... Very very good, in fact."))
assert get_sentence_lists(
    "Hello, Jack. How is it going? Not bad; pretty good, actually... Very very good, in fact.") == [['hello', 'jack'],
                                                                                                    ['how', 'is', 'it',
                                                                                                     'going'],
                                                                                                    ['not', 'bad',
                                                                                                     'pretty', 'good',
                                                                                                     'actually'],
                                                                                                    ['very', 'very',
                                                                                                     'good', 'in',
                                                                                                     'fact']]
#print(get_sentence_lists("Including exclamation marks would be intelligent!! What about \"quotes\""))
assert get_sentence_lists("Including exclamation marks would be intelligent!! What about \"quotes\"") == [
    ['including', 'exclamation', 'marks', 'would', 'be', 'intelligent'], ['what', 'about', 'quotes']]

#print(get_sentence_lists("This line has no trailing period. Although the case wasn't defined, let's see what happens"))
assert get_sentence_lists(
    "This line has no trailing period. Although the case wasn't defined, let's see what happens") == [
           ['this', 'line', 'has', 'no', 'trailing', 'period'],
           ['although', 'the', 'case', 'wasn', 't', 'defined', 'let', 's', 'see', 'what', 'happens']]

#print(get_sentence_lists("PUNCTUATION IS FUN--so we should; improperly-punctuate:this?sentence"))
assert get_sentence_lists("PUNCTUATION IS FUN--so we should; improperly-punctuate:this?sentence") == [
    ['punctuation', 'is', 'fun', 'so', 'we', 'should', 'improperly', 'punctuate', 'this'], ['sentence']]

#print(get_sentence_lists(""))
assert get_sentence_lists("") == [[]]
