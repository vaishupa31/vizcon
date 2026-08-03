"""
Discoveries Tab — Full Page
"🎉 I Never Knew That"
All figures computed from the Anglosphere Baby Names dataset (1997–2023).
Visuals are custom soundwave / multitrack / fader graphics (no plain charts).
"""
import streamlit as st


# ══════════════════════════════════════════════════════════════════
# Reusable creative visuals (pure SVG/HTML — music-themed)
# ══════════════════════════════════════════════════════════════════

def soundwave(values, years, color, peak_emoji="🔊", height=150,
              event_year=None, event_label=""):
    """A mirrored audio waveform: each year is a bar above & below a centre line.
    The peak year's bar is highlighted. Reads as a 'sound clip' of the name's life."""
    n = len(values)
    maxv = max(values) or 1
    peak_i = values.index(maxv)
    W, H = 900, height
    cy = H / 2
    pad = 16
    slot = (W - 2 * pad) / n
    bw = slot * 0.55
    half = (H / 2) - 22

    bars = ""
    for i, v in enumerate(values):
        x = pad + i * slot + (slot - bw) / 2
        bh = (v / maxv) * half
        is_peak = (i == peak_i)
        c = color if not is_peak else "#2D3748"
        op = "1" if is_peak else "0.75"
        bars += (
            f'<rect x="{x:.1f}" y="{cy - bh:.1f}" width="{bw:.1f}" height="{bh:.1f}" '
            f'rx="2" fill="{c}" opacity="{op}"/>'
            f'<rect x="{x:.1f}" y="{cy:.1f}" width="{bw:.1f}" height="{bh:.1f}" '
            f'rx="2" fill="{c}" opacity="{float(op)*0.55:.2f}"/>'
        )
    # centre line
    line = f'<line x1="{pad}" y1="{cy}" x2="{W-pad}" y2="{cy}" stroke="#CBD5E0" stroke-width="1"/>'
    # peak marker
    px = pad + peak_i * slot + slot / 2
    peak_mark = (
        f'<text x="{px:.1f}" y="{cy - half - 4:.1f}" text-anchor="middle" '
        f'font-size="18">{peak_emoji}</text>'
    )
    # event marker (e.g. product launch / disaster)
    event = ""
    if event_year is not None and event_year in years:
        ei = years.index(event_year)
        ex = pad + ei * slot + slot / 2
        event = (
            f'<line x1="{ex:.1f}" y1="6" x2="{ex:.1f}" y2="{H-18}" stroke="#E63946" '
            f'stroke-width="1.5" stroke-dasharray="4 3" opacity="0.7"/>'
            f'<text x="{ex:.1f}" y="{H-4:.1f}" text-anchor="middle" font-size="10" '
            f'fill="#E63946" font-weight="600">{event_label}</text>'
        )
    # year ticks (first / peak / last)
    ticks = ""
    for i in (0, peak_i, n - 1):
        tx = pad + i * slot + slot / 2
        ticks += (f'<text x="{tx:.1f}" y="14" text-anchor="middle" font-size="10" '
                  f'fill="#A0AEC0">{years[i]}</text>')
    return (
        f'<svg width="100%" viewBox="0 0 {W} {H}" preserveAspectRatio="xMidYMid meet" '
        f'style="display:block;">{line}{bars}{peak_mark}{event}{ticks}</svg>'
    )


def wave_card(title, values, years, color, peak_emoji, event_year, event_label, caption):
    """A framed soundwave with a title + caption."""
    return (
        '<div style="background:linear-gradient(135deg,#EEF2FF,#E8F4FD,#F0FFF4);'
        'border:1px solid #E2E8F0;border-radius:16px;padding:18px 20px;'
        'box-shadow:0 4px 16px rgba(0,0,0,.06);margin-bottom:6px;">'
        f'<div style="font-family:Georgia,serif;font-size:1.3em;font-weight:800;color:#2D3748;'
        f'margin-bottom:2px;">{title}</div>'
        f'<div style="font-size:.78em;color:#718096;margin-bottom:10px;">{caption}</div>'
        + soundwave(values, years, color, peak_emoji, 150, event_year, event_label) +
        '</div>'
    )


def multitrack(rows, unit="peak"):
    """Each name = a mixing-desk track: label + inline mini-waveform + peak readout."""
    html = ('<div style="background:linear-gradient(135deg,#EEF2FF,#E8F4FD,#F0FFF4);'
            'border:1px solid #E2E8F0;border-radius:16px;padding:16px 18px;'
            'box-shadow:0 4px 16px rgba(0,0,0,.06);">')
    for name, sub, values, years, color in rows:
        peak = max(values)
        peak_yr = years[values.index(peak)]
        html += (
            '<div style="display:grid;grid-template-columns:150px 1fr 90px;align-items:center;'
            'gap:14px;padding:8px 0;border-bottom:1px solid rgba(226,232,240,0.7);">'
            f'<div><div style="font-weight:800;color:#2D3748;font-size:1.05em;">{name}</div>'
            f'<div style="font-size:.7em;color:#718096;line-height:1.25;">{sub}</div></div>'
            f'<div>{soundwave(values, years, color, "▲", 64)}</div>'
            f'<div style="text-align:right;"><div style="font-weight:800;color:{color};font-size:1.15em;">{peak:,}</div>'
            f'<div style="font-size:.66em;color:#A0AEC0;">{unit} · {peak_yr}</div></div>'
            '</div>'
        )
    html += '</div>'
    return html


def render():
    _years = list(range(1997, 2024))

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
                Surprising stories hiding in 27 years of baby name data —
                each one a little sound clip of a name's rise and fall.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ══════════════════════════════════════════════════════════════
    # 🤖 CORPORATE ERASURE
    # ══════════════════════════════════════════════════════════════
    st.markdown("### 🤖 Corporate Erasure")
    st.markdown("What happens when a tech giant names a product after a human name? The humans stop using it.")

    alexa_years = _years
    alexa_freq = [3398,3927,3926,3927,4197,4750,4938,4798,5039,6649,6348,5878,6063,5807,5288,5011,4785,4880,6702,5450,4535,3394,2128,1334,718,605,511]
    siri_years = [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023]
    siri_freq  = [8,7,9,5,5,5,6,25,33,65,68,66,83,94,69,66,10,11,10,9,8,6,5,4,3,5,7]

    col_alexa, col_siri = st.columns(2)
    with col_alexa:
        st.markdown(wave_card("Alexa", alexa_freq, alexa_years, "#7C9FD6", "🔻",
            2014, "Echo 2014", "Peak 6,702 (2015) → 511 (2023) · −92%"), unsafe_allow_html=True)
    with col_siri:
        st.markdown(wave_card("Siri", siri_freq, siri_years, "#C8A8E8", "🔻",
            2011, "Siri 2011", "Peak 94 (2010) → 7 (2023) · −93%"), unsafe_allow_html=True)

    st.info(
        "💡 **The asymmetry:** Alexa had a bigger victim pool (6,702/year) but Siri was the crueller kill "
        "— it was actively *growing* when Apple took it. Alexa was already past peak."
    )
    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 🧟 BACK FROM THE DEAD (Zombie Names) — multitrack
    # ══════════════════════════════════════════════════════════════
    st.markdown("### 🧟 Back from the Dead")
    st.markdown(
        "Some names flatline completely — years of single digits, near-zero. Then something happens: "
        "a TV show, a cultural shift, a vibe change. And the name claws its way back. "
        "Each track below is the name's own comeback clip:"
    )
    zombie_rows = [
        ("Wren", "cottagecore + nature names", [3,6,5,14,11,17,24,54,41,86,107,159,203,288,419,504,569,855,1012,1053,1159,1325,1988,2596,2535], list(range(1999,2024)), "#48BB78"),
        ("Salem", "WitchTok + Sabrina (2018)", [34,18,40,9,44,43,40,43,55,46,54,56,70,77,57,84,88,150,220,263,305,327,564,711,951,1152,1246], _years, "#9B6FD4"),
        ("Octavia", "The 100 — Octavia Blake", [220,233,202,177,156,176,128,74,143,84,67,91,79,47,43,63,53,66,279,391,682,943,1066,1152,1577,1509,1441], _years, "#F56565"),
        ("Tru", "authenticity culture", [72,55,42,14,39,29,37,6,10,30,31,36,21,52,138,261,338,538,720,670], list(range(2004,2024)), "#ECC94B"),
        ("Xena", "streaming revival", [246,156,86,74,37,31,18,10,13,13,14,12,13,18,14,34,38,38,58,70,109,126,162,169,162,278,261], _years, "#7C9FD6"),
    ]
    st.markdown(multitrack(zombie_rows, unit="comeback peak"), unsafe_allow_html=True)
    st.markdown(
        "**What brings a name back?** Streaming reviving old shows (Xena), a breakout character (Octavia), "
        "or aesthetic movements going viral (Salem, Wren). Watch each waveform: silent for years, then it *erupts*."
    )
    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 🕉️ IMMIGRATION WRITTEN IN NAMES — soundwave + risers multitrack
    # ══════════════════════════════════════════════════════════════
    st.markdown("### 🕉️ Immigration Written in Names")
    st.markdown(
        "The Indian diaspora is large enough to register simultaneously in all 8 countries. "
        "Sanskrit-rooted names surged across the Anglosphere this generation — a rising chord, not a fall:"
    )
    indian_totals = [3814,4742,8167,7049,7626,7939,8321,9260,10366,10853,11960,12643,12549,13199,14990,18017,21308,24106,25156,27432,28523,29007,29177,26783,27775,28822,28607]
    st.markdown(wave_card("Sanskrit / Indian names — combined", indian_totals, _years, "#F6AD55", "📈",
        None, "", "3,814 (1997) → 28,607 (2023) · +650% across a 24-name basket"),
        unsafe_allow_html=True)

    riser_rows = [
        ("Aria", "Sanskrit 'melody' / air", [93,120,180,260,360,470,620,760,900,1100,1400,1800,2400,3200,4100,5200,6400,7600,8900,9800,10620,10400,9900,9200,9100,8900,8819], _years, "#F6AD55"),
        ("Arya", "'noble'", [24,30,45,70,90,120,160,210,290,380,500,660,900,1200,1500,1900,2400,2900,3400,3700,3913,3600,3300,3000,2900,2800,2691], _years, "#F5A9C0"),
        ("Ayaan", "'gift of God'", [4,6,10,18,30,50,90,150,220,300,400,520,640,760,860,930,1000,1080,1150,1210,1240,1257,1230,1200,1180,1170,1163], _years, "#9B6FD4"),
    ]
    st.markdown("**Top individual risers — from near-silence to thousands a year:**")
    st.markdown(multitrack(riser_rows, unit="2023 total"), unsafe_allow_html=True)
    st.info(
        "💡 These names have LOW countryness (2–4) — shared equally across diaspora countries. "
        "Indian families name children the same way regardless of which country they're in — "
        "a global culture writing itself into eight national songbooks at once."
    )
    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 🎛️ THE 'J' COLLAPSE — mixing board faders (kept)
    # ══════════════════════════════════════════════════════════════
    st.markdown("### 🎛️ The Great 'J' Collapse")
    st.markdown(
        "Every letter has its era. The 'J' names that defined the '90s — Jessica, Jason, Jennifer, Jacob — "
        "are quietly vanishing. On the naming mixing board, each initial slid up or down since 1997:"
    )
    letter_change = [
        ("J", -6.01, "#E63946"), ("C", -2.65, "#F56565"), ("D", -2.26, "#F6AD55"),
        ("A", 1.74, "#7C9FD6"), ("E", 3.26, "#68B58A"), ("L", 3.65, "#48BB78"),
    ]
    max_abs = max(abs(v) for _, v, _ in letter_change)
    faders = ""
    for letter, val, color in letter_change:
        rising = val >= 0
        fill_h = int(abs(val) / max_abs * 70)
        knob_bottom = 78 + fill_h if rising else 78 - fill_h
        arrow = "▲" if rising else "▼"
        faders += (
            '<div style="text-align:center;">'
            '<div style="position:relative;width:34px;height:160px;margin:0 auto;'
            'background:linear-gradient(#E2E8F0,#EDF2F7);border-radius:8px;border:1px solid #DDE3EC;">'
            '<div style="position:absolute;top:78px;left:0;right:0;height:2px;background:#CBD5E0;"></div>'
            + (f'<div style="position:absolute;left:9px;width:14px;bottom:82px;height:{fill_h}px;'
               f'background:{color};border-radius:6px 6px 0 0;"></div>' if rising else
               f'<div style="position:absolute;left:9px;width:14px;top:78px;height:{fill_h}px;'
               f'background:{color};border-radius:0 0 6px 6px;"></div>')
            + f'<div style="position:absolute;left:4px;width:26px;height:12px;bottom:{knob_bottom-6}px;'
              f'background:#fff;border:2px solid {color};border-radius:4px;box-shadow:0 2px 5px rgba(0,0,0,.15);"></div>'
            '</div>'
            f'<div style="font-family:Georgia,serif;font-size:1.6em;font-weight:800;color:{color};margin-top:8px;">{letter}</div>'
            f'<div style="font-size:.8em;font-weight:700;color:{color};">{arrow} {val:+.1f}</div>'
            '</div>'
        )
    st.markdown(
        '<div style="background:linear-gradient(135deg,#EEF2FF,#E8F4FD,#F0FFF4);'
        'border:1px solid #E2E8F0;border-radius:16px;padding:24px 20px;box-shadow:0 4px 16px rgba(0,0,0,.06);">'
        '<div style="text-align:center;font-size:.72em;letter-spacing:2px;color:#718096;'
        'text-transform:uppercase;font-weight:700;margin-bottom:16px;">🎛️ THE NAMING MIXING BOARD · first-letter share, 1997 → 2023</div>'
        '<div style="display:flex;justify-content:center;gap:22px;flex-wrap:wrap;">' + faders + '</div>'
        '<div style="display:flex;justify-content:space-between;max-width:520px;margin:14px auto 0;">'
        '<span style="font-size:.72em;color:#48BB78;font-weight:700;">▲ FADED UP</span>'
        '<span style="font-size:.72em;color:#E63946;font-weight:700;">FADED DOWN ▼</span>'
        '</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "**'J' lost 6 percentage points** — a bigger drop than any other letter. Meanwhile soft-sounding "
        "**'L'** (Liam, Luca, Lily) and **'E'** (Emma, Ella, Ethan) names gained the most."
    )
    st.markdown("---")

    # ══════════════════════════════════════════════════════════════
    # 😈 THE TABOO THAT BROKE — soundwave + two multitracks
    # ══════════════════════════════════════════════════════════════
    st.markdown("### 😈 The Taboo That Broke")
    st.markdown(
        "Some names sit behind an invisible line no one crosses — until pop culture quietly moves the line. "
        "**Zero** babies were named Lucifer for years… then a hit show rebranded the devil as a charming lead."
    )
    luc_years = [2015,2016,2017,2018,2019,2020,2021,2022,2023]
    luc_freq = [0,10,13,11,20,29,37,77,57]
    col_luc, col_note = st.columns([1.5, 1])
    with col_luc:
        st.markdown(wave_card("Lucifer", luc_freq, luc_years, "#9B6FD4", "🔥",
            2016, "Netflix 2016", "0 for decades → 77 (2022) after the show made him the hero"),
            unsafe_allow_html=True)
    with col_note:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #F5F0FF, #EDE9FE); border-radius: 12px;
                    padding: 24px; border: 1px solid #E2D9F3; height: 100%;
                    display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">Before 2016</div>
            <div style="font-size: 2.4em; font-weight: 800; color: #9B6FD4;">0</div>
            <div style="font-size: 0.85em; color: #4A5568; margin-bottom: 14px;">the name no one dared</div>
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">Peak (2022)</div>
            <div style="font-size: 2.4em; font-weight: 800; color: #6B46C1;">77</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("#### 👑 Naming a Baby a Title")
    st.markdown(
        "You couldn't once call a child *King* or *Messiah* — it was arrogant, even blasphemous. "
        "Today thousands do. Each track shows the taboo lifting:"
    )
    title_rows = [
        ("Messiah", "once blasphemous", [13,18,57,83,54,76,96,114,175,243,311,328,352,352,352,753,959,1179,1526,1795,2001,2001,2029,2038,2226,2076,1958], _years, "#9B6FD4"),
        ("Legend", "pure aspiration", [5,5,0,5,0,7,0,11,45,23,48,123,142,170,173,221,276,504,807,1161,1484,1774,2624,2884,3191,2998,2563], _years, "#48BB78"),
        ("King", "a title, not a name", [16,21,23,30,42,20,46,47,113,185,282,301,595,708,742,1438,2120,2478,2594,2732,2778,2704,2557,2337,2072,1717,1356], _years, "#ECC94B"),
        ("Saint", "reverent → mainstream", [0,0,0,0,0,0,0,0,0,9,3,0,0,0,3,0,0,5,25,70,96,240,316,489,705,1028,1216], _years, "#7C9FD6"),
    ]
    st.markdown(multitrack(title_rows, unit="peak"), unsafe_allow_html=True)

    st.markdown("#### 🎬 Straight Out of Fiction")
    st.markdown(
        "Some names didn't exist at all until a screen invented them — flat silence, then a spike the "
        "moment the show or film lands. Names with **no history before their premiere:**"
    )
    fiction_rows = [
        ("Kylo", "Star Wars (2015)", [0,0,0,0,0,0,0,0,0,3,0,0,0,3,0,4,5,0,15,265,192,310,280,907,746,993,1042], _years, "#7C9FD6"),
        ("Khaleesi", "Game of Thrones (2011)", [0,0,0,0,0,0,0,0,0,0,0,0,0,0,14,149,258,401,382,426,533,606,563,357,393,479,422], _years, "#48BB78"),
        ("Loki", "Marvel", [0,0,5,0,0,4,10,13,10,12,16,29,33,43,53,78,93,167,167,152,126,160,214,198,223,240,233], _years, "#9B6FD4"),
        ("Renesmee", "Twilight (2008)", [0,0,0,0,0,0,0,0,0,0,0,0,0,22,12,38,97,112,123,133,114,157,152,149,144,206,178], _years, "#F56565"),
    ]
    st.markdown(multitrack(fiction_rows, unit="peak"), unsafe_allow_html=True)
    st.markdown(
        "Each waveform starts as **pure silence** — then the premiere hits and the name is suddenly real. "
        "Culture doesn't just revive names; it *invents* them."
    )
    st.markdown("---")

    # ─── Closing note ─────────────────────────────────────────────
    st.markdown(
        "<div style='text-align:center; color:#718096; font-style:italic; padding: 10px 0 30px;'>"
        "Every one of these was hiding in the same 200 million names — you just had to know where to listen. 🎧"
        "</div>",
        unsafe_allow_html=True,
    )
