from flask import Blueprint, render_template, session, request, jsonify

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart')
def cart():
    # Get cart items from session (you can modify this based on your cart logic)
    cart_items = session.get('cart', [])
    total = sum(item.get('price', 0) * item.get('quantity', 1) for item in cart_items)
    return render_template('shop/cart.html', title="Green Bean - Cart", cart_items=cart_items, total=total)

@cart_bp.route('/sync-cart', methods=['POST'])
def sync_cart():
    """Sync cart from localStorage to Flask session"""
    try:
        data = request.get_json()
        cart_items = data.get('cart_items', [])
        session['cart'] = cart_items
        session.modified = True
        return jsonify({'success': True, 'message': 'Cart synced successfully'})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})

@cart_bp.route('/add-to-cart', methods=['POST'])
def add_to_cart():
    # Sample add to cart functionality
    data = request.get_json()
    if 'cart' not in session:
        session['cart'] = []
    
    # Add item to cart (modify based on your requirements)
    session['cart'].append({
        'id': data.get('id'),
        'name': data.get('name'),
        'price': data.get('price'),
        'quantity': data.get('quantity', 1)
    })
    session.modified = True
    
    return jsonify({'success': True, 'message': 'Item added to cart'})

@cart_bp.route('/remove-from-cart/<int:item_id>', methods=['POST'])
def remove_from_cart(item_id):
    # Remove item from cart
    if 'cart' in session:
        session['cart'] = [item for item in session['cart'] if item.get('id') != item_id]
        session.modified = True
    
    return jsonify({'success': True, 'message': 'Item removed from cart'})
