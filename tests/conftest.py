import pytest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VIDEO_PATH = ROOT / ".assets" / "videos"


@pytest.fixture
def video_path():
    return VIDEO_PATH
