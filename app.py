import streamlit as st
import joblib

# ── Page config ──────────────────────────────────────────────
st.set_page_config(
    page_title="SpamShield 🛡️",
    page_icon="🛡️",
    layout="centered",
)

# ── Custom CSS ────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=DM+Sans:wght@300;400;500;600&display=swap');

  /* ── Hide Streamlit chrome ── */
  [data-testid="stHeader"]     { display: none !important; }
  [data-testid="stToolbar"]    { display: none !important; }
  [data-testid="stDecoration"] { display: none !important; }
  footer                       { display: none !important; }
  .block-container             { padding-top: 2.5rem !important; max-width: 520px !important; }

  /* ── Deep Space background ── */
  html, body, [data-testid="stAppViewContainer"] {
    background: #07071a !important;
    color: #ddd8ff !important;
    font-family: 'DM Sans', sans-serif !important;
  }

  /* Radial purple glow */
  [data-testid="stAppViewContainer"]::before {
    content: "";
    position: fixed;
    inset: 0;
    background:
      radial-gradient(ellipse 80% 60% at 50% -10%, rgba(109,40,217,0.35) 0%, transparent 70%),
      radial-gradient(ellipse 60% 50% at 80% 100%, rgba(79,70,229,0.2) 0%, transparent 60%),
      radial-gradient(ellipse 40% 40% at 10% 80%, rgba(139,92,246,0.12) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
  }

  /* Dot grid */
  [data-testid="stAppViewContainer"]::after {
    content: "";
    position: fixed;
    inset: 0;
    background-image: radial-gradient(rgba(139,92,246,0.18) 1px, transparent 1px);
    background-size: 28px 28px;
    pointer-events: none;
    z-index: 0;
  }

  /* ── Floating icon ── */
  .brand-icon {
    font-size: 2.8rem;
    text-align: center;
    display: block;
    margin-bottom: 0.2rem;
    filter: drop-shadow(0 0 14px rgba(167,139,250,0.8));
    animation: float 3.5s ease-in-out infinite;
  }
  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50%       { transform: translateY(-6px); }
  }

  .brand-title {
    font-family: 'Space Mono', monospace !important;
    font-size: 1.7rem;
    font-weight: 700;
    text-align: center;
    background: linear-gradient(135deg, #c4b5fd 0%, #818cf8 50%, #6366f1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: 0.04em;
    margin-bottom: 0.25rem;
  }

  .brand-sub {
    text-align: center;
    font-size: 0.78rem;
    color: rgba(196,181,253,0.45);
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 1.6rem;
    font-weight: 500;
  }

  /* ── Badges ── */
  .badge-row {
    display: flex;
    gap: 0.5rem;
    justify-content: center;
    flex-wrap: wrap;
    margin-bottom: 1.6rem;
  }
  .badge {
    background: rgba(109,40,217,0.15);
    border: 1px solid rgba(139,92,246,0.3);
    border-radius: 20px;
    padding: 0.22rem 0.75rem;
    font-size: 0.72rem;
    color: rgba(196,181,253,0.75);
    letter-spacing: 0.05em;
    font-weight: 500;
  }

  /* ── Divider ── */
  .space-hr {
    border: none;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(109,40,217,0.5), transparent);
    margin: 1.2rem 0 1.4rem;
  }

  /* ── Label ── */
  label[data-testid="stWidgetLabel"] p {
    color: rgba(196,181,253,0.7) !important;
    font-size: 0.8rem !important;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
  }

  /* ── Textarea ── */
  textarea {
    background: rgba(7, 5, 20, 0.7) !important;
    color: #e2d9ff !important;
    border: 1px solid rgba(109,40,217,0.35) !important;
    border-radius: 14px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.92rem !important;
    line-height: 1.6 !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
    caret-color: #a78bfa !important;
  }
  textarea::placeholder { color: rgba(139,92,246,0.35) !important; }
  textarea:focus {
    border-color: rgba(139,92,246,0.7) !important;
    box-shadow:
      0 0 0 3px rgba(109,40,217,0.15),
      0 0 20px rgba(109,40,217,0.2) !important;
    outline: none !important;
  }

  /* ── Button ── */
  div.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #6d28d9 0%, #4f46e5 60%, #7c3aed 100%) !important;
    color: #ede9fe !important;
    font-family: 'Space Mono', monospace !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    border: 1px solid rgba(167,139,250,0.3) !important;
    border-radius: 14px !important;
    padding: 0.78rem 1.5rem !important;
    margin-top: 0.6rem;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.3s ease, filter 0.3s ease !important;
    box-shadow:
      0 0 20px rgba(109,40,217,0.4),
      0 4px 15px rgba(0,0,0,0.3),
      inset 0 1px 0 rgba(255,255,255,0.1) !important;
  }
  div.stButton > button:hover {
    transform: translateY(-3px) scale(1.015) !important;
    box-shadow:
      0 0 35px rgba(109,40,217,0.7),
      0 0 70px rgba(79,70,229,0.35),
      0 8px 25px rgba(0,0,0,0.4),
      inset 0 1px 0 rgba(255,255,255,0.15) !important;
    filter: brightness(1.15) !important;
  }
  div.stButton > button:active {
    transform: translateY(0px) scale(0.98) !important;
  }

  /* ── Alerts ── */
  [data-testid="stAlert"] {
    border-radius: 14px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.92rem !important;
    backdrop-filter: blur(10px) !important;
    margin-top: 0.8rem !important;
  }

  /* ── Expander ── */
  [data-testid="stExpander"] {
    background: rgba(15,12,35,0.5) !important;
    border: 1px solid rgba(109,40,217,0.2) !important;
    border-radius: 14px !important;
  }
  [data-testid="stExpander"] summary {
    color: rgba(196,181,253,0.6) !important;
    font-size: 0.82rem !important;
    font-weight: 600;
    letter-spacing: 0.05em;
  }

  /* ── Footer ── */
  .footer {
    text-align: center;
    padding: 0.8rem 0 0.2rem;
    font-size: 0.72rem;
    color: rgba(139,92,246,0.35);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    font-weight: 500;
  }
  .footer span {
    color: rgba(167,139,250,0.7);
    font-weight: 700;
  }
</style>
""", unsafe_allow_html=True)

# ── Load model ────────────────────────────────────────────────
@st.cache_resource
def load_model():
    model      = joblib.load("nb_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# ── Floating Widget ───────────────────────────────────────────
st.markdown('<span class="brand-icon">🛡️</span>', unsafe_allow_html=True)
st.markdown('<div class="brand-title">SpamShield</div>', unsafe_allow_html=True)
st.markdown('<div class="brand-sub">✦ Deep Space Email Guard ✦</div>', unsafe_allow_html=True)

st.markdown("""
<div class="badge-row">
  <div class="badge">🤖 Naive Bayes</div>
  <div class="badge">📊 99% Accuracy</div>
  <div class="badge">⚡ Instant</div>
  <div class="badge">🔐 Secure</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<hr class="space-hr">', unsafe_allow_html=True)

email = st.text_area(
    "📩 EMAIL CONTENT",
    height=140,
    placeholder="Paste your email message here to scan for spam...",
)

predict_clicked = st.button("🔭 Scan for Spam →")

if predict_clicked:
    if email.strip() == "":
        st.warning("⚠️  Drop an email in the field above first.")
    else:
        with st.spinner("🌌 Scanning across the galaxy..."):
            transformed = vectorizer.transform([email])
            prediction  = model.predict(transformed)
            proba       = model.predict_proba(transformed)[0]

        st.markdown('<hr class="space-hr">', unsafe_allow_html=True)

        if prediction[0] == 1:
            confidence = round(proba[1] * 100, 1)
            st.error(f"🚨 **SPAM DETECTED** — Confidence `{confidence}%`\n\nThis message shows suspicious patterns. Avoid clicking any links!")
        else:
            confidence = round(proba[0] * 100, 1)
            st.success(f"✅ **CLEAN EMAIL** — Confidence `{confidence}%`\n\nThis message looks legitimate. You're safe to proceed!")


# ── How it works ──────────────────────────────────────────────
with st.expander("🌠 How does SpamShield work?"):
    st.markdown("""
    **SpamShield** uses a **Multinomial Naive Bayes** model trained on ~5,500 real emails.

    - 🧹 **Preprocessing** — Tokenization, stopword removal, TF-IDF vectorization
    - 🔢 **Features** — Bag-of-words representation of email content
    - 🤖 **Classifier** — Probabilistic prediction with confidence score
    - 🌌 **Result** — Instant SPAM / SAFE verdict
    """)

# ── Footer ────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  🛡️ SpamShield &nbsp;·&nbsp; Crafted with ♥ by <span>Aayush Sharma</span> &nbsp;·&nbsp; Streamlit × Scikit-learn
</div>
""", unsafe_allow_html=True)