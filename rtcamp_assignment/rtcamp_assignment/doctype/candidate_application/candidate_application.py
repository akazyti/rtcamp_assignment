# Copyright (c) 2023, God and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
from rtcamp_assignment.api.profile import is_profile_complete

def validate_candidate_application(candidate, position):
	
	if not frappe.db.exists('Open Position', position):
		frappe.log_error(title='NO_SUCH_POSITION')
		frappe.throw('No Such Position Exists')

	position_doc = frappe.get_doc("Open Position", position)

	if not position_doc.status == 'Open':
		frappe.throw("Position has Closed Applications")

	# Duplicate application check
	if frappe.db.exists('Candidate Application', {
			'candidate': candidate,
			'position': position
	}):
			frappe.throw("Already Applied for This Position")
	
	candidate_doc = frappe.get_doc("Candidate", candidate)

	# Profile completeness check
	if not is_profile_complete(candidate_doc.user):
			frappe.throw("Profile is Not Complete")


class CandidateApplication(Document):
	def before_insert(self):
		"""
		Hooks from Frappe Class
		Know more at https://frappeframework.com/docs/user/en/python-api/hooks
		"""
		validate_candidate_application(self.candidate, self.position)
	
	


