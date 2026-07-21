import streamlit as st
from utils.data_loader import load_metrics
from utils.charts import countryness_over_time, COLORS


def render():
    # ─── Hero Section ─────────────────────────────────────────────
    st.markdown(
        """
        <div style="text-align:center; padding: 30px 0 20px;">
            <h1 style="font-size:2.8em; font-weight:800; 
                       background: linear-gradient(135deg, #667eea, #764ba2);
                       -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                       margin-bottom: 8px;">
                What's in a Name?
            </h1>
            <p style="font-size:1.2em; color:#6b7280; max-width:700px; margin:0 auto;">
                8 countries. 1 language. 27 years of baby names.<br>
                Do they name babies the same way? The answer is more surprising than you think.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Stats bar
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Unique Names", "17,000+")
    with col2:
        st.metric("Countries", "8")
    with col3:
        st.metric("Time Span", "1997–2023")
    with col4:
        st.metric("Records", "1.55M")

    st.markdown("---")

    # ─── The Anglosphere ──────────────────────────────────────────
    st.markdown("### 🌍 The Anglosphere")
    st.markdown(
        """
        Eight countries united by one language — English.
        Connected through colonization, migration, and shared media.
        But each carries its **own cultural currents** beneath the surface.
        """
    )

    # Country grid
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
