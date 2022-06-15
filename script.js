// variavel
let optionLanguage = document.querySelector('#language')
let optionMonth = document.querySelector('#month')

// executa funcao considerando variavel
optionLanguage.addEventListener('change', definirOutput)
optionMonth.addEventListener('change', definirOutput)

// fetch
function definirOutput() {

  let url = `https://raw.githubusercontent.com/gabrielacaesar/wiki-calendar-scraper/main/data/${optionLanguage.value}-${optionMonth.value}-content.json`;
  console.log(url)

  // esperar carregar para o console.log
  fetch(url).then(
    function(resposta){
      return resposta.json()
    }
  ).then(
    function(data) {
      let html = '';
      // insere dados em cada linha com o respectivo link
      // adiciona cada linha ao html
      for (let row of data){
        let efemeride = '<li><a href="' + row.url + '">' + row.event + '</a></li>';
        html += efemeride
      }
      // insere dentro do ul no html
      document.querySelector('ul').innerHTML = html
      console.log(data);
    }
  )

}
