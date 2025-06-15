
# 🤖 Instagram Auto Following Bot (Python)

This project is a Python-based Instagram **auto-following bot** using [`instagrapi`](https://github.com/adw0rd/instagrapi). It lets you automatically follow the followers of specific users in a way that mimics human activity — with randomized delays, private account checks, and rate limit handling.

> ⚠️ **Disclaimer**: This script violates Instagram’s [Terms of Use](https://help.instagram.com/581066165581870). Use at your own risk, and only for learning or testing on alternate accounts.

---

## 🚀 Features

- 🔐 Secure login via environment variables
- ⏱️ Random human-like delay between follows
- 🚫 Skips private or inactive users
- 📉 Handles Instagram rate limiting
- 🔧 Easy customization (target users, limits, delays)

---

## 📁 File Structure

```

instagram-auto-following/
├── insta_auto_following.py 
└── README.md               

````

---

## 🧰 Requirements

- Python 3.7 to 3.10
- `instagrapi` library (uses Instagram’s private API)

Install it:

```bash
pip install instagrapi
````

---

## 🔐 Setup & Run

1. **Clone the repo:**

```bash
git clone https://github.com/nafiul-afk/instagram-auto-following.git
cd instagram-auto-following
```

2. **Set Instagram credentials as environment variables:**

On **Linux/macOS**:

```bash
export IG_USERNAME='your_instagram_username'
export IG_PASSWORD='your_instagram_password'
```

On **Windows (CMD)**:

```cmd
set IG_USERNAME=your_instagram_username
set IG_PASSWORD=your_instagram_password
```

3. **Run the bot:**

```bash
python insta_auto_following.py
```

---

## ⚙️ Configuration Inside the Script

Open `insta_auto_following.py` and edit the top section:

```python
# --- CONFIGURATION ---
TARGET_USERS = ["natgeo", "python.learning"]  # Usernames to target
FOLLOW_LIMIT = 20         # Total users to follow
FOLLOW_PER_TARGET = 10    # Max followers to follow per target
DELAY_RANGE = (15, 40)    # Random delay in seconds between follows
```

---

## 🧠 How It Works

* Logs in using `instagrapi.Client()`
* Gets followers of users in `TARGET_USERS`
* Skips private or empty accounts
* Randomly waits `15–40` seconds between each follow
* Stops if it reaches `FOLLOW_LIMIT` or if Instagram rate-limits the account

---

