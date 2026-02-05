from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol, collections


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
        return self.run_stages(data)


class CSVAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        return self.run_stages(data)


class StreamAdapter(ProcessingPipeline):
    def process(self, data: Any) -> Union[str, Any]:
        return self.run_stages(data)
