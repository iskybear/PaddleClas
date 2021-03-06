import importlib

from processor.algo_mod.predictor.paddle_predictor import PaddlePredictor
from processor.algo_mod.predictor.onnx_predictor import ONNXPredictor


def build_predictor(config):
    processor_mod = importlib.import_module(__name__)
    processor_name = config.get("name")
    return getattr(processor_mod, processor_name)(config)
