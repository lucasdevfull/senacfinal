//to criando uma função atraves de dom usando o id do elemento e adicionando um evento click 
document.getElementById('modalfab').addEventListener('click',function() {
    document.getElementById('fabricante').classList.remove('hidden');
})

document.getElementById('modalcate').addEventListener('click',function() {
    document.getElementById('categoria').classList.remove('hidden');
})

window.addEventListener('click',function(event) {
    if (event.target == document.getElementById('fabricante')) {
        document.getElementById('fabricante').classList.add('hidden');
    }
})


window.addEventListener('click',function(event) {
    if (event.target == document.getElementById('categoria')) {
        document.getElementById('categoria').classList.add('hidden');
    }
})