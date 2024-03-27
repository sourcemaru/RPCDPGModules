import pandas as pd


#path = '140X_mcRun3_2024_design_v6.csv'
path = 'auto_run3_data.csv'
geometry = pd.read_csv(path, sep=',', index_col=False)

geometry = geometry.sort_values(by='roll_name')
geometry = geometry.round(decimals=2)

geometry.to_csv(f"sorted_{path}", index=False)