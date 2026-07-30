from abc import ABC, abstractmethod ##abstract base classes : anyone inheriting from this class must implement these moethods

class BaseProvider(ABC):
    @abstractmethod ##decorator ; This function must be implemented by every child class.
    def detect(self):
        pass
    @abstractmethod
    def get_models(self):
        pass