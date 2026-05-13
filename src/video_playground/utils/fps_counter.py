import time


class FPSCounter:
    def __init__(self):
        self.start_time = time.perf_counter()
        self.frame_count = 0

    def update(self) -> None:
        self.frame_count += 1

    def fps(self) -> float:
        elapsed = time.perf_counter() - self.start_time

        if elapsed == 0:
            return 0

        return self.frame_count / elapsed
