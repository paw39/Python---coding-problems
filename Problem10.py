# This problem was asked by Microsoft.
#
# Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list.
# If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
#
# For example, given the set of words 'quick', 'brown', 'the', 'fox',
#  and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
#
# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond",
# return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

words = ['quick', 'brown', 'the', 'fox']
words2 = ['bed', 'bath', 'bedbath', 'and', 'beyond']
sentence = "thequickbrownfox"
sentence2 = "bedbathandbeyond"
result = []

def f(words, sentence, result):
    for word in words:
        start = sentence.find(word)
        stop = sentence.find(word) + len(word)
        result.append((sentence[start:stop], start))
    result = sorted(result, key=lambda x: x[1])
    print([x[0] for x in result])

f(words2, sentence2, result)

