# 🌱 Green Bean - Plant Store

A modern, responsive Flask-based e-commerce platform for plant enthusiasts. Built with Bootstrap 5 and featuring a complete shopping experience from browsing to checkout.

## ✨ Features

### 🛍️ **E-commerce Functionality**
- **Product Catalog**: Browse plants by categories (Indoor, Outdoor, Accessories, Pots)
- **Advanced Filtering**: Filter by category, price range, and plant type
- **Smart Search**: Search products with real-time filtering
- **Shopping Cart**: Add/remove items with quantity management
- **Checkout System**: Complete order processing with customer info and payment options

### 🎨 **User Experience**
- **Responsive Design**: Mobile-friendly interface with Bootstrap 5
- **Product Details**: Comprehensive product pages with specifications and care instructions
- **Quick Navigation**: Scroll spy navigation and quick category links
- **Interactive Cart**: Real-time cart updates and shipping calculations

### 📧 **Communication**
- **Contact Form**: Integrated with Telegram bot notifications
- **Order Notifications**: Automatic order confirmations via Telegram
- **Customer Support**: Easy contact and inquiry system

### 💻 **Technical Features**
- **Component-Based Templates**: Reusable Jinja2 components
- **Session Management**: Persistent cart and user sessions
- **Error Handling**: Comprehensive error handling and user feedback
- **Clean Architecture**: Blueprint-based Flask structure

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8+
- Flask
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/pengratha20-lang/Flask-Plant-Store.git
   cd Flask-Plant-Store
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # source .venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install flask requests
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

## 📁 Project Structure

```
FlaskProject_Final/
├── app.py                  # Main application file
├── routes/
│   └── fronts/            # Blueprint routes
│       ├── index.py       # Home page routes
│       ├── shop.py        # Shop functionality
│       ├── cart.py        # Cart management
│       ├── product.py     # Product details
│       ├── checkout.py    # Checkout process
│       ├── contact.py     # Contact form
│       ├── about.py       # About page redirects
│       └── service.py     # Services redirects
├── services/
│   └── telegram_bot.py    # Telegram integration
├── static/
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript files
│   └── images/           # Product images
├── templates/
│   ├── base.html         # Base template
│   ├── shop-base.html    # Shop base template
│   ├── components/       # Reusable components
│   ├── home/             # Home page templates
│   ├── shop/             # Shop templates
│   └── checkout/         # Checkout templates
└── .gitignore
```

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5.3, HTML5, CSS3, JavaScript
- **Icons**: Font Awesome 6.6
- **Integration**: Telegram Bot API
- **Architecture**: Blueprint-based modular design

## 🎯 Key Features Breakdown

### Shopping Experience
- **Product Browsing**: Clean, grid-based product display
- **Category Filtering**: Quick category selection with counters
- **Price Range Filter**: Slider-based price filtering
- **Cart Management**: Add/remove items with quantity controls
- **Shipping Options**: Standard, Express, and Overnight shipping
- **Order Processing**: Complete checkout with customer information

### Technical Implementation
- **Component System**: Modular Jinja2 templates for maintainability
- **Session Storage**: Persistent cart data across sessions
- **Error Handling**: User-friendly error messages and fallbacks
- **Responsive Design**: Mobile-first approach with Bootstrap

### Admin Features
- **Order Notifications**: Automatic Telegram alerts for new orders
- **Contact Management**: Form submissions sent via Telegram
- **Easy Content Updates**: Component-based content management

## 🔧 Configuration

### Telegram Bot Setup (Optional)
1. Create a bot with [@BotFather](https://t.me/botfather)
2. Get your bot token and chat ID
3. Update `services/telegram_bot.py` with your credentials

### Customization
- Update product data in templates or integrate with a database
- Modify styling in `static/css/` files
- Add new routes in `routes/fronts/` directory
- Create new components in `templates/components/`

## 🚀 Deployment

### Render.com Deployment

This application is configured for easy deployment on Render.com:

1. **Fork/Clone this repository**
2. **Connect to Render:**
   - Go to [Render.com](https://render.com)
   - Create a new Web Service
   - Connect your GitHub repository
   - Select `Flask-Plant-Store` repository

3. **Configure the service:**
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Environment**: Python 3
   - **Plan**: Free tier available

4. **Set Environment Variables:**
   - `SECRET_KEY`: Generate a secure random key
   - `TELEGRAM_BOT_TOKEN`: Your bot token (keep this secret!)
   - `TELEGRAM_CHAT_ID`: Your chat ID (keep this secret!)
   
   ⚠️ **Security Note**: Never commit API tokens or secrets to your repository. Always use environment variables in production.

5. **Deploy**: Click "Create Web Service"

### Live Demo
- 🌐 **Live Site**: [https://green-bean-plant-store.onrender.com](https://green-bean-plant-store.onrender.com)
- 📂 **GitHub Repository**: [https://github.com/pengratha20-lang/Flask-Plant-Store](https://github.com/pengratha20-lang/Flask-Plant-Store)

### Local Development
```bash
python app.py
```

### Production Deployment
- Use a WSGI server like Gunicorn
- Set up environment variables for sensitive data
- Configure a reverse proxy (Nginx)
- Set up SSL certificates

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📞 Contact

- **Email**: pengratha20@gmail.com
- **GitHub**: [@pengratha20-lang](https://github.com/pengratha20-lang)
- **Project Link**: [https://github.com/pengratha20-lang/Flask-Plant-Store](https://github.com/pengratha20-lang/Flask-Plant-Store)
- **Live Demo**: [https://green-bean-plant-store.onrender.com](https://green-bean-plant-store.onrender.com)

## 🙏 Acknowledgments

- Bootstrap team for the amazing CSS framework
- Font Awesome for the beautiful icons
- Flask community for the excellent documentation
- All plant enthusiasts who inspired this project

---

**Happy Gardening! 🌿**