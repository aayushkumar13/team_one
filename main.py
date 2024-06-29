from  reading_pdf_text import reading_pdf_text
from gemini_response import get_prompt_response

import pandas as pd


file_path = "metadata_file.xlsx"

df = pd.read_excel(file_path)

files_list=df.to_dict(orient='records')

file_text={}

for record in files_list:
    file_name = record['file_name']
    file_extension = record['file_extension']
    file_type=record['file_type']
    file_text[file_type] = (
        file_text.get(file_type, '') + '   ' + reading_pdf_text('pdf/' + file_name + file_extension)
    )


for file_type in file_text:
    file_text[file_type] = file_text[file_type].replace('\n', '    ')
    res = get_prompt_response(file_text[file_type])
    print(f'Possible template for {file_type} is : {res}')

