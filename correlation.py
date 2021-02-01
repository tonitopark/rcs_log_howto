import logging

from opencensus.ext.azure.log_exporter import AzureLogHandler
from opencensus.ext.azure.trace_exporter import AzureExporter
from opencensus.trace import config_integration
from opencensus.trace.samplers import ProbabilitySampler
from opencensus.trace.tracer import Tracer


config_integration.trace_integrations(['logging'])

logger = logging.getLogger(__name__)

handler = AzureLogHandler(connection_string='InstrumentationKey=<Your Key>')

handler.setFormatter(logging.Formatter('%(traceId)s %(spanId)s %(message)s'))

logger.addHandler(handler)

tracer = Tracer(
    exporter=AzureExporter(connection_string='InstrumentationKey=<Your Key>'),
    sampler=ProbabilitySampler(1.0)

)

logger.warning('Before the span')
with tracer.span(name='azka_test_1'):
    logger.warning('In the span azka_test_1')
with tracer.span(name='azka_test_2'):
    logger.warning('In the span azka_test_2')
logger.warning('After the span')


input("...asdfd")

##traces
## | where message contains 'azka_test'