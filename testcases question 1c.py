#Test cases for question 1c

from synonyms import build_semantic_descriptors

print (build_semantic_descriptors(
[['hello', 'jack'],
['jack', 'is', 'good'],
['jack', 'is', 'not', 'bad'],
['jack', 'is', 'very', 'very', 'good', 'in', 'fact']]))

assert (build_semantic_descriptors(
[['hello', 'jack'],
['jack', 'is', 'good'],
['jack', 'is', 'not', 'bad'], 
['jack', 'is', 'very', 'very', 'good', 'in', 'fact']]) == 

{'jack': {'in': 1, 'not': 1, 'hello': 1, 'bad': 1, 'fact': 1, 'very': 1, 'is': 3, 'good': 2}, 
'in': {'jack': 1, 'fact': 1, 'very': 1, 'is': 1, 'good': 1}, 
'not': {'bad': 1, 'jack': 1, 'is': 1}, 'hello': {'jack': 1}, 
'bad': {'jack': 1, 'is': 1, 'not': 1}, 
'fact': {'jack': 1, 'in': 1, 'very': 1, 'is': 1, 'good': 1}, 
'very': {'jack': 1, 'in': 1, 'fact': 1, 'is': 1, 'good': 1}, 
'is': {'jack': 3, 'in': 1, 'not': 1, 'bad': 1, 'fact': 1, 'very': 1, 'good': 2}, 
'good': {'jack': 2, 'in': 1, 'fact': 1, 'very': 1, 'is': 2}})

i_am_a_sick_man_sentence = build_semantic_descriptors (
[['i', 'am', 'a', 'sick', 'man'], 
['i', 'am', 'a', 'spiteful', 'man'], 
['i', 'am', 'an', 'unattractive', 'man'], 
['i', 'believe', 'my', 'liver', 'is', 'diseased'], 
['however', 'i', 'know', 'nothing', 'at', 'all', 'about', 'my', 'disease', 'and', 'do', 'not', 'know', 'for', 'certain', 'what', 'ails', 'me']])

assert i_am_a_sick_man_sentence['man'] == {"i": 3, "am": 3, "a": 2, "sick": 1, "spiteful": 1, "an": 1, "unattractive": 1}
assert i_am_a_sick_man_sentence['liver'] == {"i": 1, "believe": 1, "my": 1, "is": 1, "diseased": 1}