import unittest
import numpy as np
import sys
from unittest.mock import MagicMock

# --- Mocking phase ---
mock_cv2 = MagicMock()
mock_pygame = MagicMock()

sys.modules['cv2'] = mock_cv2
sys.modules['pygame'] = mock_pygame

# Ensure the main loop exits immediately by simulating K_ESCAPE
mock_event = MagicMock()
mock_pygame.KEYDOWN = 1
mock_pygame.K_ESCAPE = 2
mock_pygame.K_SPACE = 3
mock_event.type = 1
mock_event.key = 2
mock_pygame.event.get.return_value = [mock_event]

# Provide arrays of the ORIGINAL size so numba doesn't crash on the first compilation pass.
dummy_frame = np.zeros((1080+200, 1920+200, 4), dtype=np.uint8)
mock_cv2.imread.return_value = dummy_frame
mock_cv2.resize.return_value = dummy_frame
mock_cv2.IMREAD_UNCHANGED = -1

mock_camera = MagicMock()
mock_camera.read.return_value = (True, np.zeros((1080, 1920, 3), dtype=np.uint8))
mock_cv2.VideoCapture.return_value = mock_camera
mock_cv2.cvtColor.return_value = np.zeros((1080, 1920, 3), dtype=np.uint8)

import main

class TestProcessImage(unittest.TestCase):

    def test_processimage_basic(self):
        # We must use the original sizes because the function is already compiled for them.
        w = 1920
        h = 1080
        b = 100
        canvas_size_w = w + 2*b # 2120
        canvas_size_h = h + 2*b # 1280

        main.alpha.fill(1.0)
        main.fotoframe.fill(0.0)

        # The input image from camera
        _image = np.ones((h, w, 3), dtype=np.uint8) * 100
        # For fliplr to be noticeable, make left side different from right side
        half_w = w // 2
        _image[:, :half_w, :] = 50
        _image[:, half_w:, :] = 150

        canvas = np.zeros((canvas_size_h, canvas_size_w, 3), dtype=np.float64)

        result = main.processimage(_image, canvas)

        # The border should be 0 because alpha is 1 but we only placed image in the center,
        # and canvas started at 0. So border is canvas*1 + fotoframe(0) = 0
        np.testing.assert_array_equal(result[0, :, :], 0)
        np.testing.assert_array_equal(result[:, 0, :], 0)

        # The center should be the flipped image.
        # The original image left side was 50, right was 150.
        # Flipped left side should be 150, right should be 50.
        # Canvas center starts at [b:h+b, b:w+b]
        center_left = result[b:h+b, b:b+half_w, :]
        center_right = result[b:h+b, b+half_w:w+b, :]

        np.testing.assert_array_equal(center_left, 150)
        np.testing.assert_array_equal(center_right, 50)

    def test_processimage_with_alpha_and_frame(self):
        w = 1920
        h = 1080
        b = 100
        canvas_size_w = w + 2*b # 2120
        canvas_size_h = h + 2*b # 1280

        _image = np.ones((h, w, 3), dtype=np.uint8) * 100
        canvas = np.zeros((canvas_size_h, canvas_size_w, 3), dtype=np.float64)

        main.alpha.fill(0.5)
        main.fotoframe.fill(10.0)

        result = main.processimage(_image, canvas)

        # Result = canvas * alpha + fotoframe
        # Center of canvas was 100 * 0.5 + 10 = 60
        np.testing.assert_array_equal(result[b:h+b, b:w+b, :], 60)

        # Border of canvas was 0 * 0.5 + 10 = 10
        np.testing.assert_array_equal(result[0:2, :, :], 10)

    def test_crop_frame(self):
        # crop_frame rotates 90 degrees and flips up/down
        frame = np.array([
            [[1, 1, 1], [2, 2, 2]],
            [[3, 3, 3], [4, 4, 4]]
        ])
        # np.rot90 rotates counter-clockwise
        # [[1, 2],
        #  [3, 4]]
        # rot90 -> [[2, 4],
        #           [1, 3]]
        # flipud -> [[1, 3],
        #            [2, 4]]
        expected = np.array([
            [[1, 1, 1], [3, 3, 3]],
            [[2, 2, 2], [4, 4, 4]]
        ])
        result = main.crop_frame(frame)
        np.testing.assert_array_equal(result, expected)

if __name__ == '__main__':
    unittest.main()
