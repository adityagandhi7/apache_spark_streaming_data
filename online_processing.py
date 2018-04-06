from __future__ import print_function
import sys
import pandas as p
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import subprocess

# Helper function to split on the comma in the delimiter in the data
def list_create(row):
    datalist = row.split(',')
    x = int(datalistlist[1])
    y = int(datalist[2])
    value = datalist[3]
    return (x,y), value


if __name__ == "__main__":
    
    # Error Handler
    if len(sys.argv) != 2:
        print("Usage: sql_network_wordcount.py <hostname> <port> ", file=sys.stderr)
        exit(-1)
    host = sys.argv[1]
    
    # Connection to Spark Streaming
    sc = SparkContext(appName="PythonSqlNetworkWordCount")
    ssc = StreamingContext(sc, 20)
    ssc.checkpoint("hdfs:///user/ag1419/spark_stream_v1")
    
    # Definition of batch interval window length and sliding window
    lines = ssc.textFileStream(host)
    batchInterval = 1  # seconds
    window_len = 120 * batchInterval
    sliding = 20 * batchInterval
    print("Before Window")
    
    # MapReduce job that used the list_create() function based on the window and sliding length
    words = lines.window(window_len,sliding).flatMap(lambda line: line.split(" ")).map(list_create).reduceByKey(lambda a, b: max(int(a), int(b))-min(int(a), int(b)))

    # Saving in a text file
    words.saveAsTextFiles("difference")
    
    # Keeping the session running until multiple amounts of data are regularly streaming. We use manual termination to stop the code.
    ssc.start()
    ssc.awaitTermination()
