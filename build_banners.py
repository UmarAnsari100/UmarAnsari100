import os

def create_banner():
    b64_path = r"d:\github\assets\character_b64.txt"
    if os.path.exists(b64_path):
        with open(b64_path, "r") as f:
            b64_data = f.read().strip()
    else:
        b64_data = ""

    banner_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="100%" height="auto">
  <defs>
    <style type="text/css">
      @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@700&amp;family=IBM+Plex+Mono:ital,wght@0,400;0,600;1,400&amp;family=Inter:wght@300;400;500;600;700&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap');

      * {{ margin: 0; padding: 0; box-sizing: border-box; }}

      .font-heading {{ font-family: 'Space Grotesk', 'Inter', -apple-system, sans-serif; }}
      .font-serif {{ font-family: 'Cinzel', serif; }}
      .font-mono {{ font-family: 'IBM Plex Mono', monospace; }}
      .font-sans {{ font-family: 'Inter', -apple-system, sans-serif; }}

      /* Luxury Dark Glassmorphism */
      .glass-card {{
        fill: rgba(18, 18, 18, 0.58);
        stroke: rgba(255, 180, 70, 0.22);
        stroke-width: 1.2px;
        backdrop-filter: blur(25px);
        filter: drop-shadow(0 20px 50px rgba(0, 0, 0, 0.65));
        transition: all 0.4s ease;
      }}
      .glass-card:hover {{
        stroke: rgba(255, 180, 70, 0.45);
        fill: rgba(24, 24, 24, 0.68);
      }}

      /* Sun Bloom Pulse (6s) */
      .sun-pulse {{
        animation: sunBloom 6s ease-in-out infinite alternate;
        transform-origin: 640px 300px;
      }}
      @keyframes sunBloom {{
        0% {{ opacity: 0.65; transform: scale(0.96); }}
        100% {{ opacity: 1.0; transform: scale(1.06); }}
      }}

      /* Blinking Cursor (700ms) */
      .cursor {{
        animation: blink 700ms steps(2, start) infinite;
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      /* Hologram Continuous Scanner (3.5s) */
      .scanner-line {{
        animation: scanSweep 3.5s ease-in-out infinite alternate;
      }}
      @keyframes scanSweep {{
        0% {{ transform: translateY(0px); opacity: 0.15; }}
        50% {{ opacity: 0.75; }}
        100% {{ transform: translateY(735px); opacity: 0.15; }}
      }}

      /* Glowing Luxury Sign Flicker Effect */
      .sign-flicker {{
        animation: signGlow 4s ease-in-out infinite alternate;
      }}
      @keyframes signGlow {{
        0%, 100% {{ opacity: 0.85; filter: drop-shadow(0 0 8px rgba(255, 179, 71, 0.6)); }}
        48% {{ opacity: 0.85; }}
        50% {{ opacity: 0.40; filter: drop-shadow(0 0 2px rgba(255, 179, 71, 0.2)); }}
        52% {{ opacity: 0.95; filter: drop-shadow(0 0 14px rgba(255, 179, 71, 0.9)); }}
      }}

      /* Floating Sakura Petals (14s) */
      .petal {{
        animation: petalFall 14s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        transform-origin: center;
      }}
      .p1 {{ animation-delay: 0s; }}
      .p2 {{ animation-delay: 3s; }}
      .p3 {{ animation-delay: 6s; }}
      .p4 {{ animation-delay: 9s; }}
      .p5 {{ animation-delay: 11.5s; }}

      @keyframes petalFall {{
        0% {{ transform: translate(0, -30px) rotate(0deg); opacity: 0; }}
        15% {{ opacity: 0.95; }}
        85% {{ opacity: 0.95; }}
        100% {{ transform: translate(-200px, 760px) rotate(450deg); opacity: 0; }}
      }}

      /* Ambient Light Orbs (18s) */
      .light-orb {{
        animation: orbFloat 18s ease-in-out infinite alternate;
      }}
      @keyframes orbFloat {{
        0% {{ transform: translate(0, 0); opacity: 0.3; }}
        50% {{ transform: translate(30px, -40px); opacity: 0.75; }}
        100% {{ transform: translate(-25px, -80px); opacity: 0.2; }}
      }}

      /* Tech Stack Hover Effects */
      .tech-pill {{
        transition: transform 0.25s ease, fill 0.25s ease;
      }}
      .tech-pill:hover {{
        transform: translateY(-2px);
      }}

      /* Character One-Time Hologram Reveal */
      .hologram-reveal {{
        animation: revealMask 2.5s ease-out forwards;
      }}
      @keyframes revealMask {{
        0% {{ clip-path: inset(0 0 100% 0); }}
        100% {{ clip-path: inset(0 0 0 0); }}
      }}
    </style>

    <!-- Clip Path for Rounded Corners Scanner -->
    <clipPath id="bannerClip">
      <rect width="1280" height="740" rx="24" ry="24" />
    </clipPath>

    <!-- Warm Sunset Gradients -->
    <linearGradient id="bgVignette" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#151515" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#2B1810" stop-opacity="0.1"/>
      <stop offset="100%" stop-color="#0D0D0D" stop-opacity="0.5"/>
    </linearGradient>

    <radialGradient id="sunGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF4E5" stop-opacity="0.8"/>
      <stop offset="35%" stop-color="#FF9A3C" stop-opacity="0.45"/>
      <stop offset="70%" stop-color="#D97706" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#D97706" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="goldGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFB347"/>
      <stop offset="50%" stop-color="#F7C873"/>
      <stop offset="100%" stop-color="#FF9A3C"/>
    </linearGradient>

    <linearGradient id="scannerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(255, 180, 70, 0)"/>
      <stop offset="20%" stop-color="rgba(255, 180, 70, 0.35)"/>
      <stop offset="50%" stop-color="rgba(247, 200, 115, 0.85)"/>
      <stop offset="80%" stop-color="rgba(255, 180, 70, 0.35)"/>
      <stop offset="100%" stop-color="rgba(255, 180, 70, 0)"/>
    </linearGradient>
  </defs>

  <!-- Container Clipped to Rounded Banner Corners -->
  <g clip-path="url(#bannerClip)">

    <!-- Embedded Base64 Character Artwork Background -->
    <g class="hologram-reveal">
      <image href="data:image/png;base64,{b64_data}" x="0" y="0" width="1280" height="740" preserveAspectRatio="xMidYMid slice" />
    </g>

    <!-- Warm Vignette & Atmospheric Haze -->
    <rect width="1280" height="740" fill="url(#bgVignette)" />

    <!-- Sun Bloom Pulse behind Horizon -->
    <circle cx="640" cy="300" r="160" fill="url(#sunGlow)" class="sun-pulse" />

    <!-- Ambient Floating Light Orbs -->
    <g class="light-orb">
      <circle cx="240" cy="180" r="3" fill="#F7C873" opacity="0.8"/>
      <circle cx="480" cy="120" r="2" fill="#FFB347" opacity="0.7"/>
      <circle cx="750" cy="220" r="3.5" fill="#FFF4E5" opacity="0.9"/>
      <circle cx="980" cy="140" r="2.2" fill="#F7C873" opacity="0.7"/>
      <circle cx="1120" cy="240" r="3" fill="#FF9A3C" opacity="0.8"/>
    </g>

    <!-- Floating Sakura Petals -->
    <g opacity="0.9">
      <path class="petal p1" d="M 1050,30 Q 1058,20 1064,32 Q 1056,44 1048,32 Z" fill="#FFB7C5" />
      <path class="petal p2" d="M 1180,60 Q 1188,50 1194,62 Q 1186,74 1178,62 Z" fill="#FF8095" />
      <path class="petal p3" d="M 920,15 Q 928,5 934,17 Q 926,29 918,17 Z" fill="#FFB7C5" opacity="0.7"/>
      <path class="petal p4" d="M 1100,120 Q 1108,110 1114,122 Q 1106,134 1098,122 Z" fill="#FF5376" />
      <path class="petal p5" d="M 850,40 Q 858,30 864,42 Q 856,54 848,42 Z" fill="#FFB7C5" />
    </g>

    <!-- Continuous Full-Width Horizontal Scanner Line (3.5s) -->
    <rect x="0" y="0" width="1280" height="2.5" fill="url(#scannerGrad)" class="scanner-line" />

    <!-- ================================================================= -->
    <!-- LEFT PANEL: DEVELOPER INFO, TYPING TERMINAL & ABOUT ME           -->
    <!-- ================================================================= -->
    <g transform="translate(45, 45)">
      <!-- Main Left Glass Card Container -->
      <rect x="0" y="0" width="380" height="650" rx="20" ry="20" class="glass-card" />
      
      <!-- Terminal Header Bar -->
      <circle cx="24" cy="24" r="5" fill="#FF5F56" />
      <circle cx="40" cy="24" r="5" fill="#FFBD2E" />
      <circle cx="56" cy="24" r="5" fill="#27C93F" />
      <text x="75" y="28" fill="#F7C873" font-size="11" class="font-mono" opacity="0.9">user@UmarAnsari100:~$</text>

      <!-- Terminal Command -->
      <g transform="translate(24, 62)">
        <text x="0" y="0" fill="#FFB347" font-size="12" font-weight="600" class="font-mono">❯ cat README.md</text>
      </g>

      <!-- Vector Outlined Developer Name with Pop-In Style -->
      <g transform="translate(24, 105)">
        <text x="0" y="0" fill="#FFF4E5" font-size="26" font-weight="700" class="font-heading">Muhammad</text>
        <text x="0" y="32" fill="url(#goldGradient)" font-size="28" font-weight="700" class="font-heading">Umar Ansari</text>
      </g>

      <!-- Cycling Typed Role Titles Pill Capsule -->
      <g transform="translate(24, 155)">
        <rect x="0" y="0" width="220" height="30" rx="15" fill="rgba(219, 119, 6, 0.22)" stroke="#D97706" stroke-width="1.2"/>
        <circle cx="15" cy="15" r="4" fill="#27C93F" />
        <text x="28" y="19" fill="#FFF4E5" font-size="11" font-weight="600" class="font-sans">Full-Stack Web Developer</text>
      </g>

      <!-- Tagline Quote Box (Tall Window to prevent font clipping) -->
      <g transform="translate(24, 202)">
        <rect x="0" y="0" width="332" height="74" rx="10" fill="rgba(12, 12, 12, 0.5)" stroke="rgba(255, 180, 70, 0.18)" stroke-width="1"/>
        <text x="14" y="24" fill="#F7C873" font-size="14" class="font-mono">“</text>
        <text x="26" y="26" fill="#E2E8F0" font-size="11" class="font-sans">Building digital experiences</text>
        <text x="26" y="44" fill="#E2E8F0" font-size="11" class="font-sans">that are not just functional,</text>
        <text x="26" y="62" fill="#F7C873" font-size="11" font-weight="600" class="font-sans">but memorable. <tspan fill="#F7C873">”</tspan></text>
      </g>

      <!-- About Me Lines -->
      <g transform="translate(24, 298)" font-size="11" class="font-sans" fill="#CBD5E1">
        <text x="0" y="0" fill="#F7C873" font-weight="700" class="font-mono" letter-spacing="1">// ABOUT ME</text>
        <text x="0" y="22" fill="#E2E8F0">Computer Science student passionate</text>
        <text x="0" y="38" fill="#E2E8F0">about building high-performance,</text>
        <text x="0" y="54" fill="#E2E8F0">modern &amp; responsive web apps.</text>
        <text x="0" y="70" fill="#F7C873">HITEC University Taxila (6th Sem)</text>
      </g>

      <!-- Contact Info -->
      <g transform="translate(24, 400)" font-size="11" class="font-sans" fill="#CBD5E1">
        <g transform="translate(0, 0)">
          <circle cx="5" cy="5" r="4" fill="#FFB347"/>
          <text x="16" y="9" fill="#FFF4E5">Rawalpindi, Pakistan</text>
        </g>
        <g transform="translate(0, 24)">
          <path d="M1 2L13 2L13 11L1 11Z" fill="none" stroke="#FFB347" stroke-width="1.2"/>
          <text x="16" y="9" fill="#F7C873">mumaransari1607@gmail.com</text>
        </g>
        <g transform="translate(0, 48)">
          <circle cx="5" cy="5" r="4.5" fill="none" stroke="#FFB347" stroke-width="1.2"/>
          <text x="16" y="9" fill="#FFF4E5" font-weight="500">umar-two.vercel.app</text>
        </g>
      </g>

      <!-- Tech Stack Badges (Row 1) -->
      <g transform="translate(24, 492)">
        <g transform="translate(0, 0)" class="tech-pill">
          <rect width="102" height="32" rx="8" fill="rgba(30, 30, 30, 0.6)" stroke="rgba(255, 180, 70, 0.2)" stroke-width="1"/>
          <circle cx="18" cy="16" r="4" fill="#61DAFB"/>
          <text x="30" y="20" fill="#FFF4E5" font-size="11" font-weight="500" class="font-sans">React.js</text>
        </g>
        <g transform="translate(112, 0)" class="tech-pill">
          <rect width="104" height="32" rx="8" fill="rgba(30, 30, 30, 0.6)" stroke="rgba(255, 180, 70, 0.2)" stroke-width="1"/>
          <circle cx="18" cy="16" r="6" fill="#FFF"/>
          <text x="15" y="19" fill="#000" font-size="8" font-weight="900" class="font-sans">N</text>
          <text x="30" y="20" fill="#FFF4E5" font-size="11" font-weight="500" class="font-sans">Next.js</text>
        </g>
        <g transform="translate(226, 0)" class="tech-pill">
          <rect width="104" height="32" rx="8" fill="rgba(30, 30, 30, 0.6)" stroke="rgba(255, 180, 70, 0.2)" stroke-width="1"/>
          <rect x="12" y="9" width="14" height="14" rx="2" fill="#F7DF1E"/>
          <text x="14" y="20" fill="#000" font-size="9" font-weight="800" class="font-mono">JS</text>
          <text x="34" y="20" fill="#FFF4E5" font-size="11" font-weight="500" class="font-sans">JavaScript</text>
        </g>
      </g>

      <!-- Tech Stack Badges (Row 2) -->
      <g transform="translate(24, 534)">
        <g transform="translate(0, 0)" class="tech-pill">
          <rect width="102" height="32" rx="8" fill="rgba(30, 30, 30, 0.6)" stroke="rgba(255, 180, 70, 0.2)" stroke-width="1"/>
          <rect x="12" y="9" width="14" height="14" rx="2" fill="#3178C6"/>
          <text x="14" y="20" fill="#FFF" font-size="9" font-weight="800" class="font-mono">TS</text>
          <text x="32" y="20" fill="#FFF4E5" font-size="11" font-weight="500" class="font-sans">TypeScript</text>
        </g>
        <g transform="translate(112, 0)" class="tech-pill">
          <rect width="104" height="32" rx="8" fill="rgba(30, 30, 30, 0.6)" stroke="rgba(255, 180, 70, 0.2)" stroke-width="1"/>
          <path d="M12,16 C13,13 15,13 16,14.5 C17,16 19,16.5 20.5,15" fill="none" stroke="#38BDF8" stroke-width="2"/>
          <text x="30" y="20" fill="#FFF4E5" font-size="11" font-weight="500" class="font-sans">Tailwind</text>
        </g>
        <g transform="translate(226, 0)" class="tech-pill">
          <rect width="104" height="32" rx="8" fill="rgba(30, 30, 30, 0.6)" stroke="rgba(255, 180, 70, 0.2)" stroke-width="1"/>
          <text x="14" y="20" fill="#777BB4" font-size="10" font-weight="800" class="font-mono">PHP</text>
          <text x="42" y="20" fill="#FFF4E5" font-size="11" font-weight="500" class="font-sans">MySQL</text>
        </g>
      </g>

      <!-- Action Button -->
      <g transform="translate(24, 584)">
        <g transform="translate(0, 0)" class="tech-pill">
          <rect x="0" y="0" width="160" height="36" rx="10" fill="url(#goldGradient)" />
          <text x="24" y="23" fill="#151515" font-size="12" font-weight="700" class="font-sans">Visit Portfolio ↗</text>
        </g>
        <g transform="translate(172, 0)" class="tech-pill">
          <rect x="0" y="0" width="160" height="36" rx="10" fill="rgba(35, 35, 35, 0.8)" stroke="rgba(255, 180, 70, 0.3)" stroke-width="1"/>
          <text x="42" y="23" fill="#FFF4E5" font-size="12" font-weight="600" class="font-sans">GitHub 🐙</text>
        </g>
      </g>

    </g>

    <!-- ================================================================= -->
    <!-- RIGHT PANEL: CODE EDITOR & GLOWING LUXURY SIGN                    -->
    <!-- ================================================================= -->
    <g transform="translate(855, 45)">
      <!-- Main Right Glass Card Container -->
      <rect x="0" y="0" width="380" height="650" rx="20" ry="20" class="glass-card" />

      <!-- Glowing Luxury Sign (Flickering: BUILD • CREATE • INSPIRE) -->
      <g transform="translate(24, 28)" class="sign-flicker">
        <rect x="0" y="0" width="332" height="36" rx="8" fill="rgba(219, 119, 6, 0.15)" stroke="#D97706" stroke-width="1.2"/>
        <text x="166" y="23" text-anchor="middle" fill="#FFB347" font-size="11" font-weight="700" class="font-mono" letter-spacing="2">BUILD • CREATE • INSPIRE</text>
      </g>

      <!-- Code Editor Window Header -->
      <g transform="translate(24, 82)">
        <circle cx="6" cy="6" r="4" fill="#FF5F56" />
        <circle cx="18" cy="6" r="4" fill="#FFBD2E" />
        <circle cx="30" cy="6" r="4" fill="#27C93F" />
        <text x="44" y="9" fill="#F7C873" font-size="11" class="font-mono">buildDreams.js</text>
      </g>

      <!-- Code Editor Canvas (Tall window to prevent font clipping) -->
      <g transform="translate(24, 102)">
        <rect width="332" height="310" rx="10" fill="rgba(10, 10, 10, 0.78)" stroke="rgba(255, 180, 70, 0.2)" stroke-width="1"/>
        
        <!-- Line Numbers -->
        <g font-size="11" class="font-mono" fill="#64748B">
          <text x="14" y="28">01</text>
          <text x="14" y="52">02</text>
          <text x="14" y="76">03</text>
          <text x="14" y="100">04</text>
          <text x="14" y="124">05</text>
          <text x="14" y="148">06</text>
          <text x="14" y="172">07</text>
          <text x="14" y="196">08</text>
          <text x="14" y="220">09</text>
          <text x="14" y="244">10</text>
          <text x="14" y="268">11</text>
          <text x="14" y="292">12</text>
        </g>

        <!-- Syntax Lines -->
        <g font-size="11" class="font-mono" transform="translate(42, 0)">
          <text x="0" y="28" fill="#F43F5E">function <tspan fill="#F7C873">buildDreams</tspan>() {{</text>
          <text x="12" y="52" fill="#F43F5E">return <tspan fill="#FFF">{{</tspan></text>
          <text x="24" y="76" fill="#38BDF8">discipline<tspan fill="#FFF">:</tspan> <tspan fill="#F7C873">"Daily"</tspan><tspan fill="#FFF">,</tspan></text>
          <text x="24" y="100" fill="#38BDF8">consistency<tspan fill="#FFF">:</tspan> <tspan fill="#FF9A3C">true</tspan><tspan fill="#FFF">,</tspan></text>
          <text x="24" y="124" fill="#38BDF8">learning<tspan fill="#FFF">:</tspan> <tspan fill="#F7C873">"Never Stops"</tspan><tspan fill="#FFF">,</tspan></text>
          <text x="24" y="148" fill="#38BDF8">goal<tspan fill="#FFF">:</tspan> <tspan fill="#F7C873">"Impact"</tspan><tspan fill="#FFF">,</tspan></text>
          <text x="24" y="172" fill="#38BDF8">passion<tspan fill="#FFF">:</tspan> <tspan fill="#F7C873">"Infinite"</tspan></text>
          <text x="12" y="196" fill="#FFF">}};</text>
          <text x="0" y="220" fill="#FFF">}}</text>
          <g transform="translate(0, 252)">
            <text x="0" y="0" fill="#64748B" font-style="italic">// Code. Build. Deploy. Repeat. 🚀</text>
            <rect x="210" y="-10" width="7" height="14" fill="#FFB347" class="cursor"/>
          </g>
        </g>
      </g>

      <!-- Animated Stats Bar inside Banner -->
      <g transform="translate(24, 432)">
        <rect width="332" height="195" rx="12" fill="rgba(15, 15, 15, 0.6)" stroke="rgba(255, 180, 70, 0.2)" stroke-width="1"/>
        <text x="16" y="24" fill="#F7C873" font-size="11" font-weight="700" class="font-mono" letter-spacing="1">// METRICS &amp; ACHIEVEMENTS</text>
        
        <g transform="translate(16, 44)" font-size="11" class="font-sans">
          <!-- Projects -->
          <g transform="translate(0, 0)">
            <text x="0" y="12" fill="#E2E8F0" font-weight="500">Completed Projects</text>
            <text x="290" y="12" fill="#FFB347" font-weight="700" class="font-mono" text-anchor="end">15+</text>
          </g>
          <!-- Happy Clients -->
          <g transform="translate(0, 30)">
            <text x="0" y="12" fill="#E2E8F0" font-weight="500">Happy Clients</text>
            <text x="290" y="12" fill="#F7C873" font-weight="700" class="font-mono" text-anchor="end">10+</text>
          </g>
          <!-- Cups of Coffee -->
          <g transform="translate(0, 60)">
            <text x="0" y="12" fill="#E2E8F0" font-weight="500">Cups of Coffee</text>
            <text x="290" y="12" fill="#FF9A3C" font-weight="700" class="font-mono" text-anchor="end">∞</text>
          </g>
          <!-- Lines of Code -->
          <g transform="translate(0, 90)">
            <text x="0" y="12" fill="#E2E8F0" font-weight="500">Lines of Code Written</text>
            <text x="290" y="12" fill="#D97706" font-weight="700" class="font-mono" text-anchor="end">25K+</text>
          </g>
          <!-- Passion -->
          <g transform="translate(0, 120)">
            <text x="0" y="12" fill="#E2E8F0" font-weight="500">Passion &amp; Dedication</text>
            <text x="290" y="12" fill="#27C93F" font-weight="700" class="font-mono" text-anchor="end">100%</text>
          </g>
        </g>
      </g>

    </g>

  </g>
</svg>'''

    with open(r"d:\github\banner.svg", "w", encoding="utf-8") as f:
        f.write(banner_svg)
    print("banner.svg created successfully!")

if __name__ == "__main__":
    create_banner()
