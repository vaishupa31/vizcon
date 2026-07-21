import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import os
from utils.data_loader import load_metrics, load_summary
from utils.charts import CHART_LAYOUT, COLORS, COUNTRY_COLORS


def render():
    # ─── Header ───────────────────────────────────────────────────
    st.markdown(
        """
        <div style="text-align:center; padding: 20px 0 10px;">
            <h1 style="font-size: 2.4em; color: #4A5568;">
                💿 The Local Vinyl
            </h1>
            <p style="font-size: 1.15em; color: #718096; max-width: 700px; margin: 0 auto;">
                Some names never leave the record shop. Despite sharing a language,<br>
                cultural walls keep 39% of names locked to a single country.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

    df = load_metrics()
    summary = load_summary()

    # ─── Interactive: "Can You Say This?" ─────────────────────────
    st.markdown("### 🎤 Can You Say This?")
    st.markdown(
        "These names are **cultural passwords** — if you can't say them, "
        "they'll never leave their home country. Give it a try!"
    )

    # Pronunciation challenge data
    challenges = [
        {
            "name": "Sadhbh",
            "country": "🇮🇪 Ireland",
            "language": "Irish Gaelic",
            "countryness": 8171,
            "actual": "SIVE (just one syllable!)",
            "hint": "It's only ONE syllable! 6 letters, 3 sounds.",
            "letters": 6,
            "sounds": 3,
        },
        {
            "name": "Seumas",
            "country": "🏴󠁧󠁢󠁳󠁣󠁴󠁿 Scotland",
            "language": "Scottish Gaelic",
            "countryness": 4629,
            "actual": "SHAY-mus",
            "hint": "It's the Gaelic version of 'James'!",
            "letters": 6,
            "sounds": 6,
        },
        {
            "name": "Ffion",
            "country": "🏴󠁧󠁢󠁷󠁬󠁳󠁿 Wales",
            "language": "Welsh",
            "countryness": 1761,
            "actual": "FEE-on",
            "hint": "Double-F in Welsh = 'F' sound. Single F = 'V' sound!",
            "letters": 5,
            "sounds": 4,
        },
        {
            "name": "Frédérique",
            "country": "🇨🇦 Canada",
            "language": "French",
            "countryness": 10588,
            "actual": "fray-day-REEK",
            "hint": "Every accent (é) changes the vowel. It's 4 syllables.",
            "letters": 10,
            "sounds": 9,
            "audio_file": "frederique"
        },
        {
            "name": "Ophélie",
            "country": "🇨🇦 Canada",
            "language": "French",
            "countryness": 3786,
            "actual": "oh-fay-LEE",
            "hint": "Not 'Ophelia' — the French ending is '-lee' not '-lia'.",
            "letters": 7,
            "sounds": 6,
            "audio_file": "ophelie"
        },
        {
            "name": "Ngaire",
            "country": "🇳🇿 New Zealand",
            "language": "Māori",
            "countryness": 11270,
            "actual": "NY-ree",
            "hint": "'Ng' at the start is one sound — like the 'ng' in 'sing'!",
            "letters": 6,
            "sounds": 4,
        },
        {
            "name": "Aroha",
            "country": "🇳🇿 New Zealand",
            "language": "Māori",
            "countryness": 13713,
            "actual": "ah-ROH-ha",
            "hint": "It means 'love' in Māori. Every letter is pronounced!",
            "letters": 5,
            "sounds": 5,
        },
        {
            "name": "Narelle",
            "country": "🇦🇺 Australia",
            "language": "Aboriginal Australian",
            "countryness": 4738,
            "actual": "nah-RELL",
            "hint": "An Aboriginal name meaning 'woman from the sea'.",
            "letters": 7,
            "sounds": 5,
        },
        {
            "name": "Caoimhín",
            "country": "🏴 N. Ireland",
            "language": "Irish Gaelic",
            "countryness": 465,
            "actual": "KEE-veen",
            "hint": "It's the Irish version of 'Kevin'! The 'aoi'='ee', 'mh'='v'.",
            "letters": 8,
            "sounds": 6,
            "audio_file": "caoimhin"
        },
        {
            "name": "Nikau",
            "country": "🇳🇿 New Zealand",
            "language": "Māori",
            "countryness": 29620,
            "actual": "NEE-kow",
            "hint": "Named after the Nikau palm — NZ's only native palm tree.",
            "letters": 5,
            "sounds": 4,
        },
    ]

    # Random challenge selector
    if "challenge_idx" not in st.session_state:
        st.session_state.challenge_idx = 0
    if "revealed" not in st.session_state:
        st.session_state.revealed = False

    challenge = challenges[st.session_state.challenge_idx]

    # Display the challenge card
    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #F0F8FF, #E8F4FD); 
                    border: 2px solid #7C9FD6; border-radius: 16px; 
                    padding: 30px; text-align: center; margin: 20px 0;">
            <div style="font-size: 0.85em; color: #718096; text-transform: uppercase; 
                        letter-spacing: 2px;">How do you pronounce...</div>
            <div style="font-size: 3em; font-weight: 800; color: #4A5568; 
                        margin: 15px 0; font-family: Georgia, serif;">
                {challenge['name']}
            </div>
            <div style="font-size: 0.9em; color: #718096;">
                {challenge['country']} · Countryness: <b>{challenge['countryness']:,}</b> · 
                {challenge['letters']} letters, {challenge['sounds']} sounds
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Buttons row
    col_hint, col_reveal, col_next = st.columns([1, 1, 1])

    with col_hint:
        if st.button("💡 Hint", use_container_width=True):
            st.info(f"💡 {challenge['hint']}")

    with col_reveal:
        if st.button("🔊 Reveal Pronunciation", use_container_width=True):
            st.session_state.revealed = True

    with col_next:
        if st.button("➡️ Next Name", use_container_width=True):
            st.session_state.challenge_idx = (st.session_state.challenge_idx + 1) % len(challenges)
            st.session_state.revealed = False
            st.rerun()

    # Reveal section
    if st.session_state.revealed:
        st.markdown(
            f"""
            <div style="background: #F0FFF4; border: 2px solid #A8E6C8; border-radius: 12px;
                        padding: 20px; text-align: center; margin-top: 16px;">
                <div style="font-size: 0.85em; color: #059669; text-transform: uppercase; 
                            letter-spacing: 2px;">It's pronounced:</div>
                <div style="font-size: 2.2em; font-weight: 700; color: #059669; margin: 8px 0;">
                    "{challenge['actual']}"
                </div>
                <div style="font-size: 0.9em; color: #718096; margin-top: 8px;">
                    {challenge['hint']}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Audio playback (if audio files exist)
        audio_key = challenge.get('audio_file', challenge['name'].lower())
        audio_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets", "audio", f"{audio_key}.wav"
        )
        if os.path.exists(audio_path):
            st.audio(audio_path)
        else:
            st.caption("🔈 Audio clip coming soon!")

        # Why it matters
        st.markdown(
            f"""
            <div style="background: #FFF5F5; border-radius: 8px; padding: 12px; 
                        margin-top: 12px; text-align: center;">
                <span style="color: #e63946; font-weight: 600;">
                    Countryness: {challenge['countryness']:,}
                </span>
                <span style="color: #718096;"> — This is why </span>
                <span style="font-weight: 600;">{challenge['name']}</span>
                <span style="color: #718096;"> never left {challenge['country']}</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Progress dots
    dots = ""
    for i in range(len(challenges)):
        if i == st.session_state.challenge_idx:
            dots += "● "
        else:
            dots += "○ "
    st.caption(f"Name {st.session_state.challenge_idx + 1} of {len(challenges)}:  {dots}")

    st.markdown("---")

    
    # ─── Section 1: The Pronunciation Wall ────────────────────────
    st.markdown("### 🗣️ The Pronunciation Wall")
    st.markdown(
        "Two Irish names. Both ancient. Both beautiful. **Completely different fates.**"
    )

    st.markdown("---")
    # ─── Declan vs Niamh comparison ───────────────────────────────
    st.markdown("### 📊 The Proof: Declan vs Niamh")

    col_dec, col_niamh = st.columns(2)
    with col_dec:
        st.markdown(
            """
            <div style="background: #E8F4FD; border: 2px solid #A8E6C8; border-radius: 12px;
                        padding: 20px; text-align: center;">
                <div style="font-size: 2em; font-weight: 800; color: #4A5568;">Declan</div>
                <div style="font-size: 0.9em; color: #718096; margin: 4px 0;">Pronounced: "DECK-lin" ✅</div>
                <div style="font-size: 2.5em; font-weight: 800; color: #A8E6C8; margin: 8px 0;">2.5</div>
                <div style="font-size: 0.85em; color: #718096;">Countryness (2023)</div>
                <div style="font-size: 0.8em; color: #A8E6C8; margin-top: 6px;">🌍 Gone global — in all 8 countries</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_niamh:
        st.markdown(
            """
            <div style="background: #FFF5F5; border: 2px solid #F5B7C5; border-radius: 12px;
                        padding: 20px; text-align: center;">
                <div style="font-size: 2em; font-weight: 800; color: #4A5568;">Niamh</div>
                <div style="font-size: 0.9em; color: #718096; margin: 4px 0;">Pronounced: "NEEV" ❌</div>
                <div style="font-size: 2.5em; font-weight: 800; color: #F5B7C5; margin: 8px 0;">28</div>
                <div style="font-size: 0.85em; color: #718096;">Countryness (2023)</div>
                <div style="font-size: 0.8em; color: #F5B7C5; margin-top: 6px;">🏠 Stayed home — locked in Ireland/NI</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")
    st.markdown("**Why?** You can say one. You can't say the other.")

    # 3.2% vs 30.2% chart
    st.markdown("#### Gaelic Orthography = Cultural Lock")

    fig_gaelic = go.Figure()
    fig_gaelic.add_trace(go.Bar(
        x=["Names that ESCAPED Ireland", "Names that STAYED"],
        y=[3.2, 30.2],
        marker_color=["#A8E6C8", "#F5B7C5"],
        text=["3.2%", "30.2%"],
        textposition="outside",
        textfont=dict(size=16, color="#4A5568"),
    ))
    fig_gaelic.update_layout(
        **CHART_LAYOUT,
        title=None,
        yaxis_title="% with Gaelic spelling (bh, dh, gh, mh, aoi)",
        height=350,
        showlegend=False,
    )
    st.plotly_chart(fig_gaelic, use_container_width=True)

    st.info("💡 **10x difference.** Gaelic spelling is literally a cultural lock. Names with 'bh', 'dh', 'gh', 'mh', or 'aoi' are **7.4x more culturally locked** than names without.")

    # Three borders table
    st.markdown("#### Three Borders Within One Language")
    border_data = {
        "Border": ["🟣 Gaelic ↔ Anglophone", "🔵 Francophone ↔ Anglophone", "🟢 Hispanic ↔ Anglophone"],
        "Locked (can't cross)": ["Sadhbh, Caoilfhionn, Niamh, Aoife", "Frédérique, Océanne, Laurianne", "Almost none!"],
        "Escaped (crossed)": ["Declan, Ronan, Connor, Liam", "Very few escape", "Santiago, Diego, Carlos, Isabella"],
        "Verdict": ["Hard wall 🧱", "Hard wall (but fading) 📉", "No wall! 🌍"],
    }
    st.dataframe(border_data, use_container_width=True, hide_index=True)

    st.markdown("---")

    # ─── Section 2: Political Identity — NI Resistance ────────────
    st.markdown("### 🏴 Political Identity — Northern Ireland Goes Opposite")
    st.markdown(
        "While the entire Anglosphere converges, **Northern Ireland is going the other direction.**"
    )

    # NI vs Ireland divergence chart
    ni_data = df[
        (df["max_country"].isin(["Northern Ireland", "Ireland"]))
        & (df["countryness"] > 100)
    ].groupby(["year", "max_country"])["name"].nunique().reset_index()
    ni_data.columns = ["year", "country", "high_identity_names"]

    fig_ni = px.line(
        ni_data,
        x="year",
        y="high_identity_names",
        color="country",
        color_discrete_map={
            "Northern Ireland": "#9FE6C8",
            "Ireland": "#F5B7C5",
        },
        markers=True,
    )
    fig_ni.update_layout(
        **CHART_LAYOUT,
        title="High-Identity Names (countryness > 100) Over Time",
        xaxis_title="Year",
        yaxis_title="Number of Highly Distinct Names",
        legend_title=None,
        height=400,
    )
    st.plotly_chart(fig_ni, use_container_width=True)

    col_ni, col_irl = st.columns(2)
    with col_ni:
        st.markdown(
            """
            <div style="background: #E6FFF5; border-left: 4px solid #A8E6C8; 
                        border-radius: 8px; padding: 16px;">
                <div style="font-weight: 700; color: #059669;">🏴 Northern Ireland</div>
                <div style="font-size: 1.8em; font-weight: 800; color: #059669;">+38%</div>
                <div style="color: #718096; font-size: 0.9em;">
                    47 → 65 high-identity names (1997–2021)<br>
                    Getting MORE distinct while everyone converges
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col_irl:
        st.markdown(
            """
            <div style="background: #FFF5F5; border-left: 4px solid #F5B7C5; 
                        border-radius: 8px; padding: 16px;">
                <div style="font-weight: 700; color: #e63946;">🇮🇪 Ireland</div>
                <div style="font-size: 1.8em; font-weight: 800; color: #e63946;">−52%</div>
                <div style="color: #718096; font-size: 0.9em;">
                    71 → 34 high-identity names (1997–2021)<br>
                    Same heritage — opposite response
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")
    st.info("💡 **Same Gaelic heritage. Opposite response.** In NI, naming a child in Gaelic is a political and cultural statement tied to the Irish language movement.")

    st.markdown("---")

    # ─── Section 3: Active Cultural Revival ───────────────────────
    st.markdown("### 📜 Active Cultural Revival — Creating NEW Locked Names")
    st.markdown(
        "These aren't old names surviving — they're **brand new**, invented since 2010."
    )

    revival_data = {
        "Name": ["Iarla", "Siún", "Cadain", "Siomha", "Caragh", "Aibhlinn", "Bradan", "Breagha", "Doireann", "Saorla"],
        "First Appeared": [2015, 2013, 2017, 2017, 2021, 2018, 2016, 2018, 2020, 2012],
        "Country": ["Ireland", "Ireland", "N. Ireland", "Ireland", "Ireland", "N. Ireland", "N. Ireland", "Scotland", "Ireland", "N. Ireland"],
        "Countryness": [815, 713, 702, 547, 532, 465, 458, 446, 422, 374],
    }
    st.dataframe(revival_data, use_container_width=True, hide_index=True)

    st.markdown("**85 brand-new high-identity Celtic names** since 2010. Communities are inventing names *designed* to be unpronounceable by outsiders.")

    st.markdown("---")

    # ─── Section 4: Religious Tradition ───────────────────────────
    st.markdown("### ✝️ Same Saint, Different Fate")
    st.markdown("The **local form** carries identity that the English translation strips away.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div style="background: #F0F8FF; border-radius: 10px; padding: 16px; text-align: center;">
                <div style="color: #A8E6C8; font-size: 0.8em;">GLOBAL</div>
                <div style="font-size: 1.3em; font-weight: 700;">Patrick</div>
                <div style="font-size: 1.6em; font-weight: 800; color: #A8E6C8;">~2</div>
                <div style="color: #718096; font-size: 0.8em;">countryness</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div style="text-align: center; padding-top: 30px;">
                <div style="font-size: 2em;">⚡</div>
                <div style="font-size: 0.85em; color: #718096;">Same saint.<br>Different name.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div style="background: #FFF5F5; border-radius: 10px; padding: 16px; text-align: center;">
                <div style="color: #F5B7C5; font-size: 0.8em;">LOCKED</div>
                <div style="font-size: 1.3em; font-weight: 700;">Pádraig</div>
                <div style="font-size: 1.6em; font-weight: 800; color: #F5B7C5;">343</div>
                <div style="color: #718096; font-size: 0.8em;">countryness</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

    # ─── Section 5: Geographic Isolation ──────────────────────────
    st.markdown("### 🏝️ Culture > Geography")

    # Horizontal bar: avg countryness by country 2023
    country_cn = df[df["year"] == 2023].groupby("max_country")["countryness"].mean().sort_values(ascending=True).reset_index()

    fig_geo = go.Figure()
    fig_geo.add_trace(go.Bar(
        x=country_cn["countryness"],
        y=country_cn["max_country"],
        orientation="h",
        marker_color=[COUNTRY_COLORS.get(c, "#7C9FD6") for c in country_cn["max_country"]],
        text=[f"{v:.1f}" for v in country_cn["countryness"]],
        textposition="outside",
    ))
    fig_geo.update_layout(
        **CHART_LAYOUT,
        title="Avg Countryness by Country (2023) — Higher = More Culturally Distinct",
        height=350,
        xaxis_title="Avg Countryness Score",
    )
    st.plotly_chart(fig_geo, use_container_width=True)

    st.info(
        "💡 **Ireland** (close to UK) remains 5x more distinct than **Australia** "
        "(geographically isolated but culturally connected via media). "
        "Culture > Geography."
    )
