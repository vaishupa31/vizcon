import streamlit as st

st.set_page_config(
    page_title="What's in a Name? | VizCon 2026",
    page_icon="👶",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Sidebar Navigation ───────────────────────────────────────────
st.sidebar.markdown("## 👶 What's in a Name?")
st.sidebar.caption("VizCon 2026 | Analyticon")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🤝 Convergence",
        "🧱 Invisible Borders",
        "🎉 Discoveries",
        "📋 Methods",
    ],
    index=0,
    label_visibility="collapsed",
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<small style='color:#6b7280'>8 countries · 1 language · 17,000+ names · 1997–2023</small>",
    unsafe_allow_html=True,
)

# ─── Page Routing ─────────────────────────────────────────────────
if page == "🏠 Home":
    from views.home import render
    render()
elif page == "🤝 Convergence":
    from views.convergence import render
    render()
elif page == "🧱 Invisible Borders":
    from views.borders import render
    render()
elif page == "🎉 Discoveries":
    from views.discoveries import render
    render()
elif page == "📋 Methods":
    from views.methods import render
    render()
