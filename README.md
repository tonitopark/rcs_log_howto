# rcs_log_howto


## dependencies
```
opencensus-ext-azure==1.0.7
opencensus-ext-logging==0.1.0
```


## Initializaiton

```python

import logging

# 1. Import opencensus azure log handler
from opencensus.ext.azure.log_exporter import AzureLogHandler
# 2. Initialize Logger
logger = logging.getLogger(__name__) # __name__ is used to denote the full name of the current module

# 3. Add Azure Log Handler to the logger
logger.addHandler(AzureLogHandler(
    connection_string='InstrumentationKey=<Your Key>'
)) 
```

## Trace Log

### Simple trace
```python
    logger.warning('Simple Trace Sentenect')
```
### Custom dimensions
```python

    log_dict = {'custom_dimensions':{'aska-1':'res-1','aska-1':'res-2'}}
    logger.warning('action', extra=log_dict)
```
![trace_cust_dim](/images/trace_custom_dim.png)


## Metrics (custom)
* A. define a metrics 
   ```python
   m_line_lengths = measure_module.MeasureInt("repl_line_lengths", "The distribution of line lengths", "By")
   ```
* B. define a view 
    ```python
    line_count_view = view_module.View("demo_lines_in", "The number of lines from standard input",
        [key_method, key_status, key_error],
        m_line_lengths,
        aggregation_module.CountAggregation())

    ```
* C. setup view & exporter
  ```python
    view_manager = stats.view_manager
    exporter = metrics_exporter.new_metrics_exporter(connection_string='InstrumentationKey=<Your Key>')
    view_manager.register_exporter(exporter)
    view_manager.register_view(line_count_view)
  ```
![metrics_custom](/images/metrics_custom.png)

### Metric display
![metrics_display](/images/metric_plot.png)


## Exceptions

    ```python
    # exceptions

    try:
        result = 1 / 0  # generate a ZeroDivisionError
    except Exception:

        logger.exception('Captured an exception.', extra=log_dict)
    ```

![exception](/images/exception.png)



## Callbacks

```python
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
```
![callback](/images/callback.png)