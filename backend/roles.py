from rolepermissions.roles import AbstractUserRole

class Change(AbstractUserRole):
    available_permissions = {
        'change_product': True,
    }
