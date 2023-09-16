import frappe

@frappe.whitelist()
def update_profile(payload):
	user = frappe.session.user

	# Get the Candidate document associated with the current user
	candidate_doc = frappe.get_doc("Candidate", {'user': user})

	# Define a list of fields that can be updated
	allowed_fields = ['date_of_birth', 'resume', 'full_name', 'cgpa', 'address', 'contact', 'gender']

	for field, value in payload.items():
			# Check if the field is allowed to be updated
			if field not in allowed_fields:
					continue

			# Set the field value in the Candidate document
			candidate_doc.set(field, value)

	# Save the Candidate document with permissions ignored
	candidate_doc.save(ignore_permissions=True)
    
	# Commit the changes to the database
	frappe.db.commit()

@frappe.whitelist()
def get_profile():
	user = frappe.session.user

	# Get the Candidate document associated with the current user
	candidate_doc = frappe.get_doc("Candidate", {'user': user})

	# Return the Candidate document
	return candidate_doc


@frappe.whitelist()
def is_profile_complete(user=None):
    user = user if user else frappe.session.user

    # Get the Candidate document associated with the specified user
    candidate_doc = frappe.get_doc("Candidate", {'user': user})

    # Define the list of required fields for a complete profile
    required_fields = ['date_of_birth', 'resume', 'full_name', 'contact', 'gender', 'cgpa', 'address']

    # Check if all required fields have values
    is_complete = all(getattr(candidate_doc, field) for field in required_fields)

    return is_complete

@frappe.whitelist()
def apply_for_job(position):
	user = frappe.session.user

	# Custom Api Checks for Candidate
	if not frappe.db.exists('Candidate',{'user': user}):
		frappe.log_error(title='APPLICATION_WITHOUT_CANDIDATE')
		frappe.throw('No Such Candidate Exists')
	
	candidate_doc = frappe.get_doc("Candidate", {'user': user})

	# This will Trigger All Before Insert Hooks	
	application = frappe.get_doc({
		'doctype': 'Candidate Application',
		'position': position,
		'candidate': candidate_doc.name
	})

	application.save(ignore_permissions=True)
	frappe.db.commit()


@frappe.whitelist()
def already_applied(position):
	user = frappe.session.user
	candidate_doc = frappe.get_doc("Candidate", {'user': user})
	return frappe.db.exists('Candidate Application', {
		'candidate': candidate_doc.name, 
		'position': position }
	)