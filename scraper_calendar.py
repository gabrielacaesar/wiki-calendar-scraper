import requests
import pandas as pd
import lxml.html

base_links = pd.read_csv("data/base-links_calendar-trends.csv")

def get_events(user_input_month, user_input_lang):

  filter = base_links['url'].str.contains(f'{user_input_month}') & base_links['language'].str.contains(f'{user_input_lang}')

  filtered_base_links = base_links.loc[filter]
  date_range = filtered_base_links['url'].tolist()
  agendas = []
  date_agendas = []
  
  for date in date_range:
    page = requests.get(date)
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
      date_agendas.append(date)
      
    dic_events = {'event': agendas,
                'url': date_agendas}
    df_events = pd.DataFrame(dic_events)
    json_events = df_events.to_json(orient="index")
    
  return json_events
