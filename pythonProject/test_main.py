import sys
import unittest
from unittest.mock import MagicMock
import numpy as np

# Mock dependencies before importing main
mock_pygame = MagicMock()
class MockEvent:
    type = 2
    key = 27
mock_pygame.event.get.return_value = [MockEvent()]
sys.modules['pygame'] = mock_pygame

mock_cv2 = MagicMock()
mock_cv2.VideoCapture().read.return_value = (True, MagicMock())
sys.modules['cv2'] = mock_cv2

import main

class TestMain(unittest.TestCase):
    def test_crop_frame_shape(self):
        # crop_frame rotates 90 degrees then flips vertically

        # Original: 3 rows, 4 cols
        # [0 1 2 3]
        # [4 5 6 7]
        # [8 9 A B]

        # After rot90 (k=1 default is counter-clockwise):
        # [3 7 B]
        # [2 6 A]
        # [1 5 9]
        # [0 4 8]
        # Shape becomes: 4 rows, 3 cols

        # After flipud (vertical flip):
        # [0 4 8]
        # [1 5 9]
        # [2 6 A]
        # [3 7 B]

        frame = np.array([
            [0, 1, 2, 3],
            [4, 5, 6, 7],
            [8, 9, 10, 11]
        ])

        result = main.crop_frame(frame)

        expected = np.array([
            [0, 4, 8],
            [1, 5, 9],
            [2, 6, 10],
            [3, 7, 11]
        ])

        # The crop_frame uses numba, we can test it handles numpy arrays correctly
        np.testing.assert_array_equal(result, expected)
        self.assertEqual(result.shape, (4, 3))

    def test_crop_frame_3d(self):
        # Test with a 3D array (like an image with RGB channels)
        # 2x2 image with 3 channels
        frame = np.arange(12).reshape((2, 2, 3))

        result = main.crop_frame(frame)

        # Just check it doesn't crash and returns the right shape
        self.assertEqual(result.shape, (2, 2, 3))

if __name__ == '__main__':
    unittest.main()
