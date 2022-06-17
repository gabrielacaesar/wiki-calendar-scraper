from pandas._libs import index
import requests
import pandas as pd
import lxml.html
import json

base_links = pd.read_csv("base-links_calendar-trends.csv")

dic_lang = {'en': ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
            'de': ["Januar", "Februar", "März", "April", "Mai", "Juni", "Juli", "August", "September", "Oktober", "November", "Dezember"],
            'pt': ["janeiro", "fevereiro", "mar%C3%A7o", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],
            'es': ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
            'fr': ["janvier", "f%C3%A9vrier", "mars", "avril", "mai", "juin", "juillet", "ao%C3%BBt", "septembre", "octobre", "novembre", "d%C3%A9cembre"],
            'it': ["gennaio", "febbraio", "marzo", "aprile", "maggio", "giugno", "luglio", "agosto", "settembre", "ottobre", "novembre", "dicembre"],
            'nl': ["januari", "februari", "maart", "april", "mei", "juni", "juli", "augustus", "september", "oktober", "november", "december"]}

def get_events(user_input_month, user_input_lang):

  filter = base_links['url'].str.contains(f'{user_input_month}') & base_links['language'].str.contains(f'{user_input_lang}')

  filtered_base_links = base_links.loc[filter]
  url_list = filtered_base_links['url'].tolist()
  #print(url_list)
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
    elif user_input_lang == 'fr':
      eventos = doc.xpath('//span[@id="C.C3.A9l.C3.A9brations"]/parent::h2/following-sibling::ul/li')
    elif user_input_lang == 'it':
      eventos = doc.xpath('//span[@id="Feste_e_ricorrenze"]/parent::h2/following-sibling::ul/li')
    elif user_input_lang == 'nl':
      eventos = doc.xpath('//span[@id="Viering.2Fherdenking"]/parent::h2/following-sibling::ul/li')
    else:
      print("Failed!")  
      
    for evento in eventos:
      agenda = evento.text_content()
      agendas.append(agenda)
      url_agendas.append(url)
      
    dic_events = {'event': agendas,
                'url': url_agendas}
    df_events = pd.DataFrame(dic_events)

    df_events['date'] = df_events['url'].str.replace(f'http://{user_input_lang}.wikipedia.org/wiki/', '')
    df_events['date_clean'] = df_events['date'].str.replace('_', ' ')
    if user_input_lang in ['en', 'de', 'fr', 'it', 'nl']:
      df_events[['month', 'day']] = df_events['date_clean'].str.split(expand = True)
    elif user_input_lang in ['pt', 'es']:
      df_events[['day', 'month']] = df_events['date_clean'].str.replace(' de ', ' ').str.split(expand = True)
    else:
      print('other lang')
      
    month_id = dic_lang[f"{user_input_lang}"]
    df_events['month_id'] = month_id.index(f"{user_input_month}") + 1

    df_events['day'] = df_events['day'].str.pad(width=2, fillchar='0')
    df_events['month_id'] = df_events['month_id'].astype(str).str.pad(width=2, fillchar='0')
    df_events['format_date'] = df_events['month_id'].astype(str) + "/" + df_events['day'].astype(str)
    df_events.drop(['month', 'day', 'date'], inplace=True, axis=1) 

    #arquivo = df_events.to_csv(f"content_{user_input_lang}_{user_input_month}.csv", encoding='utf-8', index=False)
    json_events = df_events.to_json(f"{user_input_lang}-{df_events['month_id'].values[0]}-content.json", orient="records", date_format="iso")
    
  return json_events
