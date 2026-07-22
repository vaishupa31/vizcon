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
        <div style="background: linear-gradient(135deg, #EEF2FF, #E8F4FD, #F0FFF4); 
                    border-radius: 16px; padding: 50px 30px; text-align: center; 
                    margin-bottom: 20px; border: 1px solid #E2E8F0;">
            <h1 style="font-size: 2.8em; font-weight: 800; color: #2D3748; margin: 0 0 12px 0;">
                💿 The Local Vinyl
            </h1>
            <p style="font-size: 1.2em; color: #4A5568; max-width: 650px; margin: 0 auto; line-height: 1.7;">
                Not every name makes it to the global playlist.<br>
                Some never leave the local record shop.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")

    df = load_metrics()
    summary = load_summary()
    data_2023 = df[df["year"] == 2023]

    # ══════════════════════════════════════════════════════════════
    # SECTION 1: QUIZ — Integrated Record Shop Card
    # ══════════════════════════════════════════════════════════════

    # Pronunciation challenge data
    challenges = [
        {
            "name": "Sadhbh",
            "country": "🇮🇪 Ireland",
            "countryness": 8171,
            "actual": "SIVE (just one syllable!)",
            "hint": "Rhymes with a number between four and six.",
            "explain": "In Irish Gaelic, 'dh' and 'bh' are both silent between vowels. So Sa-dh-bh = just 'S' + 'ive'.",
            "audio_file": "sadhbh",
        },
        {
            "name": "Ngaire",
            "country": "🇳🇿 New Zealand",
            "countryness": 11270,
            "actual": "NY-ree",
            "hint": "The first two letters are actually one sound you already know.",
            "explain": "In Māori, 'Ng' is a single consonant — the same sound as the 'ng' in 'singing', but at the start.",
            "audio_file": "ngaire",
        },
        {
            "name": "Frédérique",
            "country": "🇨🇦 Canada",
            "countryness": 10588,
            "actual": "fray-day-REEK",
            "hint": "The accents aren't decorative — each one changes a vowel.",
            "explain": "In French, 'é' always sounds like 'ay'. Three é's = three 'ay' sounds: fray-day-reek.",
            "audio_file": "frederique",
        },
        {
            "name": "Caoimhín",
            "country": "🏴 N. Ireland",
            "countryness": 465,
            "actual": "KEE-veen",
            "hint": "You already know this name — just not in this spelling.",
            "explain": "It's literally 'Kevin' in Irish! 'Aoi' = 'ee', 'mh' = 'v', 'ín' = 'een'. Kevin → Kee-veen.",
            "audio_file": "caoimhin",
        },
        {
            "name": "Ffion",
            "country": "🏴󠁧󠁢󠁷󠁬󠁳󠁿 Wales",
            "countryness": 1761,
            "actual": "FEE-on",
            "hint": "In Welsh, one of these letters is lying to you.",
            "explain": "Welsh rule: 'ff' = English 'f' sound. A single 'f' in Welsh = English 'v' sound. So 'Ffion' = 'Fee-on'.",
            "audio_file": "ffion",
        },
    ]

    # Session state
    if "challenge_idx" not in st.session_state:
        st.session_state.challenge_idx = 0
    if "revealed" not in st.session_state:
        st.session_state.revealed = False
    if "show_hint" not in st.session_state:
        st.session_state.show_hint = False

    challenge = challenges[st.session_state.challenge_idx]

    # Pull values out to avoid f-string quote conflicts
    c_name = challenge["name"]
    c_country = challenge["country"]
    c_idx = st.session_state.challenge_idx + 1
    c_total = len(challenges)

    st.markdown(
        f"""
        <div style="background: linear-gradient(135deg, #EEF2FF, #E8F4FD, #F0FFF4); 
                    border-radius: 16px; padding: 40px 30px; margin-bottom: 20px;
                    border: 1px solid #E2E8F0;">
            <div style="text-align: center; margin-bottom: 28px;">
                <h2 style="font-size: 1.8em; font-weight: 800; color: #2D3748; margin: 0 0 10px 0;">
                    🎤 Can You Say This?
                </h2>
                <p style="font-size: 1.05em; color: #4A5568; max-width: 550px; margin: 0 auto; line-height: 1.6;">
                    These names are <strong>cultural passwords</strong> — if you can't say them, 
                    they'll never leave their home country. Give it a try!
                </p>
            </div>
            <div style="display: flex; align-items: center; justify-content: center; gap: 30px; flex-wrap: wrap;">
                <div style="flex-shrink: 0;">
                    <svg width="140" height="140" viewBox="0 0 140 140">
                        <circle cx="70" cy="70" r="66" fill="#2D3748" stroke="#4A5568" stroke-width="1"/>
                        <circle cx="70" cy="70" r="59" fill="none" stroke="#3D4A5C" stroke-width="0.5"/>
                        <circle cx="70" cy="70" r="53" fill="none" stroke="#354258" stroke-width="0.5"/>
                        <circle cx="70" cy="70" r="47" fill="none" stroke="#3D4A5C" stroke-width="0.5"/>
                        <circle cx="70" cy="70" r="41" fill="none" stroke="#354258" stroke-width="0.5"/>
                        <circle cx="70" cy="70" r="35" fill="none" stroke="#3D4A5C" stroke-width="0.5"/>
                        <circle cx="70" cy="70" r="29" fill="none" stroke="#354258" stroke-width="0.5"/>
                        <ellipse cx="52" cy="52" rx="20" ry="13" fill="rgba(255,255,255,0.04)" transform="rotate(-30 52 52)"/>
                        <circle cx="70" cy="70" r="22" fill="#7C9FD6" opacity="0.9"/>
                        <circle cx="70" cy="70" r="17" fill="none" stroke="#5A82BE" stroke-width="0.8"/>
                        <circle cx="70" cy="70" r="13" fill="#2D3748"/>
                        <circle cx="70" cy="70" r="4" fill="#4A5568"/>
                        <circle cx="70" cy="70" r="2.5" fill="#2D3748"/>
                    </svg>
                </div>
                <div style="text-align: center; min-width: 200px;">
                    <div style="font-size: 0.7em; color: #718096; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 4px;">
                        SIDE {c_idx} OF {c_total}
                    </div>
                    <div style="font-size: 2.6em; font-weight: 800; color: #2D3748; font-family: Georgia, serif; margin: 6px 0;">
                        {c_name}
                    </div>
                    <div style="font-size: 0.95em; color: #4A5568; margin-top: 4px;">
                        {c_country}
                    </div>
                    <div style="background: rgba(124,159,214,0.12); border-radius: 8px; padding: 5px 12px; margin-top: 12px; display: inline-block; border: 1px solid rgba(124,159,214,0.25);">
                        <span style="font-size: 0.72em; color: #5A82BE; letter-spacing: 1px;">🎵 LOCAL VINYL RECORDS</span>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Buttons — full width
    col_hint, col_reveal, col_next = st.columns([1, 1, 1])

    with col_hint:
        if st.button("💡 Hint", use_container_width=True, key="btn_hint"):
            st.session_state.show_hint = True

    with col_reveal:
        if st.button("🔊 Reveal", use_container_width=True, key="btn_reveal"):
            st.session_state.revealed = True

    with col_next:
        if st.button("➡️ Next", use_container_width=True, key="btn_next"):
            st.session_state.challenge_idx = (st.session_state.challenge_idx + 1) % len(challenges)
            st.session_state.revealed = False
            st.session_state.show_hint = False
            st.rerun()

    # Hint display
    if st.session_state.get("show_hint"):
        st.info(f'💡 {challenge["hint"]}')

    # Progress dots
    dots = ""
    for i in range(len(challenges)):
        dots += "● " if i == st.session_state.challenge_idx else "○ "
    st.caption(dots)

    # Reveal section
    if st.session_state.revealed:
        c_actual = challenge["actual"]
        c_explain = challenge["explain"]
        c_countryness = challenge["countryness"]

        st.markdown(
            f"""
            <div style="background: linear-gradient(135deg, #F0FFF4, #E6FFF5); 
                        border: 2px solid #A8E6C8; border-radius: 12px;
                        padding: 18px; text-align: center; margin-top: 14px;">
                <div style="font-size: 0.75em; color: #059669; text-transform: uppercase; 
                            letter-spacing: 2px;">▶ Now Playing:</div>
                <div style="font-size: 1.8em; font-weight: 700; color: #059669; margin: 6px 0;">
                    "{c_actual}"
                </div>
                <div style="font-size: 0.85em; color: #4A5568; margin-top: 8px; 
                            background: rgba(6,214,160,0.08); border-radius: 6px; padding: 8px 12px;">
                    📖 {c_explain}
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # Audio playback
        audio_key = challenge.get("audio_file", challenge["name"].lower())
        audio_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "assets", "audio", f"{audio_key}.wav"
        )
        if os.path.exists(audio_path):
            with open(audio_path, "rb") as audio_file:
                audio_bytes = audio_file.read()
            st.audio(audio_bytes, format="audio/wav", autoplay=True)
        else:
            st.caption("🔈 Audio clip coming soon!")

        # Countryness fact
        st.markdown(
            f"""
            <div style="background: #FFF5F5; border-radius: 8px; padding: 10px; 
                        margin-top: 10px; text-align: center; font-size: 0.9em;">
                <span style="color: #e63946; font-weight: 600;">
                    Countryness: {c_countryness:,}
                </span>
                <span style="color: #718096;"> — A name {c_countryness:,}x more popular in </span>
                <span style="font-weight: 600;">{c_country}</span>
                <span style="color: #718096;"> than anywhere else</span>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("---")

        # ══════════════════════════════════════════════════════════════
    # SECTION 2: WHAT STAYED IN THE SHOP
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 🏪 What Stayed in the Shop?")
    st.markdown(
        "Could you read all of those? Probably not — and that's the point. "
        "But before we explore *why*, we need a way to **measure** how locked a name is."
    )

    # ─── Formula + Classification side by side ────────────────────
    col_formula, col_class = st.columns([1, 1])

    with col_formula:
        st.markdown(
            """
            <div style="background: linear-gradient(135deg, #EEF2FF, #E8F4FD); 
                        border-radius: 12px; padding: 24px; margin: 0;
                        border: 1px solid #E2E8F0; text-align: center; height: 100%;">
                <div style="font-size: 0.7em; color: #7C9FD6; text-transform: uppercase; 
                            letter-spacing: 2px; margin-bottom: 8px;">HOW WE MEASURED IT</div>
                <div style="font-size: 1.4em; font-weight: 800; color: #2D3748; margin-bottom: 4px;">
                    The Countryness Score
                </div>
                <div style="font-size: 0.88em; color: #4A5568; margin-bottom: 12px; font-style: italic;">
                    How many times more popular is this name at <strong>home</strong> vs <strong>abroad</strong>?
                </div>
                <div style="background: white; border-radius: 8px; padding: 14px; margin: 10px auto;
                            max-width: 400px; border: 1px solid #E2E8F0;">
                    <div style="font-size: 0.95em; color: #7C9FD6; font-family: 'Courier New', monospace;
                                border-bottom: 2px solid #2D3748; padding-bottom: 8px; margin-bottom: 8px;">
                        proportion in top country
                    </div>
                    <div style="font-size: 0.95em; color: #718096; font-family: 'Courier New', monospace;">
                        avg proportion in other countries
                    </div>
                </div>
                <div style="background: rgba(124,159,214,0.08); border-radius: 8px; padding: 10px; 
                            margin: 12px auto 0; max-width: 400px; text-align: left;">
                    <div style="font-size: 0.8em; color: #4A5568; line-height: 1.5;">
                        <strong style="color: #7C9FD6;">Proportion</strong> = how many babies out of ALL babies 
                        born that year got this name.<br>
                        <span style="color: #718096;">e.g., 2,450 Niamhs out of 100,000 Irish babies = <strong>0.0245</strong> (or 2.45%)</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col_class:
        st.markdown("#### How We Classified Them")
        st.markdown("Not all locked names are locked equally:")
        st.markdown(
            """
            <div style="margin: 8px 0;">
                <table style="width: 100%; border-collapse: collapse; font-size: 0.85em;">
                    <thead>
                        <tr style="border-bottom: 2px solid #E2E8F0;">
                            <th style="text-align: left; padding: 9px 6px; color: #4A5568;">Label</th>
                            <th style="text-align: left; padding: 9px 6px; color: #4A5568;">Score</th>
                            <th style="text-align: left; padding: 9px 6px; color: #4A5568;">Meaning</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #F0FFF4;">
                            <td style="padding: 9px 6px; font-weight: 600; color: #059669;">✅ Global</td>
                            <td style="padding: 9px 6px; color: #4A5568;">< 5</td>
                            <td style="padding: 9px 6px; color: #4A5568;">Shared — no single home</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #FFFFF0;">
                            <td style="padding: 9px 6px; font-weight: 600; color: #B7791F;">⚠️ Leaning</td>
                            <td style="padding: 9px 6px; color: #4A5568;">5 – 10</td>
                            <td style="padding: 9px 6px; color: #4A5568;">Concentrating in one place</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #FFF5F5;">
                            <td style="padding: 9px 6px; font-weight: 600; color: #C53030;">🔒 Locked</td>
                            <td style="padding: 9px 6px; color: #4A5568;">10 – 100</td>
                            <td style="padding: 9px 6px; color: #4A5568;">Clearly belongs to one country</td>
                        </tr>
                        <tr style="border-bottom: 1px solid #E2E8F0; background: #FFF0F0;">
                            <td style="padding: 9px 6px; font-weight: 600; color: #9B2C2C;">🔐 Very Locked</td>
                            <td style="padding: 9px 6px; color: #4A5568;">100 – 1,000</td>
                            <td style="padding: 9px 6px; color: #4A5568;">Barely exists elsewhere</td>
                        </tr>
                        <tr style="background: #FFE8E8;">
                            <td style="padding: 9px 6px; font-weight: 600; color: #742A2A;">🚫 Extreme</td>
                            <td style="padding: 9px 6px; color: #4A5568;">1,000+</td>
                            <td style="padding: 9px 6px; color: #4A5568;">A cultural password</td>
                        </tr>
                    </tbody>
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # ─── Paragraph explanation (full width below) ─────────────────
    st.markdown(
        """
        <div style="font-size: 0.92em; color: #4A5568; line-height: 1.7; margin: 12px 0 16px 0;">
            <p style="margin: 0 0 8px 0;">A score below <strong>5</strong> means a name is genuinely shared — it's roughly equally popular 
            across all countries. Think <em>Liam</em>, <em>Thomas</em>, <em>Emily</em>. No single country owns them.</p>
            <p style="margin: 0 0 8px 0;">Once a name crosses <strong>5</strong>, something shifts. Over <strong>62%</strong> of all babies with that name 
            are concentrated in a single country. It's no longer shared — it's <em>leaning</em>.</p>
            <p style="margin: 0 0 8px 0;">By the time you hit <strong>50–100</strong>, nearly <strong>88%</strong> of the name's usage is in one place. 
            These names — like <em>Siobhan</em> or <em>Conor</em> — are clearly Irish, clearly Scottish, clearly somewhere specific.</p>
            <p style="margin: 0 0 8px 0;">And at <strong>1,000+</strong>? Over <strong>97%</strong> of all babies with that name live in one country. 
            These are cultural passwords — names like <em>Narelle</em> (Australia) or <em>Sadhbh</em> (Ireland) 
            that effectively don't exist anywhere else on Earth.</p>
            <p style="margin: 0;">We drew the line at <strong>5</strong> because that's the tipping point: 
            below it, a name belongs to everyone. Above it, one country <strong>owns</strong> it.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ─── See it in action: Staircase Cards ────────────────────────
    st.markdown("#### See it in action:")

    staircase = [
        ("Liam", "Scotland", "1.84%", "0.66%", "2.8", "✅ Global", "#059669", "#F0FFF4"),
        ("Joseph", "USA", "4.80%", "0.96%", "5", "⚠️ Leaning", "#B7791F", "#FFFFF0"),
        ("Siobhan", "Ireland", "0.14%", "0.002%", "71", "🔒 Locked", "#C53030", "#FFF5F5"),
        ("Innes", "Scotland", "0.22%", "0.00026%", "861", "🔐 Very Locked", "#9B2C2C", "#FFF0F0"),
        ("Narelle", "Australia", "0.05%", "0.00001%", "4,738", "🚫 Extreme", "#742A2A", "#FFE8E8"),
    ]

    staircase_html = '<div style="display: flex; gap: 8px; flex-wrap: wrap; margin: 12px 0;">'
    for s_name, s_country, s_home, s_abroad, s_score, s_verdict, s_color, s_bg in staircase:
        staircase_html += (
            '<div style="flex: 1; min-width: 140px; background: ' + s_bg + ';'
            ' border: 2px solid ' + s_color + '40; border-radius: 10px;'
            ' padding: 14px 10px; text-align: center;">'
            '<div style="font-size: 0.65em; color: ' + s_color + '; text-transform: uppercase;'
            ' letter-spacing: 1.5px; font-weight: 600;">' + s_verdict + '</div>'
            '<div style="font-size: 1.3em; font-weight: 800; color: #2D3748; margin: 6px 0;">'
            + s_name + '</div>'
            '<div style="font-size: 0.7em; color: #718096; margin-bottom: 8px;">' + s_country + '</div>'
            '<div style="font-size: 2em; font-weight: 800; color: ' + s_color + ';">'
            + s_score + '</div>'
            '<div style="font-size: 0.6em; color: #718096; margin-top: 4px; font-family: monospace;">'
            + s_home + ' ÷ ' + s_abroad + '</div>'
            '</div>'
        )
    staircase_html += '</div>'
    st.markdown(staircase_html, unsafe_allow_html=True)

    # ─── The Local Collection: CD Cases (HTML) ────────────────────
    st.markdown("#### 🎵 The Local Collection")
    st.markdown("So in 2023, how much of each country's naming culture is locked?")

    tapes = [
        ("Northern Ireland", "65%", "#9FE6C8", ["Éireann", "Roisé", "Dáithí", "Ruadhán", "Cianán"]),
        ("Ireland", "55%", "#A8E6C8", ["Naoise", "Sadhbh", "Iarla", "Laoise", "Aoibhínn"]),
        ("Scotland", "52%", "#C8A8E8", ["Innes", "Ruairidh", "Munro", "Murdo", "Breagha"]),
        ("USA", "44%", "#A8D8F0", ["Kaylani", "Anahi", "Tadeo", "Itzel", "Malani"]),
        ("Canada", "36%", "#F5B7C5", ["Édouard", "Éloi", "Ludovic", "Frédérique", "Noélie"]),
        ("New Zealand", "36%", "#C8A8E8", ["Kauri", "Manaia", "Ardie", "Nikau", "Amarni"]),
        ("England & Wales", "35%", "#F5D68A", ["Barney", "Isla-rose", "Delilah-rose", "Tommy-lee", "Ffion"]),
        ("Australia", "23%", "#F5C878", ["Darcy", "Pippa", "Billie", "Harvey", "Matilda"]),
    ]

    tape_html = '<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; margin: 16px 0;">'

    for t_country, t_pct, t_color, t_names in tapes:
        tracks = ""
        for i, n in enumerate(t_names):
            tracks += '<div style="font-size: 0.8em; color: #4A5568; padding: 2px 0;">' + str(i + 1) + ". " + n + "</div>"

        tape_html += (
            # Outer case
            '<div style="background: linear-gradient(145deg, ' + t_color + '35, ' + t_color + '20); border-radius: 6px;'
            ' padding: 0; overflow: hidden; border: 1px solid ' + t_color + '60;'
            ' box-shadow: 0 4px 12px rgba(0,0,0,0.12), inset 0 1px 0 rgba(255,255,255,0.05);'
            ' position: relative;">'
            # Spine
            '<div style="position: absolute; left: 0; top: 0; bottom: 0; width: 7px;'
            ' background: ' + t_color + ';'
            ' box-shadow: 1px 0 4px rgba(0,0,0,0.4);"></div>'
            # Top section
            '<div style="padding: 14px 14px 10px 22px; border-bottom: 1px solid ' + t_color + '40;'
            ' position: relative; min-height: 60px;">'
            # Cassette icon (top right)
            '<div style="position: absolute; top: 10px; right: 12px;">'
            '<svg width="52" height="36" viewBox="0 0 52 36">'
            '<rect x="1" y="1" width="50" height="34" rx="4" fill="#2D3748" stroke="#4A5568" stroke-width="1.5"/>'
            '<rect x="8" y="6" width="36" height="16" rx="2" fill="#1A202C" stroke="#4A5568" stroke-width="0.8"/>'
            '<circle cx="18" cy="14" r="5" fill="none" stroke="' + t_color + '" stroke-width="1.5"/>'
            '<circle cx="34" cy="14" r="5" fill="none" stroke="' + t_color + '" stroke-width="1.5"/>'
            '<circle cx="18" cy="14" r="1.5" fill="' + t_color + '"/>'
            '<circle cx="34" cy="14" r="1.5" fill="' + t_color + '"/>'
            '<line x1="23" y1="14" x2="29" y2="14" stroke="#4A5568" stroke-width="0.8"/>'
            '<rect x="12" y="25" width="28" height="6" rx="1" fill="#4A5568"/>'
            '</svg>'
            '</div>'
            # Country title
            '<div style="font-weight: 700; font-size: 0.9em; color: #2D3748;">'
            + t_country +
            "</div>"
            '<div style="font-size: 0.72em; color: #4A5568; margin-top: 3px; font-weight: 600;">'
            + t_pct + ' locked'
            "</div>"
            "</div>"
            # Track listing
            '<div style="padding: 10px 14px 12px 22px; background: ' + t_color + '15;">'
            '<div style="font-size: 0.6em; color: #718096; text-transform: uppercase;'
            ' letter-spacing: 1.5px; margin-bottom: 5px; font-weight: 600;">TRACKLIST</div>'
            + tracks +
            "</div>"
            "</div>"
        )

    tape_html += "</div>"
    st.markdown(tape_html, unsafe_allow_html=True)

    st.markdown(
        "So **why** do these names stay locked? We found four forces keeping them home:"
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # SECTION 3: REASONS WHY
    # ══════════════════════════════════════════════════════════════

    # ─── Reason 1: Pronunciation Wall ─────────────────────────────
    st.markdown("### 🗣️ Reason 1: The Pronunciation Wall")
    st.markdown(
        "The most powerful predictor of whether a name stays locked is simple: "
        "**can outsiders read it?**"
    )

    # Declan vs Niamh
    st.markdown("#### Two Irish Names. Two Fates.")

    col_dec, col_niamh = st.columns(2)
    with col_dec:
        st.markdown(
            """
            <div style="background: #E8F4FD; border: 2px solid #A8E6C8; border-radius: 12px;
                        padding: 20px; text-align: center;">
                <div style="font-size: 2em; font-weight: 800; color: #4A5568;">Declan</div>
                <div style="font-size: 0.9em; color: #718096; margin: 4px 0;">"DECK-lin" ✅ Easy to read</div>
                <div style="font-size: 2.5em; font-weight: 800; color: #A8E6C8; margin: 8px 0;">2.5</div>
                <div style="font-size: 0.85em; color: #718096;">countryness → Gone global</div>
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
                <div style="font-size: 0.9em; color: #718096; margin: 4px 0;">"NEEV" ❌ Impossible to guess</div>
                <div style="font-size: 2.5em; font-weight: 800; color: #F5B7C5; margin: 8px 0;">28</div>
                <div style="font-size: 0.85em; color: #718096;">countryness → Stayed home</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    # Orthographic complexity
    st.markdown("#### It's Not Just Sound — It's How It LOOKS")
    st.markdown(
        "If a name *looks* impossible on paper, parents in other countries won't even attempt it. "
        "The letter-to-sound mismatch creates a visual wall:"
    )

    complexity_data = {
        "Name": ["Liam", "Declan", "Niamh", "Sadhbh", "Caoilfhionn"],
        "Letters": [4, 6, 5, 6, 11],
        "Actual Sounds": [4, 6, 3, 3, 5],
        "Mismatch": ["None — what you see is what you say", "None — readable", "5 letters → 3 sounds", "6 letters → 3 sounds!", "11 letters → 5 sounds!!"],
        "Countryness": [1.5, 2.5, 28, 905, 2974],
        "Fate": ["🌍 Global", "🌍 Global", "🏠 Locked", "🔒 Very locked", "🔒 Extremely locked"],
    }
    st.dataframe(complexity_data, use_container_width=True, hide_index=True)

    st.markdown(
        """
        **The pattern:** Names where letters = sounds (Liam, Declan) go global.
        Names where letters ≠ sounds (Sadhbh, Caoilfhionn) stay locked.
        The bigger the mismatch, the higher the countryness.
        """
    )

    # Name length vs countryness
    st.markdown("#### Longer Names = More Locked")

    fig_length = go.Figure()
    fig_length.add_trace(go.Bar(
        x=["3-4 letters", "5-6 letters", "7-8 letters", "9-10 letters", "11+ letters"],
        y=[64, 81, 82, 122, 205],
        marker_color=["#A8E6C8", "#A8D8F0", "#F5D68A", "#F5C878", "#F5B7C5"],
        text=["64", "81", "82", "122", "205"],
        textposition="outside",
        textfont=dict(size=13, color="#4A5568"),
    ))
    fig_length.update_layout(
        **CHART_LAYOUT,
        title=None,
        yaxis_title="Avg Countryness Score",
        xaxis_title="Name Length",
        height=350,
        showlegend=False,
    )
    st.plotly_chart(fig_length, use_container_width=True)

    st.info(
        "💡 Names with 11+ letters have **3x higher countryness** than short names. "
        "Complexity = barrier."
    )

    st.markdown("---")

    # ─── Reason 2: Culture & Tradition ────────────────────────────
    st.markdown("### ✝️ Reason 2: Culture & Tradition")
    st.markdown(
        "Even when a name has a perfectly pronounceable equivalent in English, "
        "communities choose the **local form** — because the form IS the identity."
    )

    # Patrick vs Pádraig
    st.markdown("#### Same Saint. Different Name. Different Fate.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div style="background: #F0F8FF; border-radius: 10px; padding: 16px; text-align: center;">
                <div style="color: #A8E6C8; font-size: 0.8em; font-weight: 600;">GLOBAL VERSION</div>
                <div style="font-size: 1.4em; font-weight: 700; margin: 6px 0;">Patrick</div>
                <div style="font-size: 1.8em; font-weight: 800; color: #A8E6C8;">~2</div>
                <div style="color: #718096; font-size: 0.8em;">countryness — everywhere</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div style="text-align: center; padding-top: 25px;">
                <div style="font-size: 2.5em;">⚡</div>
                <div style="font-size: 0.85em; color: #718096; margin-top: 4px;">Same person.<br>Same meaning.<br>Different identity.</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div style="background: #FFF5F5; border-radius: 10px; padding: 16px; text-align: center;">
                <div style="color: #F5B7C5; font-size: 0.8em; font-weight: 600;">LOCAL VERSION</div>
                <div style="font-size: 1.4em; font-weight: 700; margin: 6px 0;">Pádraig</div>
                <div style="font-size: 1.8em; font-weight: 800; color: #F5B7C5;">343</div>
                <div style="color: #718096; font-size: 0.8em;">countryness — locked in Ireland</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown("")

    more_saints = {
        "English (Global)": ["Patrick (~2)", "Kieran (1.4)", "Brendan (4.7)", "Bridget (~3)"],
        "Gaelic (Locked)": ["Pádraig (343)", "Ciarán (24)", "Breandán (—)", "Brigid (6)"],
    }
    st.dataframe(more_saints, use_container_width=True, hide_index=True)

    st.markdown(
        "**Choosing Pádraig over Patrick is a cultural statement.** "
        "It says: *I belong to this place, this language, this tradition.* "
        "The pronunciation wall is real — but sometimes staying locked is a **choice**."
    )

    st.markdown("---")

    # ─── Reason 3: Political Identity ─────────────────────────────
    st.markdown("### 🏴 Reason 3: Political Identity")
    st.markdown(
        "If pronunciation and tradition were the only factors, all Celtic countries "
        "would behave the same. But they don't. Look at **Northern Ireland vs Ireland**:"
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

    st.info(
        "💡 **Same Gaelic heritage. Opposite response.** In Northern Ireland, "
        "naming a child in Gaelic is tied to the Irish language movement and "
        "post-Troubles cultural identity. It's not just tradition — it's a political act."
    )

    st.markdown("---")

    # ─── Reason 4: Active Cultural Revival ────────────────────────
    st.markdown("### 📜 Reason 4: Active Cultural Revival")
    st.markdown(
        "It's not just old names surviving — communities are actively **inventing** "
        "brand-new names designed to never leave."
    )

    revival_data = {
        "Name": ["Iarla", "Siún", "Cadain", "Siomha", "Caragh", "Aibhlinn", "Bradan", "Breagha", "Doireann", "Saorla"],
        "First Appeared": [2015, 2013, 2017, 2017, 2021, 2018, 2016, 2018, 2020, 2012],
        "Country": ["Ireland", "Ireland", "N. Ireland", "Ireland", "Ireland", "N. Ireland", "N. Ireland", "Scotland", "Ireland", "N. Ireland"],
        "Countryness": [815, 713, 702, 547, 532, 465, 458, 446, 422, 374],
    }
    st.dataframe(revival_data, use_container_width=True, hide_index=True)

    st.markdown(
        "**85 brand-new high-identity Celtic names** created since 2010. "
        "None of these existed in the data before — they're freshly minted "
        "cultural markers, designed with Gaelic orthography that outsiders can't read."
    )

    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # SECTION 4: DATA FACTS
    # ══════════════════════════════════════════════════════════════

    st.markdown("### 📊 The Numbers Behind the Wall")

    # 3.2% vs 30.2% chart
    st.markdown("#### Gaelic Spelling = Cultural Lock")

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
        title="% of Names with Gaelic Orthography (bh, dh, gh, mh, aoi)",
        yaxis_title="Percentage",
        height=350,
        showlegend=False,
    )
    st.plotly_chart(fig_gaelic, use_container_width=True)

    st.markdown(
        "Of **126** Irish names that escaped to other countries, only **3.2%** had Gaelic spelling. "
        "Of **86** that stayed locked, **30.2%** did. A **10x difference** — and a **7.4x cultural lock factor**."
    )

    # Three borders table
    st.markdown("#### Three Linguistic Borders Within One Language")
    border_data = {
        "Border": ["🟣 Gaelic ↔ Anglophone", "🔵 Francophone ↔ Anglophone", "🟢 Hispanic ↔ Anglophone"],
        "Locked (can't cross)": ["Sadhbh, Caoilfhionn, Niamh, Aoife", "Frédérique, Océanne, Laurianne", "Almost none!"],
        "Escaped (crossed)": ["Declan, Ronan, Connor, Liam", "Very few escape", "Santiago, Diego, Carlos, Isabella"],
        "Wall Strength": ["Hard wall 🧱 (7.4x lock)", "Hard wall but fading 📉 (−79% since 1997)", "No wall! 🌍 (phonetically accessible)"],
    }
    st.dataframe(border_data, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Culture > Geography
    st.markdown("#### Culture > Geography")
    st.markdown(
        "If distance were the barrier, Australia would be the most distinct. "
        "It's not. **Cultural tradition trumps physical isolation.**"
    )

    country_cn = data_2023.groupby("max_country")["countryness"].mean().sort_values(ascending=True).reset_index()

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
        title="Avg Countryness by Country (2023)",
        height=350,
        xaxis_title="Avg Countryness Score (Higher = More Distinct)",
    )
    st.plotly_chart(fig_geo, use_container_width=True)

    st.info(
        "💡 **Ireland** (right next to the UK) remains 5x more distinct than **Australia** "
        "(on the other side of the planet but culturally connected via media). "
        "A non-English linguistic tradition matters more than distance."
    )
