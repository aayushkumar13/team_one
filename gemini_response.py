import google.generativeai as genai

api_key='AIzaSyD8KTrDWj1Hjm1fFImWPpdeFmcc34oFcnY'

genai.configure(api_key=api_key)

def get_prompt_response(text):
  input_prompt=f'Please list out (separated by comma) the the keywords or phrases that could be used as\
   fields of insurance related documents from the following text: |{text}|'


  response = genai.chat(messages=[input_prompt])
  # print(response.last)
  return response.last