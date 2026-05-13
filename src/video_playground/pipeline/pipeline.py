from typing import TYPE_CHECKING, Iterable, Generator

if TYPE_CHECKING:
    import numpy as np

    from video_playground.ingestion import VideoReader
    from video_playground.processing.processor import Processor


class Pipeline:
    def __init__(
        self,
        reader: VideoReader,
        processors: Iterable[Processor],
    ):
        self.reader = reader
        self.processors = processors

    def run(self) -> Generator[np.ndarray, None, None]:
        for frame in self.reader.frames():
            for processor in self.processors:
                frame = processor.process(frame)

            yield frame
