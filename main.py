import sys
from Count import Count
from operation import operation

operation_code = sys.argv[1]
file_name = sys.argv[2]

datas = {
    'line_count' : 0,
    'word_count' : 0,
    'character_count' : 0
}

datas = Count(file_name, 'r', datas)

operation(file_name, operation_code, datas)
