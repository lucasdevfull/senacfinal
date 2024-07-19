from rolepermissions.roles import AbstractUserRole

class ProdutoManager(AbstractUserRole):
    name = 'manager'
    permissions = {
        'change_product': True,
        'create_product': True,
        'delete_product': True,
        'view_product': True,
        'create_category': True,
        'create_fabricante': True,
    }
