import numpy as np
import random


def make_pairs(corp):
    for i in range(len(corp) - 1):
        yield (corp[i], corp[i + 1])


def gen():

    text = open('рандомайзер.txt', encoding='utf-8').read()

    corpus = text.split()
    pairs = make_pairs(corpus)
    word_dict = {}
    for word_1, word_2 in pairs:
        if word_1 in word_dict.keys():
            word_dict[word_1].append(word_2)
        else:
            word_dict[word_1] = [word_2]
    first_word = np.random.choice(corpus)

    while first_word.islower() or first_word == '—' or first_word == '-':
        first_word = np.random.choice(corpus)
    chain = [first_word]
    n_words = random.randint(8, 35)
    for y in range(n_words):
        try:
            chain.append(np.random.choice(word_dict[chain[-1]]))
        except KeyError:
            pass
    prt = ' '.join(chain)

    prt = prt.rsplit('.', -1)[0] + '.'
    if "!" in prt:
        prt = prt.rsplit('!', -1)[0] + '!'
    if ";" in prt:
        prt = prt.rsplit(';', -1)[0] + '.'
    if "?" in prt:
        prt = prt.rsplit('?', -1)[0] + '?'

    return prt
