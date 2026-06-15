hello
# app.py
# MiniStore - Demo E-commerce Website using Streamlit

import streamlit as st

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS Styling
# ---------------------------------------------------
st.markdown("""
<style>
    .main {
        padding-top: 1rem;
    }

    .hero {
        background: linear-gradient(135deg, #4F46E5, #7C3AED);
        padding: 40px;
        border-radius: 15px;
        color: white;
        margin-bottom: 30px;
    }

    .hero h1 {
        margin-bottom: 10px;
    }

    .product-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e6e6e6;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
    }

    .product-name {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 8px;
    }

    .price {
        color: #16A34A;
        font-size: 20px;
        font-weight: bold;
    }

    .category {
        color: #6B7280;
        font-size: 14px;
    }

    .footer {
        text-align: center;
        color: gray;
        margin-top: 40px;
        padding: 20px;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Sample Product Data
# ---------------------------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "description": "Noise-cancelling headphones with premium sound quality.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 4999,
        "description": "Track fitness, notifications, and daily activities.",
        "category": "Electronics"
    },
    {
        "name": "Classic Backpack",
        "price": 1499,
        "description": "Durable backpack suitable for work and travel.",
        "category": "Fashion"
    },
    {
        "name": "Running Shoes",
        "price": 3499,
        "description": "Lightweight shoes designed for comfort and performance.",
        "category": "Fashion"
    },
    {
        "name": "Coffee Maker",
        "price": 2499,
        "description": "Brew delicious coffee in minutes at home.",
        "category": "Home"
    },
    {
        "name": "Desk Lamp",
        "price": 999,
        "description": "Modern LED desk lamp with adjustable brightness.",
        "category": "Home"
    }
]

# ---------------------------------------------------
# Session State for Shopping Cart
# ---------------------------------------------------
if "cart_count" not in st.session_state:
    st.session_state.cart_count = 0

if "cart_total" not in st.session_state:
    st.session_state.cart_total = 0

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.radio(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart")
st.sidebar.write(f"Items: {st.session_state.cart_count}")
st.sidebar.write(f"Total: ₹{st.session_state.cart_total}")

# ---------------------------------------------------
# Homepage Hero Section
# ---------------------------------------------------
st.markdown("""
<div class="hero">
    <h1>Welcome to MiniStore 🛍️</h1>
    <p>
        Discover quality products at affordable prices.
        Shop the latest trends across electronics,
        fashion, and home essentials.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Featured Products Title
# ---------------------------------------------------
st.header("⭐ Featured Products")

# Filter products by category
if selected_category != "All":
    filtered_products = [
        product for product in products
        if product["category"] == selected_category
    ]
else:
    filtered_products = products

# ---------------------------------------------------
# Display Products Using Columns
# ---------------------------------------------------
for i in range(0, len(filtered_products), 3):

    cols = st.columns(3)

    for col, product in zip(cols, filtered_products[i:i+3]):

        with col:

            st.markdown(f"""
            <div class="product-card">
                <div class="product-name">{product['name']}</div>
                <div class="category">
                    Category: {product['category']}
                </div>
                <br>
                <div>{product['description']}</div>
                <br>
                <div class="price">
                    ₹{product['price']}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if st.button(
                f"Add to Cart - {product['name']}",
                key=product["name"]
            ):
                st.session_state.cart_count += 1
                st.session_state.cart_total += product["price"]

                st.success(
                    f"{product['name']} added to cart!"
                )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------
st.markdown("""
<div class="footer">
    © 2026 MiniStore • Demo E-commerce Website
</div>
""", unsafe_allow_html=True)
```
