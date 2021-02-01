import logging

from opencensus.ext.azure.log_exporter import AzureLogHandler

logger = logging.getLogger(__name__)
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=<Your Key>'
))

my_dict = {'message_type_A':"{'aska','members':['holden','andy','jc','jeric','tony']}" }
properties = {'custom_dimensions':my_dict}

logger.warning('action', extra=properties)