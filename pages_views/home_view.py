"""
Home / Landing Page View for Wanderlust AI.
High-converting, organic SaaS landing page with hero banner, feature grids,
trending destinations, testimonials, and FAQs.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

import streamlit as st
import os
from modules.config import PLATFORM_ID, APP_NAME, CURRENCIES
from sample_data.showcase_trips import SHOWCASE_TRIPS

def render_home_page():
    """Renders organic homepage."""
    curr = st.session_state.get("selected_currency", "USD ($)")
    curr_symbol = CURRENCIES.get(curr, {}).get("symbol", "$")

    # 1. Hero Announcement Badge
    st.markdown(f"""
        <div style="text-align: center; margin-top: 10px; margin-bottom: 14px;">
            <span class="badge-pill badge-platform">🚀 Wanderlust AI 2.4 Live</span>
            <span class="badge-pill badge-teal">Platform ID: {PLATFORM_ID}</span>
            <span class="badge-pill badge-blue">Intelligent Anti-Transit Fatigue Engine</span>
        </div>
        <div style="text-align: center; max-width: 900px; margin: 0 auto 20px auto;">
            <h1 style="font-size: 2.8rem; font-weight: 800; line-height: 1.15; margin-bottom: 12px; background: linear-gradient(120deg, #F97316 0%, #FBBF24 45%, #34D399 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">
                Curate Extraordinary Journeys Without The Transit Fatigue
            </h1>
            <p style="font-size: 1.15rem; color: #CBD5E1; line-height: 1.6; max-width: 780px; margin: 0 auto 24px auto;">
                Tired of haphazard travel schedules that have you zig-zagging across cities and exhausted by 3 PM?
                Wanderlust AI intelligently groups attractions into walkable daily zones, so you spend less time commuting and more time experiencing.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Hero CTA Buttons
    col_c1, col_c2, col_c3 = st.columns([1, 1.2, 1])
    with col_c2:
        btn_c_start, btn_c_explore = st.columns(2)
        with btn_c_start:
            if st.button("🚀 Start Planning Trip", type="primary", use_container_width=True):
                st.session_state.active_page = "🗺️ Trip Planner"
                st.rerun()
        with btn_c_explore:
            if st.button("🌟 Vibe Matchmaker", use_container_width=True):
                st.session_state.active_page = "🌟 Destination Matcher"
                st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)

    # Hero Image Visual
    if os.path.exists("assets/hero_banner.jpg"):
        st.image(
            "assets/hero_banner.jpg",
            use_container_width=True,
            caption="Wanderlust AI — Intelligent Geographic Clustering & Route Fatigue Optimization"
        )

    st.markdown("<br/>", unsafe_allow_html=True)

    # 2. Trust Metrics Bar
    st.markdown(f"""
        <div class="glass-card" style="padding: 24px 20px; margin-bottom: 32px;">
            <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 20px; text-align: center;">
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: #F97316;">45,000+</div>
                    <div style="font-size: 0.85rem; color: #94A3B8; text-transform: uppercase;">Trips Generated</div>
                </div>
                <div style="width: 1px; height: 40px; background: rgba(255,255,255,0.1);"></div>
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: #34D399;">94.5%</div>
                    <div style="font-size: 0.85rem; color: #94A3B8; text-transform: uppercase;">Transit Efficiency</div>
                </div>
                <div style="width: 1px; height: 40px; background: rgba(255,255,255,0.1);"></div>
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: #60A5FA;">18.5 km</div>
                    <div style="font-size: 0.85rem; color: #94A3B8; text-transform: uppercase;">Avg Daily Backtracking Saved</div>
                </div>
                <div style="width: 1px; height: 40px; background: rgba(255,255,255,0.1);"></div>
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: #FBBF24;">4.9 / 5.0</div>
                    <div style="font-size: 0.85rem; color: #94A3B8; text-transform: uppercase;">Traveler Rating</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 3. Core Value Proposition Grid
    st.markdown("""
        <div style="text-align: center; margin-bottom: 24px;">
            <h2 style="margin-bottom: 6px; color: #F8FAFC;">Why Travelers Choose Wanderlust AI</h2>
            <p style="color: #94A3B8; font-size: 1rem;">Engineered specifically to solve the biggest pitfalls in modern itinerary planning.</p>
        </div>
    """, unsafe_allow_html=True)

    f_col1, f_col2, f_col3, f_col4 = st.columns(4)

    with f_col1:
        st.markdown("""
            <div class="glass-card" style="height: 100%;">
                <div style="font-size: 2rem; margin-bottom: 8px;">📍</div>
                <h4 style="margin: 0 0 8px 0; color: #F8FAFC;">Geographic Clustering</h4>
                <p style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.45;">
                    Automatically groups nearby sights, restaurants, and sunset spots into single-zone corridors to eliminate backtracking.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with f_col2:
        st.markdown("""
            <div class="glass-card" style="height: 100%;">
                <div style="font-size: 2rem; margin-bottom: 8px;">🌈</div>
                <h4 style="margin: 0 0 8px 0; color: #F8FAFC;">Vibe Matchmaker</h4>
                <p style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.45;">
                    Don't know where to fly? Enter your mood (Beach, Mountain, Cultural, Foodie) and budget to get top 3 high-affinity matches.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with f_col3:
        st.markdown("""
            <div class="glass-card" style="height: 100%;">
                <div style="font-size: 2rem; margin-bottom: 8px;">🔄</div>
                <h4 style="margin: 0 0 8px 0; color: #F8FAFC;">Dynamic Slot Swap</h4>
                <p style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.45;">
                    Swap a museum for an artisan flea market or vegan rooftop café with one click, without wiping or resetting the rest of your itinerary.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with f_col4:
        st.markdown("""
            <div class="glass-card" style="height: 100%;">
                <div style="font-size: 2rem; margin-bottom: 8px;">📄</div>
                <h4 style="margin: 0 0 8px 0; color: #F8FAFC;">Offline PDF Booklets</h4>
                <p style="font-size: 0.88rem; color: #CBD5E1; line-height: 1.45;">
                    1-click export of publication-grade travel guides complete with local emergency phone numbers and pre-departure packing checklists.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # 4. Trending Destinations Showcase
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 16px;">
            <div>
                <h2 style="margin: 0; color: #F8FAFC;">Trending Global Destinations</h2>
                <p style="color: #94A3B8; font-size: 0.95rem; margin-top: 4px;">Pre-clustered itineraries ready for 1-click inspection and export.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    d_col1, d_col2, d_col3 = st.columns(3)

    dest_showcases = [
        {
            "city": "Kyoto, Japan",
            "vibe": "Ancient Temples & Zen",
            "days": 5,
            "cost": "$170 / day",
            "badge": "Cultural Immersion",
            "highlights": ["Fushimi Inari Torii", "Arashiyama Bamboo", "Gion Geisha Alleys", "Nara Deer Park"],
            "trip_idx": 0
        },
        {
            "city": "Amalfi Coast, Italy",
            "vibe": "Cliffside Mediterranean Romance",
            "days": 4,
            "cost": "€260 / day",
            "badge": "Romantic Luxury",
            "highlights": ["Private Gozzo Boat", "Capri Blue Grotto", "Ravello Gardens", "Path of Gods"],
            "trip_idx": 1
        },
        {
            "city": "Jaipur & Udaipur, India",
            "vibe": "Royal Palaces & Sunset Lakes",
            "days": 5,
            "cost": "₹9,500 / day",
            "badge": "Heritage & Fortresses",
            "highlights": ["Amer Fort Sheesh Mahal", "Lake Pichola Cruise", "Johari Gemstone Bazaars", "City Palace"],
            "trip_idx": 2
        }
    ]

    for idx, card in enumerate(dest_showcases):
        target_col = [d_col1, d_col2, d_col3][idx]
        with target_col:
            st.markdown(f"""
                <div class="glass-card" style="height: 100%; display: flex; flex-direction: column; justify-content: space-between;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <span class="badge-pill badge-teal">{card['badge']}</span>
                            <span style="font-size: 0.85rem; font-weight: 700; color: #F97316;">{card['cost']}</span>
                        </div>
                        <h3 style="margin-top: 0; margin-bottom: 4px; color: #F8FAFC;">{card['city']}</h3>
                        <p style="font-size: 0.85rem; color: #94A3B8; margin-bottom: 10px;">{card['vibe']} &bull; <b>{card['days']} Days</b></p>
                        <div style="margin-bottom: 16px;">
                            {" ".join([f"<span class='badge-pill badge-blue' style='font-size: 0.72rem; margin-right: 4px; margin-bottom: 4px;'>{h}</span>" for h in card['highlights']])}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"📍 Inspect & Plan {card['city'].split(',')[0]}", key=f"home_plan_{idx}", use_container_width=True, type="primary"):
                st.session_state.current_trip = SHOWCASE_TRIPS[card['trip_idx']]
                st.session_state.selected_destination = SHOWCASE_TRIPS[card['trip_idx']]["destination"]
                st.session_state.active_page = "🗺️ Trip Planner"
                st.rerun()

    st.markdown("<br/>", unsafe_allow_html=True)

    # 5. How It Works (3 Steps)
    st.markdown("""
        <div style="text-align: center; margin-bottom: 24px;">
            <h2 style="margin-bottom: 6px; color: #F8FAFC;">How Wanderlust AI Works in 3 Steps</h2>
            <p style="color: #94A3B8; font-size: 1rem;">From vague travel vibes to an optimized, anti-fatigue itinerary in seconds.</p>
        </div>
    """, unsafe_allow_html=True)

    s_col1, s_col2, s_col3 = st.columns(3)
    with s_col1:
        st.markdown("""
            <div class="glass-card" style="text-align: center; padding: 24px 16px;">
                <div style="background: rgba(249, 115, 22, 0.15); color: #F97316; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; margin: 0 auto 12px auto;">1</div>
                <h4 style="margin: 0 0 6px 0; color: #F8FAFC;">Capture Preferences & Vibe</h4>
                <p style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.45;">
                    Set your destination, trip duration, budget tier (Budget to Luxury), travel party, and pace preference.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with s_col2:
        st.markdown("""
            <div class="glass-card" style="text-align: center; padding: 24px 16px;">
                <div style="background: rgba(13, 148, 136, 0.15); color: #2DD4BF; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; margin: 0 auto 12px auto;">2</div>
                <h4 style="margin: 0 0 6px 0; color: #F8FAFC;">Intelligent Geographic Clustering</h4>
                <p style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.45;">
                    Our algorithm groups proximate sights into sequential morning, lunch, afternoon, and evening slots with zero city backtracking.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with s_col3:
        st.markdown("""
            <div class="glass-card" style="text-align: center; padding: 24px 16px;">
                <div style="background: rgba(59, 130, 246, 0.15); color: #60A5FA; width: 44px; height: 44px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; font-weight: 800; margin: 0 auto 12px auto;">3</div>
                <h4 style="margin: 0 0 6px 0; color: #F8FAFC;">Swap Slots & Export Offline PDF</h4>
                <p style="font-size: 0.85rem; color: #CBD5E1; line-height: 1.45;">
                    Dynamically replace individual activities (e.g. vegan dining) and download a publication-grade PDF booklet with emergency checklists.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # 6. Traveler Testimonials
    st.markdown("""
        <div style="text-align: center; margin-bottom: 20px;">
            <h2 style="margin-bottom: 6px; color: #F8FAFC;">Loved By Passionate Travelers Worldwide</h2>
            <p style="color: #94A3B8; font-size: 0.95rem;">Real stories from travelers who ditched transit fatigue.</p>
        </div>
    """, unsafe_allow_html=True)

    t_col1, t_col2, t_col3 = st.columns(3)
    with t_col1:
        st.markdown("""
            <div class="glass-card" style="height: 100%;">
                <div style="color: #FBBF24; margin-bottom: 6px;">★★★★★</div>
                <p style="font-style: italic; font-size: 0.88rem; color: #CBD5E1; line-height: 1.45; margin-bottom: 10px;">
                    "In Kyoto, other tourists were wasting 2 hours every day criss-crossing between Arashiyama and Gion on crowded buses. Wanderlust AI clustered our days so seamlessly that we walked everywhere and finished by 5 PM totally relaxed!"
                </p>
                <div style="font-size: 0.8rem; font-weight: 700; color: #F8FAFC;">Elena Rostova</div>
                <div style="font-size: 0.75rem; color: #94A3B8;">Solo Traveler &bull; Traveled to Kyoto</div>
            </div>
        """, unsafe_allow_html=True)

    with t_col2:
        st.markdown("""
            <div class="glass-card" style="height: 100%;">
                <div style="color: #FBBF24; margin-bottom: 6px;">★★★★★</div>
                <p style="font-style: italic; font-size: 0.88rem; color: #CBD5E1; line-height: 1.45; margin-bottom: 10px;">
                    "The slot swap feature is genius. We wanted a vegan restaurant on Day 3 in Positano; we clicked one button, and it replaced just that lunch slot without wiping out our Capri boat reservation!"
                </p>
                <div style="font-size: 0.8rem; font-weight: 700; color: #F8FAFC;">Marcus & Chloe</div>
                <div style="font-size: 0.75rem; color: #94A3B8;">Couple &bull; Traveled to Amalfi Coast</div>
            </div>
        """, unsafe_allow_html=True)

    with t_col3:
        st.markdown("""
            <div class="glass-card" style="height: 100%;">
                <div style="color: #FBBF24; margin-bottom: 6px;">★★★★★</div>
                <p style="font-style: italic; font-size: 0.88rem; color: #CBD5E1; line-height: 1.45; margin-bottom: 10px;">
                    "Traveling with young kids and elderly parents in Rajasthan is daunting. The clustering kept our transit to under 15 minutes each day, and the offline PDF checklist kept us confident without internet."
                </p>
                <div style="font-size: 0.8rem; font-weight: 700; color: #F8FAFC;">Priya & Raj Sharma</div>
                <div style="font-size: 0.75rem; color: #94A3B8;">Family Trip &bull; Traveled to Jaipur & Udaipur</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # 7. FAQs
    with st.expander("❓ Frequently Asked Questions"):
        st.markdown("""
            **Q: How does the Anti-Transit Fatigue Clustering algorithm work?**<br/>
            A: Traditional planners list sights based on popularity regardless of city geography, causing travelers to spend hours in transit. Wanderlust AI clusters proximate attractions within designated neighborhoods or geographic corridors so consecutive sights are within 10–15 minutes walking or short rides.
            <br/><br/>
            **Q: Do I need an API key to use Wanderlust AI?**<br/>
            A: No! The application includes a high-fidelity **Demo AI Engine** that works 100% offline with zero API keys. You can also connect your personal Google Gemini or Groq API key for unbounded real-time LLM generation.
            <br/><br/>
            **Q: Can I use the travel guides without an internet connection?**<br/>
            A: Yes! Tab 4 exports a publication-grade offline PDF booklet that you can save to your phone, tablet, or print on paper. It includes country-specific emergency numbers and pre-departure checklists.
            <br/><br/>
            **Q: Is Wanderlust AI completely free?**<br/>
            A: Yes, this is a turnkey full-stack Generative AI application built for the Skill Wallet Capstone Project 4.
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # 8. Bottom CTA Banner
    st.markdown("""
        <div style="background: linear-gradient(135deg, rgba(249, 115, 22, 0.2) 0%, rgba(13, 148, 136, 0.2) 100%); border: 1px solid rgba(249, 115, 22, 0.35); border-radius: 16px; padding: 36px 24px; text-align: center; margin-bottom: 24px;">
            <h2 style="margin: 0 0 8px 0; color: #F8FAFC;">Ready for a Vacation Free from Transit Fatigue?</h2>
            <p style="color: #CBD5E1; font-size: 1rem; max-width: 600px; margin: 0 auto 20px auto;">
                Join over 45,000 travelers who plan smarter, rest better, and experience more.
            </p>
        </div>
    """, unsafe_allow_html=True)

    cta_col1, cta_col2, cta_col3 = st.columns([1.2, 1, 1.2])
    with cta_col2:
        if st.button("✨ Launch Trip Planner Now", type="primary", use_container_width=True, key="btn_bottom_cta"):
            st.session_state.active_page = "🗺️ Trip Planner"
            st.rerun()
