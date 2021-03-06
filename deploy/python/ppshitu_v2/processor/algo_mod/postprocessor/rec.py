import numpy as np

from ...base_processor import BaseProcessor


class FeatureNormalizer(BaseProcessor):
    def __init__(self, config=None):
        pass

    def process(self, data):
        batch_output = data["pred"]["features"]
        feas_norm = np.sqrt(
            np.sum(np.square(batch_output), axis=1, keepdims=True))
        batch_output = np.divide(batch_output, feas_norm)
        data["pred"]["features"] = batch_output
        return data
