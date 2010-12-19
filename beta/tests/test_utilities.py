import unittest

from numpy import array

import beta.utilities

class TestCoordHandling(unittest.TestCase):

    def test_split_coords(self):
        cases = {
            (0, 0): (0, 0, 0, 0),
            (1, 1): (0, 1, 0, 1),
            (16, 16): (1, 0, 1, 0),
            (-1, -1): (-1, 15, -1, 15),
            (-16, -16): (-1, 0, -1, 0),
        }
        for x, z in cases:
            self.assertEqual(beta.utilities.split_coords(x, z), cases[x, z])

class TestBitTwiddling(unittest.TestCase):

    def test_unpack_nibbles(self):
        self.assertEqual(beta.utilities.unpack_nibbles(["a"]), [6, 1])
        self.assertEqual(beta.utilities.unpack_nibbles("nibbles"),
            [6, 14, 6, 9, 6, 2, 6, 2, 6, 12, 6, 5, 7, 3])

    def test_pack_nibbles(self):
        self.assertEqual(list(beta.utilities.pack_nibbles(array([6, 1]))),
            ["a"])
        self.assertEqual(
            list(beta.utilities.pack_nibbles(
                    array([6, 14, 6, 9, 6, 2, 7, 3]))),
            list("nibs"))
