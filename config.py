import os


def _require(key: str) -> str:
    val = os.environ.get(key)
    if not val:
        raise RuntimeError(f"Missing required environment variable: {key}")
    return val


# ── Telegram ──────────────────────────────────────────────────────────────────
API_ID: int = int(_require("38056031"))
API_HASH: str = _require("e5c735453082183ed853ccdc97d96e65")
BOT_TOKEN: str = _require("8837623113:AAHhv4GMA8GPkn3D54bj-GP6mrS_YYpjT2o")

# Optional: private channel ID for logging (e.g. -100123456789)
LOG_CHANNEL: int | None = int(os.environ["https://t.me/xgfxkx"]) if os.environ.get("LOG_CHANNEL") else None

# Developer profile URL shown in /start button
DEV_URL: str = os.environ.get("DEV_URL", "https://t.me/xgfxkx")

# ── MongoDB ───────────────────────────────────────────────────────────────────
MONGO_URI: str = _require("mongodb+srv://rupamedical:dQv9oKG7QK93BkIh@james.oufkybu.mongodb.net/?appName=james")
MONGO_DB: str = os.environ.get("MONGO_DB", "apple_music_bot")
