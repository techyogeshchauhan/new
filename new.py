import streamlit as st
import time
from PIL import Image, ImageDraw, ImageFont
import numpy as np
from datetime import datetime

def create_festive_animation(output_file, frame_count=40, width=600, height=400):
    frames = []
    current_year = datetime.now().year

    for i in range(frame_count):
        img = Image.new("RGB", (width, height), "black")
        draw = ImageDraw.Draw(img)

        # Animated starry background
        for _ in range(100):
            star_x = np.random.randint(0, width)
            star_y = np.random.randint(0, height)
            brightness = int(255 * abs(np.sin(2 * np.pi * (i / frame_count + np.random.rand()))))
            draw.point((star_x, star_y), fill=(brightness, brightness, brightness))

        # Dynamic text effects
        scale = 1.3 + 0.3 * np.sin(2 * np.pi * i / frame_count)
        main_font_size = int(50 * scale)
        main_font = ImageFont.truetype("arial.ttf", main_font_size)
        sub_font = ImageFont.truetype("arial.ttf", 30)

        # Main greeting with color animation
        main_text = f"Happy New Year {current_year}!"
        color_r = int(255 * abs(np.sin(2 * np.pi * i / frame_count)))
        color_g = int(255 * abs(np.sin(2 * np.pi * (i / frame_count + 0.33))))
        color_b = int(255 * abs(np.sin(2 * np.pi * (i / frame_count + 0.66))))
        
        # Center the main text
        main_bbox = draw.textbbox((0, 0), main_text, font=main_font)
        main_width = main_bbox[2] - main_bbox[0]
        main_x = (width - main_width) // 2
        draw.text((main_x, 100), main_text, fill=(color_r, color_g, color_b), font=main_font)

        # Personal message with fade effect
        wishes = [
            "Best Wishes, You!",
            "May all your dreams come true",
            "Success and happiness ahead"
        ]
        
        for idx, wish in enumerate(wishes):
            opacity = int(255 * abs(np.sin(2 * np.pi * (i / frame_count + idx * 0.2))))
            wish_bbox = draw.textbbox((0, 0), wish, font=sub_font)
            wish_width = wish_bbox[2] - wish_bbox[0]
            wish_x = (width - wish_width) // 2
            draw.text((wish_x, 200 + idx * 50), wish, fill=(255, 255, opacity), font=sub_font)

        # Firework effects
        for _ in range(5):
            center_x = np.random.randint(0, width)
            center_y = np.random.randint(0, height)
            for angle in range(0, 360, 30):
                length = 20 * np.random.rand()
                end_x = center_x + length * np.cos(np.radians(angle))
                end_y = center_y + length * np.sin(np.radians(angle))
                draw.line([(center_x, center_y), (end_x, end_y)], 
                         fill=(255, 215, 0), width=2)

        frames.append(img)

    frames[0].save(output_file, save_all=True, append_images=frames[1:],
                  optimize=False, duration=80, loop=0)

# Streamlit app with enhanced styling
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1a1a1a 0%, #0a192f 100%);
        color: white;
    }
    h1 {
        text-align: center;
        background: linear-gradient(45deg, #FFD700, #FFA500);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        padding: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✨ Magical New Year Wishes ✨")

# Create and display animation
output_file = "festive_new_year.gif"
create_festive_animation(output_file)
st.image(output_file, use_container_width=True)

# Additional festive messages
st.markdown("""
    <div style='text-align: center; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 10px;'>
        <h2 style='color: #FFD700;'>Dear You</h2>
        <p style='color: #E0E0E0; font-size: 18px;'>
            May the coming year bring you endless opportunities and beautiful moments.
            Wishing you 365 days of success, happiness, and prosperity!
        </p>
    </div>
    """, unsafe_allow_html=True)