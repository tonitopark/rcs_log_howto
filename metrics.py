# This is a sample Python script for setting up Azure Monitor.
# https://docs.microsoft.com/en-us/azure/azure-monitor/app/opencensus-python

import time
import random
# 1. Logs

import logging
from opencensus.ext.azure.log_exporter import AzureLogHandler

# __name__ contains the full name of the current module
logger = logging.getLogger(__name__) 


logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=<Your Key>'
))

# 2. Metrics


#Initialization
from datetime import datetime
from opencensus.stats import aggregation as aggregation_module
from opencensus.stats import measure as measure_module
from opencensus.stats import stats as stats_module
from opencensus.stats import view as view_module
from opencensus.tags import tag_map as tag_map_module

stats = stats_module.stats
view_manager = stats.view_manager
stats_recorder = stats.stats_recorder


prompt_measure = measure_module.MeasureInt("rcs_log_num",
                                           "number of rcs_logs",
                                           "logs")
prompt_view = view_module.View("rcs_log_view_3",
                               "number of logs",
                               [],
                               prompt_measure,
                               aggregation_module.SumAggregation())
view_manager.register_view(prompt_view)
mmap = stats_recorder.new_measurement_map()
tmap = tag_map_module.TagMap()

# Register the metrics exporter

##customMetrics
## | where name =='prompt view'
from opencensus.ext.azure import metrics_exporter
exporter = metrics_exporter.new_metrics_exporter(
    connection_string='InstrumentationKey=<Your Key>')

view_manager.register_exporter(exporter)

# metrics usage example
def test_metrics():
    for _ in range(100):
        value = random.randint(1,10)
        mmap.measure_int_put(prompt_measure, value)
        mmap.record(tmap)
        metrics = list(mmap.measure_to_view_map.get_metrics(datetime.utcnow()))
        print(value, ' : ', metrics[0].time_series[0].points[0])
        time.sleep(1)

    time.sleep(100)




if __name__ == '__main__':


    print("Starting metric test...")
    while True:
        
        test_metrics()

    print("Finished metric test...")

