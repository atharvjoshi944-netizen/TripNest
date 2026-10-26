"""
Tab 1: Smart Destination Recommender Engine (Epic 3).
Suggests top matching destinations based on vibe, budget, season, party type, and interests.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

from typing import List, Dict, Any
from modules.config import CURRENCIES, BUDGET_TIERS

# Comprehensive Destination Database for offline / demo mode
DESTINATIONS_DB = [
    {
        "city": "Kyoto",
        "country": "Japan",
        "vibes": ["Cultural & Historic Heritage", "Romantic & Scenic Escapes", "Spiritual & Wellness Sanctuary"],
        "budget_tiers": ["Budget ($/₹)", "Moderate ($$/₹₹)", "Luxury ($$$/₹₹₹)"],
        "best_season": "Spring (Mar-May cherry blossoms) & Autumn (Oct-Nov fiery maples)",
        "climate": "Mild & Pleasant (15°C - 22°C)",
        "highlight_tags": ["#ZenGardens", "#AncientTemples", "#MatchaTeaTradition", "#GeishaHeritage", "#UNESCOSites"],
        "why_love_it": "A serene sanctuary preserving 1,200 years of imperial artistry with walkable temple belts and tranquil bamboo groves.",
        "signature_experience": "Sunrise walk through 10,000 vermilion Torii gates at Fushimi Inari and riverside tea tasting in Arashiyama.",
        "walkability": "98% Walkable / Pristine Rail & Bus Network",
        "daily_cost_usd": {"budget": 60, "moderate": 170, "luxury": 420}
    },
    {
        "city": "Amalfi Coast & Capri",
        "country": "Italy",
        "vibes": ["Romantic & Scenic Escapes", "Beach & Tropical Islands", "Culinary & Gastronomic Trail"],
        "budget_tiers": ["Moderate ($$/₹₹)", "Luxury ($$$/₹₹₹)"],
        "best_season": "May to October (Sun-drenched Mediterranean warmth)",
        "climate": "Sunny & Coastal (22°C - 28°C)",
        "highlight_tags": ["#CliffsideVillas", "#CapriGrottos", "#LemonGroves", "#MichelinDining", "#LimoncelloCoast"],
        "why_love_it": "Pastel villages cascading down sheer cliffs directly into turquoise waters with unforgettable clifftop terrace dining.",
        "signature_experience": "Chartering a wooden Italian gozzo boat to secret Capri sea caves followed by candlelit dinner in Positano.",
        "walkability": "Steep Hillside Stairs / Scenic Ferry & Private Boat Cruising",
        "daily_cost_usd": {"budget": 95, "moderate": 260, "luxury": 550}
    },
    {
        "city": "Jaipur & Udaipur",
        "country": "India",
        "vibes": ["Cultural & Historic Heritage", "Romantic & Scenic Escapes", "Culinary & Gastronomic Trail"],
        "budget_tiers": ["Budget ($/₹)", "Moderate ($$/₹₹)", "Luxury ($$$/₹₹₹)"],
        "best_season": "October to March (Crisp royal winter days)",
        "climate": "Sunny & Dry (18°C - 26°C)",
        "highlight_tags": ["#PinkCityRamparts", "#LakePalaces", "#RajasthaniThali", "#RoyalForts", "#HandloomBazaars"],
        "why_love_it": "Living Maharaja castles, sparkling lakeside palaces, vibrant textile bazaars, and legendary Indian hospitality.",
        "signature_experience": "Lake Pichola sunset boat ride past floating marble palaces and dinner inside Amer Fort's 1135 AD hall.",
        "walkability": "Old City Walkable / Auto-rickshaws & Chauffeur Cars",
        "daily_cost_usd": {"budget": 35, "moderate": 110, "luxury": 320}
    },
    {
        "city": "Zermatt & Lucerne",
        "country": "Switzerland",
        "vibes": ["Alpine & Mountain Adventure", "Romantic & Scenic Escapes", "Nature, Wildlife & Eco-Retreat"],
        "budget_tiers": ["Moderate ($$/₹₹)", "Luxury ($$$/₹₹₹)"],
        "best_season": "Year-round (Summer alpine hikes or Winter Matterhorn skiing)",
        "climate": "Crisp Alpine (10°C - 20°C in Summer; Snow in Winter)",
        "highlight_tags": ["#MatterhornPeak", "#GlacierExpress", "#LakeCruises", "#AlpineSpas", "#SwissFondue"],
        "why_love_it": "Car-free village at the base of the iconic Matterhorn, offering panoramic cogwheel trains and crystal-clear glacier lakes.",
        "signature_experience": "Gornergrat cogwheel train summit view of 29 four-thousand-meter alpine peaks and evening raclette dining.",
        "walkability": "100% Car-free Pristine Village / World-class Rail",
        "daily_cost_usd": {"budget": 120, "moderate": 280, "luxury": 650}
    },
    {
        "city": "Bali (Ubud & Uluwatu)",
        "country": "Indonesia",
        "vibes": ["Beach & Tropical Islands", "Spiritual & Wellness Sanctuary", "Nature, Wildlife & Eco-Retreat"],
        "budget_tiers": ["Budget ($/₹)", "Moderate ($$/₹₹)", "Luxury ($$$/₹₹₹)"],
        "best_season": "April to October (Dry tropical trade winds)",
        "climate": "Tropical Warmth (26°C - 30°C)",
        "highlight_tags": ["#RiceTerraces", "#CliffsideBeaches", "#YogaSanctuary", "#WaterfallTreks", "#SunsetBeachClubs"],
        "why_love_it": "Lush emerald jungle ravines, spiritual sound healing ceremonies, dramatic cliffside ocean temples, and world-class surfing.",
        "signature_experience": "Morning walk along Tegalalang rice terraces, holy water temple cleanse at Tirta Empul, and Kecak fire dance at sunset.",
        "walkability": "Scooter / Private Driver Network",
        "daily_cost_usd": {"budget": 40, "moderate": 105, "luxury": 280}
    },
    {
        "city": "Reykjavik & South Coast",
        "country": "Iceland",
        "vibes": ["Nature, Wildlife & Eco-Retreat", "Alpine & Mountain Adventure", "Romantic & Scenic Escapes"],
        "budget_tiers": ["Moderate ($$/₹₹)", "Luxury ($$$/₹₹₹)"],
        "best_season": "Sept-March for Northern Lights, June-August for Midnight Sun",
        "climate": "Cool & Temperate (5°C - 15°C in Summer; -2°C in Winter)",
        "highlight_tags": ["#NorthernLights", "#GeothermalLagoons", "#GlacierIceCaves", "#BlackSandBeaches", "#VolcanoTours"],
        "why_love_it": "Otherworldly landscapes of steaming hot springs, crashing waterfalls, and cosmic aurora borealis curtains.",
        "signature_experience": "Soaking in mineral-rich milky blue waters of the Blue Lagoon surrounded by black lava fields.",
        "walkability": "Compact Capital Walkable / 4x4 Ring Road Exploration",
        "daily_cost_usd": {"budget": 110, "moderate": 270, "luxury": 580}
    },
    {
        "city": "Barcelona",
        "country": "Spain",
        "vibes": ["Vibrant Metropolises & Urban", "Cultural & Historic Heritage", "Culinary & Gastronomic Trail", "Beach & Tropical Islands"],
        "budget_tiers": ["Budget ($/₹)", "Moderate ($$/₹₹)", "Luxury ($$$/₹₹₹)"],
        "best_season": "May to June & September to October (Golden warm Mediterranean)",
        "climate": "Mild Mediterranean (20°C - 26°C)",
        "highlight_tags": ["#GaudíArchitecture", "#SagradaFamília", "#TapasCrawl", "#GothicQuarter", "#BarcelonetaBeach"],
        "why_love_it": "Whimsical modernist architecture, lively pedestrian boulevards, sun-soaked beaches, and midnight tapas hopping.",
        "signature_experience": "Marveling at the stained-glass forest inside Sagrada Família and savoring Iberian ham with cava in El Born.",
        "walkability": "96% Walkable Pedestrian Superblocks & Efficient Metro",
        "daily_cost_usd": {"budget": 70, "moderate": 180, "luxury": 420}
    },
    {
        "city": "Tokyo",
        "country": "Japan",
        "vibes": ["Vibrant Metropolises & Urban", "Culinary & Gastronomic Trail", "Cultural & Historic Heritage"],
        "budget_tiers": ["Budget ($/₹)", "Moderate ($$/₹₹)", "Luxury ($$$/₹₹₹)"],
        "best_season": "Spring (Cherry blossoms) & Autumn (Ginkgo golden foliage)",
        "climate": "Moderate & Pleasant (16°C - 23°C)",
        "highlight_tags": ["#NeonScramble", "#MichelinStars", "#ShibuyaCrossing", "#AnimeDistrict", "#TeamLabArt"],
        "why_love_it": "The pinnacle of futuristic hyper-modernity coexisting seamlessly with ancient Shinto shrines and supreme gastronomy.",
        "signature_experience": "Crossing Shibuya Scramble at twilight, dining in an 8-seat omakase sushi bar, and exploring teamLab immersive digital art.",
        "walkability": "100% Supreme Metro Transit & Walkable Wards",
        "daily_cost_usd": {"budget": 75, "moderate": 195, "luxury": 490}
    }
]

import streamlit as st

@st.cache_data(show_spinner=False)
def recommend_destinations(vibe: str, budget_tier: str, party_type: str, interests: List[str], currency: str = "USD ($)") -> List[Dict[str, Any]]:
    """
    Intelligently scores and ranks destinations based on preferences,
    returning top 3 recommendations with rich metadata and converted pricing.
    """
    curr_info = CURRENCIES.get(currency, CURRENCIES["USD ($)"])
    rate = curr_info["rate"]
    symbol = curr_info["symbol"]

    scored_destinations = []

    for d in DESTINATIONS_DB:
        score = 70.0  # Baseline score

        # Vibe affinity match
        if any(vibe.lower() in v.lower() or v.lower() in vibe.lower() for v in d["vibes"]):
            score += 18.0

        # Budget match
        if budget_tier in d["budget_tiers"]:
            score += 10.0
        else:
            score -= 5.0

        # Interests match
        matched_interests = 0
        for tag in d["highlight_tags"]:
            tag_clean = tag.replace("#", "").lower()
            for user_interest in interests:
                if any(word in tag_clean for word in user_interest.lower().split() if len(word) > 3):
                    matched_interests += 1
                    break
        score += min(matched_interests * 3.0, 12.0)

        # Party type tuning
        if "Couple" in party_type and ("Romantic" in " ".join(d["vibes"]) or "Amalfi" in d["city"] or "Kyoto" in d["city"]):
            score += 5.0
        elif "Family" in party_type and ("Walkable" in d["walkability"] or "Japan" in d["country"] or "Lucerne" in d["city"]):
            score += 5.0
        elif "Solo" in party_type and ("Walkable" in d["walkability"] or "Hostels" in d["budget_tiers"]):
            score += 4.0

        # Cap at 99%
        final_score = min(round(score, 1), 99.0)

        # Calculate budget pricing in user currency
        tier_key = "moderate"
        if "Budget" in budget_tier:
            tier_key = "budget"
        elif "Luxury" in budget_tier:
            tier_key = "luxury"

        daily_usd = d["daily_cost_usd"].get(tier_key, 150)
        daily_conv = round(daily_usd * rate, 0)
        cost_display = f"{symbol}{int(daily_conv):,} / day"

        scored_destinations.append({
            **d,
            "match_score": final_score,
            "cost_display": cost_display,
            "tier_key": tier_key
        })

    # Sort descending by match score
    scored_destinations.sort(key=lambda x: x["match_score"], reverse=True)
    return scored_destinations[:3]
