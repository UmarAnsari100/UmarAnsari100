import os

def create_lanyard():
    b64_path = r"d:\github\assets\character_b64.txt"
    if os.path.exists(b64_path):
        with open(b64_path, "r") as f:
            b64_data = f.read().strip()
    else:
        b64_data = ""

    lanyard_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 540" width="100%" height="auto">
  <defs>
    <style type="text/css">
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@500;700&amp;family=Inter:wght@400;500;600;700&amp;family=Space+Grotesk:wght@600;700&amp;display=swap');

      .font-heading {{ font-family: 'Space Grotesk', -apple-system, sans-serif; }}
      .font-mono {{ font-family: 'IBM Plex Mono', monospace; }}
      .font-sans {{ font-family: 'Inter', -apple-system, sans-serif; }}

      .badge-glass {{
        fill: rgba(20, 20, 20, 0.78);
        stroke: rgba(255, 180, 70, 0.35);
        stroke-width: 1.5px;
        backdrop-filter: blur(25px);
        filter: drop-shadow(0 25px 50px rgba(0, 0, 0, 0.65));
      }}

      .lanyard-strap {{
        fill: none;
        stroke: url(#strapGrad);
        stroke-width: 14;
        stroke-linecap: round;
      }}

      .status-pulse {{
        animation: pulseDot 2s ease-in-out infinite;
      }}
      @keyframes pulseDot {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.4; transform: scale(1.3); }}
      }}

      .holo-sweep {{
        animation: shineSweep 4s ease-in-out infinite;
      }}
      @keyframes shineSweep {{
        0% {{ transform: translateX(-350px) rotate(25deg); opacity: 0; }}
        20% {{ opacity: 0.5; }}
        50% {{ transform: translateX(350px) rotate(25deg); opacity: 0; }}
        100% {{ opacity: 0; }}
      }}
    </style>

    <linearGradient id="strapGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#151515"/>
      <stop offset="50%" stop-color="#D97706"/>
      <stop offset="100%" stop-color="#FFB347"/>
    </linearGradient>

    <linearGradient id="badgeGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFB347"/>
      <stop offset="50%" stop-color="#F7C873"/>
      <stop offset="100%" stop-color="#D97706"/>
    </linearGradient>

    <linearGradient id="clipMetal" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#E4E4E7"/>
      <stop offset="50%" stop-color="#71717A"/>
      <stop offset="100%" stop-color="#27272A"/>
    </linearGradient>

    <linearGradient id="holoGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(255, 255, 255, 0)"/>
      <stop offset="50%" stop-color="rgba(255, 248, 240, 0.45)"/>
      <stop offset="100%" stop-color="rgba(255, 255, 255, 0)"/>
    </linearGradient>

    <clipPath id="avatarClip">
      <circle cx="50" cy="50" r="47" />
    </clipPath>

    <clipPath id="badgeCardClip">
      <rect width="320" height="430" rx="20" />
    </clipPath>
  </defs>

  <!-- Animated Pendulum Physics Sway Loop -->
  <g>
    <animateTransform attributeName="transform" type="rotate" values="-2.5 200 0; 2.5 200 0; -2.5 200 0" dur="11s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1; 0.4 0 0.6 1"/>

    <!-- Lanyard Straps -->
    <path d="M 155,-20 L 192,55" class="lanyard-strap" />
    <path d="M 245,-20 L 208,55" class="lanyard-strap" />

    <!-- Brushed Metal Clasp & Ring -->
    <rect x="184" y="45" width="32" height="24" rx="5" fill="url(#clipMetal)" stroke="#18181B" stroke-width="1.2"/>
    <circle cx="200" cy="57" r="5" fill="#09090B"/>
    <rect x="193" y="67" width="14" height="20" rx="3" fill="url(#clipMetal)"/>

    <!-- ID Badge Group -->
    <g transform="translate(40, 85)">
      <g clip-path="url(#badgeCardClip)">
        <!-- Main Badge Container -->
        <rect width="320" height="430" rx="20" class="badge-glass" />
        
        <!-- Top Accent Banner Strip -->
        <path d="M 0,20 Q 0,0 20,0 L 300,0 Q 320,0 320,20 L 320,42 L 0,42 Z" fill="url(#badgeGold)" />
        <text x="160" y="27" text-anchor="middle" fill="#151515" font-size="11" font-weight="700" class="font-mono" letter-spacing="2">OFFICIAL PASSPORT</text>

        <!-- Clip Slot Cutout -->
        <rect x="135" y="10" width="50" height="8" rx="4" fill="#0D0D0D" />

        <!-- Avatar Photo with Glowing Gold Ring -->
        <g transform="translate(110, 65)">
          <rect width="100" height="100" rx="50" fill="rgba(30, 30, 30, 0.9)" stroke="url(#badgeGold)" stroke-width="2.5"/>
          <image href="data:image/png;base64,{b64_data}" x="-20" y="-10" width="140" height="140" clip-path="url(#avatarClip)" />
        </g>

        <!-- Developer Details -->
        <g text-anchor="middle" transform="translate(160, 192)">
          <text x="0" y="0" fill="#FFFFFF" font-size="20" font-weight="700" class="font-heading">Muhammad Umar</text>
          <text x="0" y="24" fill="#F7C873" font-size="18" font-weight="700" class="font-heading">Ansari</text>
          
          <text x="0" y="48" fill="#FFB347" font-size="12" font-weight="600" class="font-sans">Full-Stack Web Developer</text>
          <text x="0" y="64" fill="#94A3B8" font-size="10" font-weight="500" class="font-mono">@UmarAnsari100</text>
          
          <rect x="-110" y="76" width="220" height="1" fill="rgba(255, 180, 70, 0.2)"/>
          
          <text x="0" y="96" fill="#E2E8F0" font-size="11" font-weight="500" class="font-sans">BS Computer Science</text>
          <text x="0" y="112" fill="#94A3B8" font-size="10" class="font-sans">HITEC University, Taxila</text>
          <text x="0" y="132" fill="#CBD5E1" font-size="10" class="font-sans">📍 Rawalpindi, Pakistan</text>
        </g>

        <!-- Availability Status Badge -->
        <g transform="translate(60, 348)">
          <rect x="0" y="0" width="200" height="28" rx="14" fill="rgba(39, 201, 63, 0.15)" stroke="#27C93F" stroke-width="1.2"/>
          <circle cx="20" cy="14" r="4" fill="#27C93F" class="status-pulse"/>
          <text x="32" y="18" fill="#4ADE80" font-size="10" font-weight="700" class="font-mono" letter-spacing="0.5">OPEN TO OPPORTUNITIES</text>
        </g>

        <!-- Micro Barcode Footer -->
        <g transform="translate(50, 392)" opacity="0.7">
          <rect x="0" y="0" width="3" height="18" fill="#F7C873"/>
          <rect x="5" y="0" width="1" height="18" fill="#F7C873"/>
          <rect x="8" y="0" width="4" height="18" fill="#F7C873"/>
          <rect x="14" y="0" width="2" height="18" fill="#F7C873"/>
          <rect x="18" y="0" width="3" height="18" fill="#F7C873"/>
          <rect x="23" y="0" width="6" height="18" fill="#F7C873"/>
          <rect x="31" y="0" width="2" height="18" fill="#F7C873"/>
          <rect x="35" y="0" width="4" height="18" fill="#F7C873"/>
          <rect x="41" y="0" width="3" height="18" fill="#F7C873"/>
          <rect x="46" y="0" width="2" height="18" fill="#F7C873"/>
          <rect x="50" y="0" width="6" height="18" fill="#F7C873"/>
          <rect x="58" y="0" width="3" height="18" fill="#F7C873"/>
          <rect x="63" y="0" width="4" height="18" fill="#F7C873"/>
          <rect x="69" y="0" width="2" height="18" fill="#F7C873"/>
          <rect x="73" y="0" width="3" height="18" fill="#F7C873"/>
          <rect x="78" y="0" width="6" height="18" fill="#F7C873"/>
          <rect x="86" y="0" width="2" height="18" fill="#F7C873"/>
          <rect x="90" y="0" width="4" height="18" fill="#F7C873"/>
          <rect x="96" y="0" width="3" height="18" fill="#F7C873"/>
          <rect x="101" y="0" width="2" height="18" fill="#F7C873"/>
          <rect x="105" y="0" width="6" height="18" fill="#F7C873"/>
          <text x="175" y="13" fill="#94A3B8" font-size="9" class="font-mono">DEV-100</text>
        </g>

        <!-- Holographic Shine Sweep -->
        <rect x="0" y="0" width="80" height="500" fill="url(#holoGrad)" class="holo-sweep" />
      </g>
    </g>
  </g>
</svg>'''

    with open(r"d:\github\lanyard.svg", "w", encoding="utf-8") as f:
        f.write(lanyard_svg)
    print("lanyard.svg created successfully!")

if __name__ == "__main__":
    create_lanyard()
