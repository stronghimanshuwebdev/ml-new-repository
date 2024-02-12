from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
import sys
from housing.logger import logging

def main():
    try:
        pipeline = Pipeline()  # Create an instance of the Pipeline class
        pipeline.run_pipeline()  # Call the run_pipeline method on the instance
    except Exception as e:
        logging.error(f"{e}")
        print(e)
        raise HousingException(e,sys) from e

if __name__ == '__main__':
    main()
