from awpy import Demo
import pandas as pd

from demos import getDemos


def parseDemo():
    demo = getDemos()

    dem = Demo(demo[0])
    data = dem.parse()

    kills_df = dem.kills.to_pandas()
    kills = kills_df.groupby("attacker_name").size()
    deaths = kills_df.groupby("victim_name").size()
    assists = kills_df.groupby("assister_name").size()


    stats = pd.DataFrame({
        "Kills": kills,
        "Deaths": deaths,
        "Assists": assists,
    }).fillna(0)

    stats["KD"] = (stats["Kills"] / stats["Deaths"].replace(0, 1)).round(2)

    print(stats)

parseDemo()