frappe.ready(function() {
    frappe.web_form.events.on("after_save", function() {
		let data = frappe.web_form.get_values();
		let email = data.email;
		sendEmail(email);
		
	});
	
});


// Function to send mail on registration 
function sendEmail(email) {
    frappe.call({
        method: 'customer_management.customer_management.web_form.email_web_form.email_web_form.send_email_on_registration',
        args: {
            email: email 
        },
        callback: function(response) {
            // Handle the response
            if (response.message) {
                console.log('Registration');
            } else {
                console.error('Failed to register:', response.error);
            }
        }
    });
}