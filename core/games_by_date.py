# includes
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
import seaborn as sns

sns.set_theme(style="darkgrid")

directory = "D:/system_reboot_docs/2021.07.17/Wc3 replays/127492333/Replays/1900_by_Fingon_with_orcs_full_replay-pack" \
            "/1900 by Fingon with orcs (full replay-pack)"
all_replays = Path(directory).rglob('*.w3g')
tablichka = {}
for replay_name in all_replays:
    if replay_name.stat().st_size < 20000:
        continue
    date = str(replay_name.stem).split('_', 1)[1].replace('_', '/')
    date = pd.to_datetime(date[:10] + ' ' + date[11:13] + ':' + date[13:]) - pd.Timedelta("5 hours")
    date = date.replace(hour=0, minute=0)
    if date in tablichka:
        tablichka[date] += 1
    else:
        tablichka[date] = 1

items = tablichka.items()
data = pd.DataFrame({"date": [i[0] for i in items], "games": [i[1] for i in items]})
data = data.set_index("date").resample('D').asfreq().fillna(0).reset_index()
sns.lineplot(x="date", y="games", data=data, palette="tab10", linewidth=2.5)

plt.show(block=True)
