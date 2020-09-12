import time
from common.consoleLogger import CustomLoger
import subprocess
from common.environment import folders

class Deployer:
    main_bash_deploy_script = folders["main_bash_script"]
    def __init__(self,projectFolderToBeDeployed,projectLabel,framework):
        self.projectFolderToBeDeployed = projectFolderToBeDeployed
        self.projectLabel = projectLabel
        self.framework = framework
        self.logger = CustomLoger(f'deployer-{projectFolderToBeDeployed}',20)

    def deploy(self):
        self.logger.log_to_console(f"{self.projectLabel} deploy requested")
        
        return_values = subprocess.check_call(f"{self.main_bash_deploy_script} {self.framework} -p={self.projectFolderToBeDeployed}",
                                              shell=True)
        self.logger.log_to_console(f"{self.projectLabel} deploy finished with {return_values} code")