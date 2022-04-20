from abc import ABC, abstractmethod


class Controller(ABC):
    def __init__(self, model=None, status_bar=None):
        self.view = None
        self.model = model
        self.status_bar = status_bar
        print(status_bar)

    @abstractmethod
    def bind(self, view):
        raise NotImplementedError
