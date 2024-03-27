import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.offsetbox as offsetbox
import os

path = 'csv/140X_mcRun4_realistic_v3.csv'
geometry = pd.read_csv(path, sep=',', index_col=False)

region_name = 'RE-3'
region_geometry = geometry[geometry['roll_name'].str.startswith(region_name)]

fig, ax = plt.subplots(figsize=(40, 32))

for i in range(0, region_geometry.shape[0]):
    chamber = region_geometry.iloc[i]

    center_x = (chamber.x1 + chamber.x2 + chamber.x3 + chamber.x4) / 4
    center_y = (chamber.y1 + chamber.y2 + chamber.y3 + chamber.y4) / 4

    p1_p2_x = np.linspace((chamber.x1*9 + center_x)/10, (chamber.x2*9 + center_x)/10, 10)
    p1_p2_y = np.linspace((chamber.y1*9 + center_y)/10, (chamber.y2*9 + center_y)/10, 10)

    p2_p3_x = np.linspace((chamber.x2*9 + center_x)/10, (chamber.x3*9 + center_x)/10, 10)
    p2_p3_y = np.linspace((chamber.y2*9 + center_y)/10, (chamber.y3*9 + center_y)/10, 10)

    p3_p4_x = np.linspace((chamber.x3*9 + center_x)/10, (chamber.x4*9 + center_x)/10, 10)
    p3_p4_y = np.linspace((chamber.y3*9 + center_y)/10, (chamber.y4*9 + center_y)/10, 10)

    p4_p1_x = np.linspace((chamber.x4*9 + center_x)/10, (chamber.x1*9 + center_x)/10, 10)
    p4_p1_y = np.linspace((chamber.y4*9 + center_y)/10, (chamber.y1*9 + center_y)/10, 10)

    if region_name.startswith('W'):
        # W-2_RB3+_S05_Forward
        barrel_chamber_name = chamber.roll_name.split('_') # [W-2, RB3+, S05, Forward]
        ax.text(
            center_x, center_y,
            f'{barrel_chamber_name[2][2]}/{barrel_chamber_name[2][1:]}', # 3/05
            fontsize=18,
            va='center', ha='center'
        )

    elif region_name.startswith('RE'):
        # RE+3_R3_CH29_A
        endcap_chamber_name = chamber.roll_name.split('_') # [RE+3, R3, CH29, A]
        ax.text(
            center_x, center_y,
            f'{endcap_chamber_name[1][-1]}/{endcap_chamber_name[2][2:]}', # 3/29
            fontsize=18,
            va='center', ha='center'
        )
    
    p_x = np.concatenate((p1_p2_x, p2_p3_x, p3_p4_x, p4_p1_x))
    p_y = np.concatenate((p1_p2_y, p2_p3_y, p3_p4_y, p4_p1_y))

    if chamber.is_front == True:
        ax.plot(p_x, p_y, c="red")
    if chamber.is_front == False:
        ax.plot(p_x, p_y, c="blue")

ax.set_xlabel('Local X', fontsize=50)
ax.set_ylabel('Local Y', fontsize=50)

plt.plot([], [], c='red', label='front chamber')
plt.plot([], [], c='blue', label='back chamber')
ax.legend(fontsize=50)

global_tag = '140X_mcRun4_realistic_v3'
ax.set_title(f'RPC Geometry: {region_name}', fontsize=60)


geometry_tag = 'RPCRECO_Geometry_81YV023'
payload = 'b8e92ca3e159b405def0de06b5c4abd3a1b4000f'
offsetbox = offsetbox.AnchoredText(
    f'From GT: {global_tag}\nTag: {geometry_tag}\nPayload: {payload} ',
    #f'From CMSSW: rpcf/2024/v2',
    loc='upper left',
    prop=dict(size=26)
)
ax.add_artist(offsetbox)


plt.savefig(f'png/{global_tag}-{region_name}.png')
