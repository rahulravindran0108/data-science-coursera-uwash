import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate(sum(ord(ch) for ch in key+value), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    if(len(list_of_values) == 1):
        mr.emit(tuple(reversed(list_of_values[0])))
        mr.emit(tuple(list_of_values[0]))
        

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
