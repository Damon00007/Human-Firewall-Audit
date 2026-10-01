import streamlit as st
import re, hashlib
from datetime import datetime

st.set_page_config(page_title="Human Firewall Audit V3", page_icon="🛡️", layout="wide")

# ---------- SHARED SECURITY STATE ----------
defaults = {
    "password_hash": None,
    "password_strength": "Not configured",
    "login_attempts": 0,
    "locked": False,
    "events": [],
    "last_phishing": None,
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

def fingerprint(password):
    return hashlib.sha256(password.encode()).hexdigest()

def check_password(password):
    checks = {
        "Length ≥ 8": len(password) >= 8,
        "Uppercase": bool(re.search(r"[A-Z]", password)),
        "Lowercase": bool(re.search(r"[a-z]", password)),
        "Digit": bool(re.search(r"\d", password)),
        "Special character": bool(re.search(r"[^A-Za-z0-9]", password)),
    }
    score = sum(checks.values())
    strength = "Weak" if score <= 2 else "Medium" if score <= 4 else "Strong"
    return score, strength, checks

def log_event(action, status="Info"):
    st.session_state.events.insert(0, {
        "time": datetime.now().strftime("%H:%M:%S"),
        "action": action,
        "status": status
    })
    st.session_state.events = st.session_state.events[:30]

st.markdown("""
<style>
.block-container{padding-top:1.5rem}
h1,h2,h3{color:#123b5d}
.notice{padding:12px 16px;border-radius:10px;background:#eef5f9;border-left:5px solid #123b5d}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🛡️ Human Firewall V3")
page = st.sidebar.radio("Navigation", [
    "Dashboard","Phishing Analysis","Password Security",
    "Login Security","Awareness Center","Activity Log"
])

st.sidebar.markdown("---")
st.sidebar.write("**Connected Security State**")
st.sidebar.write(f"Password: `{st.session_state.password_strength}`")
st.sidebar.write(f"Login: `{'Locked' if st.session_state.locked else 'Active'}`")
st.sidebar.write(f"Events: `{len(st.session_state.events)}`")

# ---------- DASHBOARD ----------
if page == "Dashboard":
    st.title("The Human Firewall Audit")
    st.caption("Interconnected Cybersecurity Demonstration")
    st.markdown('<div class="notice"><b>Fictional educational environment:</b> no real credentials or real targets are used.</div>', unsafe_allow_html=True)
    a,b,c,d = st.columns(4)
    a.metric("Password", st.session_state.password_strength)
    b.metric("Login Attempts", st.session_state.login_attempts)
    c.metric("Account", "Locked" if st.session_state.locked else "Protected")
    d.metric("Events", len(st.session_state.events))

    st.subheader("Interconnected Flow")
    st.info("Phishing Analysis → Awareness → Password Security → Login Security → Activity Log")

    cols=st.columns(3)
    cols[0].info("👤 Human Layer\nTrust, urgency and verification.")
    cols[1].info("📄 Information Layer\nPublic information and workflow exposure.")
    cols[2].info("🔐 Technical Layer\nPassword, login, phishing analysis and monitoring.")

# ---------- PHISHING ----------
elif page == "Phishing Analysis":
    st.title("Phishing Analysis")
    sample = """Subject: Urgent Collaboration Opportunity

Please verify your account immediately using the link below.
Do not share this opportunity publicly until confirmation.

https://example.test/verify-login
"""
    msg = st.text_area("Sample message", sample, height=210)
    if st.button("Analyze Message"):
        words = ["urgent","verify","password","login","click","immediately","secret","confidential"]
        found = [w for w in words if re.search(r"\b"+re.escape(w)+r"\b", msg, re.I)]
        urls = re.findall(r"https?://\S+", msg)
        score = len(found)*10 + len(urls)*15
        risk = "High" if score >= 60 else "Medium" if score >= 30 else "Low"
        st.session_state.last_phishing = (risk, score, found, urls)
        log_event(f"Phishing analysis completed — {risk} risk", "Alert" if risk=="High" else "Review")
    if st.session_state.last_phishing:
        risk, score, found, urls = st.session_state.last_phishing
        st.metric("Risk Level", risk)
        st.write(f"**Heuristic score:** {score}")
        st.write("**Suspicious keywords:**", ", ".join(found) or "None")
        st.write("**URLs:**", ", ".join(urls) or "None")
        (st.error if risk=="High" else st.warning if risk=="Medium" else st.success)(
            "Verify independently before interacting with suspicious requests."
        )

# ---------- PASSWORD ----------
elif page == "Password Security":
    st.title("Password Security")
    st.write("Create the demo password used by Login Security. The raw password is never displayed or logged.")
    with st.form("set_password"):
        p1 = st.text_input("Create password", type="password")
        p2 = st.text_input("Confirm password", type="password")
        ok = st.form_submit_button("Set / Update Password")
    if ok:
        if not p1:
            st.error("Enter a password.")
        elif p1 != p2:
            st.error("Passwords do not match.")
        else:
            score, strength, checks = check_password(p1)
            st.session_state.password_hash = fingerprint(p1)
            st.session_state.password_strength = strength
            st.session_state.login_attempts = 0
            st.session_state.locked = False
            log_event(f"Password configured — {strength}", "Protected")
            st.success("Password configured. Login Security is now connected to it.")
            st.progress(score/5)
            st.write(f"Strength: **{strength}** ({score}/5)")
            st.caption("For this demo, only a one-way fingerprint is retained in session state.")

    if st.session_state.password_hash:
        st.success(f"Current status: {st.session_state.password_strength}")
    else:
        st.info("No password configured yet.")

# ---------- LOGIN ----------
elif page == "Login Security":
    st.title("Login Security")
    st.write("This login uses the password configured in Password Security.")

    if not st.session_state.password_hash:
        st.warning("First create a password in Password Security.")
    elif st.session_state.locked:
        st.error("Account locked after 3 failed attempts.")
        if st.button("Reset Demo Lock"):
            st.session_state.login_attempts = 0
            st.session_state.locked = False
            log_event("Demo account lock reset", "Info")
            st.rerun()
    else:
        st.info(f"Password status: {st.session_state.password_strength}")
        entered = st.text_input("Enter configured password", type="password")
        if st.button("Login"):
            if fingerprint(entered) == st.session_state.password_hash:
                st.session_state.login_attempts = 0
                log_event("Successful login", "Success")
                st.success("Login successful.")
            else:
                st.session_state.login_attempts += 1
                remaining = 3 - st.session_state.login_attempts
                log_event(f"Failed login attempt #{st.session_state.login_attempts}", "Warning")
                if st.session_state.login_attempts >= 3:
                    st.session_state.locked = True
                    log_event("Account locked after 3 failed attempts", "Locked")
                    st.error("Account locked after 3 failed attempts.")
                else:
                    st.error(f"Incorrect password. {remaining} attempt(s) remaining.")

# ---------- AWARENESS ----------
elif page == "Awareness Center":
    st.title("Awareness Center")
    st.subheader("Don't Let Fame Fool You!")
    awareness_items = [
        "Unexpected partnership or collaboration request",
        "Pressure to act immediately or keep the request secret",
        "Verification through an unrelated social-media account",
        "Domain mismatch or suspicious redirect",
        "Request for passwords, authentication codes or sensitive files",
        "Request for unreleased content",
    ]

    st.write("Tick the red flags you identified:")
    selected_flags = []
    for i, item in enumerate(awareness_items):
        if st.checkbox(item, key=f"awareness_flag_{i}"):
            selected_flags.append(item)

    if selected_flags:
        st.success(f"{len(selected_flags)} red flag(s) identified.")
    else:
        st.info("Select the warning signs you want to review.")
    st.subheader("Recommended Controls")
    for item in [
        "Independently verify the sender through an established company contact.",
        "Use least privilege and Zero-Trust access controls.",
        "Use email authentication and anti-phishing controls.",
        "Use a reporting/phish-alert mechanism.",
        "Protect sensitive media with access controls and watermarking.",
    ]:
        st.write("•", item)
    if st.button("Mark Awareness Review Complete"):
        if selected_flags:
            log_event(f"Awareness review completed — {len(selected_flags)} red flags", "Complete")
            st.success("Awareness review recorded in Activity Log.")
        else:
            st.warning("Tick at least one red flag before completing the review.")

# ---------- ACTIVITY LOG ----------
elif page == "Activity Log":
    st.title("Activity Log")
    st.write("Events from all connected security modules.")
    if not st.session_state.events:
        st.info("No events yet.")
    else:
        icons={"Success":"🟢","Warning":"🟠","Alert":"🔴","Locked":"🔒","Protected":"🔐","Complete":"✅","Review":"🟡"}
        for e in st.session_state.events:
            st.write(f"{icons.get(e['status'],'ℹ️')} **{e['time']}** — {e['action']}")
    if st.button("Clear Activity Log"):
        st.session_state.events=[]
        st.rerun()

st.sidebar.markdown("---")
st.sidebar.caption("Educational demo • Fictional target • No real credentials")
