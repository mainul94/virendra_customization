# Copyright (c) 2024, Cloudy Camp Limited and contributors
# For license information, please see license.txt

# import frappe
from virendra_customization.virendra_customization.report.lead_enquiry.lead_enquiry import execute as _execute


def execute(filters=None):
	if not filters:
		filters = {}
	filters['pending_flow_ups'] = 1
	return _execute(filters)