# apache_spark_streaming_data

This project targets an application that explores the evolution of wind
speeds in a bi-dimensional space, considering propagation only in the
X axis.

**Assumptions**

- The 2-dimensional space is square (N elements in X and Y axes), where N=1000,
i.e., the space has 1,000,000 points/coordinates.

- We assume that a number of measurements is given. Each measurement is given
in the following format: (X, Y, value).

- The measurements are not exhaustive i.e., some (X,Y) coordinates may not have
any measurement. The lack of a value in a given coordinate does NOT mean that
the wind speed is 0.

- Value is an integer, the sign of the wind speed value indicates the wind direction.

**Step 1: Input data**

- Data is being generated automatically (a few times a minute) in a project directory
- This stream of data provides data for 1000x1000 items (exhaustively)

**Step 2: Online processing**

- We compute the wind speed variability in the last two minutes of the (sliding) window by computing for each coordinate (x,y) the MAX and MIN values in that
window
- Save the result of algorithm for each window in HDFS
- Store the variability of wind speed (i.e., MAX – MIN) for each coordinate, for each
window in HDFS.

**Step 3: Batch processing**

- We execute a MapReduce code when needed.
- Process the data in the output file in HDFS from Step 2
- An output file should contain that variability of wind speed in each point for a number of time windows
- Generate a heat map with the average wind speed variability for each coordinate (x,y)
