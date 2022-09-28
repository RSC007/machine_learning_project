import os, sys

from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException

def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()
        print("Succesfully")
    except Exception as e:
        raise HousingException(e, sys) from e


if __name__=="__main__":
    main()