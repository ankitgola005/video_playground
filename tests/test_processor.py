from video_playground.ingestion.opencv_reader import VideoReader
from video_playground.processing import GrayscaleProcessor


def test_processor_returns_frame(video_path):
    reader = VideoReader(video_path / "dog_lick_sunflower.mp4")

    _, frame = reader.read()

    processor = GrayscaleProcessor()
    processed = processor.process(frame)
    assert processed is not None


def test_reader_processor_pipeline(video_path):
    reader = VideoReader(video_path / "dog_lick_sunflower.mp4")
    processor = GrayscaleProcessor()

    for frame in reader.frames():
        processed = processor.process(frame)

        assert processed is not None
        break


def test_grayscale_processor(video_path):
    reader = VideoReader(video_path / "dog_lick_sunflower.mp4")

    _, frame = reader.read()
    processor = GrayscaleProcessor()
    processed = processor.process(frame)

    assert processed is not None
    assert len(processed.shape) == 2
