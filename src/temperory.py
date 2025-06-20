from src.logger import logging
from src.exception import CustomException
import sys

def divide(x, y):
    try:
        result = x / y
        logging.info(f"Result of {x}/{y} = {result}")
        return result
    except Exception as e:
        logging.error("Exception occurred during division")
        raise CustomException(e, sys)

# Try it
if __name__ == "__main__":
    divide(10, 0)  # This will raise your custom exception
