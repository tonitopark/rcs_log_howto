import logging

from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)

# Callback function to detect mesaage type log 
# and modify message telemetry
def callback_function(envelope):
    print('\noriginal message\n')
    print(envelope.data)

    # Check if the input is message data
    if envelope.data.baseType == 'MessageData':
        new_message = envelope.data.baseData.message +'_modified'
        envelope.data.baseData.message = new_message
        print('\nnew message\n')
        print(envelope.data)
    else:
        envelope.data.baseData.message += '_hello'
    return True

handler = AzureLogHandler(connection_string='InstrumentationKey=<Your Key>')
# Register callback 
handler.add_telemetry_processor(callback_function)
logger.addHandler(handler)
logger.warning('Hello, World!')


# try:
#     result = 1 / 0  # generate a ZeroDivisionError
# except Exception:

#     logger.exception('Captured an exception.', extra={'test':'jajaja'})