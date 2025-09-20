from awpy import Demo
import pandas as pd

# ścieżka do pliku .dem
demo_path = "D:/SteamLibrary/steamapps/common/Counter-Strike Global Offensive/game/csgo/replays/match730_003667176030184931421_1136497017_189.dem"

# parser – output jako JSON
dem = Demo(demo_path)

data = dem.parse()


# Access various dictionaries & dataframes
dem.header
dem.rounds
dem.grenades
dem.kills
dem.damages
dem.bomb
dem.smokes
dem.infernos
dem.shots
dem.ticks

# --- Stats K/D/A ---
kills_df = dem.kills.to_pandas()
kills = kills_df.groupby("attacker_name").size()
deaths = kills_df.groupby("victim_name").size()
assists = kills_df.groupby("assister_name").size()

# --- ADR ---
damages_df = dem.damages.to_pandas()

# sumujemy obrażenia zadane przez gracza
total_damage = damages_df.groupby("attacker_name")["dmg_health_real"].sum()

# liczba rund
rounds_played = dem.rounds.to_pandas().shape[0]

# ADR = suma obrażeń / liczba rund
adr = (total_damage / rounds_played).round(1)
stats = pd.DataFrame({
    "Kills": kills,
    "Deaths": deaths,
    "Assists": assists,
    "ADR": adr
}).fillna(0)

stats["K/D"] = (stats["Kills"] / stats["Deaths"].replace(0, 1)).round(2) # unikamy dzielenia przez 0
print(stats)

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


print(dem.rounds.to_pandas())
