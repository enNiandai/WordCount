import sys
import os

gpus = sys.argv[2]

batch_size = sys.argv[1]
file_name=gpus
line_count=0
word_count=0
character_count=0

with open(file_name,'r',encoding='utf-8') as f:
    for line in f:
        if line.strip()=='':
            continue
        word=line.split()
        line_count+=1
        word_count+=len(word)
        character_count+=len(line)

if batch_size=='-c':
    print('%s, 字符数: %d'%(file_name, character_count))
elif batch_size=='-w':
    print('%s, 单词数: %d'% (file_name, word_count))
elif batch_size == '-l':
    print('%s, 行数: %d'% (file_name, line_count))
elif batch_size == '-o':
    try:
        f = open("result.txt", 'w+')
        f.write('%s: 字母数: %s\n单词数: %s\n行数： %s'% (file_name, character_count, word_count, line))
    except Exception as err:
        print(err)
    finally:
        f.close()
else:
    print("It is a error!")


