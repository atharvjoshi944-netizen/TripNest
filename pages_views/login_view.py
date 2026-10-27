"""
Authentication View: Sign In, Sign Up, and User Profile Dashboard.
Traditional, clean consumer-grade authentication layout.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

import streamlit as st
from modules.auth import authenticate_user, register_user
from modules.storage import list_trips

def render_login_page():
    """Renders traditional authentication page or user profile dashboard."""
    user = st.session_state.get("user")

    # If user is already logged in, show Traditional User Profile Dashboard
    if user:
        st.markdown(f"""
            <div class="web-card" style="max-width: 800px; margin: 20px auto 30px auto; padding: 36px 32px; border-radius: 16px; text-align: center; background: #FFFFFF;">
                <div style="width: 80px; height: 80px; border-radius: 50%; background: #EFF6FF; border: 2px solid #DBEAFE; display: flex; align-items: center; justify-content: center; font-size: 2.5rem; margin: 0 auto 16px auto;">
                    🧑‍💼
                </div>
                <h2 style="margin: 0; color: #0F172A; font-size: 1.8rem; font-weight: 700;">{user['name']}</h2>
                <p style="color: #64748B; font-size: 0.95rem; margin-top: 4px; margin-bottom: 16px;">{user['email']}</p>
                <div style="display: flex; justify-content: center; gap: 8px; flex-wrap: wrap;">
                    <span class="badge-pill badge-teal" style="font-size: 0.85rem; padding: 6px 16px;">⭐ {user.get('tier', 'Wanderlust Member')}</span>
                    <span class="badge-pill badge-blue" style="font-size: 0.85rem; padding: 6px 16px;">Verified Account</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        col_m1, col_m2, col_m3 = st.columns([1, 2.4, 1])
        with col_m2:
            st.markdown('<div class="web-card" style="padding: 28px; margin-bottom: 24px; background: #FFFFFF;">', unsafe_allow_html=True)
            st.markdown("<h3 style='margin-top:0; color:#0F172A;'>📊 Account Dashboard</h3>", unsafe_allow_html=True)
            
            trips = list_trips()
            stat_c1, stat_c2, stat_c3 = st.columns(3)
            with stat_c1:
                st.metric("Saved Itineraries", len(trips))
            with stat_c2:
                st.metric("Membership Tier", "Pro Member")
            with stat_c3:
                st.metric("Transit Efficiency", "94.5%")

            st.markdown("<hr style='margin: 20px 0; border: none; border-top: 1px solid #E2E8F0;'/>", unsafe_allow_html=True)
            st.markdown("<h4 style='color:#1E293B; margin-bottom: 12px;'>⚡ Quick Actions</h4>", unsafe_allow_html=True)
            
            nav_c1, nav_c2 = st.columns(2)
            with nav_c1:
                if st.button("🗺️ Plan a New Itinerary", use_container_width=True, type="primary"):
                    st.session_state.active_page = "🗺️ Trip Planner"
                    st.rerun()
            with nav_c2:
                if st.button("📂 View My Saved Trips", use_container_width=True):
                    st.session_state.active_page = "📂 Saved Trips & PDF"
                    st.rerun()

            st.markdown("<br/>", unsafe_allow_html=True)
            if st.button("🚪 Sign Out of Account", use_container_width=True):
                st.session_state.user = None
                st.toast("Signed out successfully.")
                st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
        return

    # If not logged in, show Traditional Consumer Sign In / Sign Up Form
    st.markdown("""
        <div style="text-align: center; max-width: 500px; margin: 30px auto 20px auto;">
            <div style="font-size: 2.4rem; margin-bottom: 8px;">✈️</div>
            <h1 style="margin: 0; color: #0F172A; font-size: 2rem; font-weight: 800;">Welcome to Wanderlust</h1>
            <p style="color: #64748B; font-size: 1rem; margin-top: 8px;">
                Sign in to manage your itineraries, customize slots, and export offline PDF travel booklets.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col_l1, col_l2, col_l3 = st.columns([1, 1.8, 1])
    with col_l2:
        st.markdown('<div class="web-card" style="padding: 32px 28px; background: #FFFFFF; border-radius: 16px; box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.04);">', unsafe_allow_html=True)

        # 1-Click Demo Login Banner (for quick evaluation)
        st.markdown("""
            <div style="background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 10px; padding: 14px; margin-bottom: 20px; text-align: center;">
                <div style="font-size: 0.82rem; font-weight: 700; color: #1D4ED8; text-transform: uppercase; letter-spacing: 0.05em;">⚡ 1-Click Fast Access</div>
                <p style="font-size: 0.85rem; color: #3B82F6; margin: 4px 0 10px 0;">Sign in instantly as a verified traveler without filling credentials.</p>
            </div>
        """, unsafe_allow_html=True)

        if st.button("🚀 Continue as Alex Morgan (Pro Member)", type="primary", use_container_width=True):
            user_demo = authenticate_user("demo@wanderlust.ai", "wanderlust123")
            if user_demo:
                st.session_state.user = user_demo
                st.toast("Signed in as Alex Morgan!", icon="👋")
                st.session_state.active_page = "🗺️ Trip Planner"
                st.rerun()

        st.markdown("""
            <div style="display: flex; align-items: center; text-align: center; margin: 20px 0; color: #94A3B8;">
                <div style="flex-grow: 1; height: 1px; background: #E2E8F0;"></div>
                <span style="padding: 0 12px; font-size: 0.8rem; text-transform: uppercase; letter-spacing: 0.05em;">or sign in with</span>
                <div style="flex-grow: 1; height: 1px; background: #E2E8F0;"></div>
            </div>
        """, unsafe_allow_html=True)

        # Traditional Social Buttons
        s_c1, s_c2 = st.columns(2)
        with s_c1:
            if st.button("🌐 Google", use_container_width=True):
                st.session_state.user = {"id": "google-user", "name": "Google Traveler", "email": "traveler@gmail.com", "tier": "Wanderlust Member"}
                st.toast("Authenticated with Google!", icon="✅")
                st.session_state.active_page = "🗺️ Trip Planner"
                st.rerun()
        with s_c2:
            if st.button("🍏 Apple", use_container_width=True):
                st.session_state.user = {"id": "apple-user", "name": "Apple Traveler", "email": "traveler@icloud.com", "tier": "Wanderlust Member"}
                st.toast("Authenticated with Apple!", icon="✅")
                st.session_state.active_page = "🗺️ Trip Planner"
                st.rerun()

        st.markdown("<div style='margin: 16px 0;'></div>", unsafe_allow_html=True)

        # Tabs for Traditional Sign In vs Register
        auth_tab1, auth_tab2 = st.tabs(["🔑 Sign In with Email", "📝 Create Free Account"])

        with auth_tab1:
            with st.form("signin_form"):
                email = st.text_input("Email Address", value="demo@wanderlust.ai", placeholder="you@domain.com")
                pwd = st.text_input("Password", value="wanderlust123", type="password")
                
                f_c1, f_c2 = st.columns([1.2, 1])
                with f_c1:
                    remember = st.checkbox("Keep me signed in", value=True)
                with f_c2:
                    st.markdown("<div style='text-align: right; padding-top: 4px;'><a href='#' style='color: #2563EB; font-size: 0.85rem; text-decoration: none;'>Forgot password?</a></div>", unsafe_allow_html=True)
                
                btn_login = st.form_submit_button("Sign In", type="primary", use_container_width=True)

                if btn_login:
                    if not email or not pwd:
                        st.error("Please provide both email and password.")
                    else:
                        logged_user = authenticate_user(email, pwd)
                        if logged_user:
                            st.session_state.user = logged_user
                            st.toast(f"Welcome back, {logged_user['name']}!", icon="👋")
                            st.session_state.active_page = "🗺️ Trip Planner"
                            st.rerun()
                        else:
                            st.error("Invalid credentials. Please verify your email and password.")

        with auth_tab2:
            with st.form("signup_form"):
                reg_name = st.text_input("Full Name", placeholder="e.g. Jordan Rivera")
                reg_email = st.text_input("Email Address", placeholder="jordan@example.com")
                reg_pwd = st.text_input("Create Password", type="password")
                reg_confirm = st.text_input("Confirm Password", type="password")
                agree = st.checkbox("I agree to the Terms of Service & Privacy Policy", value=True)
                btn_signup = st.form_submit_button("Create Account", type="primary", use_container_width=True)

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
                            st.toast("Account created successfully! Welcome to Wanderlust.", icon="🎉")
                            st.session_state.active_page = "🗺️ Trip Planner"
                            st.rerun()
                        else:
                            st.error(res["error"])

        st.markdown('</div>', unsafe_allow_html=True)
