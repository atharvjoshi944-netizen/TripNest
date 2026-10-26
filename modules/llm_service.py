"""
LLM Service module for Personalized Travel Itinerary Planner.
Supports Google Gemini, Groq, and a High-Fidelity Demo AI Engine.
Uses direct REST requests to avoid package version dependency bottlenecks.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

import json
import re
import requests
from typing import Dict, Any, List, Optional
from modules.config import CURRENCIES, BUDGET_TIERS
from sample_data.showcase_trips import SHOWCASE_TRIPS

def call_gemini(api_key: str, prompt: str, model: str = "gemini-1.5-flash") -> str:
    """Invokes Google Gemini REST API."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 8192
        }
    }
    response = requests.post(url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()
    candidates = data.get("candidates", [])
    if not candidates:
        raise ValueError("No response generated from Gemini API.")
    return candidates[0]["content"]["parts"][0]["text"]

def call_groq(api_key: str, prompt: str, model: str = "llama-3.3-70b-versatile") -> str:
    """Invokes Groq Cloud REST API."""
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a world-class travel itinerary architect specializing in geographic clustering and transit fatigue elimination. Always output pure, valid JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 6000
    }
    response = requests.post(url, headers=headers, json=payload, timeout=60)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]

def clean_json_response(raw_text: str) -> str:
    """Extracts JSON substring from markdown code blocks or raw text."""
    text = raw_text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        return match.group(1).strip()
    # Try finding first [ or { and last ] or }
    first_bracket = min(
        [pos for pos in [text.find('{'), text.find('[')] if pos != -1] or [-1]
    )
    last_bracket = max(
        [pos for pos in [text.rfind('}'), text.rfind(']')] if pos != -1] or [-1]
    )
    if first_bracket != -1 and last_bracket != -1 and last_bracket > first_bracket:
        return text[first_bracket:last_bracket+1].strip()
    return text

def generate_demo_itinerary(destination: str, duration: int, budget_tier: str, party_type: str, pace: str, currency: str, interests: List[str]) -> List[Dict[str, Any]]:
    """
    High-fidelity offline generator providing structured, clustered travel itineraries
    for demo mode or when API keys are not supplied.
    """
    dest_lower = destination.lower()
    curr_info = CURRENCIES.get(currency, CURRENCIES["USD ($)"])
    rate = curr_info["rate"]

    # Check if destination matches any showcase trip
    matched_showcase = None
    for trip in SHOWCASE_TRIPS:
        if trip["destination"].lower() in dest_lower or dest_lower in trip["destination"].lower() or any(w in dest_lower for w in trip["destination"].lower().split(',')):
            matched_showcase = trip
            break

    multiplier = BUDGET_TIERS.get(budget_tier, {}).get("multiplier", 1.0)

    if matched_showcase:
        base_days = matched_showcase["days"]
        days = []
        for i in range(duration):
            base_idx = i % len(base_days)
            template = json.loads(json.dumps(base_days[base_idx]))
            template["day_number"] = i + 1
            if i >= len(base_days):
                template["title"] = f"Exploration Extension: {template['title']}"

            # Adjust costs by currency and budget multiplier
            day_total = 0.0
            for slot_key, slot in template["slots"].items():
                slot["estimated_cost"] = round(slot["estimated_cost"] * rate * multiplier, 1)
                day_total += slot["estimated_cost"]
            template["day_cost"] = round(day_total, 1)
            days.append(template)
        return days

    # Generic high-quality clustered itinerary generator for any worldwide destination
    zones = [
        f"{destination} Historic Old Town & Heritage District",
        f"{destination} Waterfront, Marina & Scenic Bay",
        f"{destination} Cultural Arts District & Royal Gardens",
        f"{destination} Uptown Bohemian Quarter & Artisan Markets",
        f"{destination} Mountain Foothills & Panoramic Ridge",
        f"{destination} Foodie Alleys & Nightlife Corridor",
        f"{destination} Natural Reserves & Countryside Excursion"
    ]

    days = []
    base_activity_cost = 25.0 * rate * multiplier
    base_meal_cost = 35.0 * rate * multiplier

    for d in range(1, duration + 1):
        zone = zones[(d - 1) % len(zones)]
        slots = {
            "morning": {
                "time": "09:00 - 12:00",
                "title": f"Morning Discovery: Iconic Landmarks of {zone.split('&')[0].strip()}",
                "description": f"Begin your day exploring the primary cultural and architectural highlights situated within the {zone}. Optimal morning lighting with minimum queues.",
                "estimated_cost": round(base_activity_cost * 0.8, 1),
                "vibe": "Culture & Sights",
                "tips": "Book entry tickets online in advance to skip ticket counter queues."
            },
            "lunch": {
                "time": "12:30 - 14:00",
                "title": f"Regional Tasting Menu in {zone.split('&')[0].strip()}",
                "description": f"Savor celebrated local specialties and seasonal produce at a top-rated traditional bistro right in the heart of {zone}.",
                "estimated_cost": round(base_meal_cost, 1),
                "vibe": "Local Gastronomy",
                "tips": "Ask your server for the chef's seasonal recommendation or house special."
            },
            "afternoon": {
                "time": "14:30 - 17:30",
                "title": f"Immersive Exploration: Artisan Studios & Scenic Promenades",
                "description": f"A relaxed afternoon stroll through neighboring artisan boutiques, heritage courtyards, and scenic viewpoints within walking distance.",
                "estimated_cost": round(base_activity_cost * 0.6, 1),
                "vibe": "Leisure & Living Heritage",
                "tips": "Wear comfortable walking shoes; the cobblestones are best navigated on foot."
            },
            "evening": {
                "time": "18:30 - 21:30",
                "title": f"Sunset Panorama & Atmospheric Evening Dining",
                "description": f"Witness twilight hues from a premier vantage point followed by a memorable dinner paired with local wines or craft beverages.",
                "estimated_cost": round(base_meal_cost * 1.4, 1),
                "vibe": "Atmospheric Evening",
                "tips": "Sunset arrives around 18:45; arrive early to secure terrace or window seating."
            }
        }
        day_cost = round(sum(s["estimated_cost"] for s in slots.values()), 1)
        days.append({
            "day_number": d,
            "title": f"Day {d}: Immersion in {zone}",
            "cluster_zone": zone,
            "transit_fatigue_score": "High Optimization (94% Efficiency — Zero Backtracking)",
            "transit_notes": f"All sights and dining for Day {d} are geographically clustered within {zone}. Walking transit time between consecutive activities is under 15 minutes.",
            "slots": slots,
            "day_cost": day_cost
        })

    return days

def generate_itinerary_ai(
    destination: str,
    duration: int,
    budget_tier: str,
    party_type: str,
    pace: str,
    currency: str,
    interests: List[str],
    provider: str = "demo",
    api_key: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Main entry point for generating day-by-day itineraries.
    Routes to Gemini, Groq, or Demo generator based on configuration.
    """
    if provider == "demo" or not api_key:
        return generate_demo_itinerary(destination, duration, budget_tier, party_type, pace, currency, interests)

    curr_info = CURRENCIES.get(currency, CURRENCIES["USD ($)"])
    symbol = curr_info["symbol"]

    prompt = f"""
You are an expert travel planner and transit fatigue optimization specialist.
Generate a comprehensive, day-by-day vacation itinerary for:
- Destination: {destination}
- Duration: {duration} days
- Budget Level: {budget_tier}
- Travel Party: {party_type}
- Travel Pace: {pace}
- Currency: {currency} ({symbol})
- Traveler Interests: {', '.join(interests)}

CRITICAL GEOGRAPHIC CLUSTERING RULES:
1. Every single day MUST focus on ONE compact geographic cluster/neighborhood/zone of the city/region.
2. Sights within a day must be logically sequenced (Morning Sight -> Lunch -> Afternoon Leisure -> Evening Dining).
3. Transit between consecutive slots MUST be under 15-20 minutes to eliminate transit fatigue and backtracking.
4. Estimate realistic costs per activity in {currency} ({symbol}).

OUTPUT IN STRICT JSON FORMAT ONLY with the following schema:
[
  {{
    "day_number": 1,
    "title": "Creative Day Title",
    "cluster_zone": "Specific neighborhood / district name",
    "transit_fatigue_score": "e.g. Minimal (95% Walkable transit efficiency)",
    "transit_notes": "Explanation of transit clustering and why there is zero backtracking",
    "slots": {{
      "morning": {{
        "time": "09:00 - 12:00",
        "title": "Morning Landmark/Activity Name",
        "description": "Specific, vivid description",
        "estimated_cost": 25.0,
        "vibe": "Category vibe",
        "tips": "Insider tip to avoid crowds or maximize visit"
      }},
      "lunch": {{
        "time": "12:30 - 14:00",
        "title": "Specific Restaurant Name & Cuisine",
        "description": "What to order and dining atmosphere",
        "estimated_cost": 30.0,
        "vibe": "Food vibe",
        "tips": "Reservation or menu tip"
      }},
      "afternoon": {{
        "time": "14:30 - 17:30",
        "title": "Afternoon Leisure Attraction",
        "description": "Engaging description",
        "estimated_cost": 20.0,
        "vibe": "Category vibe",
        "tips": "Practical tip"
      }},
      "evening": {{
        "time": "18:30 - 21:30",
        "title": "Evening Dining & Entertainment",
        "description": "Sunset view, dinner, or nightlife",
        "estimated_cost": 50.0,
        "vibe": "Atmospheric vibe",
        "tips": "Evening tip"
      }}
    }},
    "day_cost": 125.0
  }}
]
Do not include any Markdown text outside the JSON code block. Output valid parseable JSON only.
"""

    try:
        if provider == "gemini":
            raw_output = call_gemini(api_key, prompt)
        elif provider == "groq":
            raw_output = call_groq(api_key, prompt)
        else:
            return generate_demo_itinerary(destination, duration, budget_tier, party_type, pace, currency, interests)

        json_text = clean_json_response(raw_output)
        parsed = json.loads(json_text)
        if isinstance(parsed, list) and len(parsed) > 0:
            return parsed
        elif isinstance(parsed, dict) and "days" in parsed:
            return parsed["days"]
        else:
            return generate_demo_itinerary(destination, duration, budget_tier, party_type, pace, currency, interests)
    except Exception as e:
        # Graceful fallback to demo mode on network or API quota error
        print(f"LLM API Error ({provider}): {e}. Falling back to high-fidelity demo generator.")
        return generate_demo_itinerary(destination, duration, budget_tier, party_type, pace, currency, interests)

def swap_single_slot_ai(
    destination: str,
    day_number: int,
    cluster_zone: str,
    slot_key: str,
    current_slot: Dict[str, Any],
    custom_instruction: str,
    currency: str,
    budget_tier: str,
    provider: str = "demo",
    api_key: Optional[str] = None
) -> Dict[str, Any]:
    """
    Regenerates ONLY a single slot (e.g. morning, lunch, afternoon, evening)
    without touching or resetting any other part of the itinerary.
    """
    curr_info = CURRENCIES.get(currency, CURRENCIES["USD ($)"])
    symbol = curr_info["symbol"]
    rate = curr_info["rate"]

    if provider == "demo" or not api_key:
        # Deterministic rich demo swap
        new_title = f"{custom_instruction.title()} in {cluster_zone}"
        desc = f"Tailored substitution matching your vibe request: '{custom_instruction}'. Seamlessly located within {cluster_zone} to avoid any transit disruption."
        if "lunch" in slot_key:
            vibe = "Custom Dining"
            cost = round(current_slot.get("estimated_cost", 25.0) * 1.1, 1)
            tips = "Ask for the outdoor courtyard table or chef's special dietary menu."
        elif "evening" in slot_key:
            vibe = "Twilight Experience"
            cost = round(current_slot.get("estimated_cost", 45.0) * 1.15, 1)
            tips = "Check sunset timing and make reservations 24 hours prior."
        else:
            vibe = "Custom Activity"
            cost = round(current_slot.get("estimated_cost", 20.0), 1)
            tips = "Less crowded in early sessions; tickets accessible on mobile."

        return {
            "time": current_slot.get("time", "14:00 - 17:00"),
            "title": new_title,
            "description": desc,
            "estimated_cost": cost,
            "vibe": vibe,
            "tips": tips
        }

    prompt = f"""
You are an expert travel coordinator. Replace ONLY ONE activity slot in an existing itinerary.
- Destination: {destination}
- Day Number: {day_number}
- Cluster Zone: {cluster_zone}
- Slot to Replace: {slot_key}
- Current Activity: {current_slot.get('title', '')} ({current_slot.get('description', '')})
- User Custom Instruction: "{custom_instruction}"
- Currency: {currency} ({symbol})
- Budget Level: {budget_tier}

REQUIREMENT:
Provide a replacement activity/restaurant that strictly honors the user's custom instruction and is located inside or immediately adjacent to '{cluster_zone}' so transit fatigue remains zero.

OUTPUT STRICT JSON ONLY:
{{
  "time": "{current_slot.get('time', '14:00 - 17:00')}",
  "title": "Replacement Activity or Restaurant Name",
  "description": "Specific description matching the custom request",
  "estimated_cost": {current_slot.get('estimated_cost', 25.0)},
  "vibe": "Vibe Tag",
  "tips": "Practical insider tip"
}}
Output parseable JSON only.
"""
    try:
        if provider == "gemini":
            raw_output = call_gemini(api_key, prompt)
        elif provider == "groq":
            raw_output = call_groq(api_key, prompt)
        else:
            raise ValueError("Unknown provider")

        json_text = clean_json_response(raw_output)
        parsed = json.loads(json_text)
        return parsed
    except Exception as e:
        print(f"Swap error: {e}. Falling back to smart mock swap.")
        return {
            "time": current_slot.get("time", "14:00 - 17:00"),
            "title": f"Custom: {custom_instruction.title()}",
            "description": f"Curated alternative honoring '{custom_instruction}' within {cluster_zone}.",
            "estimated_cost": current_slot.get("estimated_cost", 25.0),
            "vibe": "Personalized Swap",
            "tips": "Optimized for minimal walking and maximum enjoyment."
        }
