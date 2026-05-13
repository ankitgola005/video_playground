from pathlib import Path
import cv2

from video_playground.ingestion import OpenCVReader
from video_playground.pipeline import Pipeline
from video_playground.processing import GrayscaleProcessor
from video_playground.utils import FPSCounter

ROOT = Path(__file__).resolve()
VIDEO_PATH = ROOT / ".assets" / "videos"


def main():
    reader = OpenCVReader(VIDEO_PATH / "dog_lick_sunflower.mp4")
    processors = [GrayscaleProcessor()]
    pipeline = Pipeline(reader, processors)

    fps_counter = FPSCounter()

    for frame in pipeline.run():
        fps_counter.update()
        print(f"FPS: {fps_counter.fps():.2f}")
        cv2.imshow("Video", frame)
        if cv2.waitKey(1) == ord("q"):
            break


if __name__ == "__main__":
    main()
