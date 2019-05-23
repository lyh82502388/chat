# .multiprocess创建两个进程，同时复制一个文件的上下两半部分，各自复制到一个新的文件里

from multiprocessing import Process, Pipe
import os

fo = open('bb.py', 'r+')

data = os.path.getsize(fo)
data01 = fo.read(data / 2)

# 当前位置开始读操作
data02 = fo.read()

file01 = open('test01', 'w+')

def copy01(pipe):
    pipe.send(data01)
    pipe.close()


def copy02(pipe):
    pipe.send(data02)
    pipe.close()


if __name__ == '__main__':

    #管道通信
    pipe = Pipe(duplex=True)
    p01 = Process(target=copy01, args=(pipe[0],))
    p02 = Process(target=copy01, args=(pipe[0],))
    p01.start()
    p02.start()
    newfile01 = open('newfile1.text', 'a+')
    newfile02 = open('newfile2.text', 'a+')
    msg01 = pipe[1].rece()
    msg02 = pipe[1].rece()
    newfile01.write(msg01)
    newfile02.write(msg02)
    p01.join()
    p02.join()
