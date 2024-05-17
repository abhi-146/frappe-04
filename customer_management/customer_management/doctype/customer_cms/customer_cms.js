// Copyright (c) 2024, Abhinav jain  and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Customer cms", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Customer cms', {
    refresh: function(frm) {
        // Add custom button to open dialogue box
        frm.add_custom_button(__('Add data'), function() {
            // Create a new Dialog
            let d = new frappe.ui.Dialog({
                title: 'Add data',
                fields: [
                    {
                        fieldtype: 'Data',
                        label: 'Item Name',
                        fieldname: 'item_name',
                        reqd: 1
                    },
                    {
                        fieldtype: 'Int',
                        label: 'Quantity',
                        fieldname: 'quantity',
                        reqd: 1
                    },
                    {
                        fieldtype: 'Float',
                        label: 'Price',
                        fieldname: 'price',
                        reqd: 1
                    },
                ],
                primary_action_label: 'Submit',
                primary_action(values) {
                    // Actions to perform on form submission
                    var item = values.item_name;
                    var quantity = values.quantity;
                    var price = values.price;
        
                    frm.add_child('order', {
                        'item_name': item,
                        'quantity': quantity,
                        'price': price
                    });
                    
                    frm.refresh_field('order');
                    
                    d.hide();  
                }
            });

            // Show the dialog
            d.show();
        });
    }
});
