# --- vercel bootstrap: fallback DB + disable heavy ML (paste at top of main1.py) ---
import os

# If developer hasn't provided a DB URI in Vercel, use a local SQLite file
# so the app runs without an external DB. The SQLite file is ephemeral on Vercel.
if not os.environ.get("SQLALCHEMY_DATABASE_URI"):
    os.environ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vercel.db"

# Prevent heavy ML model imports on cold start when not needed.
# Recommended: set DISABLE_AI=1 in Vercel Environment Variables.
DISABLE_AI = os.environ.get("DISABLE_AI", "0") == "1"
if DISABLE_AI:
    print("DISABLE_AI=1 -> skipping heavy ML imports and model loading")
# --- end bootstrap ---
