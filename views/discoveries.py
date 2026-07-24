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

    # ─── Alexa & Siri line charts ─────────────────────────────────
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    # Data
    alexa_data = {
        "year": [1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022,2023],
        "frequency": [3398,3927,3926,3927,4197,4750,4938,4798,5039,6649,6348,5878,6063,5807,5288,5011,4785,4880,6702,5450,4535,3394,2128,1334,718,605,511]
    }

    siri_data = {
        "year": [1997,1998,1999,2000,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2017,2021,2023],
        "frequency": [8,7,9,5,6,25,33,65,68,66,83,94,69,66,10,11,8,3,3,7]
    }

    # Two side-by-side charts
    col_alexa, col_siri = st.columns(2)

    with col_alexa:
        fig_alexa = go.Figure()
        fig_alexa.add_trace(go.Scatter(
            x=alexa_data["year"],
            y=alexa_data["frequency"],
            mode="lines+markers",
            line=dict(color="#7C9FD6", width=3),
            marker=dict(size=5),
            fill="tozeroy",
            fillcolor="rgba(124,159,214,0.1)",
        ))
        # Add vertical line for Amazon Echo launch
        fig_alexa.add_vline(x=2014, line_dash="dash", line_color="#E63946", opacity=0.7)
        fig_alexa.add_annotation(
            x=2014, y=6702,
            text="Amazon Echo<br>launches",
            showarrow=True, arrowhead=2,
            font=dict(size=10, color="#E63946"),
            ax=40, ay=-30
        )
        fig_alexa.update_layout(
            **CHART_LAYOUT,
            title="Alexa",
            xaxis_title="",
            yaxis_title="Babies per year",
            height=350,
        )
        st.plotly_chart(fig_alexa, use_container_width=True)

    with col_siri:
        fig_siri = go.Figure()
        fig_siri.add_trace(go.Scatter(
            x=siri_data["year"],
            y=siri_data["frequency"],
            mode="lines+markers",
            line=dict(color="#C8A8E8", width=3),
            marker=dict(size=5),
            fill="tozeroy",
            fillcolor="rgba(200,168,232,0.1)",
        ))
        # Add vertical line for Apple Siri launch
        fig_siri.add_vline(x=2011, line_dash="dash", line_color="#E63946", opacity=0.7)
        fig_siri.add_annotation(
            x=2011, y=94,
            text="Apple launches<br>Siri",
            showarrow=True, arrowhead=2,
            font=dict(size=10, color="#E63946"),
            ax=40, ay=-30
        )
        fig_siri.update_layout(
            **CHART_LAYOUT,
            title="Siri",
            xaxis_title="",
            yaxis_title="Babies per year",
            height=350,
        )
        st.plotly_chart(fig_siri, use_container_width=True)

    # ─── Before/After stat cards ──────────────────────────────────
    col_a1, col_a2, col_a3 = st.columns(3)

    with col_a1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #EEF2FF, #E8F4FD);
                    border-radius: 12px; padding: 20px; text-align: center;
                    border: 1px solid #E2E8F0;">
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">
                Alexa — Peak (2015)
            </div>
            <div style="font-size: 2.2em; font-weight: 800; color: #7C9FD6;">
                6,702
            </div>
            <div style="font-size: 0.8em; color: #4A5568;">babies/year</div>
        </div>
        """, unsafe_allow_html=True)

    with col_a2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #FFF5F5, #FEE2E2);
                    border-radius: 12px; padding: 20px; text-align: center;
                    border: 1px solid #FECACA;">
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">
                Alexa — Now (2023)
            </div>
            <div style="font-size: 2.2em; font-weight: 800; color: #E63946;">
                511
            </div>
            <div style="font-size: 0.8em; color: #4A5568;">−92% erased</div>
        </div>
        """, unsafe_allow_html=True)

    with col_a3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #F5F0FF, #EDE9FE);
                    border-radius: 12px; padding: 20px; text-align: center;
                    border: 1px solid #E2D9F3;">
            <div style="font-size: 0.75em; color: #718096; text-transform: uppercase; letter-spacing: 1px;">
                Siri — Peak → Now
            </div>
            <div style="font-size: 2.2em; font-weight: 800; color: #9B6FD4;">
                94 → 7
            </div>
            <div style="font-size: 0.8em; color: #4A5568;">−93% erased</div>
        </div>
        """, unsafe_allow_html=True)

    # ─── Insight text ─────────────────────────────────────────────
    st.markdown("")
    st.markdown(
        "**Alexa** was a top-100 name with nearly 7,000 babies a year. Amazon named their voice assistant after it in 2014 "
        "— and initially, the name *rose* (curiosity effect?). But by 2017, reports of children being bullied "
        "(*'Alexa, do my homework'*) began spreading. The collapse was swift: −92% in 6 years."
    )
    st.markdown(
        "**Siri** was a rising Scandinavian name — growing steadily from 8 babies (1997) to 94 (2010). "
        "Then Apple launched their voice assistant in October 2011. By 2013, just 10 babies were named Siri. "
        "A name that was *on its way up* was killed overnight by a product launch."
    )

    st.info(
        "💡 **The asymmetry:** Alexa had a bigger victim pool (6,702 babies/year) but Siri was the crueller kill "
        "— it was actively *growing* when Apple took it. Alexa was already past peak."
    )

    st.markdown("---")
