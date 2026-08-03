import os

def create_light_banner():
    b64_path = r"d:\github\assets\character_b64.txt"
    if os.path.exists(b64_path):
        with open(b64_path, "r") as f:
            b64_data = f.read().strip()
    else:
        b64_data = ""

    banner_light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1600 650" width="100%" height="auto">
  <defs>
    <style type="text/css">
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,600;1,400&amp;family=Inter:wght@300;400;500;600;700&amp;family=Space+Grotesk:wght@300;500;700&amp;display=swap');

      * {{ margin: 0; padding: 0; box-sizing: border-box; }}

      .font-heading {{ font-family: 'Space Grotesk', -apple-system, sans-serif; }}
      .font-mono {{ font-family: 'IBM Plex Mono', monospace; }}
      .font-sans {{ font-family: 'Inter', -apple-system, sans-serif; }}

      /* Ultra-Sheer Sunrise Glassmorphism (Light Theme) */
      .glass-card-light {{
        fill: rgba(255, 252, 245, 0.72);
        stroke: rgba(217, 119, 6, 0.30);
        stroke-width: 1.2px;
        backdrop-filter: blur(24px);
        filter: drop-shadow(0 20px 45px rgba(180, 100, 20, 0.12));
        transition: all 0.5s cubic-bezier(0.16, 1, 0.3, 1);
      }}
      .glass-card-light:hover {{
        fill: rgba(255, 255, 250, 0.85);
        stroke: rgba(217, 119, 6, 0.50);
      }}

      .sun-bloom {{
        animation: sunPulse 6s ease-in-out infinite alternate;
        transform-origin: 800px 300px;
      }}
      @keyframes sunPulse {{
        0% {{ opacity: 0.70; transform: scale(0.97); }}
        100% {{ opacity: 1.0; transform: scale(1.04); }}
      }}

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

      .dust-group {{
        animation: dustFloat 20s ease-in-out infinite alternate;
      }}
      @keyframes dustFloat {{
        0% {{ transform: translate(0, 0); opacity: 0.40; }}
        50% {{ transform: translate(20px, -30px); opacity: 0.80; }}
        100% {{ transform: translate(-15px, -60px); opacity: 0.30; }}
      }}

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
        15% {{ opacity: 0.90; }}
        85% {{ opacity: 0.90; }}
        100% {{ transform: translate(-200px, 680px) rotate(420deg); opacity: 0; }}
      }}

      .cursor {{
        animation: blink 700ms steps(2, start) infinite;
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      .scan-line {{
        animation: laserScan 8.5s ease-in-out infinite alternate;
      }}
      @keyframes laserScan {{
        0% {{ transform: translateY(10px); opacity: 0.10; }}
        50% {{ opacity: 0.55; }}
        100% {{ transform: translateY(630px); opacity: 0.10; }}
      }}
    </style>

    <filter id="bgBlurLight">
      <feGaussianBlur stdDeviation="3.5" />
    </filter>

    <clipPath id="bannerClip">
      <rect width="1600" height="650" rx="24" ry="24" />
    </clipPath>

    <radialGradient id="sunGlowLight" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF3E0" stop-opacity="0.85"/>
      <stop offset="40%" stop-color="#FFB347" stop-opacity="0.45"/>
      <stop offset="80%" stop-color="#D97706" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#D97706" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="amberGradientDark" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D97706"/>
      <stop offset="50%" stop-color="#B45309"/>
      <stop offset="100%" stop-color="#92400E"/>
    </linearGradient>

    <linearGradient id="laserGradLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(217, 119, 6, 0)"/>
      <stop offset="25%" stop-color="rgba(217, 119, 6, 0.25)"/>
      <stop offset="50%" stop-color="rgba(245, 158, 11, 0.75)"/>
      <stop offset="75%" stop-color="rgba(217, 119, 6, 0.25)"/>
      <stop offset="100%" stop-color="rgba(217, 119, 6, 0)"/>
    </linearGradient>
  </defs>

  <g clip-path="url(#bannerClip)">

    <!-- LAYER 1: Sunrise Soft Background -->
    <image href="data:image/png;base64,{b64_data}" x="0" y="0" width="1600" height="650" preserveAspectRatio="xMidYMid slice" filter="url(#bgBlurLight)" opacity="0.90" />
    
    <!-- Sunrise Sun Bloom Pulse -->
    <circle cx="800" cy="300" r="180" fill="url(#sunGlowLight)" class="sun-bloom" />

    <!-- LAYER 2: Hero Character (52% Width in Center) -->
    <image href="data:image/png;base64,{b64_data}" x="380" y="0" width="840" height="650" preserveAspectRatio="xMidYMid slice" />

    <!-- Sakura Petals -->
    <g opacity="0.95">
      <path class="petal p1" d="M 1280,30 Q 1288,20 1294,32 Q 1286,44 1278,32 Z" fill="#FF8095" />
      <path class="petal p2" d="M 1480,70 Q 1488,60 1494,72 Q 1486,84 1478,72 Z" fill="#FF5376" />
      <path class="petal p3" d="M 1120,15 Q 1128,5 1134,17 Q 1126,29 1118,17 Z" fill="#FF8095" opacity="0.75"/>
      <path class="petal p4" d="M 1360,140 Q 1368,130 1374,142 Q 1366,154 1358,142 Z" fill="#E11D48" />
    </g>

    <!-- Laser Scanner Line -->
    <rect x="0" y="0" width="1600" height="2" fill="url(#laserGradLight)" class="scan-line" />

    <!-- LEFT SIDE LIGHT MODE -->
    <g transform="translate(75, 80)">
      <rect width="440" height="480" rx="24" class="glass-card-light" />

      <g transform="translate(38, 38)">
        <circle cx="6" cy="6" r="4.5" fill="#EF4444" />
        <circle cx="20" cy="6" r="4.5" fill="#F59E0B" />
        <circle cx="34" cy="6" r="4.5" fill="#10B981" />

        <g transform="translate(0, 36)">
          <text x="0" y="0" fill="#B45309" font-size="12" font-weight="600" class="font-mono">user@UmarAnsari100:~$ <tspan fill="#D97706">cat profile.json</tspan></text>
        </g>

        <g transform="translate(0, 96)">
          <text x="0" y="0" fill="#1E293B" font-size="32" font-weight="300" class="font-heading" letter-spacing="4">MUHAMMAD</text>
          <text x="0" y="44" fill="url(#amberGradientDark)" font-size="44" font-weight="700" class="font-heading" letter-spacing="-0.8">UMAR ANSARI</text>
        </g>

        <g transform="translate(0, 168)">
          <rect x="0" y="0" width="220" height="32" rx="16" fill="rgba(217, 119, 6, 0.15)" stroke="#D97706" stroke-width="1.2"/>
          <circle cx="16" cy="16" r="4" fill="#10B981" />
          <text x="30" y="20" fill="#78350F" font-size="12" font-weight="700" class="font-sans">Full Stack Web Developer</text>
        </g>

        <g transform="translate(0, 235)">
          <text x="0" y="0" fill="#334155" font-size="13" font-weight="500" class="font-sans">Building digital experiences</text>
          <text x="0" y="22" fill="#B45309" font-size="13" font-weight="700" class="font-sans">that people remember.</text>
        </g>
      </g>
    </g>

    <!-- RIGHT SIDE LIGHT MODE -->
    <g transform="translate(1085, 140)">
      <rect width="440" height="360" rx="24" class="glass-card-light" />

      <g transform="translate(38, 38)">
        <circle cx="6" cy="6" r="4.5" fill="#EF4444" />
        <circle cx="20" cy="6" r="4.5" fill="#F59E0B" />
        <circle cx="34" cy="6" r="4.5" fill="#10B981" />
        <text x="52" y="10" fill="#78350F" font-size="12" class="font-mono" font-weight="700">buildDreams.js</text>

        <g transform="translate(0, 32)">
          <rect width="364" height="230" rx="14" fill="rgba(255, 255, 255, 0.85)" stroke="rgba(217, 119, 6, 0.28)" stroke-width="1"/>

          <g font-size="12" class="font-mono" fill="#94A3B8">
            <text x="16" y="32">01</text>
            <text x="16" y="62">02</text>
            <text x="16" y="92">03</text>
            <text x="16" y="122">04</text>
            <text x="16" y="152">05</text>
            <text x="16" y="182">06</text>
          </g>

          <g font-size="12" class="font-mono" transform="translate(48, 0)">
            <text x="0" y="32" fill="#E11D48">function <tspan fill="#D97706">buildDreams</tspan>() {{</text>
            <text x="14" y="62" fill="#E11D48">return <tspan fill="#0F172A">{{</tspan></text>
            <text x="28" y="92" fill="#0284C7">discipline<tspan fill="#0F172A">:</tspan> <tspan fill="#D97706">"Daily"</tspan><tspan fill="#0F172A">,</tspan></text>
            <text x="28" y="122" fill="#0284C7">consistency<tspan fill="#0F172A">:</tspan> <tspan fill="#B45309">true</tspan><tspan fill="#0F172A">,</tspan></text>
            <text x="28" y="152" fill="#0284C7">learning<tspan fill="#0F172A">:</tspan> <tspan fill="#D97706">"Never Stops"</tspan></text>
            <g transform="translate(14, 182)">
              <text x="0" y="0" fill="#0F172A">}};</text>
              <rect x="32" y="-11" width="8" height="15" fill="#D97706" class="cursor"/>
            </g>
          </g>
        </g>
      </g>
    </g>

  </g>
</svg>'''

    with open(r"d:\github\banner-light.svg", "w", encoding="utf-8") as f:
        f.write(banner_light_svg)
    print("Upgraded 10/10 banner-light.svg created successfully!")

if __name__ == "__main__":
    create_light_banner()
