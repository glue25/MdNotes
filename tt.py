import os
import shutil
def delete_pycache():
    dir_ = os.getcwd()
    target = '__pycache__'
    for dirs in os.walk(dir_) :
        for dir__ in dirs[1] :
            dirname = os.path.join(dirs[0], dir__)
            if target in dirname :
                print(dirname)
                shutil.rmtree(dirname)