from video_playground.ingestion.opencv_reader import VideoReader


def test_can_open_video(video_path):
    reader = VideoReader(video_path / "dog_lick_sunflower.mp4")
    assert reader.is_opened()


def test_can_read_frame(video_path):
    reader = VideoReader(video_path / "dog_lick_sunflower.mp4")

    ret, frame = reader.read()

    assert ret is True
    assert frame is not None

    assert len(frame.shape) == 3
    assert frame.shape[0] > 0
    assert frame.shape[1] > 0


def test_can_iterate_frames(video_path):
    reader = VideoReader(video_path / "dog_lick_sunflower.mp4")

    count = 0
    for frame in reader.frames():
        assert frame is not None
        count += 1

        if count >= 10:
            break
    assert count == 10


def test_stops_at_end_of_video(video_path):
    reader = VideoReader(video_path / "dog_lick_sunflower.mp4")

    count = 0
    for _ in reader.frames():
        count += 1

    assert count > 0
