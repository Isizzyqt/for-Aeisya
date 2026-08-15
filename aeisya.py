import base64
from datetime import date
import os
import random
import streamlit as st
import streamlit.components.v1 as components
from streamlit_extras.let_it_rain import rain

# -----------------------------------------------------------------------------
# 1. PAGE SETUP & CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Nur Aeisya Khadeeja !", page_icon="🐘", layout="centered"
)


# Smart background function that finds your picture regardless of hidden file extensions
def set_local_bg():
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Search for any file in the folder starting with 'bg'
    bg_files = [
        f
        for f in os.listdir(script_dir)
        if f.lower().startswith("bg") and f != "aeisya.py"
    ]

    if not bg_files:
        return

    image_path = os.path.join(script_dir, bg_files[0])

    with open(image_path, "rb") as f:
        encoded_string = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url("data:image/jpeg;base64,{encoded_string}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# Apply background automatically
set_local_bg()

# Secret Passcode Lock
passcode = st.text_input("enter our secret passcode 🔒:", type="password")
if passcode != "aeisyakhadeeja":  # Replace 'aeisyakhadeeja' with your choice of passcode
    st.warning("please enter the correct passcode to view my app !")
    st.stop()  # Halts script execution until the correct passcode is typed
else :
    st.success("welcome my love ! 🤍")
    

# -----------------------------------------------------------------------------
# 2. DATA & CONSTANTS
# -----------------------------------------------------------------------------
MY_EMOJIS = ["💖", "❤️", "🥰", "🐘", "✨", "🌸", "🧸", "💌"]

REASONS = [
    "you make me feel alive again and again.",
    "your smiles makes me melt everytime i see them.",
    "you always makes me laugh with your silly jokes.",
    "your eyes is so beautiful, i could stare at them for hours.",
    "your laugh is so contagious, it makes me happy everytime i hear it.",
    "you always gave me the best advices and support me in everything i do.",
    "your advices also shaping me into a better person.",
    "you healed me from my past trauma and made me feel loved again.",
    "you always bringing out my inner child and make me feel like a kid again.",
    "you handle certain situations with so much consideration and maturity, it makes me admire you even more.",
    "you tried your best to make me feel loved and appriciated even though this is your first time.",
]

SPOTIFY_PLAYLIST_URL = "https://open.spotify.com/playlist/2x55Zni07pIAIlxN0KJyQi"

# -----------------------------------------------------------------------------
# 3. SESSION STATE (MEMORY)
# -----------------------------------------------------------------------------
if "reason_index" not in st.session_state:
    st.session_state.reason_index = 0

# -----------------------------------------------------------------------------
# 4. APP HEADER & DAYS COUNTER
# -----------------------------------------------------------------------------
st.title("Nur Aeisya Khadeeja !")

start_date = date(2026, 6, 9)
days_together = (date.today() - start_date).days

st.metric(
    label="days you've been in my life 🗓️", value=f"{days_together} Days !"
)
st.write("---")

# -----------------------------------------------------------------------------
# 5. BUTTONS SIDE-BY-SIDE
# -----------------------------------------------------------------------------
col1, col2 = st.columns(2)

# --- COLUMN 1: Reasons in Order ---
with col1:
    st.write("reasons why I like you...")
    if st.button("tap hereee !", use_container_width=True):
        selected_emoji = random.choice(MY_EMOJIS)
        rain(
            emoji=selected_emoji,
            font_size=45,
            falling_speed=4,
            animation_length=1,
        )

        current_reason = REASONS[st.session_state.reason_index]
        st.info(
            f"Reason #{st.session_state.reason_index + 1}: {current_reason}"
        )

        # Check if the counter hit the final reason
        if st.session_state.reason_index == len(REASONS) - 1:
            st.info(
                "thank you for being in my life, dee ! as more memories we create, more reasons to come ! i promise that."
            )

        # Increment index and loop back to start on next tap
        st.session_state.reason_index = (
            st.session_state.reason_index + 1
        ) % len(REASONS)

# --- COLUMN 2: Send a Hug ---
with col2:
    st.write("if you're having a bad day...")
    if st.button("send dee a hug now 🫂", use_container_width=True):
        rain(
            emoji="🫂",
            font_size=50,
            falling_speed=3,
            animation_length=1,
        )
        st.success("sabar yaa dee, everything will be okay !")

# -----------------------------------------------------------------------------
# 6. SPOTIFY PLAYLIST SECTION
# -----------------------------------------------------------------------------
st.write("---")
st.write("### songs that remind me of you 🎶")

embed_code = """
<iframe style="border-radius:12px" 
        src="https://open.spotify.com/embed/playlist/2x55Zni07pIAIlxN0KJyQi?utm_source=generator" 
        width="100%" 
        height="352" 
        frameBorder="0" 
        allowfullscreen="" 
        allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" 
        loading="lazy">
</iframe>
"""
components.html(embed_code, height=360)

st.link_button(
    "open playlist on spotify 🎧",
    SPOTIFY_PLAYLIST_URL,
    use_container_width=True,
)

# -----------------------------------------------------------------------------
# 7. PHOTO GALLERY (OUR MOMENTS TOGETHER)
# -----------------------------------------------------------------------------
st.write("---")
st.write("### our favorite memories 📸")

# 2-column grid layout for m1 to m14
pic_col1, pic_col2 = st.columns(2)

with pic_col1:
    try:
        st.image(
            "m1.jpg", caption="the day you really caught my attention.", use_container_width=True
        )
    except Exception:
        st.info("Add m1.jpg into your folder!")

    try:
        st.image(
            "m2.jpg",
            caption="our first time eating together !",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m6.jpg",
            caption="another day we spent together, the potato spud is amazing !",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m7.jpg",
            caption="this is your favourite picture of me and you always tease me about it !",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m8.jpg",
            caption="kemeja you gave me, it looks so good on me !",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m9.jpg",
            caption="it really does look like me...",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m13.jpg",
            caption="thank you for the birthday surprise, dee !",
            use_container_width=True,
        )
    except Exception:
        pass

with pic_col2:
    try:
        st.image(
            "m3.jpg", caption="our first selfie together !", use_container_width=True
        )
    except Exception:
        pass

    try:
        st.image(
            "m4.jpg",
            caption="your birthday !",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m5.jpg",
            caption="you with your presents, this is my background for a while !",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m10.jpg",
            caption="the pashmina looks so good on you !",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m11.jpg",
            caption="i suprised you with a lego flower set, you both look great !",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m12.jpg",
            caption="i suprised you with a flower again, but this time it's a real one !",
            use_container_width=True,
        )
    except Exception:
        pass

    try:
        st.image(
            "m14.jpg",
            caption="you look so pretty !",
            use_container_width=True,
        )
    except Exception:
        pass

# Centered final special memory (m15)
center_left, center_mid, center_right = st.columns([1, 2, 1])

with center_mid:
    try:
        st.image(
            "m15.jpg",
            caption="this is my favourite picture of us for now. i love you dee !",
            use_container_width=True,
        )
    except Exception:
        pass