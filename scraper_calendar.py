from pandas._libs import index
import requests
import pandas as pd
import lxml.html
import json

base_links = pd.read_csv("base-links_calendar-trends.csv")

month_en = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
month_de = ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"]
month_pt = ["janeiro", "fevereiro", "mar%C3%A7o", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
month_es = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]

def get_events(user_input_month, user_input_lang):

  filter = base_links['url'].str.contains(f'{user_input_month}') & base_links['language'].str.contains(f'{user_input_lang}')

  filtered_base_links = base_links.loc[filter]
  url_list = filtered_base_links['url'].tolist()
  agendas = []
  url_agendas = []
  
  for url in url_list:
    page = requests.get(url)
    doc = lxml.html.fromstring(page.content)
    
    if user_input_lang == 'pt':
      eventos = doc.xpath('//span[@id="Feriados_e_eventos_c.C3.ADclicos"]/parent::h2/following-sibling::ul/li')
    elif user_input_lang == 'en':
      eventos = doc.xpath('//span[@id="Holidays_and_observances"]/parent::h2/following-sibling::ul/li')
    elif user_input_lang == 'de':
      eventos = doc.xpath('//span[@id="Feier-_und_Gedenktage"]/parent::h2/following-sibling::ul/li')
    elif user_input_lang == 'es':
      eventos = doc.xpath('//span[@id="Celebraciones"]/parent::h2/following-sibling::ul/li')
    else:
      print("Work in progress")  
      
    for evento in eventos:
      agenda = evento.text_content()
      agendas.append(agenda)
      url_agendas.append(url)
      
    dic_events = {'event': agendas,
                'url': url_agendas}
    df_events = pd.DataFrame(dic_events)

    df_events['date'] = df_events['url'].str.replace(f'http://{user_input_lang}.wikipedia.org/wiki/', '')

    if user_input_lang in ['en', 'de']:
      df_events['date'] = df_events['date'].str.replace('_', ' ')
      df_events[['month', 'day']] = df_events['date'].str.split(expand = True)
    elif user_input_lang in ['pt', 'es']:
      df_events['date'] = df_events['date'].str.replace('_de_', ' ')
      df_events[['day', 'month']] = df_events['date'].str.split(expand = True)
    else:
      print('other lang')

    df_events['month_id'] = month_es.index(f"{user_input_month}") + 1

    df_events['day'] = df_events['day'].str.pad(width=2, fillchar='0')
    df_events['month_id'] = df_events['month_id'].astype(str).str.pad(width=2, fillchar='0')
    df_events['format_date'] = df_events['month_id'].astype(str) + "/" + df_events['day'].astype(str)
    df_events.drop(['month', 'day'], inplace=True, axis=1) 

    #arquivo = df_events.to_csv(f"content_{user_input_lang}_{user_input_month}.csv", encoding='utf-8', index=False)
    json_events = df_events.to_json(f"{user_input_lang}-{user_input_month}-content.json", orient="index", date_format="iso")
    #content_pt_01 = json.dumps(json_events)
    
  return json_events
