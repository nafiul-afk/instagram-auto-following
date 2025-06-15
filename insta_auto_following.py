import os
import time
import random
from instagrapi import Client
from instagrapi.exceptions import LoginRequired, RateLimitError, ChallengeRequired

# --- CONFIGURATION ---
TARGET_USERS = ["natgeo", "python.learning"]
FOLLOW_LIMIT = 20
FOLLOW_PER_TARGET = 10
DELAY_RANGE = (15, 40)

# --- LOGIN SETUP ---
USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

if not USERNAME or not PASSWORD:
    raise Exception("❌ Please set IG_USERNAME and IG_PASSWORD as environment variables.")

cl = Client()

try:
    cl.login(USERNAME, PASSWORD)
except (LoginRequired, ChallengeRequired) as e:
    print("⚠️ Login issue or verification required. Resolve it in the Instagram app.")
    raise e

print(f"✅ Logged in as @{USERNAME}")

# --- AUTO-FOLLOW LOGIC ---
total_followed = 0

for target in TARGET_USERS:
    if total_followed >= FOLLOW_LIMIT:
        break

    try:
        target_user_id = cl.user_id_from_username(target)
        followers = cl.user_followers(target_user_id, amount=FOLLOW_PER_TARGET)

        for user_id, user_info in followers.items():
            if total_followed >= FOLLOW_LIMIT:
                break

            if user_info.is_private or user_info.media_count == 0:
                print(f"⏭️ Skipped @{user_info.username} (private or inactive)")
                continue

            try:
                cl.user_follow(user_id)
                print(f"✅ Followed @{user_info.username}")
                total_followed += 1
                time.sleep(random.randint(*DELAY_RANGE))
            except RateLimitError:
                print("🚨 Rate limit hit. Pausing for 1 hour...")
                time.sleep(3600)
            except Exception as e:
                print(f"❌ Failed to follow @{user_info.username}: {e}")

    except Exception as e:
        print(f"❌ Error with target @{target}: {e}")

print(f"🎉 Finished! Total users followed: {total_followed}")
