frappe.listview_settings['Candidate Application'] = {
    onload: function(listview) {
        
        console.log(listview)
        listview.page.add_action_item(__('Schedule Interviews'), function() {
           
            let checked = listview.get_checked_items().map(each => each.name)
        
            frappe.call({
                method: "rtcamp_assignment.api.admin.schedule_interviews",
                type: "POST",
                args: {applications: checked},
            }).then(resp => {
                listview.clear_checked_items()
                frappe.msgprint('successfully queued for scheduling')
            })
            .catch(resp => {
                frappe.msgprint('Something went wrong')
            });
        });
    }
};




