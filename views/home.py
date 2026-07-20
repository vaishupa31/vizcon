import streamlit as st
import plotly.graph_objects as go
import numpy as np


def render():
    # ===== HERO SECTION =====
    st.markdown("""
    <style>
    .hero-title {
        font-size: 3.2rem;
        font-weight: 900;
        background: linear-gradient(135deg, #e2e8f0, #f78da7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.4rem;
        color: #94a3b8;
        text-align: center;
        font-weight: 300;
        margin-top: 0.5rem;
    }
    .stat-box {
        background: #1e1e3a;
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 12px;
        padding: 1.2rem 1rem;
        text-align: center;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: 900;
        color: #e94560;
    }
    .stat-label {
        font-size: 0.8rem;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .section-header {
        font-size: 1.8rem;
        font-weight: 800;
        margin-top: 3rem;
        margin-bottom: 0.5rem;
    }
    .insight-card {
        background: rgba(233, 69, 96, 0.08);
        border-left: 4px solid #e94560;
        border-radius: 0 12px 12px 0;
        padding: 1.2rem 1.5rem;
        margin: 1rem 0;
    }
    .truth-card {
        background: #1e1e3a;
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 14px;
        padding: 2rem;
        height: 100%;
    }
    .truth-yes {
        border-top: 4px solid #10b981;
    }
    .truth-no {
        border-top: 4px solid #e94560;
    }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.markdown('<p class="hero-title">The DNA of a Name</p>', unsafe_allow_html=True)
    st.markdown('<p class="hero-subtitle">Same Language. Different Cultures.</p>', unsafe_allow_html=True)

    st.markdown("")

    # Stat cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="stat-box"><div class="stat-number">1.5M+</div><div class="stat-label">Name Records</div></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-box"><div class="stat-number">8</div><div class="stat-label">Countries</div></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-box"><div class="stat-number">114</div><div class="stat-label">Years of Data</div></div>', unsafe_allow_html=True)
    with col4:
        st.markdown('<div class="stat-box"><div class="stat-number">76,183</div><div class="stat-label">Unique Names</div></div>', unsafe_allow_html=True)

    st.markdown("---")

    # ===== SECTION 1: THE ANGLOSPHERE =====
    st.markdown('<p class="section-header">🌍 The Anglosphere</p>', unsafe_allow_html=True)
    st.markdown("""
    Eight countries united by one language — English. Connected through British colonization, 
    migration, and shared media. Today linked by pop culture, internet, and global platforms.
    But each carries its **own cultural currents** beneath the English surface.
    """)

    # Globe visualization
    col_text, col_globe = st.columns([1, 2])

    with col_text:
        st.markdown("""
        **The Countries:**
        - 🇺🇸 USA
        - 🇬🇧 England & Wales
        - 🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scotland
        - 🏴 Northern Ireland
        - 🇮🇪 Ireland
        - 🇨🇦 Canada
        - 🇦🇺 Australia
        - 🇳🇿 New Zealand

        **Cultural undercurrents:**
        - 🍀 Gaelic heritage (Ireland, NI, Scotland)
        - 🇫🇷 Francophone identity (Quebec, Canada)
        - 🌮 Hispanic influence (USA)
        - 🦘 Indigenous cultures (Australia, NZ)

        They share a language, legal traditions, and cultural exchange — 
        but do they share a **naming culture**?
        """)

    with col_globe:
        fig = create_anglosphere_globe()
        st.plotly_chart(fig, use_container_width=True, key="globe")

    st.markdown("---")

    # ===== SECTION 2: THE TWO TRUTHS =====
    st.markdown('<p class="section-header">🔍 The Core Question</p>', unsafe_allow_html=True)
    st.markdown("""
    > *"These 8 countries share a language. Does that mean they share a culture?  
    > Baby names — the most personal choice a family makes — give us the answer."*
    """)

    st.markdown("")
    st.markdown("### The Answer: **Both are true.**")
    st.markdown("")

    # Two truths side by side
    col_yes, col_no = st.columns(2)

    with col_yes:
        st.markdown("""
        <div class="truth-card truth-yes">
            <h3 style="color: #10b981; margin-top: 0;">✓ YES — Names ARE Converging</h3>
            <p style="color: #94a3b8; font-size: 0.95rem;">
                The Anglosphere is becoming one naming culture. Shared screens, shared internet, 
                shared trends are dissolving borders.
            </p>
            <table style="width: 100%; font-size: 0.85rem; color: #e2e8f0;">
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.5rem 0;"><strong>Avg Countryness</strong></td>
                    <td style="padding: 0.5rem 0;">42 (1980s) → 11 (2023)</td>
                    <td style="padding: 0.5rem 0; color: #10b981;"><strong>−74%</strong></td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.5rem 0;"><strong>Spread Speed</strong></td>
                    <td style="padding: 0.5rem 0;">65 years (1930s) → 9 years (2000s)</td>
                    <td style="padding: 0.5rem 0; color: #10b981;"><strong>−86%</strong></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem 0;"><strong>Global Names</strong></td>
                    <td style="padding: 0.5rem 0;">36% (1930s) → 54% (2020s)</td>
                    <td style="padding: 0.5rem 0; color: #10b981;"><strong>+50%</strong></td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    with col_no:
        st.markdown("""
        <div class="truth-card truth-no">
            <h3 style="color: #e94560; margin-top: 0;">✗ BUT NO — Cultural Borders Persist</h3>
            <p style="color: #94a3b8; font-size: 0.95rem;">
                Despite sharing a language, invisible walls hold. Pronunciation, politics, 
                and cultural revival keep names locked to their homeland.
            </p>
            <table style="width: 100%; font-size: 0.85rem; color: #e2e8f0;">
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.5rem 0;"><strong>Still Distinct</strong></td>
                    <td style="padding: 0.5rem 0;">39% of names culturally locked</td>
                    <td style="padding: 0.5rem 0; color: #e94560;"><strong>39%</strong></td>
                </tr>
                <tr style="border-bottom: 1px solid rgba(255,255,255,0.1);">
                    <td style="padding: 0.5rem 0;"><strong>N. Ireland</strong></td>
                    <td style="padding: 0.5rem 0;">Getting MORE distinct, not less</td>
                    <td style="padding: 0.5rem 0; color: #e94560;"><strong>+38%</strong></td>
                </tr>
                <tr>
                    <td style="padding: 0.5rem 0;"><strong>Gaelic Lock</strong></td>
                    <td style="padding: 0.5rem 0;">Pronunciation = 7.4x cultural lock</td>
                    <td style="padding: 0.5rem 0; color: #e94560;"><strong>7.4x</strong></td>
                </tr>
            </table>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")

    # Convergence vs Divergence visualization
    st.markdown("### Convergence Over Time: Average Cultural Distinctness Declining")
    fig_countryness = create_countryness_trend()
    st.plotly_chart(fig_countryness, use_container_width=True, key="countryness_trend")

    st.markdown("""
    <div class="insight-card">
        <strong>💡 Two opposite, coexisting truths — and that's the story.</strong><br>
        The Anglosphere IS converging (countryness dropped 74%). But pockets of resistance are growing 
        stronger, not weaker. This creates the central tension of our entire analysis.
        <br><br>
        <strong>Navigate the chapters</strong> in the sidebar to explore each side of this paradox.
    </div>
    """, unsafe_allow_html=True)


def create_anglosphere_globe():
    """Create a 3D globe with Anglosphere countries highlighted."""

    # Country centroids (lat, lon)
    countries = {
        "USA": (39.8, -98.6),
        "England & Wales": (52.4, -1.5),
        "Scotland": (56.5, -4.0),
        "N. Ireland": (54.6, -6.7),
        "Ireland": (53.4, -7.9),
        "Canada": (56.1, -106.3),
        "Australia": (-25.3, 133.8),
        "New Zealand": (-41.3, 174.8),
    }

    colors = {
        "USA": "#3b82f6",
        "England & Wales": "#ef4444",
        "Scotland": "#8b5cf6",
        "N. Ireland": "#059669",
        "Ireland": "#10b981",
        "Canada": "#f59e0b",
        "Australia": "#f97316",
        "New Zealand": "#06b6d4",
    }

    lats = [v[0] for v in countries.values()]
    lons = [v[1] for v in countries.values()]
    names = list(countries.keys())
    marker_colors = [colors[n] for n in names]

    fig = go.Figure()

    # Country markers
    fig.add_trace(go.Scattergeo(
        lat=lats,
        lon=lons,
        text=names,
        mode='markers+text',
        marker=dict(
            size=14,
            color=marker_colors,
            line=dict(width=1, color='rgba(255,255,255,0.3)'),
            opacity=0.9
        ),
        textposition="top center",
        textfont=dict(color='white', size=10),
        hoverinfo='text',
        hovertext=[f"<b>{n}</b>" for n in names]
    ))

    # Draw connections (arcs between countries to show they're connected)
    connections = [
        ("USA", "England & Wales"),
        ("USA", "Canada"),
        ("England & Wales", "Australia"),
        ("England & Wales", "New Zealand"),
        ("England & Wales", "Ireland"),
        ("England & Wales", "Scotland"),
        ("Scotland", "N. Ireland"),
        ("Canada", "Australia"),
    ]

    for c1, c2 in connections:
        lat1, lon1 = countries[c1]
        lat2, lon2 = countries[c2]
        fig.add_trace(go.Scattergeo(
            lat=[lat1, lat2],
            lon=[lon1, lon2],
            mode='lines',
            line=dict(width=0.8, color='rgba(233, 69, 96, 0.25)'),
            hoverinfo='skip',
            showlegend=False
        ))

    fig.update_geos(
        projection_type="orthographic",
        projection_rotation=dict(lon=-30, lat=30),
        showland=True,
        landcolor='#1e1e3a',
        showocean=True,
        oceancolor='#0f0f1a',
        showlakes=False,
        showcountries=True,
        countrycolor='rgba(255,255,255,0.08)',
        showcoastlines=True,
        coastlinecolor='rgba(255,255,255,0.15)',
        bgcolor='rgba(0,0,0,0)',
    )

    fig.update_layout(
        height=500,
        margin=dict(l=0, r=0, t=0, b=0),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        showlegend=False,
        geo=dict(
            bgcolor='rgba(0,0,0,0)',
        )
    )

    return fig


def create_countryness_trend():
    """Create a line chart showing average countryness declining over time."""

    # Data from our analysis
    years = [1935, 1940, 1945, 1950, 1955, 1960, 1965, 1970, 1975, 1980,
             1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2023]
    avg_countryness = [41.6, 31.5, 31.5, 36.2, 27.7, 26.3, 32.8, 28.6, 37.0, 40.6,
                       41.5, 70.0, 26.1, 20.7, 20.6, 18.5, 17.6, 17.5, 16.6]

    fig = go.Figure()

    # Main trend line
    fig.add_trace(go.Scatter(
        x=years,
        y=avg_countryness,
        mode='lines+markers',
        line=dict(color='#e94560', width=3),
        marker=dict(size=6, color='#e94560'),
        fill='tozeroy',
        fillcolor='rgba(233, 69, 96, 0.08)',
        name='Avg Countryness',
        hovertemplate='<b>%{x}</b><br>Avg Countryness: %{y:.1f}<extra></extra>'
    ))

    # Add annotation for key points
    fig.add_annotation(
        x=1985, y=41.5,
        text="1980s peak: 42",
        showarrow=True,
        arrowhead=2,
        arrowcolor='rgba(255,255,255,0.4)',
        font=dict(color='white', size=11),
        ax=40, ay=-40
    )

    fig.add_annotation(
        x=2023, y=16.6,
        text="2023: 11 (−74%)",
        showarrow=True,
        arrowhead=2,
        arrowcolor='rgba(255,255,255,0.4)',
        font=dict(color='#10b981', size=11),
        ax=40, ay=30
    )

    fig.update_layout(
        height=350,
        margin=dict(l=40, r=20, t=30, b=40),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(
            title="Year",
            gridcolor='rgba(255,255,255,0.05)',
            color='#94a3b8',
            dtick=10
        ),
        yaxis=dict(
            title="Avg Countryness Score",
            gridcolor='rgba(255,255,255,0.05)',
            color='#94a3b8',
        ),
        font=dict(family="Inter, sans-serif"),
        showlegend=False,
        hovermode='x unified'
    )

    return fig
