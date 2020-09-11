import time
from common.consoleLogger import CustomLoger
from random import randint
class Deployer:
    def __init__(self,projectFolderToBeDeployed,projectLabel):
        self.projectFolderToBeDeployed = projectFolderToBeDeployed
        self.projectLabel = projectLabel
        self.logger = CustomLoger(f'deployer-{projectFolderToBeDeployed}',20)

    def deploy(self):
        self.logger.log_to_console(f"{self.projectLabel} deploy requested")
        time.sleep(1 + randint(0,9))
        self.logger.log_to_console(f"{self.projectLabel} deploy finished")