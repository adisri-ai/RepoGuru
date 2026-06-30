from abc import ABC
from abc import abstractmethod


class LLMAdapter(ABC):

    @abstractmethod
    def invoke(
        self,
        messages
    ):
        pass

    @abstractmethod
    def get_model_name(
        self
    ) -> str:
        pass