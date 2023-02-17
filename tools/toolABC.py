from abc import ABC, abstractmethod

class Tool(ABC):
    @abstractmethod
    def execute(self, path: str, *args):
        return NotImplementedError