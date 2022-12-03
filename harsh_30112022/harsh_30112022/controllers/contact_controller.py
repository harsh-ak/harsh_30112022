from odoo.http import request
from odoo import http


class Contacts(http.Controller):

    # THIS CONTROLLER DSIPLAYS ALL THE CONTACT DETAILS
    @http.route("/view_contacts", type="http", auth="public", website=True)
    def contacts(self, **kw):
        contacts = request.env["res.partner"].search([])
        return request.render("harsh_30112022.contact_page", {"contacts": contacts})

    # THIS CONTROLLER WILL REDIRECT YOU TO THE SELECT CONTACT PAGE FORM
    @http.route(
        '/contact/detail/<model("res.partner"):contact_obj>/',
        type="http",
        auth="public",
        website=True,
    )
    def contact_detail(self, contact_obj, **kw):
        return request.render(
            "harsh_30112022.contact_detail_page",
            {
                "contact_detail": contact_obj,
                "contact_name": contact_obj.name,
                "contact_email": contact_obj.email,
                "contact_phone": contact_obj.phone,
                "contact_id": contact_obj.id,
            },
        )

    # THIS CONTROLLER WILL EDIT THE CONTACT
    @http.route("/edit_contact", type="http", auth="public", website=True)
    def edit_contact_detail(self, **kw):
        current_contact = request.env["res.partner"].search(
            [("id", "=", kw["contact_id"])]
        )
        current_contact.write(
            {"name": kw["name"], "email": kw["email"], "phone": kw["phone"]}
        )
        return request.render("harsh_30112022.thankyou_page", {})
