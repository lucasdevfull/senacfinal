document.getElementById('update').addEventListener('click', () =>{
    async function formUpdate(id) {
        if (!id) return console.error(`Id (${id}) is not valid`);

        const formdata = {
            nome_produto: document.getElementById('nome_produto').value,
            descricao: document.getElementById('descricao_produto').value,
            preco: document.getElementById('preco_produto').value,
            quantidade: document.getElementById('quantidade_produto').value,
            fabricante: document.getElementById('fabricante_produto').value,
            categoria: document.getElementById('categoria_produto').value
        }
        
        try{
            const response = await fetch(`http://127.0.0.1:8000/editar_produto/${id}/`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'aplication/json',
                },
                body:JSON.stringify(formdata)
            })
            if(!response) throw new Error('HTTP error')

            const data = await response.json()
            console.log(data)
        } catch {
            console.error(`Error ao enviar os dados! ${error}`)
        } 

    }
    formUpdate('2')
})