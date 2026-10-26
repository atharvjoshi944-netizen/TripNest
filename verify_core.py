"""
Verification script testing database persistence, recommender, clustering, and showcase trips.
"""

import sys
from modules.config import PLATFORM_ID, APP_NAME, CURRENCIES
from modules.storage import init_db, save_trip, list_trips, get_trip, delete_trip
from modules.recommender import recommend_destinations
from modules.clustering import assign_clusters_to_itinerary, compute_overall_transit_score
from modules.llm_service import generate_demo_itinerary, swap_single_slot_ai
from sample_data.showcase_trips import SHOWCASE_TRIPS

def main():
    print(f"Testing {APP_NAME} [Platform ID: {PLATFORM_ID}]")

    # 1. Test Database
    print("\n--- 1. Testing SQLite Database ---")
    init_db()
    for trip in SHOWCASE_TRIPS:
        saved_id = save_trip(trip)
        print(f"Saved showcase trip: {trip['title']} with ID: {saved_id}")

    trips = list_trips()
    print(f"Total trips in database: {len(trips)}")
    assert len(trips) >= 3, "Database should contain at least 3 showcase trips"

    first_trip = get_trip(trips[0]["id"])
    print(f"Retrieved trip: {first_trip['title']} with {len(first_trip['days'])} days")
    assert len(first_trip["days"]) > 0, "Trip should contain parsed days"

    # 2. Test Recommender
    print("\n--- 2. Testing Destination Recommender ---")
    recs = recommend_destinations(
        vibe="Cultural & Historic Heritage",
        budget_tier="Moderate ($$/₹₹)",
        party_type="Couple / Romantic",
        interests=["Historic Landmarks & UNESCO Sites", "Local Street Food & Fine Dining"],
        currency="USD ($)"
    )
    print(f"Recommended {len(recs)} destinations:")
    for r in recs:
        print(f" - {r['city']}, {r['country']}: {r['match_score']}% Match | {r['cost_display']}")
    assert len(recs) == 3, "Should return top 3 recommendations"

    # 3. Test Clustering
    print("\n--- 3. Testing Geographic Clustering & Transit Fatigue Optimization ---")
    clustered = assign_clusters_to_itinerary(first_trip["days"], first_trip["destination"])
    metrics = compute_overall_transit_score(clustered)
    print(f"Transit Efficiency Score: {metrics['score_percent']}%")
    print(f"Backtracking Prevented: {metrics['backtracking_prevented_km']} km")
    print(f"Fatigue Rating: {metrics['fatigue_rating']}")
    assert metrics["score_percent"] > 90, "Transit efficiency score should be > 90%"

    # 4. Test Demo Generator & Slot Swap
    print("\n--- 4. Testing Itinerary Generation & Slot Swapping ---")
    gen_days = generate_demo_itinerary("Barcelona, Spain", 3, "Moderate ($$/₹₹)", "Solo Traveler", "Moderate", "USD ($)", ["Local Street Food & Fine Dining"])
    print(f"Generated {len(gen_days)} clustered days for Barcelona")
    assert len(gen_days) == 3

    # Swap slot
    current_slot = gen_days[0]["slots"]["lunch"]
    print(f"Original Day 1 Lunch: {current_slot['title']}")
    swapped = swap_single_slot_ai("Barcelona, Spain", 1, gen_days[0]["cluster_zone"], "lunch", current_slot, "Swap for organic vegan tapas bar", "USD ($)", "Moderate ($$/₹₹)")
    print(f"Swapped Day 1 Lunch: {swapped['title']} ({swapped['vibe']})")
    assert "organic vegan" in swapped["title"].lower() or "custom" in swapped["title"].lower() or "tapas" in swapped["title"].lower()

    print("\n[SUCCESS] All core backend and logic tests passed with 100% success!")

if __name__ == "__main__":
    main()
