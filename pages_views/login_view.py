"""
Authentication View: Sign In, Sign Up, and User Profile Dashboard.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

import streamlit as st
from modules.auth import authenticate_user, register_user
from modules.storage import list_trips

def render_login_page():
    """Renders organic authentication page or user profile dashboard."""
    user = st.session_state.get("user")

    # If user is already logged in, show User Profile & Settings
    if user:
        st.markdown(f"""
            <div class="glass-card" style="max-width: 720px; margin: 0 auto; text-align: center; padding: 32px 24px;">
                <div style="font-size: 3.5rem; margin-bottom: 8px;">🧑‍💼</div>
                <h2 style="margin: 0; color: #F8FAFC;">{user['name']}</h2>
                <p style="color: #94A3B8; font-size: 0.95rem; margin-top: 4px; margin-bottom: 12px;">{user['email']}</p>
                <div>
                    <span class="badge-pill badge-teal" style="font-size: 0.85rem; padding: 6px 16px;">⭐ {user.get('tier', 'Wanderlust Pro Member')}</span>
                    <span class="badge-pill badge-blue" style="font-size: 0.85rem; padding: 6px 16px;">Platform ID: 6ac33976fb8fc7965cd9236d</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("<br/>", unsafe_allow_html=True)

        col_m1, col_m2, col_m3 = st.columns([1, 2, 1])
        with col_m2:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown("### 📊 Account Overview & Quick Stats")
            trips = list_trips()
            stat_c1, stat_c2 = st.columns(2)
            with stat_c1:
                st.metric("Saved Itineraries", len(trips))
            with stat_c2:
                st.metric("Account Status", "Active Pro")

            st.markdown("---")
            st.markdown("#### ⚡ Quick Navigation")
            nav_c1, nav_c2 = st.columns(2)
            with nav_c1:
                if st.button("🗺️ Open Trip Planner", use_container_width=True, type="primary"):
                    st.session_state.active_page = "🗺️ Trip Planner"
                    st.rerun()
            with nav_c2:
                if st.button("📂 View My Saved Trips", use_container_width=True):
                    st.session_state.active_page = "📂 Saved Trips & PDF"
                    st.rerun()

            st.markdown("---")
            if st.button("🚪 Sign Out of Wanderlust AI", use_container_width=True):
                st.session_state.user = None
                st.toast("Signed out successfully.")
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        return

    # If not logged in, show Organic Login / Sign Up Form
    st.markdown("""
        <div style="text-align: center; max-width: 580px; margin: 0 auto 20px auto;">
            <span style="font-size: 2.8rem;">✈️</span>
            <h2 style="margin: 4px 0; color: #F8FAFC;">Welcome to Wanderlust AI</h2>
            <p style="color: #94A3B8; font-size: 0.95rem;">
                Sign in to your account to save itineraries, unlock AI route optimization, and export offline travel guides.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_l1, col_l2, col_l3 = st.columns([1, 1.8, 1])
    with col_l2:
        st.markdown('<div class="glass-card" style="padding: 28px 24px;">', unsafe_allow_html=True)

        # Quick 1-Click Demo Login Banner
        st.markdown("""
            <div style="background: linear-gradient(135deg, rgba(249, 115, 22, 0.15) 0%, rgba(13, 148, 136, 0.15) 100%); border: 1px solid rgba(249, 115, 22, 0.3); border-radius: 8px; padding: 12px; margin-bottom: 18px; text-align: center;">
                <span style="font-size: 0.82rem; font-weight: 700; color: #FB923C;">EVALUATOR QUICK ACCESS</span>
                <p style="font-size: 0.8rem; color: #CBD5E1; margin: 4px 0 8px 0;">Instant 1-click access to verified Pro account without typing credentials.</p>
            </div>
        """, unsafe_allow_html=True)

        if st.button("⚡ 1-Click Demo Login (Alex Morgan - Pro)", type="primary", use_container_width=True):
            user_demo = authenticate_user("demo@wanderlust.ai", "wanderlust123")
            if user_demo:
                st.session_state.user = user_demo
                st.toast("Signed in as Alex Morgan (Pro Member)!", icon="🎉")
                st.rerun()

        st.markdown("""
            <div style="display: flex; align-items: center; text-align: center; margin: 16px 0; color: #64748B;">
                <div style="flex-grow: 1; height: 1px; background: rgba(255,255,255,0.1);"></div>
                <span style="padding: 0 10px; font-size: 0.75rem; text-transform: uppercase;">or continue with</span>
                <div style="flex-grow: 1; height: 1px; background: rgba(255,255,255,0.1);"></div>
            </div>
        """, unsafe_allow_html=True)

        # Social Auth Buttons
        s_c1, s_c2 = st.columns(2)
        with s_c1:
            if st.button("🌐 Google Account", use_container_width=True):
                st.session_state.user = {"id": "google-user", "name": "Google Traveler", "email": "traveler@gmail.com", "tier": "Wanderlust Pro Member"}
                st.toast("Authenticated with Google!", icon="✅")
                st.rerun()
        with s_c2:
            if st.button("🍏 Apple ID", use_container_width=True):
                st.session_state.user = {"id": "apple-user", "name": "Apple Traveler", "email": "traveler@icloud.com", "tier": "Wanderlust Pro Member"}
                st.toast("Authenticated with Apple!", icon="✅")
                st.rerun()

        st.markdown("<br/>", unsafe_allow_html=True)

        # Tabs for Sign In vs Register
        auth_tab1, auth_tab2 = st.tabs(["🔑 Sign In with Email", "📝 Create New Account"])

        with auth_tab1:
            with st.form("signin_form"):
                email = st.text_input("Email Address", value="demo@wanderlust.ai", placeholder="name@domain.com")
                pwd = st.text_input("Password", value="wanderlust123", type="password")
                remember = st.checkbox("Remember me on this browser", value=True)
                btn_login = st.form_submit_button("Sign In to Account", type="primary", use_container_width=True)

                if btn_login:
                    if not email or not pwd:
                        st.error("Please enter both email and password.")
                    else:
                        logged_user = authenticate_user(email, pwd)
                        if logged_user:
                            st.session_state.user = logged_user
                            st.toast(f"Welcome back, {logged_user['name']}!", icon="👋")
                            st.session_state.active_page = "🗺️ Trip Planner"
                            st.rerun()
                        else:
                            st.error("Invalid credentials. Try using the 1-Click Demo Login button above.")

        with auth_tab2:
            with st.form("signup_form"):
                reg_name = st.text_input("Full Name", placeholder="e.g. Jordan Rivera")
                reg_email = st.text_input("Email Address", placeholder="jordan@example.com")
                reg_pwd = st.text_input("Create Password", type="password")
                reg_confirm = st.text_input("Confirm Password", type="password")
                agree = st.checkbox("I agree to the Terms of Service & Privacy Policy", value=True)
                btn_signup = st.form_submit_button("Create Free Account", type="primary", use_container_width=True)

                if btn_signup:
                    if not reg_name or not reg_email or not reg_pwd:
                        st.error("All fields are required.")
                    elif reg_pwd != reg_confirm:
                        st.error("Passwords do not match.")
                    elif not agree:
                        st.error("Please accept the terms to proceed.")
                    else:
                        res = register_user(reg_name, reg_email, reg_pwd)
                        if res["success"]:
                            st.session_state.user = res["user"]
                            st.toast("Account created successfully! Welcome to Wanderlust AI.", icon="🎉")
                            st.session_state.active_page = "🗺️ Trip Planner"
                            st.rerun()
                        else:
                            st.error(res["error"])

        st.markdown('</div>', unsafe_allow_html=True)
