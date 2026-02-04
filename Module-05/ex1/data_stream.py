from abc import ABC, abstractmethod
from typing import Any, Union, Optional, List, Dict


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type

        self.data_processed = 0
        self.stat = ""

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        if criteria is None:
            return data_batch
        return [
            data for data in data_batch if criteria and isinstance(
                data, str) and criteria in data]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "data_processed": self.data_processed,
            "stat": self.stat
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")
        print("Initializing Sensor Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing sensor batch: {data_batch}")

        self.data_processed += len(data_batch)

        filtered_data = self.filter_data(data_batch, criteria="temp:")

        temp_sum = 0.0
        temp_count = 0

        for data in filtered_data:
            try:
                temp_value = float(data.split(":")[1])
                temp_sum += temp_value
                temp_count += 1
            except (Exception):
                pass

        avg_temp = temp_sum / temp_count if temp_count > 0 else None
        if avg_temp is not None:
            self.stat = f"avg temp: {avg_temp:.1f}°C"
        else:
            self.stat = "No temperature data found."
        return self.stat


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")
        print("Initializing Transaction Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing transaction batch: {data_batch}")

        self.data_processed += len(data_batch)

        data_buy = self.filter_data(data_batch, criteria="buy:")
        data_sell = self.filter_data(data_batch, criteria="sell:")
        total = 0

        for data in data_buy:
            try:
                amount = int(data.split(":")[1])
                total += amount
            except (Exception):
                pass

        for data in data_sell:
            try:
                amount = int(data.split(":")[1])
                total -= amount
            except (Exception):
                pass

        sign = "" if total < 0 else "+"
        units = "units" if total != 1 and total != -1 else "unit"

        self.stat = f"net flow: {sign}{total} {units}"
        return self.stat


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Event Data")
        print("Initializing Event Stream...")
        print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")

    def process_batch(self, data_batch: List[Any]) -> str:
        print(f"Processing event batch: {data_batch}")

        self.data_processed += len(data_batch)

        error = self.filter_data(data_batch, criteria="error")
        if len(error) > 1:
            self.stat = f"{len(error)} errors found"
        else:
            self.stat = f"{len(error)} error found"
        return self.stat


class StreamProcessor:
    def process_stream(
            self,
            stream: DataStream,
            data_batch: List[Any]) -> None:

        try:
            stream.process_batch(data_batch)
        except Exception as e:
            print(f"Error processing stream {stream.stream_id}: {e}")


def main() -> None:
    sensor_stream = SensorStream("SENSOR_001")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor_stream.process_batch(sensor_batch)
    stats = sensor_stream.get_stats()
    print(f"Sensor analysis: {stats['data_processed']} readings processed,"
          f" {stats['stat']}")

    print()

    transaction_stream = TransactionStream("TRANS_001")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    transaction_stream.process_batch(transaction_batch)
    stats = transaction_stream.get_stats()
    print(f"Transaction analysis: {stats['data_processed']}"
          f" operations, {stats['stat']}")

    print()

    event_stream = EventStream("EVENT_001")
    event_batch = ["login", "error", "logout"]
    event_stream.process_batch(event_batch)
    stats = event_stream.get_stats()
    print(f"Event analysis: {stats['data_processed']} events processed,"
          f" {stats['stat']}")

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")

    processor = StreamProcessor()
    streams = [
        (sensor_stream, ["temp:40.5", "temp:38.2"]),
        (transaction_stream, ["buy:5000", "sell:100", "buy:2000", "sell:500"]),
        (event_stream, event_batch)
    ]

    print("Batch 1 Results:")
    for stream, batch in streams:
        processor.process_stream(stream, batch)
        if isinstance(stream, SensorStream):
            print(f"- Sensor data: {len(batch)} readings processed")
        elif isinstance(stream, TransactionStream):
            print(f"- Transaction data: {len(batch)} operations processed")
        elif isinstance(stream, EventStream):
            print(f"- Event data: {len(batch)} events processed")

    print("\nStream filtering active: High-priority data only")
    high_priority_sensor = sensor_stream.filter_data(
        ["error", "info", "error"], "error")
    high_priority_trans = transaction_stream.filter_data(
        ["buy:100000", "sell:50", "buy:500"], "000")

    print(f"Filtered results: {len(high_priority_sensor)} critical "
          f"sensor alerts, {len(high_priority_trans)} large transactions")
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
