import MapReduce
import sys
import itertools

mr = MapReduce.MapReduce()

def mapper(record):
  trimmed = record[1][:-10]
  mr.emit_intermediate(trimmed, None)

def reducer(key, list_of_values):
  mr.emit((key))

if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)