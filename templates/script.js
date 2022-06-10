// variavel

let optionLanguage = document.querySelector('.language')
let optionMonth = document.querySelector('.month')

// executa funcao considerando variavel
optionLanguage.addEventListener('change', definirOutput)
optionMonth.addEventListener('change', definirOutput)

// funcao
function definirOutput(optionMonth, optionLanguage){

  // dados com endpoint
  let json = JSON.parse(`https://wiki-calendar-scraper.herokuapp.com/events?month=${optionMonth.value}&lang=${optionLanguage.value}`)
  
  // para cada linha do json vamos...
  for (let row of json) {
    console.log(row)  
    // considera o que o usuario colocou de mes e linguage
    if (row.month == optionMonth.value && row.language == optionLanguage.value){
      // retorna o df considerando condicao
      let result = df_events
      break
    }
  }
}
