from parser.argsParser import startCommandLineArgumentsParser
from deploys.deployer import Deployer
from threads.threadHandler import threadHandler
class SCI:
    parser = startCommandLineArgumentsParser()
    def __init__(self):
        args =self.parser.parse_args()
        self.projects_paths = args.projectsRoots
        self.projects_labels = args.projectsLabels

    def deployAll(self):
        for project_id,project_path in enumerate(self.projects_paths):
            project_deployer = Deployer(project_path,self.projects_labels[project_id])
            project_threadHandler = threadHandler(project_id,self.projects_labels[project_id],project_deployer)
            project_threadHandler.start()
