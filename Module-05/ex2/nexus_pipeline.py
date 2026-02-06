from abc import ABC, abstractmethod
from typing import Any, List, Union, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Any:
        print(f"Input: {data}")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            print("Transform: Enriched with metadata and validation")
            return [
                0,
                data.get('value'),
                f"Processed temperature reading: {data.get('value')} "
                f"{data.get('unit')}\n"]
        elif isinstance(data, list) and \
                all(isinstance(x, (int, float)) for x in data):
            print("Transform: Aggregated and filtered")
            avg = sum(data) / len(data)
            return [1, [avg, len(data)], f"Stream summary: {len(data)} "
                    f"readings, avg: {avg:.1f}°C\n"]
        elif isinstance(data, str):
            print("Transform: Parsed and structured data")
            parts = data.split(",")
            i = 0
            for part in parts:
                if part == "action":
                    i += 1
            return [
                2, [i, len(parts)], f"User activity logged: {i} actions processed\n"]


class OutputStage:
    def process(self, data: Any) -> Any:
        print(f"Output: {data[2]}")
        if data[0] == 0:
            data = f"{data[1]}"
        elif data[0] == 1:
            data = [data[1][0], data[1][1]]
        elif data[0] == 2:
            data = data[1]
        return data


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str) -> None:
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def run_stages(self, data: Any) -> Any:
        res = data
        for stage in self.stages:
            res = stage.process(res)
        return res

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if not isinstance(data, dict):
                raise ValueError("JSONAdapter expects a dict\n")
            print("Processing JSON data through pipeline...")
            return self.run_stages(data)
        except Exception as e:
            print(f"Error processing JSON data: {e}")
            return data


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if not isinstance(data, str):
                raise ValueError("CSVAdapter expects a string\n")
            print("Processing CSV data through pipeline...")
            return self.run_stages(data)
        except Exception as e:
            print(f"Error processing CSV data: {e}")
            return data


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            if not isinstance(data, list) or \
                    not all(isinstance(x, (int, float)) for x in data):
                raise ValueError("StreamAdapter expects a list of numbers\n")
            print("Processing Stream data through pipeline...")
            return self.run_stages(data)
        except Exception as e:
            print(f"Error processing stream data: {e}")
            return data


class NexusManager:
    def __init__(self) -> None:
        print("Initializing Nexus Manager...\n")
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, pipeline_id: str, data: Any) -> Any:
        for pipeline in self.pipelines:
            if pipeline.pipeline_id == pipeline_id:
                return pipeline.process(data)
        return None


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    manager = NexusManager()

    json_pipeline = JSONAdapter("pipe_json")
    json_pipeline.add_stage(InputStage())
    json_pipeline.add_stage(TransformStage())
    json_pipeline.add_stage(OutputStage())
    manager.add_pipeline(json_pipeline)

    csv_pipeline = CSVAdapter("pipe_csv")
    csv_pipeline.add_stage(InputStage())
    csv_pipeline.add_stage(TransformStage())
    csv_pipeline.add_stage(OutputStage())
    manager.add_pipeline(csv_pipeline)

    stream_pipeline = StreamAdapter("pipe_stream")
    stream_pipeline.add_stage(InputStage())
    stream_pipeline.add_stage(TransformStage())
    stream_pipeline.add_stage(OutputStage())
    manager.add_pipeline(stream_pipeline)

    manager.process_data(
        "pipe_json", {
            "sensor": "temp", "value": 23.5, "unit": "C"})
    manager.process_data("pipe_csv", "user,action,timestamp")
    manager.process_data("pipe_stream", [20, 15.2, 19.2, 17.7, 28.4])

    print("\n=== NEXUS PIPELINE CHAINING DEMO ===\nPipeline A -> Pipeline B -> Pipeline C\n")

    manager.process_data(
        "pipe_stream",
        manager.process_data(
            "pipe_csv",
            manager.process_data(
                "pipe_json",
                {
                    "sensor": "temp", "value": 23.5, "unit": "C"})))

    print("\n=== Error Recovery Test ===\n")
    manager.process_data("pipe_json", "This is not a JSON dict")
    manager.process_data("pipe_csv", {"not": "a string"})
    manager.process_data("pipe_stream", "Not a list of numbers")


if __name__ == "__main__":
    main()
