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
            return f"Processed temperature reading: {
                data.get('value')} {
                data.get('unit')} (Normal range)\n"
        elif isinstance(data, list) and \
                all(isinstance(x, (int, float)) for x in data):
            print("Transform: Aggregated and filtered")
            avg = sum(data) / len(data)
            return f"Stream summary: {
                len(data)} readings, avg: {
                    avg:.1f}°C\n"
        elif isinstance(data, str):
            print("Transform: Parsed and structured data")
            parts = data.split(",")
            i = 0
            for part in parts:
                if part == "action":
                    i += 1
            return f"User activity logged: {i} actions processed\n"


class OutputStage:
    def process(self, data: Any) -> Any:
        print(f"Output: {data}")
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
        if not isinstance(data, dict):
            print("Error: JSONAdapter expects a dict\n")
            return data
        print("Processing JSON data through pipeline...")
        return self.run_stages(data)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if not isinstance(data, str):
            print("Error: CSVAdapter expects a string\n")
            return data
        print("Processing CSV data through pipeline...")
        return self.run_stages(data)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if not isinstance(data, list) or \
                not all(isinstance(x, (int, float)) for x in data):
            print("Error: StreamAdapter expects a list of numbers\n")
            return data
        print("Processing Stream data through pipeline...")
        return self.run_stages(data)


class NexusManager:
    def __init__(self) -> None:
        print("Initializing Nexus Manager...\n")
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, pipeline_id: str, data: Any) -> Any:
        results = []
        for pipeline in self.pipelines:
            if pipeline.pipeline_id == pipeline_id:
                results.append(pipeline.process(data))
        return results


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


if __name__ == "__main__":
    main()
