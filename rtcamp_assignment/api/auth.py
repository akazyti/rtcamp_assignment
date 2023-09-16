import frappe


def response(status, msg, data=None):
	data = {
		"status"  : status,
		"message" : msg,
		"data"    : data
	}
	return data

@frappe.whitelist(allow_guest=True)
def register_candidate(payload):

	if not payload:
		frappe.log_error(payload, "Invalid Sign Up Attempted")
		return response('red','User data not found',payload)  


	password = payload.get('password')
	confirm_password = payload.get('confirmPassword')

	if not password  or not confirm_password or password != confirm_password:
		return frappe.throw("password did not match") 
	
	try:
		new_user = frappe.new_doc("User")
		new_user.email = payload['email']
		new_user.first_name = "Portal User"
		new_user.send_welcome_email = 0
		new_user.role_profile_name = "Student"
		new_user.new_password = payload['password']
		new_user.save(ignore_permissions=True)
		frappe.db.commit()
	except Exception as e:
		frappe.log_error(title="create_user_doc failed",message=frappe.get_traceback())
		frappe.throw("User Already Exists") 
	
	if not frappe.db.exists({"doctype": "User", "email": payload['email']}):
		frappe.throw("Something Went Wrong")
	
	candidate =  frappe.new_doc("Candidate")
	candidate.user = payload['email']
	candidate.owner = payload['email']
	candidate.full_name = 'Portal User'
	candidate.save(ignore_permissions=True)
	frappe.db.commit()
	frappe.db.set_value('Candidate', candidate.name, 'owner', payload['email'])
	frappe.db.commit()

	return response('green','Candidate Created', data = candidate)