import os

def getDemos():
    path = 'D:/SteamLibrary/steamapps/common/Counter-Strike Global Offensive/game/csgo/replays/'

    demos = []

    for i in os.listdir(path):
        file = os.path.split(i)[1]
        if file[-3:] == 'dem':
            demo = path + file
            demos.append(demo)

    return(demos)