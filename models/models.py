from odoo import models, fields, api

class CreditRequest(models.Model):
    _name = 'credit.request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _description = 'Credit Request'

    # 
    name = fields.Char(string='Name', required=True)
    fecha_solicitud  = fields.Datetime(string='Fecha solicitud')
    partner_id = fields.Many2one('res.partner', string='Nombre Razon social', required=True)
    vat = fields.Char(related='partner_id.vat', string='Rut', readonly=True)
    giro =  fields.Char( string='Giro o actividad')
    sitioweb  = fields.Char(related = 'partner_id.website', string='Sitio Web ')
    direcc_fact  = fields.Char(string='Direccion Facturacion')
    comuna_fact  = fields.Char(string='Comuna')
    fono = fields.Char(string='Telefono')
    Direc_envio  = fields.Char(string='Direccion envio (postal)')
    direc_desp  = fields.Char(string='Direccion despacho producto / hora')
    nom_corr_compra  = fields.Char(string='Nombre y correo encargado compras')
    nom_corr_pago  = fields.Char(string='Nombre y correo encargado Pagos ')
    nom_corr_gte  = fields.Char(string='Nombre y Correo Gerente Adm. y finanzas')
    nom_corr_conta  = fields.Char(string='Nombre y correo contabilidad')
    rep_legal  = fields.Char(string='Representatnte Legal')
    rut_rep_l  = fields.Char(string='Rut Representante Legal')
    Ref_com  = fields.Char(string='Referencias comerciales')
    amount = fields.Float(string='Credito solicitado', required=True)
    condicion_pago  = fields.Char(string='condicion de Pago')
    compra_estimada  = fields.Char(string='compra estimada mensual')
    producto_id = fields.Many2one(string='Producto', comodel_name='product.template', ondelete='restrict')
    Nombre_cargo_sol  = fields.Char(string='Nombre y Cargo solicitante')

    ref_banco  = fields.Char(string='Referencia Bancaria')  
    sucursal_banc  = fields.Char(string='')

    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='State', default='draft')


    # Campos relacionados para obtener la información del cliente
    country_id = fields.Many2one('res.country', related='partner_id.country_id', readonly=False)
    street = fields.Char(related='partner_id.street', string='Street', readonly=True)
    city = fields.Char(related='partner_id.city', string='City', readonly=True)
    state_id = fields.Many2one('res.country.state', related='partner_id.state_id', string='State', readonly=True)
    email = fields.Char(related='partner_id.email', string='Email', readonly=True)
    phone = fields.Char(related='partner_id.phone', string='Phone', readonly=True)


    #kanban fields
    progress  = fields.Integer(string='Progreso')

    #attachment fields 

    identity_document = fields.Binary(string='Documento de Identidad')
    proof_of_address = fields.Binary(string='Comprobante de Domicilio')
    iva_mensual  = fields.Binary(string='Iva')
    balance  = fields.Binary(string = 'Balance')
    socofin  = fields.Binary(string='Informe socofin')

    