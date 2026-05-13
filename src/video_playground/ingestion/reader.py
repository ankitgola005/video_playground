from abc import ABC, abstractmethod


class Reader(ABC):

    @abstractmethod
    def read(self):
        raise NotImplementedError

    @abstractmethod
    def frames(self):
        raise NotImplementedError
