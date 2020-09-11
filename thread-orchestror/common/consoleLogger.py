import logging
import time
class CustomLoger(logging.Logger):
    def __init__(self, name, level):
        super().__init__(name, level)

    def log_to_console(self,message):
        print(f"[{self.level} {time.ctime(time.time())}] {message}")

    