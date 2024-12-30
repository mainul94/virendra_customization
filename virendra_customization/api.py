import frappe


@frappe.whitelist(allow_guest=True, methods=["POST"])
def wasender_message(response: dict):
    contact = response.get("contact", {})
    _map_dict = {
        "mobile_no": contact.get("phone_number"),
        "whatsapp_no": contact.get("phone_number"),
        "email_id": contact.get("email"),
        "first_name": contact.get("first_name"),
        "last_name": contact.get("last_name"),
        "country": contact.get("country"),
    }
    if not frappe.db.exists('Lead', _map_dict):
        lead = frappe.new_doc("Lead")
        lead.update(_map_dict)
        lead.set('lead_status', 'Hot')
        lead.insert(ignore_permissions=True)
    return 'Success'

