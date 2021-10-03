# includes
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import w3g
from pathlib import Path

directory = "D:/system_reboot_docs/2021.07.17/Wc3 replays/127492333/Replays/1900_by_Fingon_with_orcs_full_replay-pack" \
            "/1900 by Fingon with orcs (full replay-pack)"
all_replays = Path(directory).rglob('*.w3g')
nicknames = ["Fingon#2350", "KawerOrda#2648"]

tablichka = dict()
for x in range(0, 24):
    tablichka[x] = [0, 0]

for replay_name in all_replays:  # e.g. Replay_2021_02_11_0111.w3g
    if replay_name.stat().st_size < 15000:
        continue
    hour = int(str(replay_name.stem).rsplit('_', 1)[1][:2])
    replay = w3g.File(replay_name.as_posix())
    winner = replay.player_name(replay.winner())
    if winner in nicknames:
        tablichka[hour][0] += 1
    else:
        tablichka[hour][1] += 1

data = {"hour": [], "result": [], "amount": []}
for x in range(0, 24):
    data["hour"].append(x)
    data["hour"].append(x)
    data["result"].append("wins")
    data["result"].append("losses")
    data["amount"].append(tablichka[x][0])
    data["amount"].append(tablichka[x][1])
sns.set_theme(style="whitegrid")
colours = ["lime" if (x == "wins") else "firebrick" for x in data["result"]]
sns.barplot(x="hour", y="amount", hue="result", data=data, palette=colours)

plt.show(block=True)
