# Copyright (c) 2024, Cloudy Camp Limited and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	lead = frappe.qb.DocType("Lead")
	query = frappe.qb.from_(lead).select(
		lead.name, lead.creation, lead.lead_name, lead.mobile_no, lead.custom_model, 
		lead.custom_variant, lead.custom_vehicle_status, lead.custom_buying_in_days, lead.lead_owner
	)
	
	if filters:
		if filters.get("Name"):
			query = query.where(lead.lead_name.like(f"%{filters['Name']}%"))
		if filters.get("Mobile"):
			query = query.where(lead.mobile_no.like(f"%{filters['Mobile']}%"))
		if filters.get("Status"):
			query = query.where(lead.custom_vehicle_status == filters["Status"])
		if filters.get("From Date"):
			query = query.where(lead.creation >= filters["From Date"])
		if filters.get("To Date"):
			query = query.where(lead.creation <= filters["To Date"])
		if filters.get("brand"):
			query = query.where(lead.custom_brand == filters["brand"])
		if filters.get("model"):
			query = query.where(lead.custom_model == filters["model"])
		if filters.get("variant"):
			query = query.where(lead.custom_variant == filters["variant"])
		if filters.get("city"):
			query = query.where(lead.custom_city_name == filters["city"])
		if filters.get("lead_owner"):
			query = query.where(lead.lead_owner == filters["lead_owner"])
		if filters.get("lead_type"):
			query = query.where(lead.type == filters["lead_type"])

	data = query.run(as_dict=True)

	# for d in data:
	# 	frappe.msgprint(str(d))
	# 	notes = frappe.db.get_list("CRM Note", filters={"parent": d.name}, fields=["*"])
	# 	if notes:
	# 		d["last_note"] = notes[0].note

	columns = [
		{"fieldname": "creation", "label": "Creation", "fieldtype": "Date", "width": 150},
		{"fieldname": "lead_name", "label": "Lead Name", "fieldtype": "Data", "width": 150},
		{"fieldname": "mobile_no", "label": "Mobile No", "fieldtype": "Data", "width": 150},
		{"fieldname": "custom_model", "label": "Model", "fieldtype": "Data", "width": 150},
		{"fieldname": "custom_variant", "label": "Variant", "fieldtype": "Data", "width": 150},
		{"fieldname": "custom_vehicle_status", "label": "Vehicle Status", "fieldtype": "Data", "width": 150},
		{"fieldname": "custom_buying_in_days", "label": "Buying in Days", "fieldtype": "Data", "width": 150},
		# {"fieldname": "last_note", "label": "Last Note", "fieldtype": "Data", "width": 150},
		{"fieldname": "lead_owner", "label": "Assigned To", "fieldtype": "Data", "width": 150}
	]

	return columns, data
