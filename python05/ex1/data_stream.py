from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.counter = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "items_processed": self.counter
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Sensor"
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(f"Processing sensor batch: {data_batch}")
            filtered = self.filter_data(data_batch, "temperature")
            values = [float(item.split(":")[1]) for item in filtered]
            if not values:
                raise ValueError("No temperature readings found")
            readings = len(values)
            total = sum(values)
            avg = total / readings
            self.counter += readings
            return (f"Sensor analysis: {readings} readings processed,"
                    f" avg temp: {avg:.1f}ºC")
        except (TypeError, ValueError, IndexError) as exc:
            return f"Sensor analysis failed: {exc}"

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        normalized = [str(item).lower() for item in data_batch]
        if criteria == "temperature":
            return [item for item in normalized if item.startswith("temp:")]
        if criteria == "high":
            return [
                item for item in normalized
                if item.startswith("temp:")
                and float(item.split(":")[1]) > 25.0
            ]
        return normalized


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Transaction"
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(f"Processing transaction batch: {data_batch}")
            normalized = self.filter_data(data_batch)
            ops = len(normalized)
            net_flow = 0
            if ops == 0:
                raise ValueError("No transactions received")
            for item in normalized:
                operation, value = item.split(":")
                value = int(value)
                if operation == "buy":
                    net_flow += value
                elif operation == "sell":
                    net_flow -= value
                else:
                    raise ValueError(f"Unsupported operation: {operation}")
            net_flow_str = f"+{net_flow}" if net_flow > 0 else str(net_flow)
            self.counter += ops
            return (f"Transaction analysis: {ops} operations,"
                    f" net flow: {net_flow_str}")
        except (TypeError, ValueError, IndexError) as exc:
            return f"Transaction analysis failed: {exc}"

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        normalized = [str(item).lower() for item in data_batch]
        if criteria == "large":
            return [
                item
                for item in data_batch
                if int(item.split(":")[1]) > 100
            ]
        return normalized


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)
        self.stream_type = "Event"
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            print(f"Processing event batch: {data_batch}")
            normalized = self.filter_data(data_batch)
            events = len(normalized)
            if events == 0:
                raise ValueError("No events received")
            errors = len([item for item in normalized if item == "error"])
            self.counter += events
            return f"Event analysis: {events}, {errors} error detected"
        except (TypeError, ValueError) as exc:
            return f"Event analysis failed: {exc}"

    def filter_data(self, data_batch: List[Any], criteria:
                    Optional[str] = None) -> List[Any]:
        normalized = [str(item).lower() for item in data_batch]
        if criteria == "errors":
            return [item for item in data_batch
                    if item == "error"]
        return normalized


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, data_batches: List[List[Any]]) -> None:
        try:
            for stream, data in zip(self.streams, data_batches):
                result = stream.process_batch(data)
                stream_type = getattr(
                        stream,
                        "stream_type",
                        stream.__class__.__name__,
                )
                if result.endswith("failed"):
                    print(f"- {stream_type} data: processing failed")
                    continue
                count = self.extract_processed_count(result)
                print(f"- {stream_type} data: {count}")
        except Exception as exc:
            print(f"Batch processing failed: {exc}")

    @staticmethod
    def extract_processed_count(result: str) -> str:
        if "Sensor analysis:" in result:
            return (
                result.split("Sensor analysis: ", 1)[1]
                .split(",", 1)[0]
                + " readings processed"
            )

        if "Transaction analysis:" in result:
            return (
                result.split("Transaction analysis: ", 1)[1]
                .split(",", 1)[0]
                + " operations processed"
            )

        if "Event analysis:" in result:
            return (
                result.split("Event analysis: ", 1)[1]
                .split(",", 1)[0]
                + " events processed"
            )

        return result


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")
    print()

    sensor = SensorStream("SENSOR_001")
    print(sensor.process_batch(["temp:22.5", "humidity:65", "pressure:1013"]))
    print()

    transaction = TransactionStream("TRANS_001")
    print(transaction.process_batch(["buy:100", "sell:150", "buy:75"]))
    print()

    event = EventStream("EVENT_001")
    print(event.process_batch(["login", "error", "logout"]))
    print()

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print()

    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_002"))
    processor.add_stream(TransactionStream("TRANS_002"))
    processor.add_stream(EventStream("EVENT_002"))

    data_batches = [
        ["temp:22.5", "temp:23.1"],
        ["buy:100", "sell:150", "buy:75", "sell:200"],
        ["login", "error", "logout"],
    ]

    print("\nBatch 1 Results:")
    processor.process_all(data_batches)
    print()
    print("Stream filtering active: High-priority data only")
    high_sensor = sensor.filter_data(
        ["temp:22.5", "temp:27.0", "temp:29.0", "humidity:90"],
        "high",
    )
    large_tx = transaction.filter_data(
        ["buy:90", "sell:150", "buy:40"],
        "large",
    )
    print(
        "Filtered results: "
        f"{len(high_sensor)} critical sensor alerts, "
        f"{len(large_tx)} large transaction"
    )
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
