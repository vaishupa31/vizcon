"""
Discoveries Tab — Full Page
"🎉 I Never Knew That"
All figures computed from the Anglosphere Baby Names dataset (1997–2023).
"""
import streamlit as st
import plotly.graph_objects as go
from utils.charts import CHART_LAYOUT, COLORS, COUNTRY_COLORS


def render():
    # ─── Header ───────────────────────────────────────────────────
    st.markdown(
        """
        <div style="background: linear-gradient(135deg, #EEF2FF, #E8F4FD, #F0FFF4);
                    border-radius: 16px; padding: 50px 30px; text-align: center;
                    margin-bottom: 20px; border: 1px solid #E2E8F0;">
            <h1 style="font-size: 2.8em; font-weight: 800; color: #2D3748; margin: 0 0 12px 0;">
                🎉 I Never Knew That
            </h1>
            <p style="font-size: 1.2em; color: #4A5568; max-width: 650px; margin: 0 auto; line-height: 1.7;">
                Surprising stories hiding in 27 years of baby name data.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ══════════════════════════════════════════════════════════════
    # 🤖 CORPORATE ERASURE
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 🤖 Corporate Erasure")
    st.markdown(
        "What happens when a tech giant names a product after a human name? "
        "The humans stop using it."
    )

    alexa_data = {
        "year": [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],
        "frequency": [3398,3927,3926,3927,4197,4750,4938,4798,5039,6649,6348,5878,6063,5807,5288,5011,4785,4880,6702,5450,4535,3394,2128,1334,718,605,511]
    }
    siri_data = {
        "year": [1997,1998,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2017,2021,2023],
        "frequency": [8,7,9,5,6,25,33,65,68,66,83,94,69,66,10,11,8,3,3,7]
    }

    col_alexa, col_siri = st.columns(2)

    with col_alexa:
        fig_alexa = go.Figure()
        fig_alexa.add_trace(go.Scatter(
            x=alexa_data["year"], y=alexa_data["frequency"],
            mode="lines+markers", line=dict(color="#7C9FD6", width=3), marker=dict(size=5),
            fill="tozeroy", fillcolor="rgba(124,159,214,0.1)",
        ))
        fig_alexa.add_vline(x=2014, line_dash="dash", line_color="#E63946", opacity=0.7)
        fig_alexa.add_annotation(x=2014, y=6702, text="Amazon Echo<br>launches",
            showarrow=True, arrowhead=2, font=dict(size=10, color="#E63946"), ax=40, ay=-30)
        fig_alexa.update_layout(**CHART_LAYOUT, title="Alexa", xaxis_title="", yaxis_title="Babies per year", height=350)
        st.plotly_chart(fig_alexa, use_container_width=True)

    with col_siri:
        fig_siri = go.Figure()
        fig_siri.add_trace(go.Scatter(
            x=siri_data["year"], y=siri_data["frequency"],
            mode="lines+markers", line=dict(color="#C8A8E8", width=3), marker=dict(size=5),
            fill="tozeroy", fillcolor="rgba(200,168,232,0.1)",
        ))
        fig_siri.add_vline(x=2011, line_dash="dash", line_color="#E63946", opacity=0.7)
        fig_siri.add_annotation(x=2011, y=94, text="Apple launches<br>Siri",
            showarrow=True, arrowhead=2, font=dict(size=10, color="#E63946"), ax=40, ay=-30)
        fig_siri.update_layout(**CHART_LAYOUT, title="Siri", xaxis_title="", yaxis_title="Babies per year", height=350)
        st.plotly_chart(fig_siri, use_container_width=True)

    col_a1, col_a2, col_a3 = st.columns(3)
    with col_a1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #EEF2FF, #E8F4FD); border-radius: 12px;
                    padding: 20px; text-align: center; border: 1px solid #E2E8F0;">
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">Alexa — Peak (2015)</div>
            <div style="font-size: 2.2em; font-weight: 800; color: #7C9FD6;">6,702</div>
            <div style="font-size: 0.8em; color: #4A5568;">babies/year</div>
        </div>
        """, unsafe_allow_html=True)
    with col_a2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFF5F5, #FEE2E2); border-radius: 12px;
                    padding: 20px; text-align: center; border: 1px solid #FECACA;">
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">Alexa — Now (2023)</div>
            <div style="font-size: 2.2em; font-weight: 800; color: #E63946;">511</div>
            <div style="font-size: 0.8em; color: #4A5568;">−92% erased</div>
        </div>
        """, unsafe_allow_html=True)
    with col_a3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #F5F0FF, #EDE9FE); border-radius: 12px;
                    padding: 20px; text-align: center; border: 1px solid #E2D9F3;">
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">Siri — Peak → Now</div>
            <div style="font-size: 2.2em; font-weight: 800; color: #9B6FD4;">94 → 7</div>
            <div style="font-size: 0.8em; color: #4A5568;">−93% erased</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown(
        "**Alexa** was a top-100 name with nearly 7,000 babies a year. After Amazon named its voice "
        "assistant Alexa (2014), the collapse was swift: **−92%** by 2023."
    )
    st.markdown(
        "**Siri** was a rising Scandinavian name, climbing from 8 babies (1997) to 94 (2010). "
        "Apple launched Siri in October 2011 — by 2013, just 10 babies. A name on its way up, killed by a product launch."
    )
    st.info(
        "💡 **The asymmetry:** Alexa had a bigger victim pool (6,702/year) but Siri was the crueller kill "
        "— it was actively *growing* when Apple took it. Alexa was already past peak."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 🧟 BACK FROM THE DEAD (Zombie Names)
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 🧟 Back from the Dead")
    st.markdown(
        "Some names flatline completely — years of single digits, near-zero. Then something happens: "
        "a TV show, a cultural shift, a vibe change. And the name claws its way back."
    )
    st.markdown("")

    zombies = [
        {"name": "Wren", "trough": 3, "trough_year": 1999, "peak": "2,596", "peak_year": 2022, "ratio": "865x", "trigger": "Nature names + cottagecore + gender-neutral trend", "color": "#48BB78"},
        {"name": "Salem", "trough": 9, "trough_year": 2000, "peak": "1,246", "peak_year": 2023, "ratio": "138x", "trigger": "WitchTok + Chilling Adventures of Sabrina (2018)", "color": "#9B6FD4"},
        {"name": "Tru", "trough": 6, "trough_year": 2011, "peak": "720", "peak_year": 2022, "ratio": "120x", "trigger": "Authenticity culture — true to yourself", "color": "#ECC94B"},
        {"name": "Octavia", "trough": 43, "trough_year": 2011, "peak": "1,577", "peak_year": 2021, "ratio": "37x", "trigger": "The 100 (CW, 2014-2020) — Octavia Blake", "color": "#F56565"},
        {"name": "Xena", "trough": 10, "trough_year": 2004, "peak": "278", "peak_year": 2022, "ratio": "28x", "trigger": "Streaming brought Warrior Princess to a new generation", "color": "#7C9FD6"},
    ]
    for z in zombies:
        card_html = (
            '<div style="background: linear-gradient(135deg, #EEF2FF, #E8F4FD, #F0FFF4);'
            'border: 1px solid #E2E8F0; border-radius: 16px; padding: 24px 28px; margin-bottom: 16px;'
            'display: grid; grid-template-columns: 1fr auto 1fr auto; align-items: center; gap: 24px;">'
            '<div><div style="font-size: 28px; font-weight: 800; color: #2D3748;">' + z["name"] + '</div>'
            '<div style="font-size: 12px; color: #718096; margin-top: 4px;">' + z["trigger"] + '</div></div>'
            '<div style="text-align: center;">'
            '<div style="font-size: 11px; color: #A0AEC0; text-transform: uppercase; letter-spacing: 0.5px;">Flatlined</div>'
            '<div style="font-size: 22px; font-weight: 700; color: #E53E3E;">' + str(z["trough"]) + '</div>'
            '<div style="font-size: 10px; color: #718096;">' + str(z["trough_year"]) + '</div></div>'
            '<div style="font-size: 24px; color: ' + z["color"] + ';">&rarr;</div>'
            '<div style="text-align: center;">'
            '<div style="font-size: 11px; color: #A0AEC0; text-transform: uppercase; letter-spacing: 0.5px;">Comeback</div>'
            '<div style="font-size: 22px; font-weight: 700; color: ' + z["color"] + ';">' + z["peak"] + '</div>'
            '<div style="font-size: 10px; color: #718096;">' + str(z["peak_year"]) + ' (' + z["ratio"] + ')</div></div>'
            '</div>'
        )
        st.markdown(card_html, unsafe_allow_html=True)

    st.markdown("")
    st.markdown("#### The Comeback Curves")

    chart_data = {
        "Wren": {"years": [1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023], "freqs": [3,6,5,14,11,17,24,54,41,86,107,159,203,288,419,504,569,855,1012,1053,1159,1325,1988,2596,2535], "color": "#48BB78"},
        "Salem": {"years": [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023], "freqs": [34,18,40,9,44,43,40,43,55,46,54,56,70,77,57,84,88,150,220,263,305,327,564,711,951,1152,1246], "color": "#9B6FD4"},
        "Tru": {"years": [2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023], "freqs": [72,55,42,14,39,29,37,6,10,30,31,36,21,52,138,261,338,538,720,670], "color": "#ECC94B"},
        "Octavia": {"years": [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023], "freqs": [220,233,202,177,156,176,128,74,143,84,67,91,79,47,43,63,53,66,279,391,682,943,1066,1152,1577,1509,1441], "color": "#F56565"},
        "Xena": {"years": [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023], "freqs": [246,156,86,74,37,31,18,10,13,13,14,12,13,18,14,34,38,38,58,70,109,126,162,169,162,278,261], "color": "#7C9FD6"},
    }
    fig_zombie = go.Figure()
    for name, data in chart_data.items():
        fig_zombie.add_trace(go.Scatter(x=data["years"], y=data["freqs"], mode="lines",
            name=name, line=dict(color=data["color"], width=2.5)))
    fig_zombie.update_layout(**CHART_LAYOUT, title="", xaxis_title="", yaxis_title="Babies per year",
        height=400, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5))
    st.plotly_chart(fig_zombie, use_container_width=True)

    st.markdown(
        "**What brings a name back?** Streaming reviving old shows (Xena), a breakout character (Octavia), "
        "or aesthetic movements going viral (Salem, Wren). The names that return carry a *vibe* that suddenly fits again."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 🌊 THE HURRICANE EFFECT
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 🌊 The Hurricane Effect")
    st.markdown("Hurricane Katrina hit in August 2005. The name never recovered.")

    katrina_years = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
    katrina_freq = [1964,1792,1734,1782,1655,1480,1442,1473,1612,1123,664,585,445,402,304,341,304,274,272,217,212,166,144,128,137,142,139]
    fig_katrina = go.Figure()
    fig_katrina.add_trace(go.Scatter(x=katrina_years, y=katrina_freq, mode="lines+markers",
        line=dict(color="#7C9FD6", width=3), marker=dict(size=5), fill="tozeroy", fillcolor="rgba(124,159,214,0.1)"))
    fig_katrina.add_vline(x=2005, line_dash="dash", line_color="#E63946", opacity=0.7)
    fig_katrina.add_annotation(x=2005, y=1612, text="Hurricane Katrina<br>Aug 2005",
        showarrow=True, arrowhead=2, font=dict(size=10, color="#E63946"), ax=50, ay=-20)
    fig_katrina.update_layout(**CHART_LAYOUT, title="Katrina", xaxis_title="", yaxis_title="Babies per year", height=350)
    st.plotly_chart(fig_katrina, use_container_width=True)

    col_k1, col_k2, col_k3 = st.columns(3)
    col_k1.metric("Before (2005)", "1,612")
    col_k2.metric("Year 2 (2007)", "664", "-59%")
    col_k3.metric("Now (2023)", "139", "-91%")
    st.markdown(
        "18 years later, Katrina is still at rock bottom — a single storm rewrote the name permanently."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 🕉️ IMMIGRATION WRITTEN IN NAMES
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 🕉️ Immigration Written in Names")
    st.markdown(
        "The Indian diaspora is large enough to register simultaneously in all 8 countries. "
        "Sanskrit-rooted names surged across the Anglosphere this generation."
    )

    indian_years = list(range(1997, 2024))
    # Exact per-year totals for a basket of ~24 Sanskrit/Indian-origin names present in the data
    indian_totals_data = [3814,4742,8167,7049,7626,7939,8321,9260,10366,10853,11960,12643,12549,13199,14990,18017,21308,24106,25156,27432,28523,29007,29177,26783,27775,28822,28607]
    fig_indian = go.Figure()
    fig_indian.add_trace(go.Scatter(x=indian_years, y=indian_totals_data, mode="lines+markers",
        line=dict(color="#F6AD55", width=3), marker=dict(size=4), fill="tozeroy", fillcolor="rgba(246,173,85,0.1)"))
    fig_indian.update_layout(**CHART_LAYOUT, title="Sanskrit/Indian Names — Total Across Anglosphere", xaxis_title="", yaxis_title="Babies per year", height=350)
    st.plotly_chart(fig_indian, use_container_width=True)

    col_s1, col_s2 = st.columns(2)
    col_s1.metric("Basket total 1997", "3,814")
    col_s2.metric("Basket total 2023", "28,607", "+650%")

    st.markdown("**Top individual risers (1997 → 2023):**")
    col_i1, col_i2, col_i3, col_i4, col_i5 = st.columns(5)
    col_i1.metric("Aria", "8,819", "from 93")
    col_i2.metric("Arya", "2,691", "from 24")
    col_i3.metric("Ayaan", "1,163", "from 4")
    col_i4.metric("Aarav", "718", "from 0")
    col_i5.metric("Ishaan", "398", "from 0")
    st.markdown(
        "These names have LOW countryness (2–4) — shared equally across diaspora countries. "
        "Indian families name children the same way regardless of which country they're in — "
        "a global culture writing itself into eight national songbooks at once."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 🎯 THE DIVERSITY EXPLOSION
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 🎯 The Diversity Explosion")
    st.markdown("Parents are choosing more unique names than ever. The era of 'everyone is called John' is over.")

    col_unique, col_top10 = st.columns(2)
    _years = list(range(1997, 2024))
    with col_unique:
        unique_counts = [13889,14060,14163,14622,14842,15112,15777,16345,16779,17519,18351,18725,18935,18932,18955,19196,18704,18559,18523,18304,18092,17899,17756,17431,17763,34184,33902]
        fig_uniq = go.Figure()
        fig_uniq.add_trace(go.Bar(x=_years, y=unique_counts, marker_color="#48BB78", opacity=0.8))
        fig_uniq.update_layout(**CHART_LAYOUT, title="Unique Names Per Year", xaxis_title="", yaxis_title="Count", height=300)
        st.plotly_chart(fig_uniq, use_container_width=True)
    with col_top10:
        top10_pct = [8.83,8.61,8.33,7.98,7.64,7.55,7.39,7.16,6.68,6.24,6.01,5.89,5.91,5.97,5.94,6.00,5.91,5.75,5.68,5.62,5.61,5.53,5.55,5.47,5.41,4.57,4.53]
        fig_top10 = go.Figure()
        fig_top10.add_trace(go.Scatter(x=_years, y=top10_pct, mode="lines+markers",
            line=dict(color="#E53E3E", width=3), marker=dict(size=5)))
        fig_top10.update_layout(**CHART_LAYOUT, title="Top-10 Names as % of All Babies", xaxis_title="", yaxis_title="%", height=300, yaxis_range=[3, 10])
        st.plotly_chart(fig_top10, use_container_width=True)

    col_d1, col_d2, col_d3 = st.columns(3)
    col_d1.metric("Unique Names", "33,902", "+144% since 1997")
    col_d2.metric("Top-10 Share", "4.5%", "was 8.8% in 1997")
    col_d3.metric("Name Pool", "2.4x bigger", "in 27 years")
    st.markdown(
        "In 1997, the top 10 names accounted for nearly 1 in 11 babies. By 2023, it's 1 in 22. "
        "The long tail of naming is getting longer every year."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # ✂️ NAMES ARE SHRINKING
    # ══════════════════════════════════════════════════════════════

    st.markdown("### ✂️ Names Are Shrinking")
    st.markdown("The average baby name lost a third of a letter in 27 years — snappier, more brandable.")

    length_years = list(range(1997, 2024))
    avg_lengths = [6.063,6.042,6.016,5.999,5.972,5.947,5.914,5.895,5.882,5.880,5.874,5.860,5.851,5.841,5.832,5.822,5.820,5.818,5.813,5.805,5.792,5.774,5.759,5.745,5.719,5.740,5.730]
    fig_length = go.Figure()
    fig_length.add_trace(go.Scatter(x=length_years, y=avg_lengths, mode="lines+markers",
        line=dict(color="#4A5568", width=3), marker=dict(size=5)))
    fig_length.update_layout(**CHART_LAYOUT, title="Average Name Length (weighted by frequency)",
        xaxis_title="", yaxis_title="Letters", height=300, yaxis_range=[5.6, 6.15])
    st.plotly_chart(fig_length, use_container_width=True)

    col_l1, col_l2 = st.columns(2)
    col_l1.metric("Avg Length 1997", "6.06 letters")
    col_l2.metric("Avg Length 2023", "5.73 letters", "-0.33")
    st.markdown(
        "Short names (4 letters or fewer) grew from **13.7%** to **20.3%** of all babies. "
        "The winners: Mia, Leo, Ivy, Kai, Ava, Lux, Wren, Finn, Zoe, Max."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 🎵 SOFTER, MORE MELODIC (vowel-ending names) — NEW
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 🎵 Names Are Getting More Melodic")
    st.markdown(
        "Listen closely and names are ending on a softer note — more of them finish on a vowel "
        "(that open, singable *-a, -o, -ie* sound). The Anglosphere is trending toward names that flow."
    )

    vowel_years = list(range(1997, 2024))
    vowel_share = [33.68,33.66,33.75,33.92,34.26,34.74,35.14,35.44,35.95,36.24,36.20,36.16,36.21,36.49,36.47,36.62,36.85,37.03,37.20,37.71,38.22,38.78,39.28,39.86,40.44,41.55,41.95]
    fig_vowel = go.Figure()
    fig_vowel.add_trace(go.Scatter(x=vowel_years, y=vowel_share, mode="lines+markers",
        line=dict(color="#F5A9C0", width=3), marker=dict(size=5), fill="tozeroy", fillcolor="rgba(245,169,192,0.12)"))
    fig_vowel.update_layout(**CHART_LAYOUT, title="% of Babies With a Vowel-Ending Name",
        xaxis_title="", yaxis_title="%", height=300, yaxis_range=[30, 45])
    st.plotly_chart(fig_vowel, use_container_width=True)

    col_v1, col_v2 = st.columns(2)
    col_v1.metric("Vowel-ending 1997", "33.7%")
    col_v2.metric("Vowel-ending 2023", "41.9%", "+8.2 pts")
    st.markdown(
        "Think **Mia, Ava, Leo, Aria, Sophia, Charlie, Willow, Theo** — soft landings, all vowels. "
        "The hard-consonant endings of the 20th century (Robert, Richard, Deborah) are fading out."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 🔤 THE FALL OF 'J' — NEW
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 🔤 The Great 'J' Collapse")
    st.markdown(
        "Every letter has its era. The 'J' names that defined the '90s — Jessica, Jason, Jennifer, Jacob — "
        "are quietly vanishing. No single letter has fallen further."
    )

    letter_change = [
        ("J", -6.01, "#E63946"),
        ("C", -2.65, "#F56565"),
        ("D", -2.26, "#F6AD55"),
        ("A", 1.74, "#7C9FD6"),
        ("E", 3.26, "#68B58A"),
        ("L", 3.65, "#48BB78"),
    ]
    fig_letter = go.Figure()
    fig_letter.add_trace(go.Bar(
        x=[l[0] for l in letter_change],
        y=[l[1] for l in letter_change],
        marker_color=[l[2] for l in letter_change],
        text=[f"{l[1]:+.1f}" for l in letter_change],
        textposition="outside",
    ))
    fig_letter.update_layout(**CHART_LAYOUT, title="Change in Share of Babies by First Letter (1997 → 2023, % points)",
        xaxis_title="First letter", yaxis_title="Change (% points)", height=340, showlegend=False)
    st.plotly_chart(fig_letter, use_container_width=True)

    st.markdown(
        "**'J' lost 6 percentage points** — a bigger drop than any other letter. Meanwhile soft-sounding "
        "**'L'** (Liam, Luca, Lily, Layla) and **'E'** (Emma, Ella, Ethan) names gained the most. "
        "The alphabet of naming is being rewritten, one initial at a time."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 😈 THE TABOO THAT BROKE (Lucifer)
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 😈 The Taboo That Broke")
    st.markdown(
        "Some names sit behind an invisible line no one crosses — until pop culture quietly moves the line. "
        "**Zero** babies were named Lucifer for years… then a hit show rebranded the devil as a charming lead."
    )

    col_luc_chart, col_luc_note = st.columns([1.4, 1])
    with col_luc_chart:
        lucifer_years = [2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023]
        lucifer_freq = [10, 13, 11, 20, 29, 37, 77, 57]
        fig_luc = go.Figure()
        fig_luc.add_trace(go.Bar(x=lucifer_years, y=lucifer_freq, marker_color="#9B6FD4"))
        fig_luc.add_vline(x=2016, line_dash="dash", line_color="#E63946", opacity=0.6)
        fig_luc.add_annotation(x=2016, y=13, text="Netflix's<br>Lucifer premieres",
            showarrow=True, arrowhead=2, font=dict(size=10, color="#E63946"), ax=55, ay=-25)
        fig_luc.update_layout(**CHART_LAYOUT, title="Lucifer — the taboo that broke",
            xaxis_title="", yaxis_title="Babies per year", height=320)
        st.plotly_chart(fig_luc, use_container_width=True)
    with col_luc_note:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #F5F0FF, #EDE9FE); border-radius: 12px;
                    padding: 24px; border: 1px solid #E2D9F3; height: 100%;
                    display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">Before 2016</div>
            <div style="font-size: 2.4em; font-weight: 800; color: #9B6FD4;">0</div>
            <div style="font-size: 0.85em; color: #4A5568; margin-bottom: 14px;">babies — the name no one dared</div>
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">Peak (2022)</div>
            <div style="font-size: 2.4em; font-weight: 800; color: #6B46C1;">77</div>
            <div style="font-size: 0.85em; color: #4A5568;">after the show made him the hero</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("")
    st.markdown(
        "**Zero** babies named Lucifer until 2016. Then Netflix's *Lucifer* (2016–2021) recast the devil "
        "as a witty, likeable protagonist — and by 2022, **77 babies** carried the name. A single show can "
        "unlock a door that had been shut for centuries."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # CLOSING NOTE
    # ══════════════════════════════════════════════════════════════

    st.markdown(
        "<div style='text-align:center; color:#718096; font-style:italic; padding: 10px 0 30px;'>"
        "Every one of these was hiding in the same 200 million names — you just had to know where to listen. 🎧"
        "</div>",
        unsafe_allow_html=True,
    )
