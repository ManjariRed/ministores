import streamlit as st

st.set_page_config(
    page_title="Support Chatbot",
    page_icon="💬"
)

st.title("💬 MiniStore Support Chatbot")

st.write(
    "Ask me about products, delivery, refunds, returns, payments, or order status."
)

# --------------------------------------------------
# Product Knowledge Base
# --------------------------------------------------
products = {
    "wireless headphones": 2999,
    "smart watch": 4999,
    "running shoes": 3499,
    "classic backpack": 1499,
    "coffee maker": 2499,
    "led desk lamp": 999
}

# --------------------------------------------------
# Chat History
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --------------------------------------------------
# Rule-Based Chatbot
# --------------------------------------------------
def get_response(user_input):

    text = user_input.lower()

    # Product Questions
    for product, price in products.items():

        if product in text:

            return (
                f"{product.title()} costs ₹{price}. "
                f"It's one of our featured products."
            )

    # Delivery
    if any(word in text for word in [
        "delivery",
        "shipping",
        "deliver"
    ]):

        return (
            "Standard delivery takes 3–5 business days."
        )

    # Refunds
    if "refund" in text:

        return (
            "Refunds are processed within 5–7 business days after approval."
        )

    # Returns
    if "return" in text:

        return (
            "You can return products within 30 days if they are unused."
        )

    # Payment Methods
    if any(word in text for word in [
        "payment",
        "pay",
        "upi",
        "card"
    ]):

        return (
            "We accept UPI, debit cards, credit cards, and net banking."
        )

    # Order Status
    if any(word in text for word in [
        "order",
        "status",
        "track"
    ]):

        return (
            "Please provide your order ID to check the latest status."
        )

    # Default
    return (
        "I'm sorry, I can help with products, delivery, refunds, "
        "returns, payments, and order status."
    )

# --------------------------------------------------
# Chat Input
# --------------------------------------------------
prompt = st.chat_input(
    "Type your message..."
)

if prompt:

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    response = get_response(prompt)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)