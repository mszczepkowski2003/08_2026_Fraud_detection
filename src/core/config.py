"""File stores structured configuration classes"""
from pathlib import Path
from typing import List

# Paths to directiories
class DataConfig:
    """Contains configuration attributes regarding data"""
    def __init__(self, feature_names: List[str] = None, target: str = 'Class', raw_data_path: str = 'data/raw_data', proc_data_path: str = 'data/processed_data'):
        self.target = target
        self.feature_names = feature_names
        self.raw_data_path = Path(raw_data_path)
        self.processed_data_path = Path(proc_data_path)

class ModelConfig: 
    """Contains configuration attributes regarding modelling"""
    def __init__(self, test_size: float = 0.2, random_state: int = 42, model_path: str = 'artifacts/'):
        self.test_size = test_size 
        self.random_state = random_state
        self.model_path = Path(model_path)

class AppConfigComposite:
    """Combines configuration classes into one cohesive object"""
    def __init__(self, data_config: DataConfig = None, model_config: ModelConfig = None):
        self.data_config = data_config if data_config is not None else DataConfig
        self.model_config = model_config if model_config is not None else ModelConfig

