# -*- encoding: utf-8 -*-
from functools import reduce


def map_split(word):
    return word, 1


def show_map():
    newlist = []
    with open('words.txt', 'r') as f:
        for line in f:
            words = line.split()
            r = map(map_split, words)
            for w, c in list(r):
                newlist.append((w, c))
    return newlist


ar = {}


def word_reduce(*args):
    print(args)
    if args[0][0] in ar.keys():
        ar[args[0][0]] += 1
    else:
        ar.update({args[0][0]: 1})
    return args[1]


mlist = show_map()
wr = reduce(word_reduce, mlist)
print(ar)
