// Copyright (c) 2024, Cloudy Camp Limited and contributors
// For license information, please see license.txt

frappe.query_reports["Lead Enquiry"] = {
	"filters": [
		{
			"fieldname":"name",
			"label": __("Name"),
			"fieldtype": "Data",
		},
		{
			"fieldname":"mobile",
			"label": __("Mobile"),
			"fieldtype": "Data"
		},
		{
			"fieldname": "status",
			"label": __("Status"),
			"fieldtype": "Select",
			"options": [" ", "Test Drive Completed", "Retail", "Booking", "Lost"]
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname":"to_date",
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
