# Analysis of Vaccination Data from CoWin portal
import json
import pandas as pd
import os
from datetime import timedelta

directory = 'C:/karthik/vac-data/dump/'  ## Provide the path of the directory where sessions files are stored
files = os.listdir(directory)
print(len(files))

for f_name in files:
    sessions_list = []
    if f_name.endswith('sessions'):
        f_name = directory + f_name
        f = open(f_name)
        data = json.load(f)

        for d in data:
            d2 = d['sessions']['sessions'][0]
            d2['call_time'] = d['call_time']
            d2['received_time'] = d['received_time']
            sessions_list.append(d2)
    
    json_object = json.dumps(sessions_list)
    session_df = pd.read_json(json_object, orient = 'records')
    csv_filename = f_name + '.csv'
    session_df.to_csv(csv_filename)
    del session_df
