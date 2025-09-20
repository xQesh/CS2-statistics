import os
from config import PATH

def getDemos():
    demos = []

    for i in os.listdir(PATH):
        file = os.path.split(i)[1]
        if file[-3:] == 'dem':
            demos.append(file)

    return(demos)