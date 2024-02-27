import re
from collections import Counter

def words(text): return re.findall(r'\d*\w+', text.lower())

WORDS = Counter(words(open('assets/biblebooknames.csv').read()))

def P(word, N=sum(WORDS.values())):
    # "Probability of `word`."
    return WORDS[word] / N

def correction(word):
    # "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word):
    # "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words):
    # # "The subset of `words` that appear in the dictionary of WORDS."
    # return set(w for w in words if w in WORDS)

    # "The subset of `words` that appear in the dictionary of WORDS."
    known_words = set()
    for w in words:
        if w in WORDS:
            known_words.add(w)
        else:
            print(f"'{w}' is not a known word.")
    print("Known words:", known_words)
    return known_words

def edits1(word):
    # "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)] # [('', 'kemarin'), ('k', 'emarin'), ('ke', 'marin'), dst]
    deletes    = [L + R[1:]               for L, R in splits if R] # ['emarin', 'kmarin', 'kearin', dst]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1] # ['ekmarin', 'kmearin', 'keamrin', dst]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters] # ['aemarin', 'bemarin', 'cemarin', dst]
    inserts    = [L + c + R               for L, R in splits for c in letters] # ['akemarin', 'bkemarin', 'ckemarin', dst]
    return set(deletes + transposes + replaces + inserts)

def edits2(word):
    # "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))

kata = '1 timotias'
print('kata typo : ', kata)
print('koreksi : ', correction(kata))
print('candidates:', candidates(kata))
print('known:', known([kata]))
print('known(edits1):', known(edits1(kata)))
print('known(edits2):', known(edits2(kata)))