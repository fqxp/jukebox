import random
import itertools


class Shuffler(object):

    def shuffle(self, l1 ,l2):
        l1, l2, rest = self._split_rest(l1, l2)
        shuffled_items = l1 + l2
        random.shuffle(shuffled_items)
        random.shuffle(rest)
        return shuffled_items + rest

    def _split_rest(self, l1, l2):
        if len(l1) == len(l2):
            return l1[:], l2[:], []
        elif len(l1) > len(l2):
            return l1[:len(l2)], l2, l1[len(l2):]
        else:
            return l1, l2[:len(l1)], l2[len(l1):]

