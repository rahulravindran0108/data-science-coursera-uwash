import MapReduce
import sys

"""
This is used to produce a join operation
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    
    mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    output_order = list_of_values[0]
    for x in range(1,len(list_of_values)):
      mr.emit(output_order+list_of_values[x])
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
