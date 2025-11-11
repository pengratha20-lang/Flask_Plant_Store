from flask import Blueprint, render_template, request, session, redirect, url_for, flash, jsonify
from datetime import datetime
import json

checkout_bp = Blueprint('checkout', __name__)

@checkout_bp.route('/checkout')
def checkout():
    # Get cart items from session (in a real app you'd get from database based on user)
    cart_items = session.get('cart', [])
    
    # If session cart is empty, redirect back to cart with message
    if not cart_items:
        flash('Your cart is empty. Please add some items before checkout.', 'warning')
        return redirect(url_for('cart.cart'))
    
    # Calculate totals
    subtotal = sum(item.get('price', 0) * item.get('quantity', 1) for item in cart_items)
    shipping_cost = 0 if subtotal >= 50 else 9.99  # Free shipping over $50
    tax_rate = 0.08  # 8% tax
    tax_amount = subtotal * tax_rate
    total = subtotal + shipping_cost + tax_amount
    
    order_summary = {
        'subtotal': subtotal,
        'shipping_cost': shipping_cost,
        'tax_amount': tax_amount,
        'total': total,
        'items_count': sum(item.get('quantity', 1) for item in cart_items)
    }
    
    return render_template('checkout/checkout.html', 
                         title="Checkout - Green Bean", 
                         cart_items=cart_items, 
                         order_summary=order_summary)

@checkout_bp.route('/checkout/process', methods=['POST'])
def process_checkout():
    try:
        # Get form data
        form_data = request.get_json() if request.is_json else request.form
        
        customer_info = {
            'first_name': form_data.get('first_name'),
            'last_name': form_data.get('last_name'),
            'email': form_data.get('email'),
            'phone': form_data.get('phone'),
            'shipping_address': {
                'street': form_data.get('street_address'),
                'city': form_data.get('city'),
                'state': form_data.get('state'),
                'zip_code': form_data.get('zip_code'),
                'country': form_data.get('country', 'United States')
            },
            'billing_same_as_shipping': form_data.get('billing_same_as_shipping', 'on') == 'on'
        }
        
        # Get cart items
        cart_items = session.get('cart', [])
        
        if not cart_items:
            if request.is_json:
                return jsonify({'success': False, 'message': 'Cart is empty'})
            flash('Cart is empty', 'error')
            return redirect(url_for('cart.cart'))
        
        # Calculate totals
        subtotal = sum(item.get('price', 0) * item.get('quantity', 1) for item in cart_items)
        shipping_cost = 0 if subtotal >= 50 else 9.99
        tax_amount = subtotal * 0.08
        total = subtotal + shipping_cost + tax_amount
        
        # Generate order ID
        order_id = f"GB{datetime.now().strftime('%Y%m%d%H%M%S')}"
        
        # Create order record
        order_data = {
            'order_id': order_id,
            'customer_info': customer_info,
            'items': cart_items,
            'order_summary': {
                'subtotal': subtotal,
                'shipping_cost': shipping_cost,
                'tax_amount': tax_amount,
                'total': total
            },
            'order_date': datetime.now().isoformat(),
            'status': 'confirmed',
            'payment_method': form_data.get('payment_method', 'credit_card')
        }
        
        # Store order in session (in production, save to database)
        if 'orders' not in session:
            session['orders'] = []
        session['orders'].append(order_data)
        session.modified = True
        
        # Clear cart
        session['cart'] = []
        session.modified = True
        
        if request.is_json:
            return jsonify({
                'success': True, 
                'message': 'Order placed successfully!',
                'order_id': order_id,
                'redirect_url': url_for('checkout.order_confirmation', order_id=order_id)
            })
        else:
            flash('Order placed successfully!', 'success')
            return redirect(url_for('checkout.order_confirmation', order_id=order_id))
            
    except Exception as e:
        if request.is_json:
            return jsonify({'success': False, 'message': f'Error processing order: {str(e)}'})
        flash(f'Error processing order: {str(e)}', 'error')
        return redirect(url_for('checkout.checkout'))

@checkout_bp.route('/order-confirmation/<order_id>')
def order_confirmation(order_id):
    # Find order in session
    orders = session.get('orders', [])
    order = next((o for o in orders if o['order_id'] == order_id), None)
    
    if not order:
        flash('Order not found', 'error')
        return redirect(url_for('shop.shop'))
    
    return render_template('checkout/order_confirmation.html', 
                         title=f"Order Confirmation - {order_id}", 
                         order=order)

@checkout_bp.route('/my-orders')
def my_orders():
    # Get all orders for the user
    orders = session.get('orders', [])
    return render_template('checkout/my_orders.html', 
                         title="My Orders - Green Bean", 
                         orders=orders)