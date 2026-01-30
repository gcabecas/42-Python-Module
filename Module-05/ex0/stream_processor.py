from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}\n"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
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
    def __init__(self) -> None:
        print("Initializing Text Processor...")

    def validate(self, data: Any) -> bool:
        if type(data) is str:
            print("Validation: Text data verified")
            return True
        return False

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        if not self.validate(data):
            raise ValueError(
                "Invalid data: Data must be a strings.")
        return f"Processed text: {len(data)} caracters, " \
            f"words={len(data.split())}"


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        print("Initializing Log Processor...")

    def validate(self, data: Any) -> bool:
        if type(data) is not str:
            return False

        parts = data.split(":")
        if len(parts) != 2:
            return False

        level = parts[0].strip()
        message = parts[1].strip()
        if level == "" or message == "":
            return False
        print("Validation: Log data verified")
        return True

    def process(self, data: Any) -> str:
        print(f"Processing data: \"{data}\"")
        if not self.validate(data):
            raise ValueError(
                "Invalid data: Data must be a log string in format"
                " 'LEVEL: message'.")
        parts = data.split(":")
        level = parts[0].strip()
        message = parts[1].strip()

        return f"[{level}] {level} level detected: {message}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    try:
        NumProc = NumericProcessor()
        print(NumProc.format_output(NumProc.process([1, 2, 3, 4, 5])))
    except Exception as e:
        print(NumProc.format_output(e))

    try:
        TextProc = TextProcessor()
        print(TextProc.format_output(
            TextProc.process("Hello Nexus World")))
    except Exception as e:
        print(TextProc.format_output(e))

    try:
        LogProc = LogProcessor()
        print(LogProc.format_output(
            LogProc.process("ERROR: Connection timeout")))
    except Exception as e:
        print(LogProc.format_output(e))


if __name__ == "__main__":
    main()
