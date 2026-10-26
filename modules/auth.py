"""
Authentication and User Session Management for Wanderlust AI.
Provides local user persistence, session tracking, and demo authentication.
Platform ID: 6ac33976fb8fc7965cd9236d
"""

import sqlite3
import os
import hashlib
from typing import Optional, Dict, Any

DB_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "trips.db")

def init_auth_db():
    """Initializes users table in SQLite database."""
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            tier TEXT DEFAULT 'Wanderlust Explorer',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()

    # Create default demo user if not exists
    cursor.execute("SELECT * FROM users WHERE email = ?", ("demo@wanderlust.ai",))
    if not cursor.fetchone():
        demo_pwd_hash = hashlib.sha256("wanderlust123".encode()).hexdigest()
        cursor.execute("""
            INSERT INTO users (id, name, email, password_hash, tier)
            VALUES (?, ?, ?, ?, ?)
        """, ("user-demo-01", "Alex Morgan", "demo@wanderlust.ai", demo_pwd_hash, "Wanderlust Pro Member"))
        conn.commit()
    conn.close()

def hash_password(password: str) -> str:
    """Returns SHA-256 hash of password."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate_user(email: str, password: str) -> Optional[Dict[str, Any]]:
    """Authenticates a user by email and password."""
    init_auth_db()
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    pwd_hash = hash_password(password)
    cursor.execute("SELECT * FROM users WHERE email = ? AND password_hash = ?", (email.strip().lower(), pwd_hash))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row["id"],
            "name": row["name"],
            "email": row["email"],
            "tier": row["tier"]
        }
    return None

def register_user(name: str, email: str, password: str) -> Dict[str, Any]:
    """Registers a new user and returns user info."""
    init_auth_db()
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    cursor = conn.cursor()
    user_id = f"user-{hashlib.md5(email.encode()).hexdigest()[:8]}"
    pwd_hash = hash_password(password)
    try:
        cursor.execute("""
            INSERT INTO users (id, name, email, password_hash, tier)
            VALUES (?, ?, ?, ?, ?)
        """, (user_id, name.strip(), email.strip().lower(), pwd_hash, "Wanderlust Explorer"))
        conn.commit()
        conn.close()
        return {"success": True, "user": {"id": user_id, "name": name, "email": email, "tier": "Wanderlust Explorer"}}
    except sqlite3.IntegrityError:
        conn.close()
        return {"success": False, "error": "An account with this email already exists."}
