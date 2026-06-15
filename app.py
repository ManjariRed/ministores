# app.py
# MiniStore - Demo E-commerce Website
# Built using Streamlit

import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS Styling
# --------------------------------------------------
st.markdown("""
<style>
    /* Main page styling */
    .main {
        padding-top: 1rem;
    }

    /* Hero section */
    .hero {
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        color: white;
        padding: 35px;
        border-radius: 15px;
        margin-bottom: 30px;
    }

    .hero h1 {
        margin-bottom: 10px;
    }

    /* Product card styling */
    .product-card {
        background-color: white;
        border: 1px solid #E5E7EB;
        border-radius: 15px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }

    .product-name {
        font-size: 22px;
        font-weight: bold;
        color: #111827;
    }

    .product-category {
        color: #6B7280;
        font-size: 14px;
        margin-bottom: 10px;
    }

    .product-price {
        color: #16A34A;
        font-size: 22px;
        font-weight: bold;
        margin-top: 10px;
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 40px;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sample Product Data
# --------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "description": "Premium noise-cancelling headphones with immersive sound.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 4999,
        "description": "Track fitness, heart rate, and notifications effortlessly.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 3499,
        "description": "Lightweight and comfortable shoes for everyday performance.",
        "category": "Fashion"
    },
    {
        "name": "Classic Backpack",
        "price": 1499,
        "description": "Stylish backpack perfect for work, college, and travel.",
        "category": "Fashion"
    },
    {
        "name": "Coffee Maker",
        "price": 2499,
        "description": "Brew rich and delicious coffee at home with ease.",
        "category": "Home"
    },
    {
        "name": "LED Desk Lamp",
        "price": 999,
        "description": "Modern desk lamp with adjustable brightness settings.",
        "category": "Home"
    }
]

# --------------------------------------------------
# Initialize Shopping Cart
# --------------------------------------------------
if "cart_items" not in st.session_state:
    st.session_state.cart_items = 0

if "cart_total" not in st.session_state:
    st.session_state.cart_total = 0

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("🛒 MiniStore")

# Create category filter
categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.radio(
    "Browse Categories",
    categories
)

# Shopping cart summary
st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart Summary")
st.sidebar.write(f"Items in Cart: {st.session_state.cart_items}")
st.sidebar.write(f"Total Amount: ₹{st.session_state.cart_total}")

# --------------------------------------------------
# Homepage Title
# --------------------------------------------------
st.title("🛍️ MiniStore")

# --------------------------------------------------
# Welcome Section
# --------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>Welcome to MiniStore</h1>
    <p>
        Your one-stop destination for quality products at great prices.
        Explore our featured collections and shop your favorites today.
    </p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Featured Products Section
# --------------------------------------------------
st.header("⭐ Featured Products")

# Filter products based on selected category
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product for product in products
        if product["category"] == selected_category
    ]

# --------------------------------------------------
# Display Products in Responsive Layout
# --------------------------------------------------
for i in range(0, len(filtered_products), 3):

    cols = st.columns(3)

    for col, product in zip(cols, filtered_products[i:i+3]):

        with col:

            st.markdown(f"""
            <div class="product-card">
                <div class="product-name">{product['name']}</div>

                <div class="product-category">
                    Category: {product['category']}
                </div>

                <p>{product['description']}</p>

                <div class="product-price">
                    ₹{product['price']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            # Add to Cart Button
            if st.button(
                f"Add to Cart",
                key=product["name"]
            ):
                st.session_state.cart_items += 1
                st.session_state.cart_total += product["price"]

                st.success(
                    f"{product['name']} added to cart!"
                )

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("""
<div class="footer">
    © 2026 MiniStore | Demo E-commerce Website
</div>
""", unsafe_allow_html=True)
import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# --------------------------------------------------
# Product Data
# --------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "description": "Premium noise-cancelling headphones with immersive sound.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 4999,
        "description": "Track fitness, heart rate, and notifications effortlessly.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 3499,
        "description": "Lightweight and comfortable shoes.",
        "category": "Fashion"
    },
    {
        "name": "Classic Backpack",
        "price": 1499,
        "description": "Perfect for work and travel.",
        "category": "Fashion"
    },
    {
        "name": "Coffee Maker",
        "price": 2499,
        "description": "Brew delicious coffee at home.",
        "category": "Home"
    },
    {
        "name": "LED Desk Lamp",
        "price": 999,
        "description": "Modern adjustable desk lamp.",
        "category": "Home"
    }
]

# --------------------------------------------------
# Shopping Cart State
# --------------------------------------------------
if "cart_items" not in st.session_state:
    st.session_state.cart_items = 0

if "cart_total" not in st.session_state:
    st.session_state.cart_total = 0

# --------------------------------------------------
# CSS Styling
# --------------------------------------------------
st.markdown("""
<style>
.hero {
    background: linear-gradient(135deg,#4F46E5,#7C3AED);
    color: white;
    padding: 35px;
    border-radius: 15px;
    margin-bottom: 30px;
}

.product-card {
    border: 1px solid #ddd;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
}

.support-button {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #4F46E5;
    color: white;
    padding: 12px 18px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: bold;
    z-index: 999;
}

.support-button:hover {
    background-color: #4338CA;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Sidebar
# --------------------------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(
    list(set(p["category"] for p in products))
)

selected_category = st.sidebar.radio(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart")

st.sidebar.write(
    f"Items: {st.session_state.cart_items}"
)

st.sidebar.write(
    f"Total: ₹{st.session_state.cart_total}"
)

# --------------------------------------------------
# Homepage
# --------------------------------------------------
st.title("🛍️ MiniStore")

st.markdown("""
<div class="hero">
<h1>Welcome to MiniStore</h1>
<p>
Discover quality products at affordable prices.
Explore our latest collections today.
</p>
</div>
""", unsafe_allow_html=True)

st.header("⭐ Featured Products")

# Filter Products
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        p for p in products
        if p["category"] == selected_category
    ]

# Product Grid
for i in range(0, len(filtered_products), 3):

    cols = st.columns(3)

    for col, product in zip(cols, filtered_products[i:i+3]):

        with col:

            st.markdown(f"""
            <div class="product-card">
            <h3>{product['name']}</h3>
            <p><b>Category:</b> {product['category']}</p>
            <p>{product['description']}</p>
            <h4>₹{product['price']}</h4>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                "Add to Cart",
                key=product["name"]
            ):
                st.session_state.cart_items += 1
                st.session_state.cart_total += product["price"]

                st.success(
                    f"{product['name']} added to cart!"
                )

# --------------------------------------------------
# Floating Support Button
# --------------------------------------------------
st.markdown(
    """
    <a href="/Support_Chatbot"
       target="_self"
       class="support-button">
       💬 Support
    </a>
    """,
    unsafe_allow_html=True
)