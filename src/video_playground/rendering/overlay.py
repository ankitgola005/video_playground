import cv2
import numpy as np


def draw_fps(frame: np.ndarray, fps: float) -> np.ndarray:
    cv2.putText(
        frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2
    )

    return frame
