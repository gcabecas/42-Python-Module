from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        print(f"Output: {result}")


class NumericProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        try:
            total = sum(data)
            avg = total / len(data)
            return f" Processed {len(data)} numeric values," \
                f" sum: {total}, avg: {avg}"
        except Exception as e:
            return f"Error processing data: {e}"
