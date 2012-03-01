"""
Examples used in docstrings.

"""

# rename

table1 = [['sex', 'age'],
        ['m', 12],
        ['f', 34],
        ['-', 56]]

from petl import look, rename
look(table1)
# rename a single field
table2 = rename(table1, 'sex', 'gender')
look(table2)
# rename multiple fields by passing a dictionary as the second argument
table3 = rename(table1, {'sex': 'gender', 'age': 'age_years'})
look(table3)
# the returned table object can also be used to modify the field mapping using the suffix notation
table4 = rename(table1)
table4['sex'] = 'gender'
table4['age'] = 'age_years'
look(table4)


# cut

table1 = [['foo', 'bar', 'baz'],
          ['A', 1, 2.7],
          ['B', 2, 3.4],
          ['B', 3, 7.8],
          ['D', 42, 9.0],
          ['E', 12]]

from petl import look, cut    
look(table1)
table2 = cut(table1, 'foo', 'baz')
look(table2)
# fields can also be specified by index, starting from zero
table3 = cut(table1, 0, 2)
look(table3)
# field names and indices can be mixed
table4 = cut(table1, 'bar', 0)
look(table4)
# select a range of fields
table5 = cut(table1, *range(0, 2))
look(table5)    


# cutout

table1 = [['foo', 'bar', 'baz'],
          ['A', 1, 2.7],
          ['B', 2, 3.4],
          ['B', 3, 7.8],
          ['D', 42, 9.0],
          ['E', 12]]

from petl import cutout, look
look(table1)
table2 = cutout(table1, 'bar')
look(table2)
    

# cat

table1 = [['foo', 'bar'],
          [1, 'A'],
          [2, 'B']]
table2 = [['bar', 'baz'],
          ['C', True],
          ['D', False]]
table4 = [['foo', 'bar', 'baz'],
          ['A', 1, 2],
          ['B', '2', '3.4'],
          [u'B', u'3', u'7.8', True],
          ['D', 'xyz', 9.0],
          ['E', None]]
table5 = [['bar', 'foo'],
          ['A', 1],
          ['B', 2]]
table7 = [['bar', 'foo'],
          ['A', 1],
          ['B', 2]]
table8 = [['bar', 'baz'],
          ['C', True],
          ['D', False]]

from petl import look, cat
look(table1)
look(table2)
table3 = cat(table1, table2)
look(table3)
# can also be used to square up a single table with uneven rows
look(table4)
look(cat(table4))
# use the header keyword argument to specify a fixed set of fields 
look(table5)
table6 = cat(table5, header=['A', 'foo', 'B', 'bar', 'C'])
look(table6)
# using the header keyword argument with two input tables
look(table7)
look(table8)
table9 = cat(table7, table8, header=['A', 'foo', 'B', 'bar', 'C'])
look(table9)


# convert

table1 = [['foo', 'bar'],
          ['A', '2.4'],
          ['B', '5.7'],
          ['C', '1.2'],
          ['D', '8.3']]
table6 = [['gender', 'age'],
          ['M', 12],
          ['F', 34],
          ['-', 56]]

from petl import convert, look
look(table1)
# using the built-in float function:
table2 = convert(table1, 'bar', float)
look(table2)
# using a lambda function::
table3 = convert(table2, 'bar', lambda v: v**2)
look(table3)    
# a method of the data value can also be invoked by passing the method name
table4 = convert(table1, 'foo', 'lower')
look(table4)
# arguments to the method invocation can also be given
table5 = convert(table4, 'foo', 'replace', 'a', 'aa')
look(table5)
# values can also be translated via a dictionary
look(table6)
table7 = convert(table6, 'gender', {'M': 'male', 'F': 'female'})
look(table7)


# convertnumbers

table1 = [['foo', 'bar', 'baz', 'quux'],
          ['1', '3.0', '9+3j', 'aaa'],
          ['2', '1.3', '7+2j', None]]

from petl import convertnumbers, look
look(table1)
table2 = convertnumbers(table1)
look(table2)


# fieldconvert

table1 = [['foo', 'bar'],
          ['1', '2.4'],
          ['3', '7.9'],
          ['7', '2'],
          ['8.3', '42.0'],
          ['2', 'abc']]
table3 = [['foo', 'bar', 'baz'],
          ['1', '2.4', 14],
          ['3', '7.9', 47],
          ['7', '2', 11],
          ['8.3', '42.0', 33],
          ['2', 'abc', 'xyz']]
table5 = [['foo', 'bar', 'baz'],
          ['2', 'A', 'x'],
          ['5', 'B', 'y'],
          ['1', 'C', 'y'],
          ['8.3', 'D', 'z']]

from petl import fieldconvert, look    
look(table1)
table2 = fieldconvert(table1, {'foo': int, 'bar': float})
look(table2)
# converters can be added or updated using the suffix notation 
look(table3)
table4 = fieldconvert(table3)
table4['foo'] = int
table4['bar'] = float
table4['baz'] = lambda v: v**2
look(table4)
# converters can be functions, method names, or method names with arguments
look(table5)
table6 = fieldconvert(table5)
table6['foo'] = int
table6['bar'] = 'lower'
table6['baz'] = 'replace', 'y', 'yy'
look(table6)


# extend

table1 = [['foo', 'bar'],
          ['M', 12],
          ['F', 34],
          ['-', 56]]

from petl import extend, look
look(table1)
# using a fixed value
table2 = extend(table1, 'baz', 42)
look(table2)
# calculating the value
table2 = extend(table1, 'baz', lambda rec: rec['bar'] * 2)
look(table2)
# an expression string can also be used via expr
from petl import expr
table3 = extend(table1, 'baz', expr('{bar} * 2'))
look(table3)
    

# rowslice

table1 = [['foo', 'bar'],
          ['a', 1],
          ['b', 2],
          ['c', 5],
          ['d', 7],
          ['f', 42]]

from petl import rowslice, look
look(table1)
table2 = rowslice(table1, 2)
look(table2)
table3 = rowslice(table1, 1, 4)
look(table3)
table4 = rowslice(table1, 0, 5, 2)
look(table4)


# head

table1 = [['foo', 'bar'],
          ['a', 1],
          ['b', 2],
          ['c', 5],
          ['d', 7],
          ['f', 42],
          ['f', 3],
          ['h', 90]]

from petl import head, look
look(table1)
table2 = head(table1, 4)
look(table2)    
    

# tail

table1 = [['foo', 'bar'],
          ['a', 1],
          ['b', 2],
          ['c', 5],
          ['d', 7],
          ['f', 42],
          ['f', 3],
          ['h', 90],
          ['k', 12],
          ['l', 77],
          ['q', 2]]

from petl import tail, look
look(table1)
table2 = tail(table1, 4)
look(table2)    


# sort

table1 = [['foo', 'bar'],
          ['C', 2],
          ['A', 9],
          ['A', 6],
          ['F', 1],
          ['D', 10]]

from petl import sort, look
look(table1)
table2 = sort(table1, 'foo')
look(table2)
# sorting by compound key is supported
table3 = sort(table1, key=['foo', 'bar'])
look(table3)
# if no key is specified, the default is a lexical sort
table4 = sort(table1)
look(table4)


# melt

table1 = [['id', 'gender', 'age'],
          [1, 'F', 12],
          [2, 'M', 17],
          [3, 'M', 16]]
table3 = [['id', 'time', 'height', 'weight'],
          [1, 11, 66.4, 12.2],
          [2, 16, 53.2, 17.3],
          [3, 12, 34.5, 9.4]]

from petl import melt, look
look(table1)
table2 = melt(table1, 'id')
look(table2)
# compound keys are supported
look(table3)
table4 = melt(table3, key=['id', 'time'])
look(table4)
# a subset of variable fields can be selected
table5 = melt(table3, key=['id', 'time'], variables=['height'])    
look(table5)


# recast

table1 = [['id', 'variable', 'value'],
          [3, 'age', 16],
          [1, 'gender', 'F'],
          [2, 'gender', 'M'],
          [2, 'age', 17],
          [1, 'age', 12],
          [3, 'gender', 'M']]
table3 = [['id', 'vars', 'vals'],
          [3, 'age', 16],
          [1, 'gender', 'F'],
          [2, 'gender', 'M'],
          [2, 'age', 17],
          [1, 'age', 12],
          [3, 'gender', 'M']]
table6 = [['id', 'time', 'variable', 'value'],
          [1, 11, 'weight', 66.4],
          [1, 14, 'weight', 55.2],
          [2, 12, 'weight', 53.2],
          [2, 16, 'weight', 43.3],
          [3, 12, 'weight', 34.5],
          [3, 17, 'weight', 49.4]]
table9 = [['id', 'variable', 'value'],
          [1, 'gender', 'F'],
          [2, 'age', 17],
          [1, 'age', 12],
          [3, 'gender', 'M']]

from petl import recast, look
look(table1)
table2 = recast(table1)
look(table2)
# specifying variable and value fields
look(table3)
table4 = recast(table3, variablefield='vars', valuefield='vals')
look(table4)
# if there are multiple values for each key/variable pair, and no reducers
# function is provided, then all values will be listed
look(table6)
table7 = recast(table6, key='id')
look(table7)
# multiple values can be reduced via an aggregation function
def mean(values):
    return float(sum(values)) / len(values)

table8 = recast(table6, key='id', reducers={'weight': mean})
look(table8)    
# missing values are padded with whatever is provided via the missing 
# keyword argument (None by default)
look(table9)
table10 = recast(table9, key='id')
look(table10)

# duplicates

table1 = [['foo', 'bar', 'baz'],
          ['A', 1, 2.0],
          ['B', 2, 3.4],
          ['D', 6, 9.3],
          ['B', 3, 7.8],
          ['B', 2, 12.3],
          ['E', None, 1.3],
          ['D', 4, 14.5]]

from petl import duplicates, look    
look(table1)
table2 = duplicates(table1, 'foo')
look(table2)
# compound keys are supported
table3 = duplicates(table1, key=['foo', 'bar'])
look(table3)
    

# conflicts

table1 = [['foo', 'bar', 'baz'],
          ['A', 1, 2.7],
          ['B', 2, None],
          ['D', 3, 9.4],
          ['B', None, 7.8],
          ['E', None],
          ['D', 3, 12.3],
          ['A', 2, None]]

from petl import conflicts, look    
look(table1)
table2 = conflicts(table1, 'foo')
look(table2)


# complement

a = [['foo', 'bar', 'baz'],
     ['A', 1, True],
     ['C', 7, False],
     ['B', 2, False],
     ['C', 9, True]]
b = [['x', 'y', 'z'],
     ['B', 2, False],
     ['A', 9, False],
     ['B', 3, True],
     ['C', 9, True]]

from petl import complement, look
look(a)
look(b)
aminusb = complement(a, b)
look(aminusb)
bminusa = complement(b, a)
look(bminusa)


# recordcomplement

a = (('foo', 'bar', 'baz'),
     ('A', 1, True),
     ('C', 7, False),
     ('B', 2, False),
     ('C', 9, True))
b = (('bar', 'foo', 'baz'),
     (2, 'B', False),
     (9, 'A', False),
     (3, 'B', True),
     (9, 'C', True))

from petl import recordcomplement, look
look(a)
look(b)
aminusb = recordcomplement(a, b)
look(aminusb)
bminusa = recordcomplement(b, a)
look(bminusa)

# diff

a = [['foo', 'bar', 'baz'],
     ['A', 1, True],
     ['C', 7, False],
     ['B', 2, False],
     ['C', 9, True]]
b = [['x', 'y', 'z'],
     ['B', 2, False],
     ['A', 9, False],
     ['B', 3, True],
     ['C', 9, True]]

from petl import diff, look
look(a)
look(b)
added, subtracted = diff(a, b)
# rows in b not in a
look(added)
# rows in a not in b
look(subtracted)


# recorddiff

a = (('foo', 'bar', 'baz'),
     ('A', 1, True),
     ('C', 7, False),
     ('B', 2, False),
     ('C', 9, True))
b = (('bar', 'foo', 'baz'),
     (2, 'B', False),
     (9, 'A', False),
     (3, 'B', True),
     (9, 'C', True))

from petl import recorddiff, look    
look(a)
look(b)
added, subtracted = recorddiff(a, b)
look(added)
look(subtracted)


# capture

table1 = [['id', 'variable', 'value'],
          ['1', 'A1', '12'],
          ['2', 'A2', '15'],
          ['3', 'B1', '18'],
          ['4', 'C12', '19']]

from petl import capture, look
look(table1)
table2 = capture(table1, 'variable', '(\\w)(\\d+)', ['treat', 'time'])
look(table2)
# using the include_original argument
table3 = capture(table1, 'variable', '(\\w)(\\d+)', ['treat', 'time'], include_original=True)
look(table3)


# split

table1 = [['id', 'variable', 'value'],
          ['1', 'parad1', '12'],
          ['2', 'parad2', '15'],
          ['3', 'tempd1', '18'],
          ['4', 'tempd2', '19']]

from petl import split, look
look(table1)
table2 = split(table1, 'variable', 'd', ['variable', 'day'])
look(table2)


# select

table1 = [['foo', 'bar', 'baz'],
          ['a', 4, 9.3],
          ['a', 2, 88.2],
          ['b', 1, 23.3],
          ['c', 8, 42.0],
          ['d', 7, 100.9],
          ['c', 2]]

from petl import select, look     
look(table1)
# the second positional argument can be a function accepting a record (i.e., a 
# dictionary representation of a row).
table2 = select(table1, lambda rec: rec['foo'] == 'a' and rec['baz'] > 88.1)
look(table2)
# the second positional argument can also be an expression string, which 
# will be converted to a function using expr()
table3 = select(table1, "{foo} == 'a' and {baz} > 88.1")
look(table3)
# the condition can also be applied to a single field
table4 = select(table1, 'foo', lambda v: v == 'a')
look(table4)


# fieldmap

table1 = [['id', 'sex', 'age', 'height', 'weight'],
          [1, 'male', 16, 1.45, 62.0],
          [2, 'female', 19, 1.34, 55.4],
          [3, 'female', 17, 1.78, 74.4],
          [4, 'male', 21, 1.33, 45.2],
          [5, '-', 25, 1.65, 51.9]]

from petl import fieldmap, look
look(table1)
from collections import OrderedDict
mappings = OrderedDict()
# rename a field
mappings['subject_id'] = 'id'
# translate a field
mappings['gender'] = 'sex', {'male': 'M', 'female': 'F'}
# apply a calculation to a field
mappings['age_months'] = 'age', lambda v: v * 12
# apply a calculation to a combination of fields
mappings['bmi'] = lambda rec: rec['weight'] / rec['height']**2 
# transform and inspect the output
table2 = fieldmap(table1, mappings)
look(table2)
# field mappings can also be added and/or updated after the table is created 
# via the suffix notation
table3 = fieldmap(table1)
table3['subject_id'] = 'id'
table3['gender'] = 'sex', {'male': 'M', 'female': 'F'}
table3['age_months'] = 'age', lambda v: v * 12
# use an expression string this time
table3['bmi'] = '{weight} / {height}**2'
look(table3)


# facet

table1 = [['foo', 'bar', 'baz'],
          ['a', 4, 9.3],
          ['a', 2, 88.2],
          ['b', 1, 23.3],
          ['c', 8, 42.0],
          ['d', 7, 100.9],
          ['c', 2]]

from petl import facet, look
look(table1)
foo = facet(table1, 'foo')
foo.keys()
look(foo['a'])
look(foo['c'])


# selectre

table1 = (('foo', 'bar', 'baz'),
          ('aa', 4, 9.3),
          ('aaa', 2, 88.2),
          ('b', 1, 23.3),
          ('ccc', 8, 42.0),
          ('bb', 7, 100.9),
          ('c', 2))

from petl import selectre, look    
look(table1)
table2 = selectre(table1, 'foo', '[ab]{2}')
look(table2)


# rowreduce

table1 = [['foo', 'bar'],
          ['a', 3],
          ['a', 7],
          ['b', 2],
          ['b', 1],
          ['b', 9],
          ['c', 4]]

from petl import rowreduce, look    
look(table1)
def sumbar(key, rows):
    return [key, sum([row[1] for row in rows])]

table2 = rowreduce(table1, key='foo', reducer=sumbar, fields=['foo', 'barsum'])
look(table2)


# recordreduce

table1 = [['foo', 'bar'],
          ['a', 3],
          ['a', 7],
          ['b', 2],
          ['b', 1],
          ['b', 9],
          ['c', 4]]

from petl import recordreduce, look    
look(table1)
def sumbar(key, records):
    return [key, sum([rec['bar'] for rec in records])]

table2 = recordreduce(table1, key='foo', reducer=sumbar, fields=['foo', 'barsum'])
look(table2)


# mergereduce

table1 = [['foo', 'bar', 'baz'],
          ['A', 1, 2.7],
          ['B', 2, None],
          ['D', 3, 9.4],
          ['B', None, 7.8],
          ['E', None],
          ['D', 3, 12.3],
          ['A', 2, None]]

from petl import mergereduce, look    
look(table1)
table2 = mergereduce(table1, 'foo')
look(table2)


# merge

table1 = [['foo', 'bar', 'baz'],
          [1, 'A', True],
          [2, 'B', None],
          [4, 'C', True]]
table2 = [['bar', 'baz', 'quux'],
          ['A', True, 42.0],
          ['B', False, 79.3],
          ['C', False, 12.4]]

from petl import look, merge
look(table1)
look(table2)
table3 = merge(table1, table2, key='bar')
look(table3)


# aggregate

table1 = [['foo', 'bar'],
          ['a', 3],
          ['a', 7],
          ['b', 2],
          ['b', 1],
          ['b', 9],
          ['c', 4],
          ['d', 3],
          ['d'],
          ['e']]

from petl import aggregate, look
look(table1)
from collections import OrderedDict
aggregators = OrderedDict()
aggregators['minbar'] = 'bar', min
aggregators['maxbar'] = 'bar', max
aggregators['sumbar'] = 'bar', sum
aggregators['listbar'] = 'bar', list
table2 = aggregate(table1, 'foo', aggregators)
look(table2)
# aggregation functions can also be added and/or updated using the suffix
# notation on the returned table object, e.g.::
table3 = aggregate(table1, 'foo')
table3['minbar'] = 'bar', min
table3['maxbar'] = 'bar', max
table3['sumbar'] = 'bar', sum
table3['listbar'] = 'bar' # default aggregation is list
look(table3)
