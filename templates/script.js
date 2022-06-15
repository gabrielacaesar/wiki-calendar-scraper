// variavel

let optionLanguage = document.querySelector('#language')
let optionMonth = document.querySelector('#month')

console.log(optionLanguage.value);
console.log(optionMonth.value);

// executa funcao considerando variavel
optionLanguage.addEventListener('change', definirOutput)
optionMonth.addEventListener('change', definirOutput)

// fetch
function definirOutput() {

  console.log(optionLanguage.value)
  console.log(optionMonth.value)
  // dados com endpoint
  //let url = 'https://raw.githubusercontent.com/gabrielacaesar/wiki-calendar-scraper/main/data/' + optionLanguage.value + "-" + optionMonth.value + '-content.json?token=GHSAT0AAAAAABTCSP6ODVDWSZ63YZX6H2YUYVI4KZA'

  // dados locais

  let url;

  if (optionLanguage.value == 'pt') {

    url = `../data/pt-${optionMonth.value}-content.json`;

  } else {

    console.log('Só temos dados em português, sorry gringos.');
    return

  }

  console.log(url)
  // esperar carregar para o console.log
  fetch(url).then(
    function(resposta){
      return resposta.json()
    }
  ).then(
    function(data) {
      let html = '';
      for (let row of data){
        let efemeride = '<li><a href="' + row.url + '">' + row.event + '</a></li>';
        html += efemeride
      }
      document.querySelector('ul').innerHTML = html
      console.log(data);
    }
  )

}


