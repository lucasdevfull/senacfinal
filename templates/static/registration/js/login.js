class FormValidatorLogin {

    constructor(formId,errorId, message){
        this.formId = document.getElementById(formId)
        this.username = document.getElementById('name').value;
        this.password = document.getElementById('password').value;
        this.errorId = document.getElementById(errorId)
        this.message = document.getElementById(message)
    }

    validate() {
        if (this.username.trim() ===''){
            this.errorId.textContent = 'Username é obrigatório'
            this.errorId.classList.remove('hidden')
            timeError(this.errorId)
            return false
        }

        if (this.password.trim() ===''){
            this.errorId.textContent = 'Senha é obrigatório'
            this.errorId.classList.remove('hidden')
            timeError(this.errorId)
            return false
        }
        timeError(this.message)
        return true
    }
}

const validateFormLogin = () => {
    const form = new FormValidatorLogin('form_login', 'error_login', 'message').validate()
    return form.validate()   
}

