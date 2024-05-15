import frappe

# Function to delete Customer cms documents with status = Closed
@frappe.whitelist()
def delete_closed_customers():
    # Get list of Customer cms documents with status = Closed
    closed_customers = frappe.get_list("Customer cms", filters={"status": "Closed"}, fields=["name"])
    
    # Delete each closed customer document
    for customer in closed_customers:
        frappe.delete_doc("Customer cms", customer["name"], ignore_permissions=True)

# Enqueue the scheduler function
frappe.enqueue('customer_management.scheduler.cronjobs.delete_closed_customers')
