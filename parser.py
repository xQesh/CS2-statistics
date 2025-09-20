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

    ticks = dem.ticks.to_pandas()
    player_to_team = ticks.groupby("name")["side"].first().to_dict()

    stats["Team"] = stats["Player"].map(player_to_team)

    data = {}

    for _, row in stats.iterrows():
        team = row["Team"]
        player = row["Player"]
        data.setdefault(team, {})[player] = {
            "Kills": int(row["Kills"]),
            "Deaths": int(row["Deaths"]),
            "Assists": int(row["Assists"]),
            "KD": float(row["KD"])
        }

    data_json = json.dumps(data, indent=2)

    file = f'./data/{demo[0]}'

    try:
        with open(file, 'x') as f:
            f.write(data_json)

    except:
        print("Ten plik został już utworzony wcześniej")



parseDemo()