"""
Configuration, Constants, and Reference Dictionaries for Personalized Travel Itinerary Planner.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

APP_NAME = "Personalized Travel Itinerary Planner"
APP_SUBTITLE = "AI-Powered Vacation Itinerary & Transit Fatigue Optimization Engine"
PLATFORM_ID = "6ac33976fb8fc7965cd9236d"
APP_VERSION = "2.4.0 (Production Release)"

# Currency mappings and conversion relative to 1 USD
CURRENCIES = {
    "USD ($)": {"symbol": "$", "rate": 1.0, "code": "USD"},
    "INR (₹)": {"symbol": "₹", "rate": 83.5, "code": "INR"},
    "EUR (€)": {"symbol": "€", "rate": 0.92, "code": "EUR"},
    "GBP (£)": {"symbol": "£", "rate": 0.79, "code": "GBP"},
    "JPY (¥)": {"symbol": "¥", "rate": 155.0, "code": "JPY"}
}

# Open-ended Vibe Categories
VIBE_CATEGORIES = [
    "Beach & Tropical Islands",
    "Alpine & Mountain Adventure",
    "Cultural & Historic Heritage",
    "Vibrant Metropolises & Urban",
    "Nature, Wildlife & Eco-Retreat",
    "Culinary & Gastronomic Trail",
    "Romantic & Scenic Escapes",
    "Spiritual & Wellness Sanctuary"
]

# Budget Tiers
BUDGET_TIERS = {
    "Budget ($/₹)": {
        "desc": "Hostels, street food, public transit, free & discount attractions",
        "usd_daily": 65,
        "inr_daily": 5400,
        "multiplier": 0.65
    },
    "Moderate ($$/₹₹)": {
        "desc": "Boutique 3-4★ hotels, mix of casual & sit-down dining, rideshare/cabs, paid monuments",
        "usd_daily": 175,
        "inr_daily": 14500,
        "multiplier": 1.0
    },
    "Luxury ($$$/₹₹₹)": {
        "desc": "5★ luxury resorts, fine dining, private chauffeured transit, VIP skip-the-line tours",
        "usd_daily": 450,
        "inr_daily": 37500,
        "multiplier": 2.4
    }
}

TRAVEL_PARTY_TYPES = [
    "Solo Traveler",
    "Couple / Romantic",
    "Family (with Children/Seniors)",
    "Friends Group"
]

TRAVEL_PACES = {
    "Relaxed": "2-3 unhurried spots per day with ample café breaks & scenic downtime",
    "Moderate": "3-4 well-paced highlights per day with balanced transit and leisure",
    "Fast-Paced": "5-6 high-energy sights per day maximizing daily coverage & attractions"
}

INTEREST_OPTIONS = [
    "Local Street Food & Fine Dining",
    "Art, Museums & Architecture",
    "Historic Landmarks & UNESCO Sites",
    "Outdoor Hiking & Adventure",
    "Scenic Viewpoints & Sunset Spots",
    "Nightlife, Rooftop Bars & Speakeasies",
    "Artisan Markets & Souvenir Shopping",
    "Spas, Onsens & Wellness",
    "Hidden Gems & Local Neighborhoods",
    "Photography & Instagrammable Spots"
]

# Standard International Emergency Numbers Fallback
EMERGENCY_DIRECTORIES = {
    "Japan": {"police": "110", "ambulance": "119", "tourist_helpline": "050-3816-2720"},
    "India": {"police": "112", "ambulance": "108", "tourist_helpline": "1800-11-1363"},
    "Italy": {"police": "113", "ambulance": "118", "general_eu": "112"},
    "France": {"police": "17", "ambulance": "15", "general_eu": "112"},
    "United States": {"police": "911", "ambulance": "911", "general": "911"},
    "United Kingdom": {"police": "999", "ambulance": "999", "non_emergency": "101"},
    "Thailand": {"police": "191", "ambulance": "1669", "tourist_police": "1155"},
    "Spain": {"police": "091", "ambulance": "061", "general_eu": "112"},
    "Switzerland": {"police": "117", "ambulance": "144", "general_eu": "112"},
    "General / International": {"police": "112 / 911", "ambulance": "112 / 911", "tourist": "Contact Local Hotel Concierge"}
}
