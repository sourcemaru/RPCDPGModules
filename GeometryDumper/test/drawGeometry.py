import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

geometry = pd.read_csv('rpcf_2024_v2.csv', sep=",", index_col=False)

target_region = "RE-3"
target_geometry = geometry[geometry["roll_name"].str.startswith(target_region)]


plt.figure(figsize=(40, 32))

for i in range(0, target_geometry.shape[0]):
    chamber = target_geometry.iloc[i]
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

    #endcap_chamber_name = chamber.roll_name.split("_")
    #plt.text(
    #    center_x,
    #    center_y,
    #    endcap_chamber_name[0] + "/" + endcap_chamber_name[1][-1] + "/" +  endcap_chamber_name[2][2:],
    #    fontsize=16,
    #    verticalalignment='center',
    #    horizontalalignment='center'
    #)


    plt.plot(p1_p2_x, p1_p2_y, c="black")
    plt.plot(p2_p3_x, p2_p3_y, c="red")
    plt.plot(p3_p4_x, p3_p4_y, c="black")
    plt.plot(p4_p1_x, p4_p1_y, c="blue")

plt.xlabel("axis-x")
plt.ylabel("axis-y")
plt.title(f"Geometry: {target_region}\ncmssw:Geometry/MuonCommonData/data/rpcf/2024/v1/rpcf.xml")
plt.savefig("plot_rpcf_2024_v1_" + target_region + ".png")
