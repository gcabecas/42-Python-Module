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
        elif isinstance(data, list) and \
                all(isinstance(x, (int, float)) for x in data):
            print("Transform: Aggregated and filtered")
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            print(
                f"Output: Processed temperature reading: {
                    data.get('value')} {
                    data.get('unit')} (Normal range)\n")
        elif isinstance(data, list) and \
                all(isinstance(x, (int, float)) for x in data):
            avg = sum(data) / len(data)
            print(
                f"Output: Stream summary: {
                    len(data)} readings, avg: {
                    avg:.1f}°C\n")
        return data


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def _run_stages(self, data: Any) -> Any:
        res = data
        for stage in self.stages:
            res = stage.process(res)
        return res

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        if not isinstance(data, dict):
            return "Error: JSONAdapter expects a dict"
        print("Processing JSON data through pipeline...")
        return self._run_stages(data)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        pass


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id):
        super().__init__(pipeline_id)

    def process(self, data: Any) -> Union[str, Any]:
        print("Processing Stream data through same pipeline...")
        return self._run_stages(data)


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


def main():
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
    # manager.process_data("pipe_csv", "user,action,timestamp")
    manager.process_data("pipe_stream", [20, 15.2, 19.2, 17.7, 28.4])


if __name__ == "__main__":
    main()
