import urllib.request
import ssl

def get_skillicons(icons):
    url = f"https://skillicons.dev/icons?i={icons}&theme=dark"
    # Ignore SSL errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, context=ctx) as response:
        svg_data = response.read().decode('utf-8')
    return svg_data

categories = [
    ("LANGUAGES", "java,kotlin,dart,ts,js,py"),
    ("MOBILE & FRONTEND", "flutter,firebase,react,nextjs"),
    ("BACKEND", "spring,nodejs"),
    ("DATABASES", "postgres,mongodb,redis,mysql"),
    ("DEVOPS", "docker,kubernetes,rabbitmq,git"),
    ("DESIGN", "figma,framer,ps,illustrator")
]

width = 1600
height = 1200

svg_parts = [f'<svg width="100%" viewBox="0 0 {width} {height}" fill="none" xmlns="http://www.w3.org/2000/svg">']

# Background accents (Persona stars)
svg_parts.append('<polygon points="1200,100 1210,130 1240,135 1215,150 1220,180 1195,160 1170,180 1175,150 1150,135 1180,130" fill="#FF1001" opacity="0.8" />')
svg_parts.append('<polygon points="1400,800 1410,830 1440,835 1415,850 1420,880 1395,860 1370,880 1375,850 1350,835 1380,830" fill="#FF1001" opacity="0.6" transform="scale(0.6) translate(500, 300)" />')
svg_parts.append('<polygon points="900,1000 910,1030 940,1035 915,1050 920,1080 895,1060 870,1080 875,1050 850,1035 880,1030" fill="#FFFFFF" opacity="0.2" transform="scale(1.2) translate(-200, -100)" />')

# Giant red left banner
svg_parts.append('<polygon points="50,20 280,5 290,1180 30,1150 70,600" fill="#FF1001" stroke="#FFFFFF" stroke-width="5" stroke-linejoin="round" />')

# Text inside the red banner (vertical, slanted)
svg_parts.append('<g transform="translate(180, 1100) rotate(-90)">')
svg_parts.append('<text x="0" y="0" font-family="Arial Black, Impact, sans-serif" font-weight="900" font-size="120" fill="#000000" letter-spacing="25">THE ARSENAL</text>')
svg_parts.append('<text x="0" y="-85" font-family="Arial Black, Impact, sans-serif" font-weight="900" font-size="120" fill="#FFFFFF" letter-spacing="25" opacity="0.4" transform="translate(10, 10)">THE ARSENAL</text>')
svg_parts.append('</g>')

y_offset = 60
for title, icons in categories:
    # Jagged black strip for category title
    pts = f"350,{y_offset+10} 1200,{y_offset} 1210,{y_offset+60} 340,{y_offset+80}"
    svg_parts.append(f'<polygon points="{pts}" fill="#000000" stroke="#FF1001" stroke-width="4" stroke-linejoin="round" />')
    
    # Category Text
    svg_parts.append(f'<text x="380" y="{y_offset + 55}" font-family="Arial Black, Impact, sans-serif" font-weight="900" font-size="38" fill="#FFFFFF" letter-spacing="4" transform="rotate(-1 380 {y_offset+55})">{title}</text>')
    
    # Fetch skillicons SVG
    icon_svg = get_skillicons(icons)
    
    # Embed inside nested SVG for translation
    svg_parts.append(f'<svg x="370" y="{y_offset + 90}">{icon_svg}</svg>')
    
    y_offset += 190

svg_parts.append('</svg>')

with open('assets/images/TechArsenal.svg', 'w') as f:
    f.write('\n'.join(svg_parts))

print("TechArsenal.svg generated successfully!")
