library(tidyverse)
library(rvest)

urls <- paste0("https://pt.wikipedia.org/wiki/", 1:31)

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
  all <- paste0(urls, months[i])
  all <- as.data.frame(all)
  all_dates <- bind_rows(all)
}

all_dates <- map_dfr(1:12, get_dates)

exceptions <- '"28_de_fevereiro|29_de_fevereiro|30_de_fevereiro|31_de_fevereiro|31_de_abril|31_de_junho|31_de_setembro|31_de_novembro"'

all_dates_tidy <- all_dates %>%
  filter(!str_detect(all, exceptions))

all_dates_tidy[1] %>%
  read_html() %>%
  html_nodes("h2>span#Feriados_e_eventos_c.C3.ADclicos") %>%
  html_text()

