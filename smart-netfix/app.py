import streamlit as st
import requests
from datetime import datetime
from report import create_report
import pytz
from tzlocal import get_localzone

# --- Config ---
st.set_page_config(page_title="Smart Network Diagnostic Assistant", layout="wide")
st.title("📡 Smart Network Diagnostic Assistant")

API_URL = "http://localhost:8000/api/v1/diagnostics/run"
HISTORY_URL = "http://localhost:8000/api/v1/diagnostics/history"

USERNAME = "admin"
PASSWORD = "1234"

# --- Session Init ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "page" not in st.session_state:
    st.session_state.page = "login"

# --- Logout Button (Top-Right Only After Login) ---
if st.session_state.logged_in:
    logout_css = """
        <style>
            .logout-container {
                position: absolute;
                top: 15px;
                right: 25px;
                z-index: 9999;
            }
        </style>
        <div class="logout-container">
            <form action="" method="post">
                <input type="submit" value="🚪 Logout" name="logout_btn" style="background-color:#f44336;color:white;border:none;padding:8px 14px;border-radius:6px;cursor:pointer;font-weight:bold;">
            </form>
        </div>
    """
    st.markdown(logout_css, unsafe_allow_html=True)

    if "logout_btn" in st.session_state:
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.rerun()

# --- Login Page ---
if not st.session_state.logged_in:
    st.subheader("🔐 Admin Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")
    if st.button("Login"):
        if user == USERNAME and pwd == PASSWORD:
            st.session_state.logged_in = True
            st.session_state.page = "main"
            st.rerun()
        else:
            st.error("❌ Invalid credentials")
    st.stop()

# -----------------------
# ✅ MAIN PAGE STARTS HERE
# -----------------------

# --- Run Diagnostics ---
if st.button("▶️ Run Diagnostics"):
    with st.spinner("Running diagnostics..."):
        response = requests.post(API_URL, json={"test_type": "full"})
        if response.status_code == 200:
            result = response.json()["results"]
            st.session_state.internet = result["internet"]
            st.session_state.dns = result["dns"]
            st.session_state.download = result["download"]
            st.session_state.upload = result["upload"]
            st.session_state.ping = result["ping"]
            st.session_state.suggestions = result["suggestions"]
            st.session_state.last_run = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            st.error("❌ Diagnostics failed!")

# --- Results Display ---
if "internet" in st.session_state:
    st.success("✅ Diagnostics completed successfully.")
    st.subheader("📊 Diagnostic Dashboard")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🌐 Internet")
        st.success("✅ Connected" if st.session_state.internet else "❌ Not Connected")
    with col2:
        st.markdown("### 🧭 DNS")
        st.success("✅ Working" if st.session_state.dns else "❌ Failed")

    col3, col4, col5 = st.columns(3)
    with col3:
        st.markdown("### ⬇️ Download")
        st.metric(label="Speed", value=f"{st.session_state.download} Mbps")
    with col4:
        st.markdown("### ⬆️ Upload")
        st.metric(label="Speed", value=f"{st.session_state.upload} Mbps")
    with col5:
        st.markdown("### 📶 Ping")
        st.metric(label="Latency", value=f"{st.session_state.ping} ms")

    st.markdown("### 🧠 Suggestions")
    for s in st.session_state.suggestions:
        st.success(s)

    st.markdown(f"🕒 **Last Run:** {st.session_state.last_run}")

    if st.button("📄 Generate PDF Report"):
        filename = create_report(
            st.session_state.internet,
            st.session_state.dns,
            st.session_state.download,
            st.session_state.upload,
            st.session_state.ping,
            st.session_state.suggestions,
        )
        st.success(f"✅ PDF report saved as `{filename}`")

# --- Diagnostics History ---
st.subheader("📂 Previous Diagnostic Runs (Latest 5)")

try:
    history_response = requests.get(HISTORY_URL, params={"limit": 5})
    if history_response.status_code == 200:
        history = history_response.json()["history"]

        from_zone = pytz.utc
        to_zone = get_localzone()

        for entry in history:
            utc_time = datetime.strptime(entry["timestamp"], "%Y-%m-%d %H:%M:%S").replace(tzinfo=from_zone)
            local_time = utc_time.astimezone(to_zone)
            formatted_time = local_time.strftime("%Y-%m-%d %I:%M %p (%Z)")

            with st.expander(f"🕒 {formatted_time}"):
                st.markdown(f"**🌐 Internet:** {'✅ Connected' if entry['internet'] else '❌ Not Connected'}")
                st.markdown(f"**🧭 DNS:** {'✅ Working' if entry['dns'] else '❌ Failed'}")
                st.markdown(f"**⬇️ Download:** {entry['download']} Mbps")
                st.markdown(f"**⬆️ Upload:** {entry['upload']} Mbps")
                st.markdown(f"**📶 Ping:** {entry['ping']} ms")
                st.markdown("**🧠 Suggestions:**")
                for s in entry["suggestions"]:
                    st.markdown(f"- {s}")
    else:
        st.warning("⚠️ Could not load history.")
except Exception as e:
    st.error(f"❌ Error fetching history: {e}")
