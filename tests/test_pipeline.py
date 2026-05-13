from video_playground.ingestion import VideoReader
from video_playground.processing import GrayscaleProcessor
from video_playground.pipeline import Pipeline


def test_pipeline_processes_frames(video_path):
    reader = VideoReader(video_path / "dog_lick_sunflower.mp4")
    processors = [GrayscaleProcessor()]

    pipeline = Pipeline(reader, processors)
    frame = next(pipeline.run())

    assert frame is not None
