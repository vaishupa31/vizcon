import streamlit as st
from utils.data_loader import load_metrics
from utils.charts import countryness_over_time, COLORS


def render():
    from utils.data_loader import load_metrics

    df = load_metrics()

    # Compute actual stats from data
    unique_names = df["name"].nunique()
    num_countries = df["max_country"].nunique()
    year_min = df["year"].min()
    year_max = df["year"].max()
    total_records = len(df)

    # ─── Hero Section ─────────────────────────────────────────────
    # ─── Hero Header: "Passport for a Name" ─────────────────────────
st.markdown(
    """
    <div style="text-align:center; padding: 40px 20px 30px; position: relative;">
        <!-- Left baby decoration -->
        <span style="position:absolute; left: 8%; top: 20%; font-size: 3.5em;">👶</span>
        <span style="position:absolute; left: 5%; top: 55%; font-size: 2em;">🛂</span>
        <span style="position:absolute; left: 12%; top: 75%; font-size: 1.5em;">✈️</span>
        
        <!-- Right baby decoration -->
        <span style="position:absolute; right: 8%; top: 20%; font-size: 3.5em;">👶</span>
        <span style="position:absolute; right: 5%; top: 55%; font-size: 2em;">🛂</span>
        <span style="position:absolute; right: 12%; top: 75%; font-size: 1.5em;">🌍</span>
        
        <!-- Passport stamp decorations -->
        <span style="position:absolute; left: 20%; top: 10%; font-size: 1.2em; opacity: 0.4; transform: rotate(-15deg);">🇮🇪</span>
        <span style="position:absolute; right: 20%; top: 10%; font-size: 1.2em; opacity: 0.4; transform: rotate(10deg);">🇦🇺</span>
        <span style="position:absolute; left: 25%; bottom: 10%; font-size: 1.2em; opacity: 0.4; transform: rotate(5deg);">🇨🇦</span>
        <span style="position:absolute; right: 25%; bottom: 10%; font-size: 1.2em; opacity: 0.4; transform: rotate(-8deg);">🇺🇸</span>
        
        <!-- Main title -->
        <div style="display: inline-block; border: 3px solid #7C9FD6; border-radius: 12px; 
                    padding: 20px 50px; background: linear-gradient(135deg, #F0F8FF, #E8F4FD);
                    box-shadow: 0 4px 20px rgba(124, 159, 214, 0.2);">
            <div style="font-size: 0.85em; color: #718096; text-transform: uppercase; 
                        letter-spacing: 3px; margin-bottom: 8px;">VizCon 2026</div>
            <h1 style="font-size: 2.6em; font-weight: 800; color: #4A5568; margin: 0;
                       font-family: 'Georgia', serif;">
                🛂 Passport for a Name
            </h1>
            <p style="font-size: 1.1em; color: #718096; margin-top: 10px;">
                8 countries · 1 language · 17,000+ names · 1997–2023
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

       # ─── The Anglosphere — Globe ──────────────────────────────────
    st.markdown("### 🌍 The Anglosphere")
    st.markdown(
        "Eight countries united by one language — English. "
        "Connected through colonization, migration, and shared media. "
        "But each carries its **own cultural currents** beneath the surface."
    )

    import plotly.graph_objects as go

    # Anglosphere countries with lat/lon for markers
    anglosphere = {
        "USA": {"lat": 39.8, "lon": -98.5, "culture": "Hispanic heritage, melting pot"},
        "England & Wales": {"lat": 52.3, "lon": -1.2, "culture": "Commonwealth hub, trend bridge"},
        "Scotland": {"lat": 56.5, "lon": -4.2, "culture": "Celtic identity"},
        "Northern Ireland": {"lat": 54.6, "lon": -6.7, "culture": "Gaelic revival (political)"},
        "Ireland": {"lat": 53.1, "lon": -7.7, "culture": "Gaelic heritage"},
        "Canada": {"lat": 56.1, "lon": -106.3, "culture": "Francophone Quebec"},
        "Australia": {"lat": -25.3, "lon": 133.8, "culture": "Early adopter, exporter"},
        "New Zealand": {"lat": -40.9, "lon": 174.9, "culture": "Pacific connections"},
    }

    fig = go.Figure()

    # Add globe with highlighted countries
    fig.add_trace(
        go.Scattergeo(
            lat=[v["lat"] for v in anglosphere.values()],
            lon=[v["lon"] for v in anglosphere.values()],
            text=[f"<b>{k}</b><br>{v['culture']}" for k, v in anglosphere.items()],
            hoverinfo="text",
            mode="markers+text",
            marker=dict(size=14, color="#667eea", opacity=0.9, line=dict(width=1, color="#ffffff")),
            textfont=dict(size=9, color="#1a1a2e"),
            textposition="top center",
        )
    )

    fig.update_geos(
        projection_type="orthographic",
        showland=True,
        landcolor="#f0f0f5",
        showocean=True,
        oceancolor="#e8edf5",
        showcountries=True,
        countrycolor="#d1d5db",
        showlakes=False,
        projection_rotation=dict(lon=-30, lat=30),  # centered on Atlantic
        bgcolor="rgba(0,0,0,0)",
    )

    fig.update_layout(
        height=450,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        geo=dict(bgcolor="rgba(0,0,0,0)"),
    )

    st.plotly_chart(fig, use_container_width=True)

    # Country detail cards below the globe
    countries = {
        "🇺🇸 USA": "Hispanic heritage, melting pot",
        "🇬🇧 England & Wales": "Commonwealth hub, trend bridge",
        "🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scotland": "Celtic identity",
        "🏴 Northern Ireland": "Gaelic revival (political)",
        "🇮🇪 Ireland": "Gaelic heritage",
        "🇨🇦 Canada": "Francophone Quebec",
        "🇦🇺 Australia": "Early adopter, exporter",
        "🇳🇿 New Zealand": "Pacific connections",
    }

    cols = st.columns(4)
    for i, (country, desc) in enumerate(countries.items()):
        with cols[i % 4]:
            st.markdown(
                f"""
                <div style="background:#f5f5fa; border:1px solid #e5e7eb; 
                            border-radius:8px; padding:12px; margin-bottom:10px; text-align:center;">
                    <div style="font-size:1.1em; font-weight:600;">{country}</div>
                    <div style="font-size:0.8em; color:#6b7280;">{desc}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
    st.markdown("---")

    # ─── Core Question ────────────────────────────────────────────
    st.markdown("### 🔬 Language vs Culture")
    st.markdown(
        """
        > *"These 8 countries share a language. Does that mean they share a culture?
        > Baby names — the most personal choice a family makes — give us the answer."*
        """
    )

    st.markdown(
        """
        We measured cultural distinctness using a **"countryness" score**:
        - **Low** (1–2) → Name used equally everywhere (e.g. Noah, Olivia)
        - **High** (500+) → Name locked to one culture (e.g. Sadhbh, Frédérique)
        """
    )

    # ─── Two Truths ───────────────────────────────────────────────
    st.markdown("#### The Answer: Both Are True")

    col_yes, col_no = st.columns(2)
    with col_yes:
        st.markdown(
            """
            <div style="background:#f0fdf4; border-left:4px solid #06d6a0; 
                        border-radius:8px; padding:20px;">
                <div style="font-weight:700; color:#06d6a0; font-size:1.1em;">
                    ✅ YES — Names ARE Converging
                </div>
                <div style="font-size:2em; font-weight:800; color:#06d6a0; margin:8px 0;">
                    −50%
                </div>
                <div style="color:#4b5563;">
                    Countryness dropped from 22 (1997) to 11 (2023).
                    Countries are naming babies more similarly than ever.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_no:
        st.markdown(
            """
            <div style="background:#fef2f2; border-left:4px solid #e63946; 
                        border-radius:8px; padding:20px;">
                <div style="font-weight:700; color:#e63946; font-size:1.1em;">
                    ❌ BUT — Cultural Borders Persist
                </div>
                <div style="font-size:2em; font-weight:800; color:#e63946; margin:8px 0;">
                    39%
                </div>
                <div style="color:#4b5563;">
                    of names remain culturally distinct — locked to specific countries.
                    N. Ireland is getting MORE distinct, not less.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    # ─── Key Chart ────────────────────────────────────────────────
    st.markdown("#### Cultural Distinctness Over Time (1997–2023)")
    st.caption("Lower = more converged across countries")

    df = load_metrics()
    fig = countryness_over_time(df)
    st.plotly_chart(fig, use_container_width=True)

    # ─── Transition ───────────────────────────────────────────────
    st.info(
        "💡 **Two opposite truths coexist.** "
        "Use the sidebar to explore both sides: "
        "**Convergence** (coming together) and **Invisible Borders** (staying apart)."
    )
