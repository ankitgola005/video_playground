import cv2

from video_playground.processing.processor import Processor

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


class GrayscaleProcessor(Processor):
    def process(self, frame: np.ndarray) -> np.ndarray:
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
