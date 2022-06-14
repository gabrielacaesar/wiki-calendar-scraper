// variavel

let optionLanguage = document.querySelector('#language')
let optionMonth = document.querySelector('#month')

console.log(optionLanguage.target.value)
console.log(optionMonth)

// executa funcao considerando variavel
optionLanguage.addEventListener('change', definirOutput)
optionMonth.addEventListener('change', definirOutput)

// fetch
function definirOutput(optionMonth, optionLanguage){

  console.log(optionLanguage.value)
  console.log(optionMonth.value)
  // dados com endpoint
  let url = 'https://raw.githubusercontent.com/gabrielacaesar/wiki-calendar-scraper/main/data/' + optionLanguage.target.value + "-" + optionMonth.target.value + '-content.json?token=GHSAT0AAAAAABTCSP6ODVDWSZ63YZX6H2YUYVI4KZA'

  console.log(url)
  // esperar carregar para o console.log
  fetch(url).then(
    function(resposta){
      console.log(resposta.json())
    }
  )

}
