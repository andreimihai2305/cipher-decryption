from typing import TypedDict

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
class NGram(TypedDict):
    ngram: str
    count: int


def get_unigrams() -> NGram:
    unigrams = dict(zip(ALPHABET, [1 for _ in range(len(ALPHABET))])) 
    return unigrams


def get_bigrams() -> NGram:
    bigrams_list = []
    for i in range(len(ALPHABET)):
        for j in range((len(ALPHABET))):
            bigrams_list.append(ALPHABET[i] + ALPHABET[j])
    bigrams = dict(zip(bigrams_list, [1 for _ in range(len(ALPHABET) ** 2)]))
    
    return bigrams

