from odoo import models,fields

class Company(models.Model):
    _name = "company"

    name = fields.Char("Empresa")
    name2 = fields.Char("Rama")
    name3 = fields.Char("Descripcion")
    name4 = fields.Char("Página Web")
    status = fields.Selection(selection=[("online","Online"),("presencial","Presencial")])