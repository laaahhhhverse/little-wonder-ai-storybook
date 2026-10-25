import os
import random
from io import BytesIO
import streamlit as st
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Little Wonder Storybook", page_icon="📚", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg, #fff8ef 0%, #f4f1ff 100%);}
.hero {padding: .6rem 0 0;}
.hero h1 {color:#44336b; font-size:3rem; margin-bottom:.1rem;}
.hero p {color:#625a75; font-size:1.08rem;}
div[data-testid="stVerticalBlockBorderWrapper"] {background:rgba(255,255,255,.78);}
.stButton button, .stDownloadButton button {border-radius:12px; font-weight:600;}
</style>
""", unsafe_allow_html=True)

cover_path = os.path.join(os.path.dirname(__file__), "assets", "storybook_cover.png")

st.markdown('<div class="hero"><h1>📚 Little Wonder</h1><p>Your imagination, turned into a storybook.</p></div>', unsafe_allow_html=True)
st.write("Create a gentle, child-friendly adventure with a character, a setting, and a little lesson.")

with st.sidebar:
    st.header("✨ Make a story")
    character = st.text_input("Main character", "Milo the little fox")
    theme = st.selectbox("Story theme", ["Friendship", "Courage", "Kindness", "Adventure", "Protecting nature", "Honesty"])
    age = st.selectbox("Age group", ["3–5 years", "6–8 years", "9–12 years"])
    setting = st.text_input("Story setting", "a magical forest")
    moral = st.text_input("Story lesson", "Kindness makes us stronger")
    st.caption("This starter version runs locally without a paid API.")
    make_story = st.button("✨ Create my story", type="primary", use_container_width=True)

def build_demo_story(character, theme, age, setting, moral):
    short = age == "3–5 years"
    if theme == "Friendship":
        challenge = "A shy little bird had lost the way to its nest."
        action = f"{character} listened carefully, then asked a wise owl and two friendly rabbits to help."
        ending = "Together, they found the nest tucked safely in a leafy tree. The bird chirped happily, and a new friendship began."
    elif theme == "Courage":
        challenge = "A tiny lantern had gone dark at the edge of the woods."
        action = f"Even though the path felt unfamiliar, {character} took one small, brave step at a time."
        ending = "With help from the fireflies, the lantern glowed again and lit the path for every animal going home."
    elif theme == "Protecting nature":
        challenge = "A sparkling stream was covered with fallen leaves and litter."
        action = f"{character} invited the forest friends to carefully tidy the riverbank and sort the rubbish."
        ending = "Soon the stream sparkled again, and a family of ducklings paddled through the clear water."
    elif theme == "Honesty":
        challenge = "A shiny red berry basket had tipped over beside the path."
        action = f"{character} told the others what had happened and helped gather every berry."
        ending = "Everyone appreciated the truth, and the friends shared the berries beneath a big old tree."
    elif theme == "Adventure":
        challenge = "A tiny golden map fluttered down from an ancient oak."
        action = f"{character} followed the map's clues, solving gentle puzzles with help from forest friends."
        ending = "The treasure was a little garden of glowing flowers—and a place where everyone could play."
    else:
        challenge = "A new visitor arrived and felt left out of the forest games."
        action = f"{character} welcomed the visitor, shared a favorite game, and invited everyone to join."
        ending = "Soon laughter filled the trees, and the visitor no longer felt alone."

    length = (
        f"One sunny morning in {setting}, {character} discovered something unusual. "
        f"{challenge} "
        f"{action} "
        f"{ending} "
        f"That evening, {character} looked at the stars and felt proud. "
        f"**The lesson:** {moral}."
    )
    if short:
        return f"# {character} and the Forest Surprise\n\n{length}"
    return f"""# {character} and the Forest Surprise

One sunny morning, in {setting}, {character} set off on a little adventure. Birds sang from the branches, and soft golden light danced on the path.

Before long, something unusual happened. {challenge} The forest was quiet, and the little friend needed help.

{action} They worked together, sharing ideas and being patient with one another. When one plan did not work, they tried another.

At last, something wonderful happened. {ending}

As the sky turned pink and purple, {character} headed home feeling happier than ever. The adventure had shown that even a small act can make a big difference.

**The lesson:** {moral}.
"""

if "story" not in st.session_state:
    st.session_state.story = None

if make_story:
    st.session_state.story = build_demo_story(character.strip() or "Milo", theme, age, setting.strip() or "a magical forest", moral.strip() or "Be kind")
    st.session_state.story_title = f"{character.strip() or 'Milo'} and the Forest Surprise"

if st.session_state.story is None:
    left, right = st.columns([1.15, .85], gap="large")
    with left:
        st.subheader("🌟 Start your first adventure")
        st.write("Choose your character and story idea in the sidebar, then press **Create my story**.")
        st.info("The included sample illustration is original artwork created for this project. Demo stories are generated from templates, so no API key is needed.")
    with right:
        st.image(cover_path, use_container_width=True)
else:
    left, right = st.columns([1.15, .85], gap="large")
    with left:
        st.subheader("📖 Your story")
        st.markdown(st.session_state.story)
        st.download_button("⬇️ Download story (.md)", st.session_state.story, file_name="little_wonder_story.md", mime="text/markdown")
    with right:
        st.subheader("🎨 Storybook illustration")
        st.image(cover_path, use_container_width=True)
        st.caption("Sample cover illustration. The story and cover are starter assets; connect an image-generation API later for scene-specific artwork.")
        with open(cover_path, "rb") as f:
            st.download_button("⬇️ Download illustration (.png)", f.read(), file_name="little_wonder_cover.png", mime="image/png")

st.divider()
st.caption("Little Wonder • Beginner-friendly Python project • Please review stories before sharing them with children.")
