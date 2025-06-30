import pyspark
import findspark

from pyspark import SparkContext

print(pyspark.__version__)
print(findspark.__version__)


# 1. Initialize the Spark fir Setting up the Spark context
sc = SparkContext("local", "SparkLab")
sc.setCheckpointDir('checkpoint')

# pyspark only allows to run the one context at a time therefore, 
# we needed to store the older context before creating a new one.
#sc.stop()

# 2.  creating a resilient distributed datasets
# pyspark has multiple methods to convert different data types into the rdd.
data = [1, 2, 3, 5, 6]
rdd_list = sc.parallelize(data)
print(rdd_list.collect)

path = 'sample.txt'

# creating file
with open(path, 'w') as file:
    file.write("Hello, everyone \n ")
    file.write("This is Ajeet, Research Intern at Cloud Computing Lab")

# loading file into the rdd
rdd_file = sc.textFile(path)
# verify
print(rdd_file.collect())

# 3. Appt various map and reduce type transformations to these rdd_file
# Apply map transformation to square each element
squared_rdd = rdd_list.map(lambda x: x ** 2)

# Collect and print the result
print(squared_rdd.collect())  # Output: [1, 4, 9, 16, 25]

#------------------------------------------------------------------------------------------------------------

# Apply filter transformation to select even numbers
even_rdd = rdd_list.filter(lambda x: x % 2 == 0)

# Collect and print the result
print(even_rdd.collect())  # Output: [2, 4]

#------------------------------------------------------------------------------------------------------------

# Apply flatMap transformation to split words in a sentence
sentences = ["Spark is great", "RDDs are powerful"]
sentences_rdd = sc.parallelize(sentences)

# FlatMap to split sentences into words
words_rdd = sentences_rdd.flatMap(lambda sentence: sentence.split(" "))

# Collect and print the result
print(words_rdd.collect())  # Output: ['Spark', 'is', 'great', 'RDDs', 'are', 'powerful']

#------------------------------------------------------------------------------------------------------------

# Apply reduce to calculate the sum of the elements
sum_result = rdd_list.reduce(lambda x, y: x + y)

# Print the result
print(sum_result)  # Output: 15

#------------------------------------------------------------------------------------------------------------

# Count the number of elements
print(rdd_list.count())  # Output: 5

#------------------------------------------------------------------------------------------------------------

# Take the first 3 elements
print(rdd_list.take(3))  # Output: [1, 2, 3]

#------------------------------------------------------------------------------------------------------------

# Group elements by their parity (even or odd)
grouped_rdd = rdd_list.groupBy(lambda x: 'even' if x % 2 == 0 else 'odd')

# Collect and print the result
print(grouped_rdd.collect())
# Output: [('odd', [1, 3, 5]), ('even', [2, 4])] or [('even', iter([2, 4])), ('odd', iter([1, 3, 5]))]

#------------------------------------------------------------------------------------------------------------

# Create two RDDs
rdd1 = sc.parallelize([1, 2, 3])
rdd2 = sc.parallelize([4, 5, 6])

# Perform union
union_rdd = rdd1.union(rdd2)

# Collect and print the result
print(union_rdd.collect())  # Output: [1, 2, 3, 4, 5, 6]

#------------------------------------------------------------------------------------------------------------

# Create an RDD with duplicates
rdd_with_duplicates = sc.parallelize([1, 2, 2, 3, 3, 4])

# Apply distinct transformation
distinct_rdd = rdd_with_duplicates.distinct()

# Collect and print the result
print(distinct_rdd.collect())  # Output: [1, 2, 3, 4]

#------------------------------------------------------------------------------------------------------------

# Create an RDD of key-value pairs
pair_rdd = sc.parallelize([('a', 1), ('b', 2), ('a', 3), ('b', 4)])

# Apply reduceByKey to sum the values with the same key
reduced_rdd = pair_rdd.reduceByKey(lambda x, y: x + y)

# Collect and print the result
print(reduced_rdd.collect())  # Output: [('a', 4), ('b', 6)]

#------------------------------------------------------------------------------------------------------------

# Create an RDD of key-value pairs
pair_rdd = sc.parallelize([('a', 1), ('b', 2), ('c', 3)])

# Apply mapValues to increment each value by 1
mapped_values_rdd = pair_rdd.mapValues(lambda x: x + 1)

# Collect and print the result
print(mapped_values_rdd.collect())  # Output: [('a', 2), ('b', 3), ('c', 4)]

#------------------------------------------------------------------------------------------------------------

# Sample 50% of the RDD elements
sampled_rdd = rdd_list.sample(withReplacement=False, fraction=0.5)

# Collect and print the result
print(sampled_rdd.collect())

#------------------------------------------------------------------------------------------------------------

key_value_rdd = sc.parallelize([('a', 1), ('b', 2), ('c', 3), ('a', 4)])

# Apply mapValues to increment each value by 1
mapped_values_rdd = key_value_rdd.mapValues(lambda x: x + 1)

# Collect and print the result
print(mapped_values_rdd.collect())  # Output: [('a', 2), ('b', 3), ('c', 4), ('a', 5)]

##################
# lineage tracking : toDebugStrig()

rdd_first = sc.parallelize([1, 2, 3])
rdd_second = rdd_first.map(lambda x: x * 2)

print("RDD Lineage:", rdd_second.toDebugString())

rdd_first.checkpoint()
print(rdd_first.collect())

print(rdd_first.isCheckpointed())

print("RDD Lineage after checkpoint:", rdd_second.toDebugString())