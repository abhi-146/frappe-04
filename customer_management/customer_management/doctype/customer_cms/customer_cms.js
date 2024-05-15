// Copyright (c) 2024, Abhinav jain  and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Customer cms", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on('Customer cms', {
    refresh: function(frm) {

        // Add custom button to open dialouge box
        frm.add_custom_button(__('Add data'), function() {
            frappe.prompt([
                {
                    fieldtype: 'Data',
                    label: 'Item Name',
                    fieldname: 'item_name'
                },
                {
                    fieldtype: 'Int',
                    label: 'Quantity',
                    fieldname: 'quantity'
                },
                {
                    fieldtype: 'Float',
                    label: 'Price',
                    fieldname: 'price'
                },
        
            ], function(values) {
        
                var item = values.item_name;
                var quantity = values.quantity;
                var price = values.price;
        
                frm.add_child('order', {
                    'item_name': item,
                    'quantity': quantity,
                    'price': price
                });
                
                frm.refresh_field('order');
                
            }, 'Add data', 'Submit');
        });
    }
});
