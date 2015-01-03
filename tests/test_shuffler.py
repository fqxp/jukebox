from jukebox.shuffler import Shuffler
from statistics import median, stdev, variance
import unittest


def is_randomly_distributed_in(f, l):
    median_indices = []
    for i in range(5000):
        result = f()
        indices = [result.index(i) for i in l]
        median_indices.append(median(indices))
    return round(median(median_indices))


class ShufflerTests(unittest.TestCase):

    def test_shuffle_returns_two_lists_concatenated(self):
        l1 = range(0, 100)
        l2 = range(100, 200)

        result = Shuffler().shuffle(l1, l2)

        self.assertEqual(200, len(result))
        self.assertEqual(range(0, 200), sorted(result))

    def test_shuffle_always_returns_differently_sorted_values(self):
        l1 = range(0, 100)
        l2 = range(100, 200)

        results = []
        has_duplicates = False
        for i in range(100):
            result = Shuffler().shuffle(l1, l2)
            has_duplicates = has_duplicates or result not in results
            results.append(result)
        self.assertFalse(has_duplicates)

    def test_shuffle_returns_two_lists_shuffled_randomly(self):
        l1 = range(0, 100)
        l2 = range(100, 200)

        result = Shuffler().shuffle(l1, l2)

        self.assertNotEqual(l1, filter(lambda item: item in l1, result))
        self.assertNotEqual(l2, filter(lambda item: item in l2, result))

        l = l1 + l2
        shuffler = Shuffler()
        self.assertTrue(is_randomly_distributed_in(lambda: shuffler.shuffle(l1, l2), l))

    def test_rest_of_longer_list_is_appended_to_shuffled_part(self):
        pass
