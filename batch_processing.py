from __future__ import print_function
import sys
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql import Row, SparkSession

# Helper function to split the x,y coordinate data on the comma delimiter
def list_create(row):
    datalist = row.split(',')
    x = int(datalist[0])
    y = int(datalist[1])
    value = int(datalist[2])
    return (x,y), value


if __name__ == "__main__":

    # Error Handler
    if len(sys.argv) != 2:
        print("Usage: sql_network_wordcount.py <hostname> <port> ", file=sys.stderr)
        exit(-1)
    
    # Specifying the text file and intializing SparkContext 
    scriptname, filename = sys.argv
    sc = SparkContext(appName="Variability")
    
    # FlatMap job to split concatenated data in the text file
    dataset = sc.textFile(filename)\
          .flatMap(lambda line: (line.replace("(","").replace(")","").replace("u'","").replace("'","").split("\n")))\
          .map(list_create)
    #print(dataset.collect())
    
    # Calculating the average of the x-values since wind direction propagates in only the x direction.
    # We do not need to sort the data, since the wind goes from left to right 
    rawdata = mydata.groupByKey() \
              .mapValues(lambda x: sum(x) / len(x))

    # Creating a count and generating the new wind values by adding the wind value in the preceding cell to the left in each iteration.
    # The resulting number will be the new wind values for all the values in the rawdata container
    count  = []
    for result in sorted(rawdata.collect()):
        count.append(str(result[0])+str(result[1]))
    for item in range(0,1000000):
        print(count[item])
