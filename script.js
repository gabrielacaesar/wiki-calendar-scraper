// variavel
let optionLanguage = document.querySelector('#language')
let optionMonth = document.querySelector('#month')

console.log(optionLanguage.value)

// fetch
function definirOutput() {
  
  if (optionLanguage.value != 'blank' && optionMonth.value != 'blank'){
  
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
        let int_key = parseInt(key) // por conta do formato do json
        let row = data[int_key] // idem
        let efemeride = '<li><a href="' + row.url + '" target="_blank">' + row.date + '</a> - ' + row.event + '</li>';
        html += efemeride
      }
      // insere dentro do ul no html
      document.querySelector('ul').innerHTML = html
      console.log(data);
    }
  )
  }else{
    console.log('nao rolou!')
  }
}

// funcao para limpar resultado
function limparResultado() {
  if (optionLanguage.value == 'blank' || optionMonth.value == 'blank'){
    html = ''
    document.querySelector('ul').innerHTML = html
  }else{
    console.log('limpei!')
 }
}

// executa funcao considerando variavel
optionLanguage.addEventListener('change', definirOutput)
optionMonth.addEventListener('change', definirOutput)

optionLanguage.addEventListener('change', limparResultado)
optionMonth.addEventListener('change', limparResultado)
