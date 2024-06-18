const closemodal = () =>
  document.getElementById('modal_form').classList.add('hidden');

const openmodal = () =>
  document.getElementById('modal_form').classList.remove('hidden');

function showOnList(params) {
  //json.parse transforma o json  em um objeto javascript
    const produto_objeto = JSON.parse(params.produto);
    document.getElementById('id').value = produto_objeto.id
    document.getElementById('nome_produto').value = produto_objeto.nome_produto
    document.getElementById('descricao_produto').value = produto_objeto.descricao
    document.getElementById('preco_produto').value = produto_objeto.preco
    document.getElementById('quantidade_produto').value = produto_objeto.estoque
    document.getElementById('fabricante_produto').value = produto_objeto.fabricante
    document.getElementById('categoria_produto').value = produto_objeto.categoria

    openmodal();
}

// getProductDetails(id: string): Promise<...response>
async function getProductDetails(id) {
  // Sempre valide o parâmetro esperado
  // Isso deixa seu código mais seguro e minimiza as falhas
  if (!id) return console.error(`Id (${id}) is not valid`);

  try {
    // Fetch esperar (e busca) uma resposta (dados) da api (URL)
    const response = await fetch(
      `http://127.0.0.1:8000/details_produto/${id}/`,
      {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      }
    );
    
    // Validação: URL certa? Senão HTTP error (erro de URL)
    // throw === lança (do verbo "lançar"). throw lança um erro
    if (!response) throw new Error('HTTP error');

    // Obtenção dos dados em formato JSON
    //console.log(await response.json());
    const params = await response.json()
    showOnList(params);
    
    
  } catch (error) {
    console.error(`Erro na busca dos dados: ${error}`);
  }
}
