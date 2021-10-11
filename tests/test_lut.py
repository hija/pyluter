import unittest
import numpy as np

from pyluter import LUT

class TestLUT(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self._lut = LUT('tests/files/test.cube')

    def test_basic_file(self):
        pass

    def test_title(self):
        self.assertEqual("TestTitle", self._lut.title)

    def test_parse_numbers(self):
        # spacing
        np.testing.assert_equal(np.array([1,2,3]), self._lut._parse_numbers('1  2  3'))
        np.testing.assert_equal(np.array([1,2]), self._lut._parse_numbers(' 1 2'))
        np.testing.assert_equal(np.array([1]), self._lut._parse_numbers('1 '))

        # signs
        np.testing.assert_equal(np.array([-1,2,3]), self._lut._parse_numbers('-1 2 3'))
        np.testing.assert_equal(np.array([-1,-2,3]), self._lut._parse_numbers('-1 -2 3'))
        np.testing.assert_equal(np.array([-1,2,-3]), self._lut._parse_numbers('-1 2 -3'))
        np.testing.assert_equal(np.array([-1]), self._lut._parse_numbers('-1'))

        # decimals
        np.testing.assert_equal(np.array([1.5,2,3]), self._lut._parse_numbers('1.5 2 3'))
        np.testing.assert_equal(np.array([1,2.5]), self._lut._parse_numbers('1 2.5'))
        np.testing.assert_equal(np.array([1]), self._lut._parse_numbers('1.'))
        np.testing.assert_equal(np.array([0]), self._lut._parse_numbers('0.'))