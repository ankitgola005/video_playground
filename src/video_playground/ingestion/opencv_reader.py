import cv2
from video_playground.ingestion.reader import Reader

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np
    from pathlib import Path
    from collections.abc import Generator


class OpenCVReader(Reader):
    def __init__(self, path: str | Path):
        self.cap: cv2.VideoCapture = cv2.VideoCapture(str(path))

    def is_opened(self) -> bool:
        return self.cap.isOpened()

    def read(self) -> tuple[bool, np.ndarray | None]:
        return self.cap.read()

    def frames(self) -> Generator[np.ndarray, None, None]:
        while True:
            ret, frame = self.read()

            if not ret or frame is None:
                break

            yield frame

    def release(self) -> None:
        self.cap.release()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.release()
