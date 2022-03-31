# Sao Paulo, 31 de março de 2022
# Gabriela Caesar

## you may prefer to check wiki's api

library(tidyverse)
library(rvest)

# BRAZIL
urls <- paste0("http://pt.wikipedia.org/wiki/", 1:31)

months <- c("_de_janeiro", 
            "_de_fevereiro", 
            "_de_mar%C3%A7o", 
            "_de_abril", 
            "_de_maio", 
            "_de_junho", 
            "_de_julho",
            "_de_agosto",
            "_de_setembro",
            "_de_outubro",
            "_de_novembro",
            "_de_dezembro")

get_dates <- function(i){
  urls %>%
    paste0(months[i]) %>%
    as.data.frame() %>%
    rename(date = ".") %>%
    bind_rows()
}

all_dates <- map_dfr(1:12, get_dates)

exceptions <- "29_de_fevereiro|30_de_fevereiro|31_de_fevereiro|31_de_abril|31_de_junho|31_de_setembro|31_de_novembro"

all_dates_tidy <- all_dates %>%
  filter(!str_detect(date, exceptions))

all_dates_vec <- as.vector(all_dates_tidy$date)

get_calendar <- function(i){
  all_dates_vec[i] %>%
  read_html() %>%
  html_nodes(xpath = "//span[@id='Feriados_e_eventos_c.C3.ADclicos']/ancestor::h2/following-sibling::ul") %>%
  html_text() %>%
  as.data.frame() %>%
  rename(text = ".") %>%
  mutate(url = all_dates_vec[i],
         date = basename(all_dates_vec[i]))
}

calendar <- map_df(1:length(all_dates_vec), get_calendar)

calendar_final <- calendar %>% 
  mutate(date = str_trim(str_replace_all(date, "_", " ")),
         date = str_replace_all(date, "mar%C3%A7o", "março"))

write.csv(calendar_final, "calendar_final.csv", row.names = F)

# US

us_months <- c("January_", 
            "February_", 
            "March_", 
            "April_", 
            "May_", 
            "June_", 
            "July_",
            "August_",
            "September_",
            "October_",
            "November_",
            "December_")

us_urls <- paste0("http://en.wikipedia.org/wiki/", us_months)

us_get_dates <- function(i){
  us_urls %>%
    paste0(i) %>%
    as.data.frame() %>%
    rename(date = ".") %>%
    bind_rows()
}

us_all_dates <- map_dfr(1:31, us_get_dates)

us_exceptions <- "February_29|February_30|February_31|April_31|June_31|September_31|November_31"

us_all_dates_tidy <- us_all_dates %>%
  filter(!str_detect(date, us_exceptions)) 

us_all_dates_vec <- as.vector(us_all_dates_tidy$date)

us_get_calendar <- function(i){
  us_all_dates_vec[i] %>%
    read_html() %>%
    html_nodes(xpath = "//span[@id='Holidays_and_observances']/ancestor::h2/following-sibling::ul") %>%
    html_text() %>%
    as.data.frame() %>%
    rename(text = ".") %>%
    mutate(url = us_all_dates_vec[i],
           date = basename(us_all_dates_vec[i]))
}

us_calendar <- map_df(1:length(us_all_dates_vec), us_get_calendar)

us_calendar_final <- us_calendar %>% 
  mutate(date = str_trim(str_replace_all(date, "_", " "))) %>%
  filter(!str_detect(text, "The New York Times"),
         !str_detect(text, "Historical Events on"))

write.csv(us_calendar_final, "us_calendar_final.csv", row.names = F)
