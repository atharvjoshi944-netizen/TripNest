"""
Home / Landing Page View for Wanderlust AI.
High-converting, traditional travel website landing page (Airbnb / Expedia style)
with interactive hero search widget, curated destinations, value propositions,
traveler reviews, and FAQ.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

import streamlit as st
import os
from modules.config import PLATFORM_ID, APP_NAME, CURRENCIES, BUDGET_TIERS, TRAVEL_PARTY_TYPES
from sample_data.showcase_trips import SHOWCASE_TRIPS

def render_home_page():
    """Renders traditional consumer travel homepage."""
    curr = st.session_state.get("selected_currency", "USD ($)")
    curr_symbol = CURRENCIES.get(curr, {}).get("symbol", "$")

    # 1. Traditional Hero Section
    st.markdown("""
        <div style="text-align: center; max-width: 960px; margin: 15px auto 25px auto;">
            <div style="display: inline-flex; align-items: center; gap: 8px; background: #EFF6FF; border: 1px solid #BFDBFE; border-radius: 9999px; padding: 6px 18px; margin-bottom: 16px;">
                <span style="font-size: 0.82rem; font-weight: 700; color: #1D4ED8; letter-spacing: 0.04em; text-transform: uppercase;">✨ Intelligent Trip Planning</span>
                <span style="color: #93C5FD;">&bull;</span>
                <span style="font-size: 0.82rem; color: #3B82F6;">Anti-Transit Fatigue Engine</span>
            </div>
            <h1 style="font-size: 3.2rem; font-weight: 800; line-height: 1.15; color: #0F172A; margin: 0 0 16px 0; letter-spacing: -0.03em;">
                Explore the World Without <br/><span style="color: #2563EB;">The Transit Fatigue</span>
            </h1>
            <p style="font-size: 1.18rem; color: #475569; line-height: 1.6; max-width: 760px; margin: 0 auto;">
                Wanderlust AI intelligently groups attractions into walkable daily zones, eliminating chaotic cross-town backtracking so you spend more time experiencing and less time in transit.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # 2. Traditional Horizontal Travel Booking / Search Bar (Airbnb / Skyscanner Style)
    st.markdown("""
        <div class="web-card search-bar-container" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 20px; padding: 20px 24px; box-shadow: 0 12px 30px -4px rgba(0, 0, 0, 0.08); max-width: 1100px; margin: 0 auto 35px auto;">
    """, unsafe_allow_html=True)

    with st.form("hero_search_widget"):
        col_s1, col_s2, col_s3, col_s4, col_s5 = st.columns([1.6, 1.1, 1.2, 1.2, 1.3])
        
        with col_s1:
            st.markdown("<label style='font-size: 0.78rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em;'>📍 Where to?</label>", unsafe_allow_html=True)
            search_dest = st.text_input(
                "Destination",
                value="Kyoto, Japan",
                placeholder="City or Region (e.g. Kyoto, Paris)",
                label_visibility="collapsed"
            )
        
        with col_s2:
            st.markdown("<label style='font-size: 0.78rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em;'>📅 Duration</label>", unsafe_allow_html=True)
            search_days = st.selectbox(
                "Days",
                options=[3, 4, 5, 7, 10, 14],
                index=2,
                format_func=lambda x: f"{x} Days",
                label_visibility="collapsed"
            )

        with col_s3:
            st.markdown("<label style='font-size: 0.78rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em;'>👥 Who's going?</label>", unsafe_allow_html=True)
            search_party = st.selectbox(
                "Party",
                options=TRAVEL_PARTY_TYPES,
                index=1,
                label_visibility="collapsed"
            )

        with col_s4:
            st.markdown("<label style='font-size: 0.78rem; font-weight: 700; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em;'>💰 Budget</label>", unsafe_allow_html=True)
            search_budget = st.selectbox(
                "Budget",
                options=list(BUDGET_TIERS.keys()),
                index=1,
                label_visibility="collapsed"
            )

        with col_s5:
            st.markdown("<div style='height: 18px;'></div>", unsafe_allow_html=True)
            search_submitted = st.form_submit_button("🚀 Plan Itinerary", type="primary", use_container_width=True)

        if search_submitted:
            st.session_state.selected_destination = search_dest
            st.session_state.active_page = "🗺️ Trip Planner"
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

    # Hero Image Visual (Optional Banner)
    if os.path.exists("assets/hero_banner.jpg"):
        st.image(
            "assets/hero_banner.jpg",
            use_container_width=True,
            caption="Wanderlust AI — Smart Geographic Clustering & Route Fatigue Optimization"
        )
        st.markdown("<br/>", unsafe_allow_html=True)

    # 3. Trust Metrics Bar
    st.markdown("""
        <div class="web-card" style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 16px; padding: 24px 20px; margin-bottom: 48px;">
            <div style="display: flex; justify-content: space-around; align-items: center; flex-wrap: wrap; gap: 20px; text-align: center;">
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: #2563EB;">45,000+</div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em;">Trips Planned</div>
                </div>
                <div style="width: 1px; height: 40px; background: #E2E8F0;"></div>
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: #059669;">94.5%</div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em;">Transit Efficiency</div>
                </div>
                <div style="width: 1px; height: 40px; background: #E2E8F0;"></div>
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: #0284C7;">18.5 km</div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em;">Avg Daily Backtracking Saved</div>
                </div>
                <div style="width: 1px; height: 40px; background: #E2E8F0;"></div>
                <div>
                    <div style="font-size: 2.2rem; font-weight: 800; color: #D97706;">4.9 / 5.0</div>
                    <div style="font-size: 0.85rem; font-weight: 600; color: #64748B; text-transform: uppercase; letter-spacing: 0.05em;">Traveler Satisfaction</div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # 4. Featured Destinations
    st.markdown("""
        <div style="display: flex; justify-content: space-between; align-items: flex-end; margin-bottom: 24px;">
            <div>
                <h2 style="margin: 0; color: #0F172A; font-size: 2rem; font-weight: 800;">Featured Curated Journeys</h2>
                <p style="color: #64748B; font-size: 1rem; margin-top: 4px; margin-bottom: 0;">Pre-clustered, optimized itineraries ready to explore or customize.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    d_col1, d_col2, d_col3 = st.columns(3)

    dest_showcases = [
        {
            "city": "Kyoto, Japan",
            "vibe": "Ancient Temples & Zen Culture",
            "days": 5,
            "cost": f"{curr_symbol}170 / day",
            "badge": "Cultural Immersion",
            "highlights": ["Fushimi Inari Torii", "Arashiyama Bamboo", "Gion Geisha Alleys", "Nara Deer Park"],
            "trip_idx": 0,
            "emoji": "⛩️"
        },
        {
            "city": "Amalfi Coast, Italy",
            "vibe": "Cliffside Mediterranean Romance",
            "days": 4,
            "cost": f"{curr_symbol}260 / day",
            "badge": "Romantic Luxury",
            "highlights": ["Private Gozzo Boat", "Capri Blue Grotto", "Ravello Gardens", "Path of Gods"],
            "trip_idx": 1,
            "emoji": "🍋"
        },
        {
            "city": "Jaipur & Udaipur, India",
            "vibe": "Royal Palaces & Sunset Lakes",
            "days": 5,
            "cost": f"{curr_symbol}115 / day",
            "badge": "Heritage & Fortresses",
            "highlights": ["Amer Fort Sheesh Mahal", "Lake Pichola Cruise", "Johari Gemstone Bazaars", "City Palace"],
            "trip_idx": 2,
            "emoji": "🕌"
        }
    ]

    for idx, card in enumerate(dest_showcases):
        target_col = [d_col1, d_col2, d_col3][idx]
        with target_col:
            st.markdown(f"""
                <div class="web-card destination-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; padding: 24px; height: 100%; display: flex; flex-direction: column; justify-content: space-between; box-shadow: 0 4px 12px rgba(0,0,0,0.04); margin-bottom: 12px;">
                    <div>
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
                            <span class="badge-pill badge-teal">{card['badge']}</span>
                            <span style="font-size: 0.9rem; font-weight: 700; color: #2563EB;">{card['cost']}</span>
                        </div>
                        <div style="font-size: 2.2rem; margin-bottom: 8px;">{card['emoji']}</div>
                        <h3 style="margin: 0 0 6px 0; color: #0F172A; font-size: 1.35rem; font-weight: 700;">{card['city']}</h3>
                        <p style="font-size: 0.9rem; color: #64748B; margin-bottom: 14px;">{card['vibe']} &bull; <b>{card['days']} Days</b></p>
                        <div style="margin-bottom: 18px;">
                            {" ".join([f"<span class='badge-pill badge-blue' style='font-size: 0.75rem; margin-right: 4px; margin-bottom: 6px;'>{h}</span>" for h in card['highlights']])}
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            if st.button(f"📍 View {card['city'].split(',')[0]} Itinerary", key=f"home_plan_{idx}", use_container_width=True, type="primary"):
                st.session_state.current_trip = SHOWCASE_TRIPS[card['trip_idx']]
                st.session_state.selected_destination = SHOWCASE_TRIPS[card['trip_idx']]["destination"]
                st.session_state.active_page = "🗺️ Trip Planner"
                st.rerun()

    st.markdown("<br/><br/>", unsafe_allow_html=True)

    # 5. Core Value Propositions
    st.markdown("""
        <div style="text-align: center; margin-bottom: 32px;">
            <h2 style="margin-bottom: 8px; color: #0F172A; font-size: 2rem; font-weight: 800;">Why Travelers Choose Wanderlust</h2>
            <p style="color: #64748B; font-size: 1.05rem;">Engineered specifically to solve the biggest pitfalls in modern vacation planning.</p>
        </div>
    """, unsafe_allow_html=True)

    f_col1, f_col2, f_col3, f_col4 = st.columns(4)

    with f_col1:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; height: 100%; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="font-size: 2.2rem; margin-bottom: 12px;">🗺️</div>
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 1.15rem; font-weight: 700;">Geographic Clustering</h4>
                <p style="font-size: 0.9rem; color: #475569; line-height: 1.5; margin: 0;">
                    Groups nearby sights, dining, and scenic walks into contiguous zones to prevent cross-city zigzagging.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with f_col2:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; height: 100%; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="font-size: 2.2rem; margin-bottom: 12px;">🌟</div>
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 1.15rem; font-weight: 700;">Vibe Matchmaker</h4>
                <p style="font-size: 0.9rem; color: #475569; line-height: 1.5; margin: 0;">
                    Unsure where to fly? Discover destinations matched to your mood, seasonal weather, and budget in seconds.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with f_col3:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; height: 100%; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="font-size: 2.2rem; margin-bottom: 12px;">🔄</div>
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 1.15rem; font-weight: 700;">Dynamic Slot Swap</h4>
                <p style="font-size: 0.9rem; color: #475569; line-height: 1.5; margin: 0;">
                    Modify any individual slot (like vegan lunch or flea markets) with 1 click without losing your other days.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with f_col4:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; height: 100%; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="font-size: 2.2rem; margin-bottom: 12px;">📄</div>
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 1.15rem; font-weight: 700;">Offline PDF Guides</h4>
                <p style="font-size: 0.9rem; color: #475569; line-height: 1.5; margin: 0;">
                    Export publication-grade booklets with emergency phone numbers and travel checklists for offline roaming.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/><br/>", unsafe_allow_html=True)

    # 6. How It Works (3 Steps)
    st.markdown("""
        <div style="text-align: center; margin-bottom: 32px;">
            <h2 style="margin-bottom: 8px; color: #0F172A; font-size: 2rem; font-weight: 800;">How It Works in 3 Simple Steps</h2>
            <p style="color: #64748B; font-size: 1rem;">From idea to a publication-grade itinerary in under 60 seconds.</p>
        </div>
    """, unsafe_allow_html=True)

    s_col1, s_col2, s_col3 = st.columns(3)
    with s_col1:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; text-align: center; padding: 32px 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="background: #EFF6FF; color: #2563EB; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; font-weight: 800; margin: 0 auto 16px auto;">1</div>
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 1.15rem; font-weight: 700;">Select Your Vibe & Dates</h4>
                <p style="font-size: 0.9rem; color: #64748B; line-height: 1.5; margin: 0;">
                    Choose your destination, duration, budget tier, and exploration pace.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with s_col2:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; text-align: center; padding: 32px 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="background: #ECFDF5; color: #059669; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; font-weight: 800; margin: 0 auto 16px auto;">2</div>
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 1.15rem; font-weight: 700;">AI Clusters Each Day</h4>
                <p style="font-size: 0.9rem; color: #64748B; line-height: 1.5; margin: 0;">
                    Our algorithm groups nearby attractions into smooth corridors under 15 minutes transit.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with s_col3:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 16px; text-align: center; padding: 32px 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="background: #FFF7ED; color: #C2410C; width: 50px; height: 50px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.3rem; font-weight: 800; margin: 0 auto 16px auto;">3</div>
                <h4 style="margin: 0 0 8px 0; color: #0F172A; font-size: 1.15rem; font-weight: 700;">Customize & Hit the Road</h4>
                <p style="font-size: 0.9rem; color: #64748B; line-height: 1.5; margin: 0;">
                    Swap individual activities on the fly and download your offline PDF booklet.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/><br/>", unsafe_allow_html=True)

    # 7. Traveler Testimonials
    st.markdown("""
        <div style="text-align: center; margin-bottom: 24px;">
            <h2 style="margin-bottom: 8px; color: #0F172A; font-size: 2rem; font-weight: 800;">Loved By Travelers Around The Globe</h2>
            <p style="color: #64748B; font-size: 1rem;">Real reviews from travelers who reclaimed their vacation energy.</p>
        </div>
    """, unsafe_allow_html=True)

    t_col1, t_col2, t_col3 = st.columns(3)
    with t_col1:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; height: 100%; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="color: #F59E0B; font-size: 1.1rem; margin-bottom: 10px;">★★★★★</div>
                <p style="font-size: 0.92rem; color: #334155; line-height: 1.5; margin-bottom: 16px;">
                    "In Kyoto, other tourists were wasting 2 hours every day criss-crossing between Arashiyama and Gion on crowded buses. Wanderlust clustered our days so seamlessly that we walked everywhere and finished by 5 PM totally relaxed!"
                </p>
                <div style="font-size: 0.88rem; font-weight: 700; color: #0F172A;">Elena Rostova</div>
                <div style="font-size: 0.78rem; color: #64748B;">Solo Traveler &bull; Kyoto, Japan</div>
            </div>
        """, unsafe_allow_html=True)

    with t_col2:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; height: 100%; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="color: #F59E0B; font-size: 1.1rem; margin-bottom: 10px;">★★★★★</div>
                <p style="font-size: 0.92rem; color: #334155; line-height: 1.5; margin-bottom: 16px;">
                    "The slot swap feature is pure magic. We wanted a vegan dining spot on Day 3 in Positano; one click, and it replaced just that lunch slot without wiping out our Capri boat tour or dinner booking!"
                </p>
                <div style="font-size: 0.88rem; font-weight: 700; color: #0F172A;">Marcus & Chloe Chen</div>
                <div style="font-size: 0.78rem; color: #64748B;">Couple &bull; Amalfi Coast, Italy</div>
            </div>
        """, unsafe_allow_html=True)

    with t_col3:
        st.markdown("""
            <div class="web-card" style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 14px; padding: 24px; height: 100%; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
                <div style="color: #F59E0B; font-size: 1.1rem; margin-bottom: 10px;">★★★★★</div>
                <p style="font-size: 0.92rem; color: #334155; line-height: 1.5; margin-bottom: 16px;">
                    "Traveling with young kids in Rajasthan is daunting. The clustering kept our transit to under 15 minutes each day, and the offline PDF checklist kept us completely confident without needing constant roaming data."
                </p>
                <div style="font-size: 0.88rem; font-weight: 700; color: #0F172A;">Priya & Raj Sharma</div>
                <div style="font-size: 0.78rem; color: #64748B;">Family Holiday &bull; Rajasthan, India</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/><br/>", unsafe_allow_html=True)

    # 8. FAQs
    with st.expander("❓ Frequently Asked Questions", expanded=False):
        st.markdown("""
            <div style="padding: 12px; color: #334155; line-height: 1.6;">
                <p><b>Q: How does the Anti-Transit Fatigue Clustering algorithm work?</b><br/>
                A: Traditional planners list sights based on popularity regardless of city geography, causing travelers to spend hours in transit. Wanderlust AI clusters proximate attractions within designated neighborhoods or geographic corridors so consecutive sights are within 10–15 minutes walking or short rides.</p>
                
                <p><b>Q: Do I need an API key to use Wanderlust AI?</b><br/>
                A: No! The application includes a high-fidelity <b>Demo AI Engine</b> that works 100% offline with zero API keys. You can also connect your personal Google Gemini or Groq API key for unbounded real-time LLM generation.</p>
                
                <p><b>Q: Can I use the travel guides without an internet connection?</b><br/>
                A: Yes! You can export a publication-grade offline PDF booklet that you can save to your phone, tablet, or print on paper. It includes country-specific emergency numbers and pre-departure checklists.</p>
                
                <p><b>Q: Is Wanderlust AI completely free?</b><br/>
                A: Yes, this is a turnkey full-stack Generative AI application built for the Skill Wallet Capstone Project 4.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br/>", unsafe_allow_html=True)

    # 9. Bottom Traditional CTA Banner
    st.markdown("""
        <div class="web-card" style="background: linear-gradient(135deg, #1E40AF 0%, #2563EB 50%, #0284C7 100%); border-radius: 20px; padding: 48px 32px; text-align: center; color: #FFFFFF; box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.4);">
            <h2 style="margin: 0 0 12px 0; color: #FFFFFF; font-size: 2.2rem; font-weight: 800;">Ready for a Vacation Free from Transit Fatigue?</h2>
            <p style="color: #DBEAFE; font-size: 1.1rem; max-width: 620px; margin: 0 auto 24px auto;">
                Join over 45,000 travelers who plan smarter, rest better, and experience more.
            </p>
        </div>
    """, unsafe_allow_html=True)

    cta_col1, cta_col2, cta_col3 = st.columns([1.2, 1, 1.2])
    with cta_col2:
        if st.button("✨ Launch Trip Planner Now", type="primary", use_container_width=True, key="btn_bottom_cta"):
            st.session_state.active_page = "🗺️ Trip Planner"
            st.rerun()
