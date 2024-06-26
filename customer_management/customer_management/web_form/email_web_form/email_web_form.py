import frappe

def get_context(context):
	pass

@frappe.whitelist(allow_guest=True)
def send_email_on_registration(email):
    try:
        # Trigger email 
        frappe.sendmail(
            recipients=email,  
            subject='Customer registration', 
            content='Thank you for registering with us!', 
            now=True 
        )

        return "Form submitted successfully"
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Form Submission Error")
        return "An error occurred while submitting the form"