import os
import pandas as pd

folder_path = '/pdf'

file_list = []

for file in os.listdir(os.getcwd() + folder_path):

    file_name, file_ext = os.path.splitext(file)
    file_list.append([file_name, file_ext])

df = pd.DataFrame(file_list, columns=['File Name', 'File Extension'])

df.to_excel('metadata_file.xlsx', index=False)