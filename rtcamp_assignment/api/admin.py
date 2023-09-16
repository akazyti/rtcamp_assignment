import frappe
import json
import time


def progress_to_array(length, num_steps=10):
    """
    Convert a length into an array representing progress in percentage steps.

    Parameters:
    - length (int): The total length.
    - num_steps (int): The number of steps to divide the progress into.

    Returns:
    - list: An array representing progress in percentage steps.
    """
    if length <= 0:
        return []

    step_size = length / num_steps
    progress_array = []

    for step in range(1, num_steps + 1):
        progress = min(step * step_size, length)
        percentage = int((progress / length) * 100)
        progress_array.append(percentage)

    return progress_array

def schedule_application_interviews(applications):
	# frappe application/json bug
	if type(applications) == str:
		applications = json.loads(applications)
	
	progresses =  progress_to_array(len(applications), len(applications))
	for index, application in enumerate(applications):
		application_doc = frappe.get_doc('Candidate Application', application)
		# reduce db calls
		if application_doc.interview_scheduled != 1:
			application_doc.interview_scheduled = 1
			application_doc.save()
			frappe.publish_progress(
				progresses[index], 
				title='Scheduling Interviews', 
				description="Scheduling with {} as {}".format(application_doc.user, application_doc.applied_as)
			)
		else:
			frappe.publish_progress(
				progresses[index], 
				title='Scheduling Interviews', 
				description="Skipping for {} as {}, Already Scheuled".format(application_doc.user, application_doc.applied_as) 
			)	
	frappe.db.commit()

@frappe.whitelist()
def schedule_interviews(applications):
	frappe.enqueue(schedule_application_interviews, applications=applications)