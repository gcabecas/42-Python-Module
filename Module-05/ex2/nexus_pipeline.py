from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass


class InputStage:
    def process(self, data: Any) -> Any:
        pass


class TransformStage:
    def process(self, data: Any) -> Any:
        pass


class OutputStage:
    def process(self, data: Any) -> Any:
        pass


class ProcessingPipeline(ABC):
    def __init__(self, pipeline_id: str):
        self.stages: List[ProcessingStage] = []
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        pass


class JSONAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        pass


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        pass


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        pass


class NexusManager:
    def __init__(self) -> None:
        print("Initializing Nexus Manager...")
        self.pipelines: List[ProcessingPipeline] = []

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines.append(pipeline)

    def process_data(self, data: Any) -> Any:
        results = []
        for pipeline in self.pipelines:
            results.append(pipeline.process(data))
        return results


def main():
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
    manager = NexusManager()

    json_pipeline = JSONAdapter()
    json_pipeline.add_stage(InputStage())
    json_pipeline.add_stage(TransformStage())
    json_pipeline.add_stage(OutputStage())
    manager.add_pipeline(json_pipeline)

    print("Processing JSON data through pipeline...")
    data_json = {"sensor": "temp", "value": 23.5, "unit": "C"}
    print(f"Input: {data_json}")
    res_json = manager.process_data("pipe_json", data_json)
    print("Transform: Enriched with metadata and validation")
    print(res_json)


if __name__ == "__main__":
    main()
