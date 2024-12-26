// Copyright (c) 2024, Cloudy Camp Limited and contributors
// For license information, please see license.txt

frappe.query_reports["Sales Team"] = {
	"filters": [
		{
			"fieldname": "lead_owner",
			"label": __("Lead Owner"),
			"fieldtype": "Link",
			"options": "User"
		},
		{
			"fieldname": "brand",
			"label": __("Brand"),
			"fieldtype": "Link",
			"options": "Brand"
		},
		{
			"fieldname": "model",
			"label": __("Model"),
			"fieldtype": "Link",
			"options": "Model"
		},
		{
			"fieldname": "variant",
			"label": __("Variant"),
			"fieldtype": "Link",
			"options": "Variant"
		},
		{
			"fieldname": "city",
			"label": __("City"),
			"fieldtype": "Link",
			"options": "City"
		},
		{
			"fieldname": "dealer",
			"label": __("Dealer"),
			"fieldtype": "Link",
			"options": "Dealer"
		},
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date"
		}
	]
};
