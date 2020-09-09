import argparse

def startCommandLineArgumentsParser():
    parser = argparse.ArgumentParser(description='Deploy all your projects with openSCI, the simple one')
    parser.add_argument('--projectsRoots',nargs='+',help='Where is the main locations of yours projects? Put it here',required=True)
    parser.add_argument('--projectsLabels',nargs='+',help='What label you want to give to your projects? Put it here',required=True)
    return parser