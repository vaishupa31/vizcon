"""
🎧 Baby DJ — "How I Got My Name"
An animated, self-narrating baby that explains the COUNTRYNESS concept through the
music metaphor, using real data points. Drop into a Streamlit view (components.html
handles the animation + step-through entirely client-side).
"""
import streamlit as st
import streamlit.components.v1 as components


def render():
    st.markdown(
        "<div style='text-align:center;padding:6px 0 2px;'>"
        "<span style='font-family:Georgia,serif;font-size:1.6em;font-weight:800;color:#2D3748;'>"
        "🎧 How I Got My Name</span><br>"
        "<span style='color:#718096;'>Press play — the baby explains it themselves.</span></div>",
        unsafe_allow_html=True,
    )

    html = r"""
<!DOCTYPE html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@700&family=Quicksand:wght@500;700&family=Fraunces:ital@0;1&display=swap" rel="stylesheet">
<style>
  *{margin:0;padding:0;box-sizing:border-box;}
  body{font-family:'Quicksand',sans-serif;}
  .stage{position:relative;max-width:820px;margin:0 auto;border-radius:22px;overflow:hidden;
    background:linear-gradient(180deg,#fde3ec 0%,#f3ecfa 45%,#e6f0fb 80%,#e4f6f1 100%);
    box-shadow:0 12px 40px rgba(160,130,190,.18);min-height:440px;padding:26px 24px 90px;}
  .cloud{position:absolute;background:#fff;border-radius:50%;opacity:.55;filter:blur(2px);}
  .note{position:absolute;font-size:1.3rem;opacity:0;animation:float 3s ease-in-out infinite;}
  @keyframes float{0%{opacity:0;transform:translateY(10px);}30%{opacity:.8;}100%{opacity:0;transform:translateY(-40px);}}
  @keyframes bob{0%,100%{transform:translateY(0);}50%{transform:translateY(-10px);}}

  /* baby */
  .baby{width:120px;height:120px;margin:6px auto 4px;position:relative;animation:bob 3s ease-in-out infinite;}
  .baby svg{display:block;}
  .speech{max-width:560px;margin:8px auto 0;background:#fff;border-radius:18px;padding:20px 24px;
    box-shadow:0 6px 20px rgba(150,120,180,.18);position:relative;text-align:center;min-height:120px;
    display:flex;flex-direction:column;align-items:center;justify-content:center;}
  .speech:before{content:"";position:absolute;top:-12px;left:50%;transform:translateX(-50%);
    border-left:12px solid transparent;border-right:12px solid transparent;border-bottom:12px solid #fff;}
  .speech .line{font-size:1.12rem;color:#4a4266;line-height:1.6;}
  .speech .line b{color:#8a5bb0;}
  .speech .big{font-family:'Fraunces',serif;font-size:2.4rem;font-weight:600;margin:6px 0 2px;}
  .speech .cap{font-size:.8rem;color:#8a7fa0;}
  .stepdots{position:absolute;bottom:20px;left:0;right:0;text-align:center;}
  .stepdots i{display:inline-block;width:9px;height:9px;border-radius:50%;background:#d9c9e8;margin:0 4px;transition:all .3s;}
  .stepdots i.on{background:#8a5bb0;transform:scale(1.3);}

  /* countryness meter (drawn on relevant steps) */
  .meter{width:100%;max-width:420px;margin:14px auto 0;}
  .meter .track{height:16px;border-radius:9px;background:linear-gradient(90deg,#a9e3c9,#f5d68a,#f5b7c5,#e05a5a);position:relative;}
  .meter .pin{position:absolute;top:-6px;width:4px;height:28px;background:#2d3748;border-radius:2px;transition:left .8s cubic-bezier(.4,0,.2,1);}
  .meter .scale{display:flex;justify-content:space-between;font-size:.65rem;color:#8a7fa0;margin-top:6px;}
  .meter .lab{font-size:.72rem;color:#4a4266;font-weight:700;margin-top:6px;text-align:center;}

  .btns{position:absolute;bottom:44px;left:0;right:0;text-align:center;}
  .btns button{font-family:'Quicksand',sans-serif;font-weight:700;border:none;border-radius:20px;
    padding:9px 22px;margin:0 5px;cursor:pointer;font-size:.95rem;}
  .b-next{background:linear-gradient(135deg,#8a5bb0,#c86bd4);color:#fff;box-shadow:0 4px 12px rgba(138,91,176,.4);}
  .b-back{background:#fff;color:#8a5bb0;border:1px solid #d9c9e8;}
  .disc{width:30px;height:30px;vertical-align:middle;}
</style></head>
<body>
<div class="stage" id="stage">
  <div class="cloud" style="width:110px;height:42px;top:14px;left:24px;"></div>
  <div class="cloud" style="width:80px;height:32px;top:34px;right:30px;"></div>
  <div id="notes"></div>

  <div class="baby">
    <svg width="120" height="120" viewBox="0 0 120 120">
      <!-- headphones baby -->
      <circle cx="60" cy="62" r="34" fill="#f6d3b0"/>
      <path d="M34 40 Q34 18 60 18 Q86 18 86 40 Q78 30 60 32 Q42 30 34 40Z" fill="#3a2a1e"/>
      <!-- headphones -->
      <path d="M26 60 Q26 26 60 26 Q94 26 94 60" fill="none" stroke="#8a5bb0" stroke-width="6"/>
      <rect x="18" y="56" width="16" height="24" rx="6" fill="#8a5bb0"/>
      <rect x="86" y="56" width="16" height="24" rx="6" fill="#8a5bb0"/>
      <!-- face -->
      <circle cx="49" cy="60" r="3.5" fill="#2b2d42"/><circle cx="71" cy="60" r="3.5" fill="#2b2d42"/>
      <circle cx="43" cy="68" r="4" fill="#f5a9b8" opacity=".55"/><circle cx="77" cy="68" r="4" fill="#f5a9b8" opacity=".55"/>
      <path d="M52 72 Q60 79 68 72" stroke="#b5764f" stroke-width="2.4" fill="none" stroke-linecap="round"/>
      <!-- tiny music note in hand -->
      <text x="96" y="96" font-size="20" fill="#8a5bb0">♪</text>
    </svg>
  </div>

  <div class="speech" id="speech"></div>

  <div class="btns">
    <button class="b-back" id="back" onclick="step(-1)">◀ Back</button>
    <button class="b-next" id="next" onclick="step(1)">Play ▶</button>
  </div>
  <div class="stepdots" id="dots"></div>
</div>

<script>
  // meter helper: place the pin by countryness on a log-ish scale (1..1000+)
  function meter(cn, label){
    // map cn (1 .. 2000) to 0..100% on a log scale
    var p = Math.max(0, Math.min(100, (Math.log10(Math.max(cn,1)) / Math.log10(2000)) * 100));
    return `<div class="meter"><div class="track"><div class="pin" style="left:${p}%;"></div></div>
      <div class="scale"><span>1 · shared</span><span>10</span><span>100</span><span>1000+ · locked</span></div>
      <div class="lab">${label}</div></div>`;
  }

  const STEPS = [
    {b:"👋", html:`<div class="line">Hi! I'm a brand-new baby, born somewhere in the <b>Anglosphere</b> —
      one of <b>8 countries</b> that all speak English. Today my parents have to write my very first song… my <b>name</b>.</div>`},

    {b:"🎵", html:`<div class="line">Every name is a little <b>song</b>. Some songs become <b>global hits</b> —
      sung in all 8 countries. Others stay <b>local</b>, loved in just one place. Which will I be?</div>`},

    {b:"🎚️", html:`<div class="line">There's one dial that decides it — my parents call it <b>“countryness.”</b><br>
      It just asks: how much <b>louder</b> is my name at home than everywhere else?</div>` + meter(1, "🎚️ low = shared everywhere · high = locked to one country")},

    {b:"🎧", html:`<div class="line">If they name me <b>Isabella</b>, I'm a <b>global hit</b> 🎧 —
      played equally in all 8 countries. My countryness is basically <b>1</b>. At home anywhere… but from nowhere in particular.</div>`
      + `<div class="big" style="color:#2e8f6a;">1.06</div><div class="cap">Isabella · countryness</div>`
      + meter(1.06, "🎧 a Global Hit — the needle sits at 'shared'")},

    {b:"💿", html:`<div class="line">But if they name me <b>Sadhbh</b> (you say it <b>“SIVE”</b>) — I'm a <b>local treasure</b> 💿.
      Over a <b>thousand times</b> more common in Ireland than anywhere else!</div>`
      + `<div class="big" style="color:#a24b82;">1,711</div><div class="cap">Sadhbh · countryness</div>`
      + meter(1711, "💿 a Local Vinyl — the needle jumps to 'locked'")},

    {b:"🤔", html:`<div class="line">Same language, wildly different songs. A name like <b>Raewyn</b> is so locked to
      New Zealand its countryness is <b>168,731</b> — it basically exists nowhere else on Earth!</div>`
      + meter(2000, "🔒 the most locked name in the whole dataset")},

    {b:"🌍", html:`<div class="line">Why does it happen? If you can't <b>read</b> a name, you can't <b>sing</b> it —
      so it stays home. Gaelic, Māori, Welsh, French spellings become <b>cultural passwords</b> only locals know.</div>`},

    {b:"🎤", html:`<div class="line">So… what did they call me? Somewhere in between — <b>shared, but still ours.</b>
      Whatever song my name turns out to be, now <b>you</b> know how to read the charts. 🎶</div>`
      + `<div class="cap" style="margin-top:8px;">▶ explore the full story to meet the global hits &amp; the local legends</div>`},
  ];

  let i = 0;
  const speech = document.getElementById('speech');
  const dots = document.getElementById('dots');
  const notes = document.getElementById('notes');
  dots.innerHTML = STEPS.map((_,k)=>`<i class="${k===0?'on':''}"></i>`).join('');

  function sparkleNotes(){
    let h="";
    const gl=["♪","♫","♩","🎵","🎶"];
    for(let k=0;k<6;k++){
      h+=`<span class="note" style="left:${10+Math.random()*80}%;top:${20+Math.random()*40}%;animation-delay:${Math.random()*1.5}s;color:#c86bd4;">${gl[k%gl.length]}</span>`;
    }
    notes.innerHTML=h;
  }
  function render(){
    speech.innerHTML = STEPS[i].html;
    document.querySelectorAll('.baby text')[0] && null;
    dots.querySelectorAll('i').forEach((d,k)=>d.classList.toggle('on',k===i));
    document.getElementById('back').style.visibility = i===0 ? 'hidden':'visible';
    document.getElementById('next').textContent = i===STEPS.length-1 ? '↺ Replay' : (i===0?'Play ▶':'Next ▶');
    sparkleNotes();
  }
  function step(d){
    if(i===STEPS.length-1 && d>0){ i=0; render(); return; }
    i = Math.max(0, Math.min(STEPS.length-1, i+d));
    render();
  }
  render();
</script>
</body></html>
"""
    components.html(html, height=560, scrolling=False)

    st.caption(
        "🎧 The baby walks through **countryness** — the one metric behind the whole story — "
        "using real names from the data (Isabella, Sadhbh, Raewyn)."
    )
