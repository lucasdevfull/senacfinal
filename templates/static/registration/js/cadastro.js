document.getElementById('cep').addEventListener('input', function() {
    pesquisacep(this.value);
});

function pesquisacep(cep) {
    // Remove caracteres não numéricos do CEP
    cep = cep.replace(/\D/g, '');

    // Verifica se o CEP possui 8 dígitos
    if (cep.length !== 9) {
        limpa_formulário_cep();
        alert("CEP inválido");
        return;
    }

    // URL da API do ViaCEP
    var url = `https://viacep.com.br/ws/${cep}/json/`;

    // Faz a requisição usando fetch
    fetch(url)
        .then(response => {
            // Verifica se a requisição foi bem-sucedida
            if (!response.ok) {
                throw new Error('Erro ao buscar o CEP');
            }
            // Converte a resposta para JSON
            return response.json();
        })
        .then(data => {
            // Verifica se o CEP foi encontrado
            if (data.erro) {
                throw new Error('CEP não encontrado');
            }
            // Atualiza os campos do formulário com os dados do CEP
            document.getElementById('endereco').value = data.endereco;
            document.getElementById('estado').value = data.estado;
            document.getElementById('cidade').value = data.cidade;
            
            
        })
        .catch(error => {
            limpa_formulário_cep();
            alert(error.message);
        });
}

function limpa_formulário_cep(){
    document.getElementById('endereco').value = '';
    document.getElementById('estado').value = '';
    document.getElementById('cidade').value = '';
}