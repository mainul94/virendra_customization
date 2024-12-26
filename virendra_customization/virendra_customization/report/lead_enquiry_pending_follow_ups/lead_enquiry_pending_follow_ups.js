// Copyright (c) 2024, Cloudy Camp Limited and contributors
// For license information, please see license.txt

frappe.query_reports["Lead Enquiry Pending Follow-ups"] = {
	"filters": [
		{
			"fieldname":"Name",
			"label": __("Name"),
			"fieldtype": "Data",
		},
		{
			"fieldname":"Mobile",
			"label": __("Mobile"),
			"fieldtype": "Data"
		},
		{
			"fieldname": "Status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": [" ", "Test Drive Completed", "Retail", "Booking", "Lost"]
		},
		{
			"fieldname":"From Date",
			"label": __("From Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname":"To Date",
			"label": __("To Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname":"brand",
			"label": __("Brand"),
			"fieldtype": "Link",
			"options": "Brand"
		},
		{
			"fieldname":"model",
			"label": __("Model"),
			"fieldtype": "Link",
			"options": "Model"
		},
		{
			"fieldname":"variant",
			"label": __("Variant"),
			"fieldtype": "Link",
			"options": "Variant"
		},
		{
			"fieldname":"city",
			"label": __("City"),
			"fieldtype": "Link",
			"options": "City"
		},
		{
			"fieldname":"lead_owner",
			"label": __("Lead Owner"),
			"fieldtype": "Link",
			"options": "User"
		},
		{
			"fieldname":"lead_type",
			"label": __("Lead Type"),
			"fieldtype": "Select",
			"options": [" ", "Client", "Channel Partner", "Consultant"]
		}
	]
};