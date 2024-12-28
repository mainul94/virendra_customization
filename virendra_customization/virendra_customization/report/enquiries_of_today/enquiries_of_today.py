# Copyright (c) 2024, Cloudy Camp Limited and contributors
# For license information, please see license.txt

# import frappe
from virendra_customization.virendra_customization.report.lead_enquiry_pending_follow_ups.lead_enquiry_pending_follow_ups import (
    execute as _execute,
)
from frappe.utils import getdate


def execute(filters=None):
    if not filters:
        filters = {}
    filters["from_date"] = getdate()
    filters["to_date"] = filters["from_date"]
    return _execute(filters)
