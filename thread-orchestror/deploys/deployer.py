import time
from common.consoleLogger import CustomLoger
import subprocess
class Deployer:
    def __init__(self,projectFolderToBeDeployed,projectLabel,framework):
        self.projectFolderToBeDeployed = projectFolderToBeDeployed
        self.projectLabel = projectLabel
        self.framework = framework
        self.logger = CustomLoger(f'deployer-{projectFolderToBeDeployed}',20)

    def deploy(self):
        self.logger.log_to_console(f"{self.projectLabel} deploy requested")
        return_values = subprocess.check_call("./deployer/main.sh {} -p={}"
                                            .format(self.framework,self.projectFolderToBeDeployed),
                                            shell=True)
        self.logger.log_to_console(f"{self.projectLabel} deploy finished with {return_values} code")