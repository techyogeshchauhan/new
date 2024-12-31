import streamlit as st
import time
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Function to create a GIF animation for Happy New Year
def create_happy_new_year_gif(output_file, frame_count=30, width=500, height=300):
    frames = []
    font = ImageFont.truetype("arial.ttf", 40)

    for i in range(frame_count):
        img = Image.new("RGB", (width, height), "black")
        draw = ImageDraw.Draw(img)

        # Background animation with gradient
        gradient = np.linspace(0, 255, width).astype(np.uint8)
        gradient = np.tile(gradient, (height, 1))
        for y in range(height):
            color = (gradient[y][0], 0, gradient[y][0])
            draw.line([(0, y), (width, y)], fill=color, width=1)

        # Animation effect: Pulsating text
        scale = 1.5 + 0.5 * np.sin(2 * np.pi * i / frame_count)
        font_size = int(40 * scale)
        dynamic_font = ImageFont.truetype("arial.ttf", font_size)

        text_color = (255, 255, int(255 * abs(np.sin(2 * np.pi * i / frame_count))))
        text = "Happy New Year!"
        text_bbox = draw.textbbox((0, 0), text, font=dynamic_font)
        text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]
        text_position = ((width - text_width) // 2, (height - text_height) // 2)

        draw.text(text_position, text, fill=text_color, font=dynamic_font)

        # Add sparkle effect
        for _ in range(20):
            sparkle_x = np.random.randint(0, width)
            sparkle_y = np.random.randint(0, height)
            sparkle_color = (255, 255, 255) if np.random.rand() > 0.5 else (255, 215, 0)
            draw.ellipse([(sparkle_x, sparkle_y), (sparkle_x + 2, sparkle_y + 2)], fill=sparkle_color)

        frames.append(img)

    frames[0].save(
        output_file,
        save_all=True,
        append_images=frames[1:],
        optimize=False,
        duration=100,
        loop=0,
    )

# Create the Happy New Year animation
output_file = "happy_new_year.gif"
create_happy_new_year_gif(output_file)

# Streamlit app
st.title("Happy New Year Animation 🎉")
st.markdown(
    """<style>
    .stApp {
        background-color: #1a1a1a;
        color: white;
    }
    </style>""",
    unsafe_allow_html=True,
)
st.write("Greeting for the New Year!")

# Display GIF animation
if output_file:
    st.image(output_file, caption="Happy New Year! 🎉")

st.write("Wishing you a fantastic year ahead! ✨")
