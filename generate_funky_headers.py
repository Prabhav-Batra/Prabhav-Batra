import math
import random

categories = [
    ("cat_languages.svg", "LANGUAGES", -3),
    ("cat_mobile.svg", "MOBILE & FRONT", 4),
    ("cat_backend.svg", "BACKEND", -2),
    ("cat_databases.svg", "DATABASES", 5),
    ("cat_devops.svg", "DEVOPS", -4),
    ("cat_design.svg", "DESIGN", 3)
]

def generate_svg(filename, text, angle):
    # A funky jagged polygon
    pts = "5,15 280,5 290,45 230,55 120,45 5,55"
    
    svg = f"""<svg width="300" height="60" viewBox="0 0 300 60" fill="none" xmlns="http://www.w3.org/2000/svg">
  <polygon points="{pts}" fill="#000000" stroke="#FF1001" stroke-width="3" stroke-linejoin="round"/>
  <polygon points="10,20 25,50 8,35" fill="#FF1001" />
  <polygon points="270,15 285,45 265,50" fill="#FF1001" />
  <text x="150" y="42" text-anchor="middle" font-family="Arial Black, Impact, sans-serif" font-weight="900" font-size="24" fill="#FFFFFF" transform="rotate({angle} 150 42)" letter-spacing="2">{text}</text>
  <polygon points="40,5 45,15 55,17 47,23 48,33 40,27 32,33 33,23 25,17 35,15" fill="#FF1001" transform="scale(0.5) translate(100, -20)"/>
</svg>"""
    
    with open(f"assets/images/{filename}", "w") as f:
        f.write(svg)

for fn, txt, ang in categories:
    generate_svg(fn, txt, ang)

print("Funky headers generated!")
