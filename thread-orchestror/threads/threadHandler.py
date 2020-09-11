import threading

class threadHandler(threading.Thread):
    def __init__(self,threadID,
                      threadLabel,
                      deployer,
                      *args):
        threading.Thread.__init__(self)
        self.thread_label = threadLabel
        self.threadID = threadID
        self.deployer = deployer

    def run(self):
        self.deployer.deploy()
