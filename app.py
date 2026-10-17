import streamlit as st

from cart import PRODUCTS, add_to_cart, recommend, remove_from_cart, subtotal

st.set_page_config(page_title="SmartCart Demo", page_icon="🛒")
st.title("SmartCart Demo")
st.caption("Browse a small sample catalog and build an in-session cart.")
st.info("Sample inventory only. No orders, accounts, or payments are processed.")

if "cart" not in st.session_state:
    st.session_state.cart = {}

for product in PRODUCTS:
    left, right = st.columns([4, 1])
    left.markdown(
        f"**{product['name']}** · {product['category']} · "
        f"${product['price']:.2f} · sample stock {product['stock']}"
    )
    if right.button("Add", key=f"add-{product['id']}"):
        try:
            st.session_state.cart = add_to_cart(
                st.session_state.cart, product["id"]
            )
            st.rerun()
        except ValueError as error:
            st.warning(str(error))
    count = st.session_state.cart.get(product["id"], 0)
    if count:
        left.caption(f"In demo cart: {count}")

st.divider()
st.header("Cart")
for product in PRODUCTS:
    count = st.session_state.cart.get(product["id"], 0)
    if count:
        left, right = st.columns([4, 1])
        left.write(f"{product['name']} × {count}: ${product['price'] * count:.2f}")
        if right.button("Remove one", key=f"remove-{product['id']}"):
            st.session_state.cart = remove_from_cart(
                st.session_state.cart, product["id"]
            )
            st.rerun()
st.metric("Sample subtotal", f"${subtotal(st.session_state.cart):.2f}")
suggestions = recommend(st.session_state.cart)
if suggestions:
    st.subheader("Related items")
    st.write(", ".join(item["name"] for item in suggestions))
