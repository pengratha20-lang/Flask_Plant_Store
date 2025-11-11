from flask import Flask
import os

# Import blueprints
from routes.fronts.index import home_bp
from routes.fronts.about import about_bp
from routes.fronts.contact import contact_bp
from routes.fronts.service import service_bp
from routes.fronts.shop import shop_bp
from routes.fronts.cart import cart_bp
from routes.fronts.product import product_bp
from routes.fronts.checkout import checkout_bp

# Create Flask app
app = Flask(__name__)

# Configuration
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

# Register blueprints
app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(contact_bp)
app.register_blueprint(service_bp)
app.register_blueprint(shop_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(product_bp)
app.register_blueprint(checkout_bp)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
