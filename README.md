# WordCount
---
## 题目描述
1. 实现一个简单而完整的软件工具（源程序特征统计程序）。
2. 进行单元测试、回归测试、效能测试，在实现上述程序的过程中使用相关的工具。
3. 进行个人软件过程（PSP）的实践，逐步记录自己在每个软件工程环节花费的时间。

## PSP
|PSP2.1|Personal Software Process Stages|预估耗时（分钟）|实际耗时（分钟）|
|:--|:--|:--|:--|
|Planning|计划| 15| 20|
|· Estimate|· 估计这个任务需要多少时间| 15| 20|
|Development|开发| 200| 370|
|· Analysis|· 需求分析 (包括学习新技术)| 20| 30|
|· Design Spec|· 生成设计文档| 10| 15|
|· Design Review|· 设计复审 (和同事审核设计文档)| 10| 10|
|· Coding Standard|· 代码规范 (为目前的开发制定合适的规范)| 5| 5|
|· Design|· 具体设计| 30| 35|
|· Coding|· 具体编码| 100| 250|
|· Code Review|· 代码复审| 10| 15|
|· Test|· 测试（自我测试，修改代码，提交修改）| 15| 30|
|Reporting|报告| 55| 100|
|· Test Report|· 测试报告| 15| 30|
|· Size Measurement|· 计算工作量| 15| 30|
|· Postmortem & Process Improvement Plan|· 事后总结, 并提出过程改进计划| 25| 40|
|合计|| 270| 490|

## 解题思路
将题目分成两部分，一部分为对文件文本进行计数，另一部分为对计数结果进行输出。并对于Python中现有的库进行寻找可以对文件文本进行操作的函数。

## 设计实现过程
代码分成了两个函数，一个是Count，对文件文本进行计数；另一个是operation，根据输入的操作码对计数结果进行输出。

## 代码说明
Count函数代码
```Python
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
```
用循环对文件进行遍历，以行为单位。如果该行是空行，则跳过。遍历每一行的时候将每一行进行拆分，从而统计每一行的单词数量与字符数量。

operation函数代码
```Python
def operation(file_name, operation_code, datas):
    if operation_code == '-c':
        print('%s, 字符数: %d' % (file_name, datas['character_count']))
    elif operation_code == '-l':
        print('%s, 行数: %d' % (file_name, datas['line_count']))
    elif operation_code == '-w':
        print('%s, 单词数: %d' % (file_name, datas['word_count']))
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
```
对输入进来的操作码进行判断，并输出。对于写入文件操作，将结果写入进文件“result.txt”中，并在命令行告诉用户输出完毕，随后关闭文件。

## 测试运行
![Github](https://img2020.cnblogs.com/blog/1962776/202003/1962776-20200324151810985-269493637.png)
![Github](https://img2020.cnblogs.com/blog/1962776/202003/1962776-20200324151847706-1845765483.png)
![Github](https://img2020.cnblogs.com/blog/1962776/202003/1962776-20200324151908762-1833566968.png)

## 项目小结
对于自己在PSP表中预计的情况来看，并没有完成的十分好。对于Python的掌握并不是很到位,争取在下一次的作业中可以让自己的python水平有进步。
