# This is a sample Python script for setting up Azure Monitor.
# https://docs.microsoft.com/en-us/azure/azure-monitor/app/opencensus-python


# 1. Logs

import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

# __name__ contains the full name of the current module
logger = logging.getLogger(__name__) 


logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=<Your Key>'
))



# Testing Log
def test_logger():
    # this log can be found under "traces"
    # at the level of warning https://docs.python.org/3/library/logging.html#logging.Logger.setLevel

    #traces
    #| where message == 3
    print('inside test_logger')
    line = input("Enter a value: ")
    logger.warning(line)

    # customDimensions
    #traces
    #  | where message == 'action'

    log_dict = {'custom_dimensions':{'aska':'good','aska':'good'}}
    logger.warning('action', extra=log_dict)


    # send exceptions
    # exceptions
    # | where method == 'test_logger'

    try:
        result = 1 / 0  # generate a ZeroDivisionError
    except Exception:

        logger.exception('Captured an exception.', extra=log_dict)


    # send events
    logger.setLevel(logging.INFO)
    logger.info('Hello, World!')



if __name__ == '__main__':

    print("Starting logger test...")
        
        test_logger()

    print("Finished logger test...")

