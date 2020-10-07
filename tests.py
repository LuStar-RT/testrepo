
'''
def mystery(s):
    i = 0
    result = ''

    while not s[i].isdigit():
        result = result + s[i]
        i = i + 1

    return result


print(mystery('123'))

def example(L):
    """ (list) -> list
    """
    i = 0
    result = []
    while i < len(L):
        result.append(L[i])
        i = i + 3
    return result

print(example([1,2,3,4,5,6,7,8,9]))

def compress_list(L):
    """ (list of str) -> list of str

    Return a new list with adjacent pairs of string elements       from Lconcatenated together, starting with indices 0 and 1,    2 and 3,and so on.

    Precondition: len(L) >= 2 and len(L) % 2 == 0

    >>> compress_list(['a', 'b', 'c', 'd'])
    ['ab', 'cd']
    """
    compressed_list = []
    i = 0

    while i < len(L):
        compressed_list.append(L[i] + L[i + 1])
        i = i + 2
        return compressed_list

print(compress_list(['a', 'b', 'c', 'd']))

suma = 0
i = 1523
while i <= 10503:
    suma = suma + i
    i = i +2

print(suma)

def increment_items(L, increment):
    i = 0
    while i < len(L):
        L[i] = L[i] + increment
        i = i + 1

values = [1, 2, 3]
print(increment_items(values, 2))
print(values)

values = []
for num in range(3, 10, 3):
    values.append(num)
print(values)

#def matrixElementsSum(matrix):

def allLongestStrings(inputArray):
    max_string = max(len(i) for i in inputArray)
    result = [i for i in inputArray if len(i) == max_string]
    return result


inputArray = ["aba", "aa", "ad", "vcd", "aba"]

print(allLongestStrings(inputArray))
'''

def mystery(s) -> object:
    """ (str) -> bool
    Return true if an only if s is equal to the reverse of s
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is         this line reached?
            matches = matches + 1
    return matches == (len(s) // 2)

print(mystery('anitalavalatina'))


def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    for i in range(1, len(L)):
        L[len(L) - i] = L[len(L) - i - 1]

    L[0] = last_item

L = ['a', 'b', 'c', 'd']

shift_right(L)

print(L)

def make_pairs(list1, list2):
    ''' (list of str, list of int) -> list of [str, int] list

    Return a new list in which each item is a 2-item list with     the string from thecorresponding position of list1 and the     int from the corresponding position of list2.

    Precondition: len(list1) == len(list2)

    >>> make_pairs(['A', 'B', 'C'], [1, 2, 3])
    [['A', 1], ['B', 2], ['C', 3]]
    '''

    pairs = []

    for i in range(len(list1)):
        inner_list = []
        inner_list.append(list1[i])
        inner_list.append(list2[i])
        pairs.append(inner_list)

    return pairs

print(make_pairs(['A', 'B', 'C'], [1, 2, 3]))

values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(values[1][1])

treats = [['apple', 'pie'], ['vanilla', 'ice-cream'], ['chocolate', 'cake']]

print(treats[-3][-1])

for i in range(2, 5):
    for j in range(4, 9):
        print(i, j)


def contains(value, lst):
    """ (object, list of list) -> bool
    Return whether value is an element of one of the nested        lists in lst.
    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
    True
    """
    found = False  # We have not yet found value in the list.
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True
    return found

print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]]))


#
# def contains(value, lst):
#     """ (object, list of list) -> bool
#     Return whether value is an element of one of the nested        lists in lst.
#     >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])True
#    """
# found = False
#
#    for item in lst:
#        if value == item:
#             value = True
#
#    return found
#
# print(contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]]))
#
#
def lines_startswith(file, letter):
    """ (file open for reading, str) -> list of str
    Return the list of lines from file that begin with letter.     The lines should have thenewline removed.
    Precondition: len(letter) == 1
    """
    matches = []
    for line in file:
        if letter == line[0]:
            matches.append(line.rstrip('\n'))
    return matches

flander_file = open('In Fladers Fields.txt', 'r')
print('lines starswith: ', lines_startswith(flander_file, 'I'))

flander_file.seek(0,0) #Reset the cursor position to the beggining

a = [i for i in flander_file.readlines() if i.startswith('The torch')] #Comprehension list equivalent to the 'for' below

print(a)

flander_file.seek(0,0) #Reset the cursor position to the beggining

l = []
for i in flander_file.readlines():
    if i.startswith('The torch'):
        l.append(i)
print(l)
