from pathlib import Path
import os

def get_root_folder():
    return Path(Path(__file__).parent).parent

folders = {
    "main_bash_script":os.path.join(get_root_folder(),"scripts/","main.sh")
}