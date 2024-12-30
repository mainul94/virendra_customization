# Copyright (c) 2024, Cloudy Camp Limited and contributors
# For license information, please see license.txt

import frappe
from frappe import _, scrub


def execute(filters=None):
	lead = frappe.qb.DocType("Lead")
	query = frappe.qb.from_(lead).select(lead.lead_owner, lead.lead_progress)
	if filters.get('from_date'):
		query = query.where(lead.creation >= filters.get('from_date'))
	if filters.get('to_date'):
		query = query.where(lead.creation <= filters.get('to_date'))
	
	if filters.get('lead_owner'):
		query = query.where(lead.lead_owner == filters.get('lead_owner'))

	if filters.get('brand'):
		query = query.where(lead.custom_brand == filters.get('brand'))

	if filters.get('model'):
		query = query.where(lead.custom_model == filters.get('model'))

	if filters.get('variant'):
		query = query.where(lead.custom_variant == filters.get('variant'))

	if filters.get('city'):
		query = query.where(lead.custom_city_name == filters.get('city'))

	if filters.get('dealer'):
		query = query.where(lead.custom_dealer == filters.get('dealer'))
	if filters.get('status'):
		query = query.where(lead.lead_status == filters.get('status'))
	if filters.get('lead_progress'):
		query = query.where(lead.lead_progress == filters.get('lead_progress'))

	data = query.run(as_dict=True)

	veicle_status = ["Callback Scheduled", "TD Requested", "Home TD Scheduled", "Showroom Visit Scheduled", "Showroom TD Scheduled",
					 "Price Quote Shared", "Purchased Other Vehicle / Lost", "Booked"]
	rows = {}

	for d in data:
		if d['lead_owner'] not in rows:
			rows[d['lead_owner']] = {
				"lead_owner": d['lead_owner'],
				"total": 0,
				**{scrub(status): 0 for status in veicle_status}
			}
		rows[d['lead_owner']]["total"] += 1
		if d['lead_progress'] in veicle_status:
			rows[d['lead_owner']][scrub(d['lead_progress'])] += 1

	result = list(rows.values())

	columns = [
		{"fieldname": "lead_owner", "label": _("Lead Owner"), "fieldtype": "Link", "options": "User", "width": 200},
		{"fieldname": "total", "label": _("Total"), "fieldtype": "Int", "width": 150}
	]
	for status in veicle_status:
		columns.append({"fieldname": scrub(status), "label": status, "fieldtype": "Int", "width": 150})
	
	return columns, result
