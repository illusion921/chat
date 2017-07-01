
#coding:utf-8
import models
import Queue


class chat_handle(object):
    def __init__(self):
        self.queue = Queue.Queue()

    def get_msg(self,request):
        new_msg=[]

        if self.queue.qsize()>0:
            for i in range(self.queue.qsize()):
                msgs = self.queue.get_nowait()
                new_msg.append(msgs)
        else:
            try:
                new_msg.append(self.queue.get(timeout=10)) #将get请求阻塞60s
            except Queue.Empty,e:
                print str(e)

        return new_msg