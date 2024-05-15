from odoo import api,models,fields
from datetime import datetime


class MaterialesLasser(models.Model):
    _name = "dtm.tubos.laser"
    _description = "Lleva el listado de los materiales a cortar en la laser"

    orden_trabajo = fields.Integer(string="Orden de Trabajo")
    fecha_entrada = fields.Date(string="Fecha de antrada")
    nombre_orden = fields.Char(string="Nombre")
    tubos_id = fields.Many2many("dtm.documentos.tubos" )
    tipo_orden = fields.Char(string="Tipo")
    materiales_id = fields.Many2many("dtm.cortadora.tubos")



class Realizados(models.Model): #--------------Muestra los trabajos ya realizados---------------------
    _name = "dtm.tubos.realizados"
    _description = "Lleva el listado de todo el material cortado en la Laser"

    orden_trabajo = fields.Integer(string="Orden de Trabajo")
    fecha_entrada = fields.Date(string="Fecha de Término")
    nombre_orden = fields.Char(string="Nombre")
    tubos_id = fields.Many2many("dtm.documentos.tubos" , readonly = True)


class Cortadora(models.Model):
    _name = "dtm.documentos.tubos"
    _description = "Guarda los nesteos del Radán"

    documentos = fields.Binary()
    nombre = fields.Char()
    # cortado = fields.Boolean()

    # @api.onchange("cortado")
    # def _action_cortado (self):
    #     if self.cortado:
    #         get_laser = self.env['dtm.tubos.laser'].search([])
    #         for main in get_laser:
    #             for n_archivo in main.cortadora_id:
    #                 if self.nombre == n_archivo.nombre:
    #
    #                     get_otd = self.env['dtm.odt'].search([("ot_number","=",main.orden_trabajo)]) # Actualiza el status en los modelos odt y proceso a corte
    #                     get_otd.write({"status":"Corte - Doblado"})
    #                     get_otp = self.env['dtm.proceso'].search([("ot_number","=",main.orden_trabajo),("tipe_order","=","OT")])
    #                     get_otp.write({"status":"cortedoblado"})
    #                     for documento in get_otp.cortadora_id:
    #                         if documento.nombre == self.nombre:
    #                             documento.cortado = "Material cortado"
    #
    #                     cont = 0
    #                     for corte in main.cortadora_id:
    #                         cont += 1
    #                         if not corte.cortado:
    #                             break
    #                     if len(main.cortadora_id) == cont:
    #                         vals = {
    #                             "orden_trabajo": main.orden_trabajo,
    #                             "fecha_entrada": datetime.today(),
    #                             "nombre_orden": main.nombre_orden,
    #                         }
    #
    #                         get_info = self.env['dtm.tubos.realizados'].search([])
    #                         get_info.create(vals)
    #
    #                         get_otd = self.env['dtm.odt'].search([("ot_number","=",main.orden_trabajo)]) # Actualiza el status en los modelos odt y proceso a corte
    #                         get_otd.write({"status":"Doblado"})
    #                         get_otp = self.env['dtm.proceso'].search([("ot_number","=",main.orden_trabajo),("tipe_order","=","OT")])
    #                         get_otp.write({"status":"doblado"})
    #
    #                         get_info =  self.env['dtm.tubos.realizados'].search([("orden_trabajo","=", main.orden_trabajo)])
    #
    #                         lines = []
    #                         for docs in main.cortadora_id:
    #                             line = (0,get_info.id,{
    #                                 "nombre": docs.nombre,
    #                                 "documentos":docs.documentos,
    #                             })
    #                             lines.append(line)
    #                         get_info.cortadora_id = lines
    #
    #                         self.env['dtm.tubos.laser'].search([("id","=",main.id)]).unlink()



class Cortadora(models.Model):
    _name = "dtm.cortadora.tubos"
    _description = "Guarda las laminas a cortar con su id, localización y medidas"

    identificador = fields.Integer(string="ID")
    nombre = fields.Char(string="Material")
    medida = fields.Char(string="Medidas")
    cantidad = fields.Integer(string="Cantidad")
    inventario = fields.Integer(string="Inventario")
    requerido = fields.Integer(string="Requerido (Compras)")
    localizacion = fields.Char(string="Localizacion")


