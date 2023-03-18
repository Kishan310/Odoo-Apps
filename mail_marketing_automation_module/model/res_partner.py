from odoo import _, api, fields, models, tools

class res_partner(models.Model):
    _inherit = 'res.partner'

    kits_mailing_contact_list_ids = fields.Many2many('mailing.list','res_partner_mailing_list_rel',string="Maling List")

    def write(self,vals):
        res = super(res_partner, self).write(vals)
        for rec in self:
            mailing_cont_id = False
            is_contact = self.env['mailing.contact'].search([('email','=',rec.email)])
            is_contact.subscription_list_ids.filtered(lambda x:x.list_id.id not in rec.kits_mailing_contact_list_ids.ids).unlink()
            for mailing_list_id in rec.kits_mailing_contact_list_ids:
                if not is_contact:
                    mailing_cont_id = self.env['mailing.contact'].create({
                        'name':rec.name,
                        'email':rec.email,
                        'is_blacklisted':False,
                        'opt_out':False
                    })
                else:
                    mailing_cont_id = self.env['mailing.contact'].search([('email','=',rec.email)])

                if mailing_cont_id and not self.env['mailing.contact.subscription'].search([('contact_id','=',mailing_cont_id.id),('list_id','=',mailing_list_id.id)]):
                    mass_mailing_sub_id = self.env['mailing.contact.subscription'].create({
                        'contact_id':mailing_cont_id.id,
                        'list_id':mailing_list_id.id
                    })

        return res