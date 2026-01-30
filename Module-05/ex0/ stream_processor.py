from abc import ABC, abstractmethod
from typing import Any

# log c'est quoi l'input ???


class DataProcessor(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        print(f"Output: {result}\n")


class NumericProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Numeric Processor...")

    def validate(self, data: Any) -> bool:
        if type(data) in (list, tuple):
            if all(type(item) in (int, float) for item in data):
                print("Validation: Numeric data verified")
                return True
        return False

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValueError(
                "Invalid data: Data must be a list or tuple of numbers.")
        total = sum(data)
        avg = total / len(data)
        return f"Processed {len(data)} numeric values, sum={total}, avg={avg}"


class TextProcessor(DataProcessor):
    def __init__(self):
        print("Initializing Text Processor...")

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            print("Validation: Text data verified")
            return True
        return False

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if not self.validate(data):
            raise ValueError(
                "Invalid data: Data must be a strings.")
        return f"Processed text: {len(data)} caracters, " \
            f"words={len(data.split())}"


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        NumProc = NumericProcessor()
        NumProc.format_output(NumProc.process([1, 2, 3, 4, 5]))
    except ValueError as e:
        NumProc.format_output(e)

    try:
        TextProc = TextProcessor()
        TextProc.format_output(
            TextProc.process("Hello Nexus World"))
    except ValueError as e:
        TextProc.format_output(e)


if __name__ == "__main__":
    main()
