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
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        print("\nInitializing Numeric Processor...")

    def validate(self, data: Any) -> bool:
        if isinstance(data, list) is True and len(data) > 0:
            if all(isinstance(x, (int, float)) for x in data):
                print("Validation: Numeric data verified")
                return True
        print("Validation: Wrong input!")
        return False

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        try:
            if not self.validate(data):
                raise ValueError("Invalid data input")
            size = len(data)
            total = sum(data)
            avg = total / size
            result = f"Processed {size} numeric values, sum={total}, avg={avg}"
        except Exception as e:
            result = f"[ALERT] ERROR level detected: {e}"

        return self.format_output(result)


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        print("\nInitializing Text Processor...")

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) is True and len(data) > 0:
            print("Validation: Text data verified")
            return True
        print("Validation: Wrong input!")
        return False

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        try:
            if not self.validate(data):
                raise ValueError("Invalid data input")
            chars = len(data)
            words = len(data.split())
            result = f"Processed text: chars={chars}, words={words}"
        except Exception as e:
            result = f"[ALERT] ERROR level detected: {e}"

        return result


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
        print("\nInitializing Log Processor...")

    def validate(self, data: Any) -> bool:
        if isinstance(data, str) is True and len(data) > 0:
            print("Validation: Log entry verified")
            return True
        print("Validation: Wrong input!")
        return False

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        try:
            if not self.validate(data):
                raise ValueError("Invalid data input")
            level, message = data.split(":", 1)
            level.strip()
            message.strip()
            if level == "ERROR":
                result = f"[INFO] LEVEL level detected: {message}"
            else:
                result = f"[INFO] LEVEL level detected: {message}"
        except ValueError as e:
            result = f"[ALERT] ERROR level detected: {e}"

        return result


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    numeric = NumericProcessor()
    numeric.process([1, 2, 3, 4, 5])
    text = TextProcessor()
    text.process("Hello Nexus World")
    log = LogProcessor()
    log.process("ERROR: Connection timeout")
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    list_process = [(numeric, [1, 2, 3]), (text, "Hello World"),
                    (log, "INFO: System ready")]
    count = 1
    for processor, data in list_process:
        result = processor.process(data)
        print(f"Result {count}: {result}")
        count += 1
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
