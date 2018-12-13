'''
Fill each each function stub (replace the "pass") according to the docstring.
To run the unit tests: Make sure you are in the root dir:assessment-day1 Then run the tests with this command: "make test"
'''

import numpy as np
import pandas as pd

### Python

def count_characters(string):
    '''
    INPUT: STRING
    OUTPUT: DICT (STRING => INT)

    Return a dictionary which contains a count of the number of times each
    character appears in the string.
    Characters which would have a count of 0 should not need to be included in
    your dictionary.
    '''
    return {k: string.count(k) for k in set(string)}


def invert_dictionary(d):
    '''
    INPUT: DICT (STRING => INT)
    OUTPUT: DICT (INT => SET OF STRINGS)

    Given a dictionary d, return a new dictionary with d's values as keys and
    the value for a given key being the set of d's keys which have the same
    value.
    e.g. {'a': 2, 'b': 4, 'c': 2} => {2: {'a', 'c'}, 4: {'b'}}
    '''
    out_dic = {}

    for k, v in d.iteritems():
        if v in out_dic.keys():
            out_dic[v].add(k)
        else:
            out_dic[v] = set(k)

    return out_dic

def word_count(filename):
    '''
    INPUT: STRING
    OUTPUT: (INT, INT, INT)

    filename refers to a text file.
    Return a tuple containing these stats for the file in this order:
      1. number of lines
      2. number of words (broken by whitespace)
      3. number of characters
    '''
    char_cnt = 0
    word_cnt = 0
    line_cnt = 0

    with open(filename) as f:
        for line in f:
            char_cnt += len(line)
            word_cnt += len(line.split())
            line_cnt += 1

    return (line_cnt, word_cnt, char_cnt)

def matrix_multiplication(A, B):
    '''
    INPUT: LIST OF LIST OF INTEGERS, LIST OF LIST OF INTEGERS
    OUTPUT: LIST OF LIST of INTEGERS

    A and B are matrices with integer values, encoded as lists of lists:
    e.g. A = [[2, 3, 4], [6, 4, 2], [-1, 2, 0]] corresponds to the matrix:
    | 2  3  4 |
    | 6  4  2 |
    |-1  2  0 |
    Return the matrix which is the product of matrix A and matrix B.
    You may assume that A and B are square matrices of the same size.
    You may not use numpy. Write your solution in straight python.
    '''
    out_list = []

    for i in xrange(len(A)):
        out_raw = []
        for j in xrange(len(A[i])):
            out_element = 0
            for k in xrange(len(A[i])):
                out_element += A[i][k] * B[k][j]
            out_raw.append(out_element)
        out_list.append(out_raw)

    return out_list

### Probability

def cookie_jar(a, b):
    '''
    INPUT: FLOAT, FLOAT
    OUTPUT: FLOAT

    There are two jars of cookies with chocolate and peanut butter cookies.
    a: fraction of Jar A which is chocolate
    b: fraction of Jar B which is chocolate
    A jar is chosen at random and a cookie is drawn.
    The cookie is chocolate.
    Return the probability that the cookie came from Jar A.
    '''
    PA = 0.5
    PB = 0.5
    PCA = a
    PCB = b
    PC = 0.5 * (a + b)
    PAC = PA*PCA / PC

    return a / (a + b)

### NumPy

def array_work(rows, cols, scalar, matrixA):
    '''
    INPUT: INT, INT, INT, NUMPY ARRAY
    OUTPUT: NUMPY ARRAY

    Create matrix of size (rows, cols) with the elements initialized to the
    scalar value. Right multiply that matrix with the passed matrixA (i.e. AB,
    not BA).
    Return the result of the multiplication.
    You should be able to accomplish this in a single line.

    Ex: array_work(2, 3, 5, [[3, 4], [5, 6], [7, 8]])
           [[3, 4],      [[5, 5, 5],
            [5, 6],   *   [5, 5, 5]]
            [7, 8]]
    '''
    new_arr = np.empty(rows * cols).reshape((rows, cols))
    new_arr.fill(scalar)

    return matrixA.dot(new_arr)


def boolean_indexing(arr, minimum):
    '''
    INPUT: NUMPY ARRAY, INT
    OUTPUT: NUMPY ARRAY

    Returns an array with all the elements of "arr" greater than
    or equal to "minimum"

    Ex:
    In [1]: boolean_indexing([[3, 4, 5], [6, 7, 8]], 7)
    Out[1]: array([7, 8])
    '''
    condition = arr >= minimum

    return np.extract(condition, arr)


### Pandas

def make_series(start, length, index):
    '''
    INPUT: INT, INT, LIST
    OUTPUT: PANDAS SERIES

    Create a pandas Series of length "length"; its elements should be
    sequential integers starting from "start".
    The series' index should be "index".

    Ex:
    In [1]: make_series(5, 3, ['a', 'b', 'c'])
    Out[1]:
    a    5
    b    6
    c    7
    dtype: int64
    '''
    return pd.Series(np.arange(start, start + length), index = index)


def data_frame_work(df, colA, colB, colC):
    '''
    INPUT: DATAFRAME, STR, STR, STR
    OUTPUT: None

    Insert a column (colC) into the dataframe that is the sum of colA and colB.
    '''
    df[colC] = df[colA] + df[colB]



### SQL
# For each of these, your python function should return a string that is the
# SQL statement which answers the question.
# For example:
#    return "SELECT * FROM farmersmarkets;"
# You may want to run "sqlite3 markets.sql" in the command line to test out
# your queries.
#
# There are two tables in the database with these columns:
# statepopulations: state, pop2010, pop2000
# farmersmarkets: FMID, MarketName, Website, Street, City, County, State,
#    WIC, WICcash
#    (plus other columns we don't care about for this exercise)

def markets_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL query which gives the states and the number of markets
    that take WIC or WICcash for each state.
    The WIC and WICcash columns contain either 'Y' or 'N'
    '''
    return """
        SELECT State, COUNT(*)
        FROM farmersmarkets
        WHERE WIC = 'Y'
        OR WICcash = 'Y'
        GROUP BY State;
    """

def state_population_gain():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives the 10 states with the highest
    population gain from 2000 to 2010.
    '''
    return """
        SELECT state, pop2010 - pop2000 AS popgain
        FROM statepopulations
        ORDER BY popgain DESC
        LIMIT 10;
        """


def market_density_per_state():
    '''
    INPUT: NONE
    OUTPUT: STRING

    Return a SQL statement which gives a table containing each state and the
    number of people per farmers market (use the population number from 2010).
    If a state does not appear in the farmersmarket table, it should still
    appear in your result with a value of 0.
    '''

    return """
        SELECT
            sp.state,
            IFNULL(sp.pop2010 / COUNT(fm.MarketName), 0) AS npfm
        FROM statepopulations sp
        LEFT OUTER JOIN farmersmarkets fm
        ON sp.state = fm.state
        GROUP BY sp.state;
       """
