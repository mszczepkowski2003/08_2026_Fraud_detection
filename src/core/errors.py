"""File stores all of the code related to handling the exceptions in this project"""

class FraudDetectionError(Exception):
    """Base class for other custom exceptions"""
    def __init__(self, message: str, value=None):
        self.message = message 
        self.value = value
        super().__init__(message) 


class DataValidationError(FraudDetectionError):
    """Specific error class to raise when incoming transaction data does not match the expected structure"""
    pass 


class ModelPipelineError(FraudDetectionError):
    """Specific error class to raise when there is an error in a pipeline or prediction process"""
    pass