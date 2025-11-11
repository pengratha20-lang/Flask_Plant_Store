from flask import Blueprint, render_template

shop_bp = Blueprint('shop', __name__)

@shop_bp.route('/shop')
@shop_bp.route('/products')
def shop():
    # Sample product data - matching actual available images
    products = [
        {"id": 1, "name": "Monstera Deliciosa", "price": 25.99, "category": "indoor", "image": "indoor/monstera.jpg", "rating": 5, "description": "The Monstera Deliciosa, also known as the Swiss Cheese Plant, is a stunning tropical houseplant famous for its unique split leaves.", "is_popular": True},
        {"id": 2, "name": "Snake Plant", "price": 19.99, "category": "indoor", "image": "indoor/snake-plant.jpg", "rating": 5, "description": "The Snake Plant is the ultimate low-maintenance houseplant, perfect for beginners or busy plant parents.", "is_popular": True},
        {"id": 3, "name": "Peace Lily", "price": 20.00, "category": "indoor", "image": "indoor/peace-lily.jpg", "rating": 4, "description": "The elegant Peace Lily is a graceful flowering houseplant that produces beautiful white blooms throughout the year."},
        {"id": 4, "name": "Golden Pothos", "price": 18.00, "category": "indoor", "image": "indoor/golden_potho.jpg", "rating": 4, "description": "The Golden Pothos is a versatile trailing vine with heart-shaped leaves variegated in golden yellow."},
        {"id": 5, "name": "Fiddle Leaf Fig", "price": 35.00, "category": "indoor", "image": "indoor/fiddle-leaf-fig.jpg", "rating": 4, "description": "The Fiddle Leaf Fig is a dramatic statement plant with large, violin-shaped glossy green leaves.", "is_new": True},
        {"id": 6, "name": "ZZ Plant", "price": 24.00, "category": "indoor", "image": "indoor/ZZ_plants.jpg", "rating": 5, "description": "The ZZ Plant is virtually indestructible with its glossy, waxy leaves and remarkable drought tolerance."},
        {"id": 7, "name": "Jade Plant", "price": 16.00, "category": "indoor", "image": "indoor/Jade Plant.jpg", "rating": 5, "description": "The Jade Plant is a beautiful succulent with thick, fleshy oval leaves that symbolize good luck.", "is_popular": True},
        {"id": 8, "name": "Money Tree", "price": 28.00, "category": "indoor", "image": "indoor/money_tree.jpg", "rating": 4, "description": "The Money Tree features a distinctive braided trunk and palmate leaves, believed to bring good fortune."},
        {"id": 9, "name": "Lavender", "price": 15.00, "category": "outdoor", "image": "outdoor/lavender.jpg", "rating": 5, "description": "Fragrant lavender is a beautiful perennial herb with silvery-green foliage and iconic purple flower spikes.", "is_popular": True},
        {"id": 10, "name": "Rosemary", "price": 12.00, "category": "outdoor", "image": "outdoor/rosemary.jpg", "rating": 4, "description": "Rosemary is an aromatic evergreen herb with needle-like leaves and a pine-like fragrance."},
        {"id": 11, "name": "Sunflower", "price": 18.00, "category": "outdoor", "image": "outdoor/sunflower.jpg", "rating": 5, "description": "Bright and cheerful sunflowers are annual plants that follow the sun throughout the day.", "is_new": True},
        {"id": 12, "name": "Palm Tree", "price": 45.00, "category": "outdoor", "image": "outdoor/palm_tree.jpg", "rating": 4, "description": "This tropical palm brings exotic beauty to outdoor spaces with its fan-shaped or feathery fronds."},
        {"id": 13, "name": "White Ceramic Pot", "price": 25.00, "category": "pot", "image": "pot/ceramic-pot-white.jpg", "rating": 4, "description": "This modern white ceramic pot features a clean, minimalist design that complements any plant.", "is_popular": True},
        {"id": 14, "name": "Decorative Planter", "price": 32.00, "category": "pot", "image": "pot/Latitude_Run.jpg", "rating": 4, "description": "This elegant decorative planter features sophisticated styling perfect for modern homes.", "is_new": True},
        {"id": 15, "name": "Garden Shears", "price": 24.00, "category": "accessories", "image": "accessories/Garden_Shears.jpg", "rating": 5, "description": "Professional-grade garden shears with sharp stainless steel blades and comfortable ergonomic handles.", "is_popular": True},
        {"id": 16, "name": "Watering Can", "price": 35.00, "category": "accessories", "image": "accessories/Bloom_Pine_Watering_Can.jpg", "rating": 4, "description": "This elegant vintage-style watering can combines functionality with aesthetic appeal.", "is_on_sale": True},
        {"id": 17, "name": "Gardening Gloves", "price": 15.00, "category": "accessories", "image": "accessories/Gardening_Gloves.jpg", "rating": 4, "description": "Durable and comfortable gardening gloves that protect your hands while maintaining dexterity."},
        {"id": 18, "name": "Modern Planter Set", "price": 42.00, "category": "pot", "image": "pot/Stewart_Garden.jpg", "rating": 5, "description": "This contemporary planter set offers versatile styling for both indoor and outdoor use.", "is_new": True},
    ]
    return render_template('shop/all_product.html', title="Green Garden - Shop", products=products)

@shop_bp.route('/shop/category/<category>')
def category(category):
    # Sample product data - matching actual available images
    all_products = [
        {"id": 1, "name": "Monstera Deliciosa", "price": 25.99, "category": "indoor", "image": "indoor/monstera.jpg", "rating": 5, "description": "The Monstera Deliciosa, also known as the Swiss Cheese Plant, is a stunning tropical houseplant famous for its unique split leaves.", "is_popular": True},
        {"id": 2, "name": "Snake Plant", "price": 19.99, "category": "indoor", "image": "indoor/snake-plant.jpg", "rating": 5, "description": "The Snake Plant is the ultimate low-maintenance houseplant, perfect for beginners or busy plant parents.", "is_popular": True},
        {"id": 3, "name": "Peace Lily", "price": 20.00, "category": "indoor", "image": "indoor/peace-lily.jpg", "rating": 4, "description": "The elegant Peace Lily is a graceful flowering houseplant that produces beautiful white blooms throughout the year."},
        {"id": 4, "name": "Golden Pothos", "price": 18.00, "category": "indoor", "image": "indoor/golden_potho.jpg", "rating": 4, "description": "The Golden Pothos is a versatile trailing vine with heart-shaped leaves variegated in golden yellow."},
        {"id": 5, "name": "Fiddle Leaf Fig", "price": 35.00, "category": "indoor", "image": "indoor/fiddle-leaf-fig.jpg", "rating": 4, "description": "The Fiddle Leaf Fig is a dramatic statement plant with large, violin-shaped glossy green leaves.", "is_new": True},
        {"id": 6, "name": "ZZ Plant", "price": 24.00, "category": "indoor", "image": "indoor/ZZ_plants.jpg", "rating": 5, "description": "The ZZ Plant is virtually indestructible with its glossy, waxy leaves and remarkable drought tolerance."},
        {"id": 7, "name": "Jade Plant", "price": 16.00, "category": "indoor", "image": "indoor/Jade Plant.jpg", "rating": 5, "description": "The Jade Plant is a beautiful succulent with thick, fleshy oval leaves that symbolize good luck.", "is_popular": True},
        {"id": 8, "name": "Money Tree", "price": 28.00, "category": "indoor", "image": "indoor/money_tree.jpg", "rating": 4, "description": "The Money Tree features a distinctive braided trunk and palmate leaves, believed to bring good fortune."},
        {"id": 9, "name": "Lavender", "price": 15.00, "category": "outdoor", "image": "outdoor/lavender.jpg", "rating": 5, "description": "Fragrant lavender is a beautiful perennial herb with silvery-green foliage and iconic purple flower spikes.", "is_popular": True},
        {"id": 10, "name": "Rosemary", "price": 12.00, "category": "outdoor", "image": "outdoor/rosemary.jpg", "rating": 4, "description": "Rosemary is an aromatic evergreen herb with needle-like leaves and a pine-like fragrance."},
        {"id": 11, "name": "Sunflower", "price": 18.00, "category": "outdoor", "image": "outdoor/sunflower.jpg", "rating": 5, "description": "Bright and cheerful sunflowers are annual plants that follow the sun throughout the day.", "is_new": True},
        {"id": 12, "name": "Palm Tree", "price": 45.00, "category": "outdoor", "image": "outdoor/palm_tree.jpg", "rating": 4, "description": "This tropical palm brings exotic beauty to outdoor spaces with its fan-shaped or feathery fronds."},
        {"id": 13, "name": "White Ceramic Pot", "price": 25.00, "category": "pot", "image": "pot/ceramic-pot-white.jpg", "rating": 4, "description": "This modern white ceramic pot features a clean, minimalist design that complements any plant.", "is_popular": True},
        {"id": 14, "name": "Decorative Planter", "price": 32.00, "category": "pot", "image": "pot/Latitude_Run.jpg", "rating": 4, "description": "This elegant decorative planter features sophisticated styling perfect for modern homes.", "is_new": True},
        {"id": 15, "name": "Garden Shears", "price": 24.00, "category": "accessories", "image": "accessories/Garden_Shears.jpg", "rating": 5, "description": "Professional-grade garden shears with sharp stainless steel blades and comfortable ergonomic handles.", "is_popular": True},
        {"id": 16, "name": "Watering Can", "price": 35.00, "category": "accessories", "image": "accessories/Bloom_Pine_Watering_Can.jpg", "rating": 4, "description": "This elegant vintage-style watering can combines functionality with aesthetic appeal.", "is_on_sale": True},
        {"id": 17, "name": "Gardening Gloves", "price": 15.00, "category": "accessories", "image": "accessories/Gardening_Gloves.jpg", "rating": 4, "description": "Durable and comfortable gardening gloves that protect your hands while maintaining dexterity."},
        {"id": 18, "name": "Modern Planter Set", "price": 42.00, "category": "pot", "image": "pot/Stewart_Garden.jpg", "rating": 5, "description": "This contemporary planter set offers versatile styling for both indoor and outdoor use.", "is_new": True},
    ]
    
    # Filter products by category
    filtered_products = [p for p in all_products if p['category'] == category]
    
    # Category display names
    category_names = {
        'indoor': 'Indoor Plants',
        'outdoor': 'Outdoor Plants', 
        'accessories': 'Accessories',
        'pot': 'Pots & Planters'
    }
    
    category_display = category_names.get(category, category.title())
    
    return render_template('shop/all_product.html', 
                         title=f"Green Garden - {category_display}", 
                         products=filtered_products,
                         category_filter=category)
