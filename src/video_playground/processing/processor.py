from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import numpy as np


class Processor(ABC):

    @abstractmethod
    def process(self, frame: np.ndarray) -> np.ndarray:
        raise NotImplementedError
