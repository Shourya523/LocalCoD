from abc import ABC, abstractmethod ##abstract base classes : anyone inheriting from this class must implement these moethods

class BaseProvider(ABC):
    @abstractmethod ##decorator ; This function must be implemented by every child class.
    def detect(self):
        """Returns a ProviderInfo if detected, otherwise None."""
        pass
    @abstractmethod
    def get_models(self):
        pass
    @abstractmethod
    def generate(self,request):
        pass
    @abstractmethod
    def complete(self, request):
        """Generates a code completion based on a CompletionRequest."""
        pass