from pyspark import SparkConf, SparkContext

conf = SparkConf().setMaster("local").setAppName("MovieTry")
sc = SparkContext(conf = conf)

def parseLine(line):
    fields = line.split(',')
    movieID = fields[1]
    return (movieID)

lines = sc.textFile("file:///SparkCourse/ml-100k/u.data")

parsedLines = lines.map(lambda x: x.split()[1])
ratingPerMovie = parsedLines.map(lambda x: (x, 1)).reduceByKey(lambda x, y: x + y)
flipped = ratingPerMovie.map(lambda (x,y) : (y,x))
sortedMovie = flipped.sortByKey()
results=sortedMovie.collect()

print(results)

for result in results:
    movieID = str(result[0])
    count = str(result[1])
    print(movieID + ":\t\t" +count)