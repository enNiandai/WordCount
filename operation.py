import os

def operation(file_name, operation_code, datas):
    if operation_code == '-c':
        print('%s, 字符数: %d' % (file_name, datas['character_count']))
    elif operation_code == '-w':
        print('%s, 单词数: %d' % (file_name, datas['word_count']))
    elif operation_code == '-l':
        print('%s, 行数: %d' % (file_name, datas['line_count']))
    elif operation_code == '-o':
        try:
            f = open("result.txt", 'w+')
            f.write('%s: \n字母数: %s\n单词数: %s\n行数：%s' % (file_name, datas['character_count'], datas['word_count'], datas['line_count']))
            print('Writing to file is complete!')
        except Exception as err:
            print(err)
        finally:
            f.close()
    else:
        print("It is a error!")