def Count(file_name, r, datas):

    with open(file_name,'r',encoding='utf-8') as f:
        for line in f:
            if line.strip()=='':
                continue
            word=line.split()
            datas['line_count']+=1
            datas['word_count']+=len(word)
            datas['character_count']+=len(line)

    return datas
