from video_playground.utils import FPSCounter


def test_fps_counter_initializes():
    fps = FPSCounter()
    assert fps.frame_count == 0
