import pandas as pd 
from src.core.config import DataConfig
from src.core.errors import DataValidationError
from pathlib import Path
from typing import List 

class TransactionDataset:
    """Class that loads and validates Pandas DataFrame object."""
    def __init__(self, df: pd.DataFrame, data_config: DataConfig = None):
        """Initializes attributes of the TransactionDataset object
        
        args: 
            self: Class instance 
            df (pd.DataFrame): pandas DataFrame
            data_config (:obj: 'class'): DataConfig object instance 
        """
        self.df = df
        self.data_config = data_config if data_config is not None else DataConfig()
        col_diff =  set(self.data_config.feature_names) - set(df.columns.to_list())
        if len(col_diff) > 0:
            raise DataValidationError(f"Passed in Data Frame is missing columns: {col_diff}")
        else: 
            print('Dataset loaded correctly')

    
    @classmethod
    def from_csv(cls, path: str = None, data_config: DataConfig = None):
        """Alternative constructor to __init__ that builds a dataframe from .csv file
        args: 
            path (str): Path to the .csv file 
            data_config (:obj: 'class') default = None: Instance of DataConfig class
        """
        data_config = data_config if data_config is not None else DataConfig()
        path = Path(path) if path is not None else data_config.raw_data_path
        df = pd.read_csv(path)
        
        return cls(df, data_config)
    @property
    def target(self) -> pd.Series:
        """Return the array of the target variable."""
        return self.df[self.data_config.target]

    @property
    def features(self) -> pd.DataFrame:
        """Return the matrix of independent variables"""
        return self.df.loc[:,[col for col in self.data_config.feature_names if col != self.data_config.target]]

    def __len__(self):
        """Controlls the behavior of the class after using a len(Instance)"""
        return len(self.df)

    def __repr__(self):
        """Controlls how the class object is displayed"""
        return f'TransactionDataset(rows={len(self.df)}, features={len(self.data_config.feature_names)})'

#### Make docstrings by hand1