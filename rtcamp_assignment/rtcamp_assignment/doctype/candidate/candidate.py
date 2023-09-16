# Copyright (c) 2023, God and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class Candidate(Document):
	def before_save(self):
		if self.cgpa and (self.cgpa <=0 or self.cgpa > 10):
			frappe.throw("Please Provide Valid CGPA")
