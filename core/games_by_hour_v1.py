# includes
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

directory = "D:/system_reboot_docs/2021.07.17/Wc3 replays/127492333/Replays/1900_by_Fingon_with_orcs_full_replay-pack" \
            "/1900 by Fingon with orcs (full replay-pack)"
all_replays = Path(directory).rglob('*.w3g')
tablichka = {}
for replay_name in all_replays:
    if replay_name.stat().st_size < 20000:
        continue
    date = str(replay_name.stem).rsplit('_', 1)[1]
    date = pd.to_datetime(date[:2] + ":" + date[2:]).replace(minute=0)
    if date in tablichka:
        tablichka[date] += 1
    else:
        tablichka[date] = 1

items = tablichka.items()
data = pd.DataFrame({"date": [i[0] for i in items], "games": [int(i[1]) for i in items]})
data = data.set_index("date").resample('H').asfreq().fillna(0).reset_index()
data = pd.DataFrame({"hour": [t.hour for t in data["date"]], "games": [i for i in data["games"]]}).set_index("hour")
data.plot()

plt.show(block=True)
