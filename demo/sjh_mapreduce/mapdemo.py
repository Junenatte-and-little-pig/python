# -*- encoding: utf-8 -*-
import re


def map_split(word):
    return word, 1


def show_map():
    newlist = []
    with open('words.txt', 'r') as f:
        for line in f:
            # words = line.split()
            words = re.split(r"[\[\s\]-]", line)
            words = [w for w in words if w != '']
            r = map(map_split, words)
            for w, c in list(r):
                newlist.append((w, c))
                print("%s\t%d" % (w, c))
    return newlist


mlist = show_map()
