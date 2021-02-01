import psutil
import time

from opencensus.ext.azure import metrics_exporter

def main():
    # All you need is the next line. You can disable performance counters by
    # passing in enable_standard_metrics=False into the constructor of
    # new_metrics_exporter()
    _exporter = metrics_exporter.new_metrics_exporter(
        connection_string='InstrumentationKey=<Your Key>'
 )

    for i in range(100):
        print(psutil.virtual_memory())
        time.sleep(5)

    print("Done recording metrics")

if __name__ == "__main__":
    main()