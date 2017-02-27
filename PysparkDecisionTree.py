from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.tree import DecisionTree
from pyspark import SparkConf, SparkContext
from numpy import array

#set local machine and app name
conf = SparkConf().setMaster("local").setAppName("SparkDecisionTree")
sc = SparkContext(conf = conf)

#select raw data as RDD without header
rawData = sc.textFile("path.csv")

#transform into list RDD
lsData = rawData.map(lambda x: x.split(","))
