class FormValidatorRegister {

    constructor(formId,errorId, message){
        this.formId = document.getElementById(formId)
        this.username = document.getElementById('name').value;
        this.email = document.getElementById('email').value;
        this.password1 = document.getElementById('password').value;
        this.password2 = document.getElementById('repeat_password').value;
        this.phone = document.getElementById('telefone').value;
        this.errorId = document.getElementById(errorId)
        this.message = document.getElementById(message)
    }

    validate() {

        if (this.username.trim() === '') {
            this.errorId.textContent = 'Username é obrigatório!'
            this.errorId.classList.remove('hidden')
            timeError(this.errorId)
            return false
        }

        if (this.email.trim() === '') {
            this.errorId.textContent = 'Email é obrigatório!'
            this.errorId.classList.remove('hidden')
            timeError(this.errorId)
            return false
        }

        if (!isEmailValid(this.email)) {
            this.errorId.textContent = 'Insira um email válido!'
            this.errorId.classList.remove('hidden')
            timeError(this.errorId)
            return false
        }

        if (this.password1.trim() < 8) {
            this.errorId.textContent = 'Senha deve ter pelo menos 8 caracteres!'
            this.errorId.classList.remove('hidden')
            timeError(this.errorId)
            return false
        }

        if (this.password1.trim() !== this.password2.trim()) {
            this.errorId.textContent = 'As senhas devem ser iguais!'
            this.errorId.classList.remove('hidden')
            timeError(this.errorId)
            return false
        } else if (this.password1.trim() === '' || this.password2.trim() === '') {
            this.errorId.textContent = 'Os campos de senha são obrigatórios!'
        }

        if (this.phone.trim() === '') {
            this.errorId.textContent = 'Telefone é obrigatório!'
            this.errorId.classList.remove('hidden')
            timeError(this.errorId)
            return false
        }

        return true
    }

    isEmailValid(email) {
    
        // cria um regex para validar o email
        const emailRegex = new RegExp(
            //usuario12@host.com
            /^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,}$/
        )
        if(emailRegex.test(email)) {
            return true
        }
        return false
    }
    

}
const validateFormRegister = () => {
    const form =  new FormValidatorRegister('form_register', 'error_cadastro', 'message').validate()
    return form
    
}

const handlePhone = (event) => {
    let celular = event.target
    celular.value = maskphone(celular.value)
}



