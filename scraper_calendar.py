import requests
import pandas as pd
import lxml.html
import json

base_links = pd.read_csv("base-links_calendar-trends.csv")

def get_events(user_input_month, user_input_lang):

  filter = base_links['url'].str.contains(f'{user_input_month}') & base_links['language'].str.contains(f'{user_input_lang}')

  filtered_base_links = base_links.loc[filter]
  urls = filtered_base_links['url'].tolist()
  agendas = []
  url_agendas = []
  
  for url in urls:
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
    df_events['date'] = df_events['date'].str.replace('_', ' ')

    #arquivo = df_events.to_csv(f"content_pt_{user_input_month}.csv", encoding='utf-8', index=False)
    #json_events = df_events.to_json(orient="index", force_ascii=False)
    #content_pt_01 = json.dumps(json_events)
    
  return df_events
