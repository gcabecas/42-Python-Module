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
        return [data for data in data_batch if criteria in str(data)]

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
            except (IndexError, ValueError) as e:
                return f"Error processing data '{data}': {e}"

        avg_temp = temp_sum / temp_count if temp_count > 0 else None
        if avg_temp is not None:
            self.stat = f"avg temp: {avg_temp:.1f}°C"
        else:
            self.stat = "No temperature data found."

        return self.stat


def main() -> None:
    sensor_stream = SensorStream("SENSOR_001")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    sensor_stream.process_batch(sensor_batch)
    stats = sensor_stream.get_stats()
    print(f"Sensor analysis: {stats['data_processed']} readings processed,"
          f" {stats['stat']}")


if __name__ == "__main__":
    main()
