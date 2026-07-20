import streamlit as st

st.set_page_config(
    page_title="The DNA of a Name | VizCon 2026",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.markdown("## 🧬 DNA of a Name")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigate",
    ["🏠 Home", "⏳ Lifespan", "🦠 Contagion", "🪞 Borders", "🌊 Convergence", "📋 Methods"],
    index=0
)

if page == "🏠 Home":
    from pages import home
    home.render()
elif page == "⏳ Lifespan":
    st.title("⏳ The Lifespan of a Name")
    st.info("Coming soon...")
elif page == "🦠 Contagion":
    st.title("🦠 How Names Spread")
    st.info("Coming soon...")
elif page == "🪞 Borders":
    st.title("🪞 Invisible Borders")
    st.info("Coming soon...")
elif page == "🌊 Convergence":
    st.title("🌊 The Great Convergence")
    st.info("Coming soon...")
elif page == "📋 Methods":
    st.title("📋 Methodology & Sources")
    st.info("Coming soon...")
