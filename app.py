"""
Personalized Travel Itinerary Planner (Skill Wallet Capstone Project 4)
Platform ID: 6ac33976fb8fc7965cd9236d
Full-Stack Travel SaaS Web Application with Multi-Page Navigation:
- Home / Landing Page
- User Authentication (Login, Sign Up, User Profile)
- Smart Destination Matchmaker
- Day-by-Day Clustered Itinerary Generator
- Dynamic Activity Slot Swap & Vibe Customizer
- Trip Persistence & ReportLab Offline PDF Export
- How It Works & Architecture Guide
"""

import streamlit as st
import datetime
import os
import json
from typing import Dict, Any, List

from modules.config import (
    APP_NAME, APP_SUBTITLE, PLATFORM_ID, APP_VERSION,
    CURRENCIES, VIBE_CATEGORIES, BUDGET_TIERS,
    TRAVEL_PARTY_TYPES, TRAVEL_PACES, INTEREST_OPTIONS
)
from modules.storage import init_db, save_trip, list_trips, get_trip, delete_trip
from modules.auth import init_auth_db, authenticate_user
from modules.recommender import recommend_destinations
from modules.clustering import assign_clusters_to_itinerary, compute_overall_transit_score
from modules.llm_service import generate_itinerary_ai, swap_single_slot_ai
from modules.pdf_export import generate_trip_pdf
from sample_data.showcase_trips import SHOWCASE_TRIPS

# Views
from pages_views.home_view import render_home_page
from pages_views.login_view import render_login_page
from pages_views.how_it_works_view import render_how_it_works_page

# Configure Page
st.set_page_config(
    page_title=f"{APP_NAME} | TripNest",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Organic Modern Web Application CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3, h4, .wander-heading {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
        letter-spacing: -0.02em;
    }

    /* Main Container Padding */
    .main .block-container {
        padding-top: 1.2rem;
        padding-bottom: 3rem;
        max-width: 1350px;
    }

    /* Top Navigation Bar */
    .top-navbar {
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 12px 24px;
        margin-bottom: 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
    }

    .brand-logo {
        display: flex;
        align-items: center;
        gap: 10px;
        font-family: 'Outfit', sans-serif;
        font-size: 1.35rem;
        font-weight: 800;
        color: #F8FAFC;
    }

    .badge-pill {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        text-transform: uppercase;
        margin-right: 6px;
        margin-bottom: 6px;
    }

    .badge-platform {
        background: rgba(249, 115, 22, 0.15);
        color: #FB923C;
        border: 1px solid rgba(249, 115, 22, 0.3);
    }

    .badge-teal {
        background: rgba(13, 148, 136, 0.15);
        color: #2DD4BF;
        border: 1px solid rgba(13, 148, 136, 0.3);
    }

    .badge-blue {
        background: rgba(59, 130, 246, 0.15);
        color: #60A5FA;
        border: 1px solid rgba(59, 130, 246, 0.3);
    }

    /* Glass Cards */
    .glass-card {
        background: rgba(30, 41, 59, 0.65);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 20px 24px;
        margin-bottom: 16px;
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .glass-card:hover {
        border-color: rgba(249, 115, 22, 0.35);
        transform: translateY(-2px);
    }

    /* Time Slot Card */
    .slot-card {
        border-left: 4px solid #F97316;
        background: rgba(15, 23, 42, 0.65);
        border-radius: 8px;
        padding: 14px 16px;
        margin-bottom: 12px;
    }

    .slot-time {
        font-size: 0.8rem;
        font-weight: 700;
        color: #F97316;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    .slot-title {
        font-size: 1.05rem;
        font-weight: 600;
        color: #F8FAFC;
        margin-top: 2px;
        margin-bottom: 4px;
    }

    .slot-desc {
        font-size: 0.88rem;
        color: #CBD5E1;
        line-height: 1.45;
        margin-bottom: 6px;
    }

    .slot-meta {
        font-size: 0.8rem;
        color: #94A3B8;
    }

    /* Transit Metrics Banner */
    .transit-banner {
        background: linear-gradient(90deg, rgba(13, 148, 136, 0.2) 0%, rgba(15, 23, 42, 0.6) 100%);
        border: 1px solid rgba(13, 148, 136, 0.35);
        border-radius: 12px;
        padding: 16px 22px;
        margin-bottom: 20px;
    }

    /* Buttons */
    .stButton > button {
        border-radius: 8px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 4px 14px rgba(249, 115, 22, 0.3);
    }

    /* Radio Navigation in Header */
    div[role="radiogroup"] {
        display: flex;
        flex-direction: row;
        justify-content: center;
        background: rgba(15, 23, 42, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 6px;
        gap: 8px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Databases
init_db()
init_auth_db()

# Preload Showcase Trips
saved_existing = list_trips()
if not saved_existing:
    for trip in SHOWCASE_TRIPS:
        save_trip(trip)

# Session State Initialization
if "current_trip" not in st.session_state:
    st.session_state.current_trip = SHOWCASE_TRIPS[0]
if "selected_destination" not in st.session_state:
    st.session_state.selected_destination = "Kyoto, Japan"
if "recommendations" not in st.session_state:
    st.session_state.recommendations = []
if "swap_history" not in st.session_state:
    st.session_state.swap_history = []
if "active_page" not in st.session_state:
    st.session_state.active_page = "🏠 Home"
if "user" not in st.session_state:
    # Set default logged in demo user for immediate rich experience
    st.session_state.user = {
        "id": "user-demo-01",
        "name": "Alex Morgan",
        "email": "alex.morgan@wanderlust.ai",
        "tier": "Wanderlust Pro Member"
    }

# ==============================================================================
# TOP NAVIGATION BAR (Organic Website Feel)
# ==============================================================================
user = st.session_state.get("user")
user_label = f"🧑‍💼 {user['name'].split()[0]}" if user else "👤 Sign In"

nav_col1, nav_col2, nav_col3 = st.columns([1.4, 3.4, 1.2])

with nav_col1:
    st.markdown(f"""
        <div style="display: flex; align-items: center; gap: 8px; padding-top: 6px;">
            <span style="font-size: 1.8rem;">✈️</span>
            <div>
                <span style="font-family: 'Outfit'; font-size: 1.35rem; font-weight: 800; color: #0F172A;">TripNest</span><br/>
                <span class="badge-pill badge-platform" style="font-size: 0.65rem;">ID: {PLATFORM_ID}</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

with nav_col2:
    # Organic Top Navigation Pages
    pages = [
        "🏠 Home",
        "🗺️ Trip Planner",
        "🌟 Destination Matcher",
        "🔄 Slot Customizer",
        "📂 Saved Trips & PDF",
        "ℹ️ How It Works"
    ]
    # Keep active page synchronized
    cur_index = pages.index(st.session_state.active_page) if st.session_state.active_page in pages else 0

    selected_nav = st.radio(
        "Navigation",
        options=pages,
        index=cur_index,
        horizontal=True,
        label_visibility="collapsed"
    )
    if selected_nav != st.session_state.active_page:
        st.session_state.active_page = selected_nav
        st.rerun()

with nav_col3:
    st.markdown('<div style="text-align: right; padding-top: 4px;">', unsafe_allow_html=True)
    if user:
        if st.button(f"{user_label} (Pro)", key="nav_user_btn", use_container_width=True):
            st.session_state.active_page = "👤 Account / Profile"
            st.rerun()
    else:
        if st.button("🔑 Sign In / Join", key="nav_login_btn", type="primary", use_container_width=True):
            st.session_state.active_page = "👤 Account / Profile"
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<hr style='margin-top: 8px; margin-bottom: 20px; border-color: rgba(255,255,255,0.08);'/>", unsafe_allow_html=True)

# ==============================================================================
# SIDEBAR CONFIGURATION (Epic 3)
# ==============================================================================
with st.sidebar:
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <span style="font-size: 2.2rem;">✈️</span>
            <h3 style="margin: 2px 0; color: #F8FAFC;">Wanderlust AI</h3>
            <p style="font-size: 0.78rem; color: #94A3B8;">Capstone Project 4 &bull; ID: {PLATFORM_ID}</p>
        </div>
    """, unsafe_allow_html=True)

    # Active User Status Card
    if user:
        st.markdown(f"""
            <div style="background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255,255,255,0.1); border-radius: 10px; padding: 10px 14px; margin-bottom: 14px;">
                <div style="display: flex; align-items: center; justify-content: space-between;">
                    <div>
                        <strong style="color: #F8FAFC; font-size: 0.9rem;">{user['name']}</strong><br/>
                        <span style="font-size: 0.75rem; color: #34D399;">⭐ {user.get('tier', 'Pro Member')}</span>
                    </div>
                    <span style="font-size: 1.5rem;">🧑‍💼</span>
                </div>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background: rgba(249, 115, 22, 0.1); border: 1px solid rgba(249, 115, 22, 0.3); border-radius: 10px; padding: 10px; margin-bottom: 14px; text-align: center;">
                <span style="font-size: 0.8rem; color: #FB923C;">Not signed in</span>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("### 💱 Global Currency")
    selected_currency = st.selectbox(
        "Display & Calculate In:",
        options=list(CURRENCIES.keys()),
        index=0
    )
    st.session_state.selected_currency = selected_currency

    st.markdown("---")
    st.markdown("### ⚙️ Engine & API Setup")
    llm_provider = st.selectbox(
        "AI Generation Engine",
        options=["Demo Mode (High-Fidelity Offline)", "Google Gemini", "Groq Cloud"],
        index=0,
        help="Demo mode operates 100% offline with zero API keys required. Switch to Gemini or Groq to supply your personal API key."
    )

    api_key = None
    provider_code = "demo"
    if llm_provider == "Google Gemini":
        provider_code = "gemini"
        api_key = st.text_input(
            "Gemini API Key",
            type="password",
            placeholder="AIzaSy...",
            help="Get free Gemini API key from Google AI Studio"
        )
    elif llm_provider == "Groq Cloud":
        provider_code = "groq"
        api_key = st.text_input(
            "Groq API Key",
            type="password",
            placeholder="gsk_...",
            help="Get fast free Groq API key from console.groq.com"
        )

    st.markdown("---")
    st.markdown("### 💡 Quick Showcase Trips")
    s_col1, s_col2 = st.columns(2)
    with s_col1:
        if st.button("🇯🇵 Kyoto Zen", use_container_width=True):
            st.session_state.current_trip = SHOWCASE_TRIPS[0]
            st.session_state.selected_destination = SHOWCASE_TRIPS[0]["destination"]
            st.session_state.active_page = "🗺️ Trip Planner"
            st.success("Loaded Kyoto 5-Day Plan!")
            st.rerun()
    with s_col2:
        if st.button("🇮🇹 Amalfi", use_container_width=True):
            st.session_state.current_trip = SHOWCASE_TRIPS[1]
            st.session_state.selected_destination = SHOWCASE_TRIPS[1]["destination"]
            st.session_state.active_page = "🗺️ Trip Planner"
            st.success("Loaded Amalfi 4-Day Plan!")
            st.rerun()

    if st.button("🇮🇳 Royal Rajasthan", use_container_width=True):
        st.session_state.current_trip = SHOWCASE_TRIPS[2]
        st.session_state.selected_destination = SHOWCASE_TRIPS[2]["destination"]
        st.session_state.active_page = "🗺️ Trip Planner"
        st.success("Loaded Rajasthan 5-Day Plan!")
        st.rerun()

    st.markdown("---")
    st.markdown(f"<div style='font-size: 0.72rem; color: #64748B; text-align: center;'>Version {APP_VERSION}<br/>Ready for Streamlit Community Cloud</div>", unsafe_allow_html=True)

# ==============================================================================
# ROUTER: RENDER ACTIVE PAGE VIEW
# ==============================================================================
active_page = st.session_state.active_page

# ------------------------------------------------------------------------------
# PAGE 1: HOME PAGE
# ------------------------------------------------------------------------------
if active_page == "🏠 Home":
    render_home_page()

# ------------------------------------------------------------------------------
# PAGE 2: AUTH / LOGIN / USER PROFILE
# ------------------------------------------------------------------------------
elif active_page == "👤 Account / Profile":
    render_login_page()

# ------------------------------------------------------------------------------
# PAGE 3: HOW IT WORKS
# ------------------------------------------------------------------------------
elif active_page == "ℹ️ How It Works":
    render_how_it_works_page()

# ------------------------------------------------------------------------------
# PAGE 4: DESTINATION MATCHMAKER (Tab 1 of Core Planner)
# ------------------------------------------------------------------------------
elif active_page == "🌟 Destination Matcher":
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #F8FAFC;">🌟 AI Destination Matchmaker</h2>
            <p style="color: #94A3B8; font-size: 1rem;">
                Not sure where to travel? Discover top 3 matching cities based on your mood vibe, season, and budget.
            </p>
        </div>
    """, unsafe_allow_html=True)

    with st.container():
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        r_col1, r_col2, r_col3 = st.columns(3)

        with r_col1:
            rec_vibe = st.selectbox("🌈 Desired Travel Mood / Vibe", options=VIBE_CATEGORIES, index=2)
            rec_budget = st.selectbox("💰 Budget Category", options=list(BUDGET_TIERS.keys()), index=1)

        with r_col2:
            rec_party = st.selectbox("👥 Travel Party", options=TRAVEL_PARTY_TYPES, index=1)
            rec_pace = st.selectbox("⏱️ Desired Exploration Pace", options=list(TRAVEL_PACES.keys()), index=1)

        with r_col3:
            rec_interests = st.multiselect(
                "🎯 Priority Interests",
                options=INTEREST_OPTIONS,
                default=[INTEREST_OPTIONS[0], INTEREST_OPTIONS[2], INTEREST_OPTIONS[4]]
            )

        trigger_rec = st.button("✨ Discover Top 3 Matching Destinations", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if trigger_rec or not st.session_state.recommendations:
        with st.spinner("Analyzing global climate zones, seasonal travel indices, and vibe affinities..."):
            st.session_state.recommendations = recommend_destinations(
                vibe=rec_vibe,
                budget_tier=rec_budget,
                party_type=rec_party,
                interests=rec_interests,
                currency=selected_currency
            )

    if st.session_state.recommendations:
        st.markdown("#### 🎯 Your Curated Top 3 Destination Matches:")
        c_cols = st.columns(3)
        for i, rec in enumerate(st.session_state.recommendations):
            with c_cols[i]:
                st.markdown(f"""
                    <div class="glass-card" style="height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                                <span class="badge-pill badge-teal">{rec['match_score']}% Match</span>
                                <span style="font-size: 0.85rem; font-weight: 700; color: #F97316;">{rec['cost_display']}</span>
                            </div>
                            <h3 style="margin-top: 0; margin-bottom: 4px; color: #F8FAFC;">{rec['city']}, {rec['country']}</h3>
                            <p style="font-size: 0.8rem; color: #34D399; margin-bottom: 8px;">🌤️ {rec['best_season']}</p>
                            <p style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.4; margin-bottom: 12px;">{rec['why_love_it']}</p>
                            <div style="margin-bottom: 10px;">
                                <strong style="font-size: 0.8rem; color: #94A3B8;">SIGNATURE EXPERIENCE:</strong><br/>
                                <span style="font-size: 0.85rem; color: #F1F5F9;">{rec['signature_experience']}</span>
                            </div>
                            <div style="margin-bottom: 14px;">
                                {" ".join([f"<span class='badge-pill badge-blue' style='font-size: 0.7rem; margin-right: 4px;'>{t}</span>" for t in rec['highlight_tags'][:3]])}
                            </div>
                            <p style="font-size: 0.78rem; color: #94A3B8;">🚶 <b>Walkability:</b> {rec['walkability']}</p>
                        </div>
                    </div>
                """, unsafe_allow_html=True)
                if st.button(f"📍 Plan Trip to {rec['city']}", key=f"btn_plan_{i}", use_container_width=True, type="primary"):
                    st.session_state.selected_destination = f"{rec['city']}, {rec['country']}"
                    st.session_state.active_page = "🗺️ Trip Planner"
                    st.rerun()

# ------------------------------------------------------------------------------
# PAGE 5: CORE ITINERARY GENERATOR (Tab 2)
# ------------------------------------------------------------------------------
elif active_page == "🗺️ Trip Planner":
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #F8FAFC;">🗺️ Day-by-Day Clustered Itinerary Planner</h2>
            <p style="color: #94A3B8; font-size: 1rem;">
                Generate structured day-wise plans where attractions are geographically grouped to eliminate transit fatigue and city backtracking.
            </p>
        </div>
    """, unsafe_allow_html=True)

    with st.expander("📝 Trip Preference & Parameters Form", expanded=True):
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1.2, 1, 1])

        with col1:
            dest_input = st.text_input(
                "Destination (City, Country or Region)",
                value=st.session_state.selected_destination,
                placeholder="e.g. Kyoto, Japan or Amalfi Coast, Italy"
            )
            duration_days = st.slider("Trip Duration (Days)", min_value=1, max_value=14, value=st.session_state.current_trip.get("duration", 4))
            trip_title = st.text_input("Trip Title", value=f"Vacation in {dest_input}")

        with col2:
            dates = st.date_input(
                "Travel Dates",
                value=(datetime.date.today() + datetime.timedelta(days=14), datetime.date.today() + datetime.timedelta(days=14 + duration_days))
            )
            budget_select = st.selectbox("Budget Tier", options=list(BUDGET_TIERS.keys()), index=1)
            party_select = st.selectbox("Travel Party", options=TRAVEL_PARTY_TYPES, index=1)

        with col3:
            pace_select = st.selectbox("Pacing Preference", options=list(TRAVEL_PACES.keys()), index=1)
            dietary_notes = st.text_input("Dietary & Special Notes", placeholder="e.g. Vegetarian friendly, Halal, Wheelchair accessible")
            interests_select = st.multiselect(
                "Traveler Interests",
                options=INTEREST_OPTIONS,
                default=[INTEREST_OPTIONS[0], INTEREST_OPTIONS[1], INTEREST_OPTIONS[2]]
            )

        btn_generate = st.button("🚀 Generate Optimized Clustered Itinerary", type="primary", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    if btn_generate:
        with st.spinner(f"Clustering neighborhoods and crafting transit-optimized schedule for {dest_input}..."):
            start_str = str(dates[0]) if isinstance(dates, (tuple, list)) and len(dates) > 0 else str(datetime.date.today())
            end_str = str(dates[1]) if isinstance(dates, (tuple, list)) and len(dates) > 1 else str(datetime.date.today() + datetime.timedelta(days=duration_days))

            generated_days = generate_itinerary_ai(
                destination=dest_input,
                duration=duration_days,
                budget_tier=budget_select,
                party_type=party_select,
                pace=pace_select,
                currency=selected_currency,
                interests=interests_select,
                provider=provider_code,
                api_key=api_key
            )

            clustered_days = assign_clusters_to_itinerary(generated_days, dest_input)
            total_est_cost = sum(d.get("day_cost", 0.0) for d in clustered_days)

            st.session_state.current_trip = {
                "id": str(datetime.datetime.now().strftime("%y%m%d%H%M%S")),
                "title": trip_title,
                "destination": dest_input,
                "duration": duration_days,
                "start_date": start_str,
                "end_date": end_str,
                "budget_tier": budget_select,
                "party_type": party_select,
                "pace": pace_select,
                "currency": selected_currency,
                "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "days": clustered_days,
                "estimated_total_cost": round(total_est_cost, 1),
                "transit_summary": f"Geographically clustered across {len(clustered_days)} distinct zones. Zero backtracking.",
                "vibe_tag": interests_select[0] if interests_select else "Cultural"
            }
            st.session_state.selected_destination = dest_input
            st.success("🎉 Clustered Itinerary successfully generated and optimized!")

    # Display Itinerary
    cur_trip = st.session_state.current_trip
    if cur_trip and "days" in cur_trip and cur_trip["days"]:
        transit_metrics = compute_overall_transit_score(cur_trip["days"])
        curr_symbol = CURRENCIES.get(cur_trip.get("currency", selected_currency), {}).get("symbol", "$")

        # Anti-Transit Fatigue Dashboard
        st.markdown(f"""
            <div class="transit-banner">
                <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
                    <div>
                        <span class="badge-pill badge-teal">⚡ Anti-Transit Fatigue Engine</span>
                        <span class="badge-pill badge-blue">Rating: {transit_metrics['fatigue_rating'].split('(')[0].strip()}</span>
                        <h4 style="margin-top: 4px; margin-bottom: 2px; color: #F8FAFC;">Route Optimization Metrics</h4>
                        <p style="margin: 0; font-size: 0.85rem; color: #94A3B8;">{cur_trip.get('transit_summary', '')}</p>
                    </div>
                    <div style="display: flex; gap: 24px; text-align: center;">
                        <div>
                            <div style="font-size: 1.3rem; font-weight: 800; color: #34D399;">{transit_metrics['score_percent']}%</div>
                            <div style="font-size: 0.72rem; color: #94A3B8; text-transform: uppercase;">Transit Efficiency</div>
                        </div>
                        <div>
                            <div style="font-size: 1.3rem; font-weight: 800; color: #60A5FA;">{transit_metrics['backtracking_prevented_km']} km</div>
                            <div style="font-size: 0.72rem; color: #94A3B8; text-transform: uppercase;">Backtracking Prevented</div>
                        </div>
                        <div>
                            <div style="font-size: 1.3rem; font-weight: 800; color: #FBBF24;">~{transit_metrics['avg_daily_transit_mins']} mins</div>
                            <div style="font-size: 0.72rem; color: #94A3B8; text-transform: uppercase;">Avg Daily Transit</div>
                        </div>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

        # Budget Tracker Row
        b_col1, b_col2, b_col3, b_col4 = st.columns(4)
        with b_col1:
            st.metric("Total Estimated Cost", f"{curr_symbol}{cur_trip.get('estimated_total_cost', 0):,.1f}")
        with b_col2:
            daily_avg = cur_trip.get('estimated_total_cost', 0) / max(len(cur_trip['days']), 1)
            st.metric("Daily Average", f"{curr_symbol}{daily_avg:,.1f} / day")
        with b_col3:
            st.metric("Destination & Duration", f"{cur_trip.get('destination', '')} ({len(cur_trip['days'])} Days)")
        with b_col4:
            if st.button("💾 Save Trip to My Library", use_container_width=True, type="primary"):
                saved_id = save_trip(cur_trip)
                st.toast(f"Trip saved to local SQLite database with ID: {saved_id}!", icon="💾")

        st.markdown("---")

        # Day Cards
        running_cost = 0.0
        for day in cur_trip["days"]:
            d_num = day.get("day_number", 1)
            d_title = day.get("title", f"Day {d_num}")
            d_zone = day.get("cluster_zone", "Neighborhood Cluster")
            d_cost = day.get("day_cost", 0.0)
            running_cost += d_cost
            slots = day.get("slots", {})

            with st.expander(f"📍 Day {d_num}: {d_title} — Cluster: {d_zone} (Subtotal: {curr_symbol}{d_cost:,.1f})", expanded=(d_num <= 2)):
                st.markdown(f"""
                    <div style="background: rgba(13, 148, 136, 0.1); border-left: 4px solid #0D9488; padding: 8px 14px; border-radius: 6px; margin-bottom: 12px;">
                        <span style="font-size: 0.8rem; font-weight: 700; color: #2DD4BF;">GEOGRAPHIC CLUSTER & TRANSIT:</span>
                        <span style="font-size: 0.85rem; color: #E2E8F0;"> {day.get('transit_notes', '')}</span>
                    </div>
                """, unsafe_allow_html=True)

                slot_cols = st.columns(4)
                slot_info_keys = [
                    ("morning", "🌅 Morning Sightseeing", slot_cols[0], "#F97316"),
                    ("lunch", "🍽️ Lunch & Cuisine", slot_cols[1], "#10B981"),
                    ("afternoon", "🏛️ Afternoon Leisure", slot_cols[2], "#3B82F6"),
                    ("evening", "🌆 Evening Dining & Vibe", slot_cols[3], "#A855F7")
                ]

                for s_key, s_header, col_target, color_accent in slot_info_keys:
                    slot = slots.get(s_key, {})
                    with col_target:
                        st.markdown(f"""
                            <div class="slot-card" style="border-left-color: {color_accent}; height: 100%;">
                                <div class="slot-time">{s_header}</div>
                                <div style="font-size: 0.78rem; color: #94A3B8; margin-bottom: 4px;">⏰ {slot.get('time', 'Flexible')}</div>
                                <div class="slot-title">{slot.get('title', 'Exploration')}</div>
                                <div class="slot-desc">{slot.get('description', '')}</div>
                                <div style="font-size: 0.8rem; color: #E2E8F0; margin-bottom: 4px;">
                                    <b>Cost:</b> {curr_symbol}{slot.get('estimated_cost', 0):,.1f} &bull; <span style="color: {color_accent};">{slot.get('vibe', 'Leisure')}</span>
                                </div>
                                <div class="slot-meta">💡 <i>{slot.get('tips', 'Check local timings')}</i></div>
                            </div>
                        """, unsafe_allow_html=True)

                st.markdown(f"""
                    <div style="display: flex; justify-content: flex-end; gap: 20px; margin-top: 10px; font-size: 0.9rem;">
                        <span style="color: #94A3B8;">Day {d_num} Cost: <b style="color: #F8FAFC;">{curr_symbol}{d_cost:,.1f}</b></span>
                        <span style="color: #94A3B8;">Cumulative Total: <b style="color: #34D399;">{curr_symbol}{running_cost:,.1f}</b></span>
                    </div>
                """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# PAGE 6: DYNAMIC ACTIVITY SLOT SWAP (Tab 3)
# ------------------------------------------------------------------------------
elif active_page == "🔄 Slot Customizer":
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #F8FAFC;">🔄 Interactive Vibe Customization & Dynamic Activity Swap</h2>
            <p style="color: #94A3B8; font-size: 1rem;">
                Replace an individual activity with a vegan café, outdoor flea market, or high-adrenaline adventure <b>without altering any other day in your itinerary</b>.
            </p>
        </div>
    """, unsafe_allow_html=True)

    cur_trip = st.session_state.current_trip
    if not cur_trip or "days" not in cur_trip or not cur_trip["days"]:
        st.info("Please load or generate a trip in the Planner first.")
    else:
        curr_symbol = CURRENCIES.get(cur_trip.get("currency", selected_currency), {}).get("symbol", "$")
        days_list = cur_trip["days"]

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        swap_col1, swap_col2, swap_col3 = st.columns([1, 1, 1.5])

        with swap_col1:
            selected_day_idx = st.selectbox(
                "Select Day to Modify",
                options=range(len(days_list)),
                format_func=lambda idx: f"Day {days_list[idx]['day_number']}: {days_list[idx]['title'][:30]}..."
            )

        target_day = days_list[selected_day_idx]
        cluster_zone = target_day.get("cluster_zone", "Current Zone")

        with swap_col2:
            target_slot_key = st.selectbox(
                "Select Time Slot to Swap",
                options=["morning", "lunch", "afternoon", "evening"],
                format_func=lambda k: {"morning": "🌅 Morning Sightseeing", "lunch": "🍽️ Lunch Recommendation", "afternoon": "🏛️ Afternoon Leisure", "evening": "🌆 Evening Dining"}[k]
            )

        current_slot_data = target_day.get("slots", {}).get(target_slot_key, {})

        with swap_col3:
            st.markdown(f"**Current Activity in Day {target_day['day_number']} ({target_slot_key.title()}):**")
            st.markdown(f"- **Title:** {current_slot_data.get('title', 'N/A')}")
            st.markdown(f"- **Vibe:** {current_slot_data.get('vibe', 'N/A')} | **Cost:** {curr_symbol}{current_slot_data.get('estimated_cost', 0):,.1f}")

        st.markdown("---")
        st.markdown("#### 💬 Specify Your Custom Vibe Swap Requirement:")

        q_cols = st.columns(5)
        preset_val = ""
        if q_cols[0].button("🌱 Veg / Vegan Dining", use_container_width=True):
            preset_val = "Swap for an authentic organic vegetarian / vegan dining spot with farm fresh ingredients"
        if q_cols[1].button("🎨 Artisan Market", use_container_width=True):
            preset_val = "Swap for a vibrant local open-air artisanal flea market and craft stalls"
        if q_cols[2].button("☕ Rooftop View Café", use_container_width=True):
            preset_val = "Swap for a panoramic rooftop café with specialty coffee and scenic viewpoints"
        if q_cols[3].button("☔ Rainy Day Museum", use_container_width=True):
            preset_val = "Swap for a covered world-class indoor modern art gallery or interactive museum"
        if q_cols[4].button("🏃 High Adrenaline", use_container_width=True):
            preset_val = "Swap for an active high-adrenaline outdoor adventure or scenic trail"

        custom_prompt = st.text_input(
            "Custom Instruction / Swap Requirement",
            value=preset_val if preset_val else "Swap for an authentic local culinary spot or artisan walk",
            placeholder="e.g. Find vegetarian rooftop lunch spot with view, or swap museum for outdoor artisanal market"
        )

        col_act1, col_act2 = st.columns([1, 1])
        with col_act1:
            btn_do_swap = st.button("⚡ Swap This Slot Activity (Preserves Rest of Trip)", type="primary", use_container_width=True)

        st.markdown('</div>', unsafe_allow_html=True)

        if btn_do_swap:
            with st.spinner(f"Searching cluster zone '{cluster_zone}' for replacement matching '{custom_prompt}'..."):
                new_slot = swap_single_slot_ai(
                    destination=cur_trip.get("destination", "Kyoto"),
                    day_number=target_day.get("day_number", 1),
                    cluster_zone=cluster_zone,
                    slot_key=target_slot_key,
                    current_slot=current_slot_data,
                    custom_instruction=custom_prompt,
                    currency=cur_trip.get("currency", selected_currency),
                    budget_tier=cur_trip.get("budget_tier", "Moderate"),
                    provider=provider_code,
                    api_key=api_key
                )

                old_title = current_slot_data.get("title", "Previous Activity")
                st.session_state.swap_history.append({
                    "day": target_day["day_number"],
                    "slot": target_slot_key,
                    "old": old_title,
                    "new": new_slot.get("title", "New Activity"),
                    "instruction": custom_prompt,
                    "timestamp": datetime.datetime.now().strftime("%H:%M:%S")
                })

                target_day["slots"][target_slot_key] = new_slot
                target_day["day_cost"] = round(sum(s.get("estimated_cost", 0.0) for s in target_day["slots"].values()), 1)
                cur_trip["estimated_total_cost"] = round(sum(d.get("day_cost", 0.0) for d in cur_trip["days"]), 1)

                st.session_state.current_trip = cur_trip
                st.success(f"✨ Successfully replaced '{old_title}' with '{new_slot.get('title')}' in Day {target_day['day_number']}!")

        if st.session_state.swap_history:
            st.markdown("#### 📋 Activity Swap Audit Trail:")
            for item in reversed(st.session_state.swap_history[-5:]):
                st.markdown(f"""
                    <div style="background: rgba(15, 23, 42, 0.4); border-left: 3px solid #F97316; padding: 6px 12px; border-radius: 4px; margin-bottom: 6px; font-size: 0.85rem;">
                        <span style="color: #94A3B8;">[{item['timestamp']}] Day {item['day']} ({item['slot'].title()}):</span>
                        <span style="text-decoration: line-through; color: #EF4444;">{item['old']}</span> &rarr;
                        <span style="color: #34D399; font-weight: 600;">{item['new']}</span>
                        <span style="color: #64748B; font-size: 0.75rem;">(Reason: "{item['instruction']}")</span>
                    </div>
                """, unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# PAGE 7: SAVED TRIPS & PDF EXPORT (Tab 4)
# ------------------------------------------------------------------------------
elif active_page == "📂 Saved Trips & PDF":
    st.markdown("""
        <div style="margin-bottom: 20px;">
            <h2 style="margin: 0; color: #F8FAFC;">📂 Trip Library & Publication-Grade PDF Export</h2>
            <p style="color: #94A3B8; font-size: 1rem;">
                Browse saved trips persisted in your local SQLite database and export clean offline travel guides.
            </p>
        </div>
    """, unsafe_allow_html=True)

    p_col1, p_col2 = st.columns([1.1, 1.4])

    with p_col1:
        st.markdown("#### 🗄️ Saved Trips Library (SQLite)")
        saved_list = list_trips()
        if not saved_list:
            st.info("No saved trips found. Generate an itinerary in the Planner and save it!")
        else:
            for item in saved_list:
                with st.container():
                    st.markdown(f"""
                        <div class="glass-card" style="padding: 12px 16px; margin-bottom: 10px;">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <h4 style="margin: 0; color: #F8FAFC; font-size: 1rem;">{item['title']}</h4>
                                <span class="badge-pill badge-teal" style="margin: 0;">{item['duration']} Days</span>
                            </div>
                            <p style="font-size: 0.8rem; color: #94A3B8; margin-top: 4px; margin-bottom: 6px;">
                                📍 {item['destination']} &bull; {item['budget_tier']} &bull; {item['party_type']}
                            </p>
                            <p style="font-size: 0.75rem; color: #64748B; margin-bottom: 8px;">Saved on: {item['created_at']}</p>
                        </div>
                    """, unsafe_allow_html=True)

                    btn_c1, btn_c2 = st.columns([2, 1])
                    with btn_c1:
                        if st.button("📂 Load Trip", key=f"load_{item['id']}", use_container_width=True):
                            loaded = get_trip(item["id"])
                            if loaded:
                                st.session_state.current_trip = loaded
                                st.session_state.selected_destination = loaded["destination"]
                                st.session_state.active_page = "🗺️ Trip Planner"
                                st.success(f"Loaded '{loaded['title']}' into active workspace!")
                                st.rerun()
                    with btn_c2:
                        if st.button("🗑️ Delete", key=f"del_{item['id']}", use_container_width=True):
                            delete_trip(item["id"])
                            st.toast("Trip deleted from library.", icon="🗑️")
                            st.rerun()

    with p_col2:
        st.markdown("#### 📄 1-Click Offline PDF Travel Guide Generator")
        cur_trip = st.session_state.current_trip

        if not cur_trip or "days" not in cur_trip or not cur_trip["days"]:
            st.warning("Please load or generate a trip first to create an offline PDF guide.")
        else:
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown(f"""
                <h3 style="margin-top: 0; color: #F8FAFC;">{cur_trip.get('title', 'Travel Guide')}</h3>
                <p style="color: #94A3B8; font-size: 0.9rem;">
                    <b>Destination:</b> {cur_trip.get('destination')}<br/>
                    <b>Duration:</b> {len(cur_trip.get('days', []))} Days &bull; <b>Pace:</b> {cur_trip.get('pace')}<br/>
                    <b>Estimated Total Budget:</b> {CURRENCIES.get(cur_trip.get('currency', 'USD ($)'), {}).get('symbol', '$')}{cur_trip.get('estimated_total_cost', 0):,.1f}
                </p>
                <div style="background: rgba(15, 23, 42, 0.7); padding: 12px; border-radius: 8px; margin-bottom: 14px;">
                    <strong style="color: #34D399; font-size: 0.85rem;">Included in Generated Travel Booklet:</strong>
                    <ul style="font-size: 0.82rem; color: #CBD5E1; margin-top: 4px; padding-left: 18px;">
                        <li>Sequential time-slot itinerary (Morning, Lunch, Afternoon, Evening)</li>
                        <li>Geographic cluster zones eliminating transit fatigue & backtracking</li>
                        <li>Activity-level itemized cost tracking & day subtotal tables</li>
                        <li><b>Emergency Contact Directory:</b> Local Police, Ambulance, Tourist Police</li>
                        <li><b>Pre-Departure Travel Checklist:</b> Passports, Insurance, Offline Maps, Power & Forex</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

            try:
                pdf_bytes = generate_trip_pdf(cur_trip)
                clean_filename = f"{cur_trip.get('destination', 'travel').split(',')[0].strip().lower()}_itinerary_guide.pdf"

                st.download_button(
                    label="📥 Download Publication-Grade Travel Guide (PDF)",
                    data=pdf_bytes,
                    file_name=clean_filename,
                    mime="application/pdf",
                    type="primary",
                    use_container_width=True
                )
                st.success("✅ PDF compilation ready! Click above to download offline travel guide.")
            except Exception as e:
                st.error(f"Error compiling PDF: {str(e)}")

            st.markdown('</div>', unsafe_allow_html=True)

# ==============================================================================
# GLOBAL FOOTER
# ==============================================================================
st.markdown("<br/><hr style='border-color: rgba(255,255,255,0.08);'/><br/>", unsafe_allow_html=True)
st.markdown(f"""
    <div style="text-align: center; color: #64748B; font-size: 0.85rem; padding-bottom: 24px;">
        <div style="margin-bottom: 8px;">
            <a href="#" style="color: #94A3B8; text-decoration: none; margin: 0 12px;">Home</a> &bull;
            <a href="#" style="color: #94A3B8; text-decoration: none; margin: 0 12px;">Planner</a> &bull;
            <a href="#" style="color: #94A3B8; text-decoration: none; margin: 0 12px;">Destination Matcher</a> &bull;
            <a href="#" style="color: #94A3B8; text-decoration: none; margin: 0 12px;">How It Works</a> &bull;
            <a href="#" style="color: #94A3B8; text-decoration: none; margin: 0 12px;">Privacy Policy</a> &bull;
            <a href="#" style="color: #94A3B8; text-decoration: none; margin: 0 12px;">Terms of Service</a>
        </div>
        <div>
            <b>{APP_NAME}</b> &bull; Platform ID: <b>{PLATFORM_ID}</b> &bull; Skill Wallet Capstone Project 4<br/>
            Engineered with Streamlit, SQLite, ReportLab, and Generative AI. Zero external database dependencies.
        </div>
    </div>
""", unsafe_allow_html=True)
