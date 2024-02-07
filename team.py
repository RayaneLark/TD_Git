from abc import ABC, abstractmethod

class Team(ABC):
    def __init__(self, members):
        self._members = members

        @abstractmethod
        def __len__(self):
            pass

        @abstractmethod
        def __getitem__(self):
            pass

        @abstractmethod
        def __getitem__(self):
            pass