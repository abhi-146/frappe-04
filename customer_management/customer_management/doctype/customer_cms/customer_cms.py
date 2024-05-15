# Copyright (c) 2024, Abhinav jain  and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Customercms(Document):
    def validate(self):
        if self.show_full_name and self.first_name and self.last_name:
            self.full_name = f'{self.first_name} {self.last_name}'
        else:
            self.full_name = ''

# API to create new customer cms
@frappe.whitelist()
def create_customer_cms(data):
    try:
        if frappe.request.method != "POST":
            frappe.respond_as_web_page("Method Not Allowed", str(''),http_status_code=405)
            return

        doc = frappe.get_doc({
            "doctype": "Customer cms",
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "show_full_name": data.get("show_full_name")
        })
        doc.insert()
        return ("Customer CMS created successfully.")
    except Exception as e:
        frappe.respond_as_web_page("Error creating Customer CMS", str(''),http_status_code=500)
        return 

# API to create get customer cms
@frappe.whitelist()
def read_customer_cms(customer_cms_name):
    try:
        if frappe.request.method != "GET":
            frappe.respond_as_web_page("Method Not Allowed", str(''),http_status_code=405)
            return

        doc = frappe.get_doc("Customer cms", customer_cms_name)
        return doc.as_dict()
    except Exception as e:
        frappe.respond_as_web_page("Error Reading Customer CMS", str(''),http_status_code=500)
        return

# API to create update customer cms
@frappe.whitelist()
def update_customer_cms(data):
    try:
        if frappe.request.method != "PUT":
            frappe.respond_as_web_page("Method Not Allowed", str(''),http_status_code=405)
            return

        doc = frappe.get_doc("Customer cms", data.get("name"))
        doc.update({
            "first_name": data.get("first_name"),
            "last_name": data.get("last_name"),
            "show_full_name": data.get("show_full_name")
        })
        doc.save()
        return ("Customer CMS updated successfully.")
    except Exception as e:
        frappe.respond_as_web_page("Error Updating Customer CMS", str(''),http_status_code=500)
        return

# API to create delete customer cms
@frappe.whitelist()
def delete_customer_cms(customer_cms_name):
    try:
        if frappe.request.method != "DELETE":
            frappe.respond_as_web_page("Method Not Allowed", str(''),http_status_code=405)
            return
        frappe.delete_doc("Customer cms", customer_cms_name)
        return ("Customer CMS deleted successfully.")
    except Exception as e:
        frappe.respond_as_web_page("Error Deleting Customer CMS", str(''),http_status_code=500)
        return