from awpy import Demo
import pandas as pd
from config import PATH

import json

from demos import getDemos


def parseDemo():
    demo = getDemos()

    dem = Demo(PATH + demo[0])
    p = dem.parse()

    kills_data = dem.kills.to_pandas()
    kills = kills_data.groupby("attacker_name").size()
    deaths = kills_data.groupby("victim_name").size()
    assists = kills_data.groupby("assister_name").size()

    stats = pd.DataFrame({
        "Kills": kills,
        "Deaths": deaths,
        "Assists": assists,
    }).fillna(0)

    stats["KD"] = (stats["Kills"] / stats["Deaths"].replace(0, 1)).round(2)

    stats = stats.reset_index().rename(columns={"index": "Player"})

    data = stats.to_json(orient = 'records', indent = 2)

    file = f'./data/{demo[0]}'

    try:
        with open(file, 'x') as f:
            f.write(data)

    except:
        print("Ten plik został już utworzony wcześniej")

parseDemo()