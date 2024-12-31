# Copyright (c) 2024, Cloudy Camp Limited and contributors
# For license information, please see license.txt

import frappe
from pypika import Order
from frappe.utils import add_to_date


def execute(filters=None):
	lead = frappe.qb.DocType("Lead")
	lead_note = frappe.qb.DocType("CRM Note")
	last_noste_as = frappe.qb.from_(lead_note).select(
		lead_note.note
	).where(lead.name == lead_note.parent).orderby(
		lead_note.idx, order=Order.desc
	).limit(1)
	query = (frappe.qb.from_(lead).select(
			lead.name, lead.creation, lead.lead_name, lead.mobile_no, lead.custom_model, 
			lead.custom_variant, lead.lead_status, lead.lead_progress, lead.custom_buying_in_days, lead.lead_owner, last_noste_as.as_('last_note')
		).orderby(lead.modified, order=Order.desc))

	follow_ups =  filters.pop('pending_flow_ups', False)
	if follow_ups:
		ToDo = frappe.qb.DocType("ToDo")
		query = query.join(ToDo).on(lead.name == ToDo.reference_name).where(ToDo.status == 'Open')
		query = query.where(ToDo.reference_type == 'Lead')
		query = query.select(ToDo.date)
	
	if filters:
		if filters.get("name"):
			query = query.where(lead.lead_name.like(f"%{filters['name']}%"))
		if filters.get("mobile"):
			query = query.where(lead.mobile_no.like(f"%{filters['mobile']}%"))
		if filters.get("from_date"):
			if follow_ups:
				query = query.where(ToDo.date >= filters["from_date"])
			else:
				query = query.where(lead.creation >= filters["from_date"])
		if filters.get("to_date"):
			if follow_ups:
				query = query.where(ToDo.date <= add_to_date(filters["to_date"],hours=23, minutes=59, seconds=59))
			else:
				query = query.where(lead.creation <= add_to_date(filters["to_date"],hours=23, minutes=59, seconds=59))
		if filters.get("brand"):
			query = query.where(lead.custom_brand == filters["brand"])
		if filters.get("model"):
			query = query.where(lead.custom_model == filters["model"])
		if filters.get("variant"):
			query = query.where(lead.custom_variant == filters["variant"])
		if filters.get("city"):
			query = query.where(lead.custom_city_name == filters["city"])
		if filters.get("pincode"):
			query = query.where(lead.custom_pincode == filters["pincode"])
		if filters.get("status"):
			query = query.where(lead.lead_status == filters["status"])
		if filters.get("lead_progress"):
			query = query.where(lead.lead_progress == filters["lead_progress"])
		if filters.get("lead_owner"):
			query = query.where(lead.lead_owner == filters["lead_owner"])
		
		if filters.get("vehicle"):
			query = query.where(lead.custom_vehicle == filters["vehicle"])

	data = query.run(as_dict=True, debug=True)

	columns = [
		{"fieldname": "creation", "label": "Creation", "fieldtype": "Date", "width": 150},
		{"fieldname": "lead_name", "label": "Lead Name", "fieldtype": "Data", "width": 150},
		{"fieldname": "mobile_no", "label": "Mobile No", "fieldtype": "Data", "width": 150},
		{"fieldname": "custom_model", "label": "Model", "fieldtype": "Data", "width": 150},
		{"fieldname": "custom_variant", "label": "Variant", "fieldtype": "Data", "width": 150},
		{"fieldname": "lead_status", "label": "Status", "fieldtype": "Data", "width": 150},
		{"fieldname": "lead_progress", "label": "Progress", "fieldtype": "Data", "width": 150},
		{"fieldname": "custom_buying_in_days", "label": "Buying in Days", "fieldtype": "Data", "width": 150},
		{"fieldname": "last_note", "label": "Last Note", "fieldtype": "Data", "width": 150},
		{"fieldname": "lead_owner", "label": "Assigned To", "fieldtype": "Data", "width": 150}
	]
	if follow_ups:
		columns.insert(-2, {"fieldname": "date", "label": "Due Date", "fieldtype": "Date", "width": 150})

	return columns, data
