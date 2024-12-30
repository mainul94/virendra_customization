// Copyright (c) 2024, Cloudy Camp Limited and contributors
// For license information, please see license.txt

frappe.query_reports["Lead Enquiry Pending Follow-ups"] = {
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
			"fieldname":"vehicle",
			"label": __("Vehicle"),
			"fieldtype": "Link",
			"options": "Vehicle Name"
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
			"fieldname":"pincode",
			"label": __("Pincode"),
			"fieldtype": "Data"
		},
		{
			"fieldname":"status",
			"label": __("Lead Status"),
			"fieldtype": "Select",
			"options": [" ", "Hot", "Warm", "Cold", "Lost"]
		},
		{
			"fieldname":"lead_progress",
			"label": __("Lead Progress"),
			"fieldtype": "Select",
			"options": [" ", "Callback Scheduled", "TD Requested", "Home TD Scheduled", "Showroom Visit Scheduled", "Showroom TD Scheduled", "Price Quote Shared", "Purchased Other Vehicle / Lost", "Booked"]
		},
		{
			"fieldname":"lead_owner",
			"label": __("Assigned To"),
			"fieldtype": "Link",
			"options": "User"
		}
	],
	onload: report => {
		report.page.set_title(__("Pending Follow Up"))
	}
};
