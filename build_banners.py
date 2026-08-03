import os

def create_banner():
    b64_path = r"d:\github\assets\character_b64.txt"
    if os.path.exists(b64_path):
        with open(b64_path, "r") as f:
            b64_data = f.read().strip()
    else:
        b64_data = ""

    banner_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1600 650" width="100%" height="auto">
  <defs>
    <style type="text/css">
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,600;1,400&amp;family=Inter:wght@300;400;500;600;700&amp;family=Space+Grotesk:wght@300;500;700&amp;display=swap');

      * {{ margin: 0; padding: 0; box-sizing: border-box; }}

      .font-heading {{ font-family: 'Space Grotesk', -apple-system, sans-serif; }}
      .font-mono {{ font-family: 'IBM Plex Mono', monospace; }}
      .font-sans {{ font-family: 'Inter', -apple-system, sans-serif; }}

      /* Ultra-Sheer Luxury Glassmorphism (rgba(20,20,20,.32), 24px blur) */
      .glass-card {{
        fill: rgba(20, 20, 20, 0.32);
        stroke: rgba(255, 180, 80, 0.20);
        stroke-width: 1.2px;
        backdrop-filter: blur(24px);
        filter: drop-shadow(0 30px 60px rgba(0, 0, 0, 0.50));
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
      }}
      .glass-card:hover {{
        fill: rgba(26, 26, 26, 0.42);
        stroke: rgba(255, 180, 80, 0.40);
      }}

      /* Sun Bloom Breathing Pulse (6s) */
      .sun-bloom {{
        animation: sunPulse 6s ease-in-out infinite alternate;
        transform-origin: 800px 300px;
      }}
      @keyframes sunPulse {{
        0% {{ opacity: 0.60; transform: scale(0.97); }}
        100% {{ opacity: 0.95; transform: scale(1.04); }}
      }}

      /* Moving Clouds (Very Slow 50s) */
      .cloud-drift-1 {{
        animation: cloudMove1 50s linear infinite;
      }}
      .cloud-drift-2 {{
        animation: cloudMove2 70s linear infinite;
      }}
      @keyframes cloudMove1 {{
        0% {{ transform: translateX(-200px); }}
        100% {{ transform: translateX(1800px); }}
      }}
      @keyframes cloudMove2 {{
        0% {{ transform: translateX(1700px); }}
        100% {{ transform: translateX(-300px); }}
      }}

      /* Cinematic Dust Particles (20s) */
      .dust-group {{
        animation: dustFloat 20s ease-in-out infinite alternate;
      }}
      @keyframes dustFloat {{
        0% {{ transform: translate(0, 0); opacity: 0.30; }}
        50% {{ transform: translate(20px, -30px); opacity: 0.70; }}
        100% {{ transform: translate(-15px, -60px); opacity: 0.20; }}
      }}

      /* Floating Sakura Petals (14s) */
      .petal {{
        animation: petalFloat 14s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        transform-origin: center;
      }}
      .p1 {{ animation-delay: 0s; }}
      .p2 {{ animation-delay: 3.5s; }}
      .p3 {{ animation-delay: 7s; }}
      .p4 {{ animation-delay: 10.5s; }}

      @keyframes petalFloat {{
        0% {{ transform: translate(0, -30px) rotate(0deg); opacity: 0; }}
        15% {{ opacity: 0.85; }}
        85% {{ opacity: 0.85; }}
        100% {{ transform: translate(-200px, 680px) rotate(420deg); opacity: 0; }}
      }}

      /* Blinking Cursor (700ms) */
      .cursor {{
        animation: blink 700ms steps(2, start) infinite;
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      /* Scanner Line Sweeping every 8.5s */
      .scan-line {{
        animation: laserScan 8.5s ease-in-out infinite alternate;
      }}
      @keyframes laserScan {{
        0% {{ transform: translateY(10px); opacity: 0.10; }}
        50% {{ opacity: 0.55; }}
        100% {{ transform: translateY(630px); opacity: 0.10; }}
      }}

      /* Character Rim Lighting & Hair Glow */
      .character-glow {{
        filter: drop-shadow(0 0 15px rgba(255, 179, 71, 0.45));
      }}
    </style>

    <!-- Filters for Depth of Field Blur on Background -->
    <filter id="bgBlur">
      <feGaussianBlur stdDeviation="3.5" />
    </filter>

    <clipPath id="bannerClip">
      <rect width="1600" height="650" rx="24" ry="24" />
    </clipPath>

    <!-- Sunset Twilight Gradients -->
    <linearGradient id="vignetteGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E0806" stop-opacity="0.30"/>
      <stop offset="50%" stop-color="#1A0D08" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#080403" stop-opacity="0.50"/>
    </linearGradient>

    <radialGradient id="sunBloomGrad" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF4E5" stop-opacity="0.75"/>
      <stop offset="35%" stop-color="#FF9A3C" stop-opacity="0.40"/>
      <stop offset="70%" stop-color="#D97706" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#D97706" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="goldTextGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFB347"/>
      <stop offset="50%" stop-color="#F7C873"/>
      <stop offset="100%" stop-color="#FF9A3C"/>
    </linearGradient>

    <linearGradient id="amberPillGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(217, 119, 6, 0.22)"/>
      <stop offset="100%" stop-color="rgba(255, 179, 71, 0.10)"/>
    </linearGradient>

    <linearGradient id="laserGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(255, 180, 80, 0)"/>
      <stop offset="25%" stop-color="rgba(255, 180, 80, 0.25)"/>
      <stop offset="50%" stop-color="rgba(247, 200, 115, 0.75)"/>
      <stop offset="75%" stop-color="rgba(255, 180, 80, 0.25)"/>
      <stop offset="100%" stop-color="rgba(255, 180, 80, 0)"/>
    </linearGradient>
  </defs>

  <g clip-path="url(#bannerClip)">

    <!-- LAYER 1: Soft Blurred Background Image for Depth of Field -->
    <image href="data:image/png;base64,{b64_data}" x="0" y="0" width="1600" height="650" preserveAspectRatio="xMidYMid slice" filter="url(#bgBlur)" opacity="0.85" />
    
    <!-- Atmospheric Vignette -->
    <rect width="1600" height="650" fill="url(#vignetteGrad)" />

    <!-- Sun Bloom Pulse behind Character Horizon -->
    <circle cx="800" cy="300" r="180" fill="url(#sunBloomGrad)" class="sun-bloom" />

    <!-- Slow Moving Cloud Silhouettes (50s) -->
    <g opacity="0.10" fill="#FFE4B5">
      <path class="cloud-drift-1" d="M 0,100 Q 90,60 200,90 Q 310,50 420,90 L 440,150 L 0,150 Z" />
      <path class="cloud-drift-2" d="M 1200,80 Q 1310,40 1430,75 Q 1530,30 1630,75 L 1660,140 L 1200,140 Z" />
    </g>

    <!-- LAYER 2: Crisp Hero Character (Takes 52% Canvas Width in Center) with Rim Glow -->
    <g class="character-glow">
      <image href="data:image/png;base64,{b64_data}" x="380" y="0" width="840" height="650" preserveAspectRatio="xMidYMid slice" />
    </g>

    <!-- Cinematic Dust Particles (20s) -->
    <g class="dust-group">
      <circle cx="320" cy="180" r="1.8" fill="#F7C873" opacity="0.6"/>
      <circle cx="510" cy="140" r="1.2" fill="#FFB347" opacity="0.5"/>
      <circle cx="780" cy="210" r="2.2" fill="#FFF9F0" opacity="0.75"/>
      <circle cx="990" cy="160" r="1.5" fill="#F7C873" opacity="0.6"/>
      <circle cx="1220" cy="240" r="2.0" fill="#FF9A3C" opacity="0.5"/>
    </g>

    <!-- Floating Sakura Petals (14s) -->
    <g opacity="0.85">
      <path class="petal p1" d="M 1280,30 Q 1288,20 1294,32 Q 1286,44 1278,32 Z" fill="#FFB7C5" />
      <path class="petal p2" d="M 1480,70 Q 1488,60 1494,72 Q 1486,84 1478,72 Z" fill="#FF8095" />
      <path class="petal p3" d="M 1120,15 Q 1128,5 1134,17 Q 1126,29 1118,17 Z" fill="#FFB7C5" opacity="0.75"/>
      <path class="petal p4" d="M 1360,140 Q 1368,130 1374,142 Q 1366,154 1358,142 Z" fill="#FF5376" />
    </g>

    <!-- Laser Hologram Scanner Line (Sweeps every 8.5s) -->
    <rect x="0" y="0" width="1600" height="2" fill="url(#laserGrad)" class="scan-line" />

    <!-- ================================================================= -->
    <!-- LEFT SIDE: APPLE TYPOGRAPHY, TERMINAL & TAGLINE                   -->
    <!-- ================================================================= -->
    <g transform="translate(75, 80)">
      <!-- Ultra-Sheer Glass Panel -->
      <rect width="440" height="480" rx="24" class="glass-card" />

      <g transform="translate(38, 38)">
        <!-- Window Dots -->
        <circle cx="6" cy="6" r="4.5" fill="#FF5F56" />
        <circle cx="20" cy="6" r="4.5" fill="#FFBD2E" />
        <circle cx="34" cy="6" r="4.5" fill="#27C93F" />

        <!-- Minimal Terminal Line -->
        <g transform="translate(0, 36)">
          <text x="0" y="0" fill="#F7C873" font-size="12" font-weight="600" class="font-mono" opacity="0.9">user@UmarAnsari100:~$ <tspan fill="#FFB347">cat profile.json</tspan></text>
        </g>

        <!-- Apple Widescreen Typography Name -->
        <g transform="translate(0, 96)">
          <text x="0" y="0" fill="#E2E8F0" font-size="32" font-weight="300" class="font-heading" letter-spacing="4">MUHAMMAD</text>
          <text x="0" y="44" fill="url(#goldTextGrad)" font-size="44" font-weight="700" class="font-heading" letter-spacing="-0.8">UMAR ANSARI</text>
        </g>

        <!-- Role Capsule Pill -->
        <g transform="translate(0, 168)">
          <rect x="0" y="0" width="220" height="32" rx="16" fill="url(#amberPillGrad)" stroke="#D97706" stroke-width="1.2"/>
          <circle cx="16" cy="16" r="4" fill="#27C93F" />
          <text x="30" y="20" fill="#FFF9F0" font-size="12" font-weight="600" class="font-sans">Full Stack Web Developer</text>
        </g>

        <!-- Tagline -->
        <g transform="translate(0, 235)">
          <text x="0" y="0" fill="#E2E8F0" font-size="13" font-weight="400" class="font-sans" opacity="0.9">Building digital experiences</text>
          <text x="0" y="22" fill="#F7C873" font-size="13" font-weight="600" class="font-sans">that people remember.</text>
        </g>
      </g>
    </g>

    <!-- ================================================================= -->
    <!-- RIGHT SIDE: LUXURY FLOATING 6-LINE CODE EDITOR                    -->
    <!-- ================================================================= -->
    <g transform="translate(1085, 140)">
      <!-- Ultra-Sheer Glass Panel -->
      <rect width="440" height="360" rx="24" class="glass-card" />

      <g transform="translate(38, 38)">
        <!-- Window Controls & Filename -->
        <circle cx="6" cy="6" r="4.5" fill="#FF5F56" />
        <circle cx="20" cy="6" r="4.5" fill="#FFBD2E" />
        <circle cx="34" cy="6" r="4.5" fill="#27C93F" />
        <text x="52" y="10" fill="#F7C873" font-size="12" class="font-mono" font-weight="600">buildDreams.js</text>

        <!-- Code Editor Canvas (6 Lines Only - No Clutter) -->
        <g transform="translate(0, 32)">
          <rect width="364" height="230" rx="14" fill="rgba(10, 10, 10, 0.65)" stroke="rgba(255, 180, 80, 0.16)" stroke-width="1"/>

          <!-- Line Numbers -->
          <g font-size="12" class="font-mono" fill="#64748B">
            <text x="16" y="32">01</text>
            <text x="16" y="62">02</text>
            <text x="16" y="92">03</text>
            <text x="16" y="122">04</text>
            <text x="16" y="152">05</text>
            <text x="16" y="182">06</text>
          </g>

          <!-- 6-Line Code Syntax -->
          <g font-size="12" class="font-mono" transform="translate(48, 0)">
            <text x="0" y="32" fill="#F43F5E">function <tspan fill="#F7C873">buildDreams</tspan>() {{</text>
            <text x="14" y="62" fill="#F43F5E">return <tspan fill="#FFF9F0">{{</tspan></text>
            <text x="28" y="92" fill="#38BDF8">discipline<tspan fill="#FFF9F0">:</tspan> <tspan fill="#F7C873">"Daily"</tspan><tspan fill="#FFF9F0">,</tspan></text>
            <text x="28" y="122" fill="#38BDF8">consistency<tspan fill="#FFF9F0">:</tspan> <tspan fill="#FF9A3C">true</tspan><tspan fill="#FFF9F0">,</tspan></text>
            <text x="28" y="152" fill="#38BDF8">learning<tspan fill="#FFF9F0">:</tspan> <tspan fill="#F7C873">"Never Stops"</tspan></text>
            <g transform="translate(14, 182)">
              <text x="0" y="0" fill="#FFF9F0">}};</text>
              <rect x="32" y="-11" width="8" height="15" fill="#FFB347" class="cursor"/>
            </g>
          </g>
        </g>
      </g>
    </g>

  </g>
</svg>'''

    with open(r"d:\github\banner.svg", "w", encoding="utf-8") as f:
        f.write(banner_svg)
    print("Upgraded 10/10 banner.svg created successfully!")

if __name__ == "__main__":
    create_banner()
