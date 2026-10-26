"""
Storage module handling local SQLite persistence and JSON fallback for trips.
Zero external DB dependencies for seamless local and cloud deployment.
"""

import sqlite3
import json
import os
import uuid
from datetime import datetime

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "trips.db")

def get_connection():
    """Returns a connection to the SQLite database with row factory."""
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the SQLite schema if it doesn't already exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trips (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            destination TEXT NOT NULL,
            duration INTEGER NOT NULL,
            start_date TEXT,
            end_date TEXT,
            budget_tier TEXT NOT NULL,
            party_type TEXT NOT NULL,
            pace TEXT NOT NULL,
            currency TEXT NOT NULL,
            created_at TEXT NOT NULL,
            itinerary_json TEXT NOT NULL,
            transit_summary TEXT,
            estimated_total_cost REAL,
            vibe_tag TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_trip(trip: dict) -> str:
    """
    Saves a new trip or updates an existing trip.
    Returns the trip ID.
    """
    init_db()
    conn = get_connection()
    cursor = conn.cursor()

    trip_id = trip.get("id") or str(uuid.uuid4())[:8]
    created_at = trip.get("created_at") or datetime.now().strftime("%Y-%m-%d %H:%M")
    itinerary_json = json.dumps(trip.get("days", []), ensure_ascii=False)

    cursor.execute("""
        INSERT OR REPLACE INTO trips (
            id, title, destination, duration, start_date, end_date,
            budget_tier, party_type, pace, currency, created_at,
            itinerary_json, transit_summary, estimated_total_cost, vibe_tag
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        trip_id,
        trip.get("title", f"Trip to {trip.get('destination', 'Paradise')}"),
        trip.get("destination", "Unknown"),
        int(trip.get("duration", len(trip.get("days", [])))),
        trip.get("start_date", ""),
        trip.get("end_date", ""),
        trip.get("budget_tier", "Moderate ($$/₹₹)"),
        trip.get("party_type", "Solo Traveler"),
        trip.get("pace", "Moderate"),
        trip.get("currency", "USD ($)"),
        created_at,
        itinerary_json,
        trip.get("transit_summary", ""),
        float(trip.get("estimated_total_cost", 0.0)),
        trip.get("vibe_tag", "Wanderlust")
    ))
    conn.commit()
    conn.close()
    return trip_id

def list_trips() -> list:
    """Returns a list of all saved trips sorted by creation date descending."""
    init_db()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, destination, duration, start_date, budget_tier, party_type, pace, currency, created_at, estimated_total_cost, vibe_tag FROM trips ORDER BY created_at DESC")
    rows = cursor.fetchall()
    trips = []
    for r in rows:
        trips.append({
            "id": r["id"],
            "title": r["title"],
            "destination": r["destination"],
            "duration": r["duration"],
            "start_date": r["start_date"],
            "budget_tier": r["budget_tier"],
            "party_type": r["party_type"],
            "pace": r["pace"],
            "currency": r["currency"],
            "created_at": r["created_at"],
            "estimated_total_cost": r["estimated_total_cost"],
            "vibe_tag": r["vibe_tag"]
        })
    conn.close()
    return trips

def get_trip(trip_id: str) -> dict:
    """Retrieves full trip details including parsed itinerary JSON."""
    init_db()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trips WHERE id = ?", (trip_id,))
    row = cursor.fetchone()
    conn.close()
    if not row:
        return None

    return {
        "id": row["id"],
        "title": row["title"],
        "destination": row["destination"],
        "duration": row["duration"],
        "start_date": row["start_date"],
        "end_date": row["end_date"],
        "budget_tier": row["budget_tier"],
        "party_type": row["party_type"],
        "pace": row["pace"],
        "currency": row["currency"],
        "created_at": row["created_at"],
        "days": json.loads(row["itinerary_json"]),
        "transit_summary": row["transit_summary"],
        "estimated_total_cost": row["estimated_total_cost"],
        "vibe_tag": row["vibe_tag"]
    }

def delete_trip(trip_id: str) -> bool:
    """Deletes a trip by ID."""
    init_db()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM trips WHERE id = ?", (trip_id,))
    deleted = cursor.rowcount > 0
    conn.commit()
    conn.close()
    return deleted
