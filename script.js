// variavel
let optionLanguage = document.querySelector('#language')
let optionMonth = document.querySelector('#month')

// fetch
function definirOutput() {
  
  if (['en', 'pt', 'de', 'es'].includes(optionLanguage.value)){
  
  let url = `./data/${optionLanguage.value}-${optionMonth.value}-content.json`;
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
      for (let key of Object.keys(data)){
        let int_key = parseInt(key)
        let row = data[int_key]
        let efemeride = '<li><a href="' + row.url + '">' + row.date + '</a> - ' + row.event + '</li>';
        html += efemeride
      }
      // insere dentro do ul no html
      document.querySelector('ul').innerHTML = html
      console.log(data);
    }
  )
  }else{
    console.log('oi')
  }
}

// executa funcao considerando variavel
optionLanguage.addEventListener('change', definirOutput)
optionMonth.addEventListener('change', definirOutput)
