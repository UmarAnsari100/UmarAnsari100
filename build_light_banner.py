import os

def create_light_banner():
    b64_path = r"d:\github\assets\character_b64.txt"
    if os.path.exists(b64_path):
        with open(b64_path, "r") as f:
            b64_data = f.read().strip()
    else:
        b64_data = ""

    banner_light_svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 1280 740" width="100%" height="auto">
  <defs>
    <style type="text/css">
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,400;0,600;1,400&amp;family=Inter:wght@300;400;500;600;700&amp;family=Space+Grotesk:wght@500;600;700&amp;display=swap');

      * {{ margin: 0; padding: 0; box-sizing: border-box; }}

      .font-heading {{ font-family: 'Space Grotesk', 'Inter', -apple-system, sans-serif; }}
      .font-mono {{ font-family: 'IBM Plex Mono', monospace; }}
      .font-sans {{ font-family: 'Inter', -apple-system, sans-serif; }}

      .glass-card-light {{
        fill: rgba(255, 248, 240, 0.78);
        stroke: rgba(217, 119, 6, 0.35);
        stroke-width: 1.2px;
        backdrop-filter: blur(25px);
        filter: drop-shadow(0 15px 40px rgba(180, 100, 20, 0.15));
        transition: all 0.4s ease;
      }}
      .glass-card-light:hover {{
        stroke: rgba(217, 119, 6, 0.6);
        fill: rgba(255, 252, 245, 0.88);
      }}

      .sun-pulse {{
        animation: sunBloom 6s ease-in-out infinite alternate;
        transform-origin: 640px 300px;
      }}
      @keyframes sunBloom {{
        0% {{ opacity: 0.70; transform: scale(0.96); }}
        100% {{ opacity: 1.0; transform: scale(1.04); }}
      }}

      .cursor {{
        animation: blink 700ms steps(2, start) infinite;
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}

      .scanner-line {{
        animation: scanSweep 3.5s ease-in-out infinite alternate;
      }}
      @keyframes scanSweep {{
        0% {{ transform: translateY(0px); opacity: 0.15; }}
        50% {{ opacity: 0.75; }}
        100% {{ transform: translateY(735px); opacity: 0.15; }}
      }}

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

      .tech-pill-light {{
        transition: transform 0.25s ease;
      }}
      .tech-pill-light:hover {{
        transform: translateY(-2px);
      }}

      .hologram-reveal {{
        animation: revealMask 2.5s ease-out forwards;
      }}
      @keyframes revealMask {{
        0% {{ clip-path: inset(0 0 100% 0); }}
        100% {{ clip-path: inset(0 0 0 0); }}
      }}
    </style>

    <clipPath id="bannerClip">
      <rect width="1280" height="740" rx="24" ry="24" />
    </clipPath>

    <radialGradient id="sunGlowLight" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#FFF3E0" stop-opacity="0.85"/>
      <stop offset="40%" stop-color="#FFB347" stop-opacity="0.5"/>
      <stop offset="80%" stop-color="#D97706" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#D97706" stop-opacity="0"/>
    </radialGradient>

    <linearGradient id="amberGradientDark" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#D97706"/>
      <stop offset="50%" stop-color="#B45309"/>
      <stop offset="100%" stop-color="#92400E"/>
    </linearGradient>

    <linearGradient id="scannerGradLight" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="rgba(217, 119, 6, 0)"/>
      <stop offset="20%" stop-color="rgba(217, 119, 6, 0.3)"/>
      <stop offset="50%" stop-color="rgba(245, 158, 11, 0.75)"/>
      <stop offset="80%" stop-color="rgba(217, 119, 6, 0.3)"/>
      <stop offset="100%" stop-color="rgba(217, 119, 6, 0)"/>
    </linearGradient>
  </defs>

  <g clip-path="url(#bannerClip)">
    <g class="hologram-reveal">
      <image href="data:image/png;base64,{b64_data}" x="0" y="0" width="1280" height="740" preserveAspectRatio="xMidYMid slice" />
    </g>

    <circle cx="640" cy="300" r="160" fill="url(#sunGlowLight)" class="sun-pulse" />

    <g opacity="0.95">
      <path class="petal p1" d="M 1050,30 Q 1058,20 1064,32 Q 1056,44 1048,32 Z" fill="#FF8095" />
      <path class="petal p2" d="M 1180,60 Q 1188,50 1194,62 Q 1186,74 1178,62 Z" fill="#FF5376" />
      <path class="petal p3" d="M 920,15 Q 928,5 934,17 Q 926,29 918,17 Z" fill="#FF8095" opacity="0.75"/>
      <path class="petal p4" d="M 1100,120 Q 1108,110 1114,122 Q 1106,134 1098,122 Z" fill="#E11D48" />
      <path class="petal p5" d="M 850,40 Q 858,30 864,42 Q 856,54 848,42 Z" fill="#FF8095" />
    </g>

    <rect x="0" y="0" width="1280" height="2.5" fill="url(#scannerGradLight)" class="scanner-line" />

    <!-- LEFT PANEL LIGHT MODE -->
    <g transform="translate(45, 45)">
      <rect x="0" y="0" width="380" height="650" rx="20" ry="20" class="glass-card-light" />
      
      <circle cx="24" cy="24" r="5" fill="#EF4444" />
      <circle cx="40" cy="24" r="5" fill="#F59E0B" />
      <circle cx="56" cy="24" r="5" fill="#10B981" />
      <text x="75" y="28" fill="#B45309" font-size="11" class="font-mono" font-weight="600">user@UmarAnsari100:~$</text>

      <g transform="translate(24, 62)">
        <text x="0" y="0" fill="#D97706" font-size="12" font-weight="700" class="font-mono">❯ cat README.md</text>
      </g>

      <g transform="translate(24, 105)">
        <text x="0" y="0" fill="#1E293B" font-size="26" font-weight="700" class="font-heading">Muhammad</text>
        <text x="0" y="32" fill="url(#amberGradientDark)" font-size="28" font-weight="700" class="font-heading">Umar Ansari</text>
      </g>

      <g transform="translate(24, 155)">
        <rect x="0" y="0" width="220" height="30" rx="15" fill="rgba(217, 119, 6, 0.15)" stroke="#D97706" stroke-width="1.2"/>
        <circle cx="15" cy="15" r="4" fill="#10B981" />
        <text x="28" y="19" fill="#78350F" font-size="11" font-weight="700" class="font-sans">Full-Stack Web Developer</text>
      </g>

      <g transform="translate(24, 202)">
        <rect x="0" y="0" width="332" height="74" rx="10" fill="rgba(255, 255, 255, 0.65)" stroke="rgba(217, 119, 6, 0.25)" stroke-width="1"/>
        <text x="14" y="24" fill="#D97706" font-size="14" class="font-mono">“</text>
        <text x="26" y="26" fill="#334155" font-size="11" class="font-sans" font-weight="500">Building digital experiences</text>
        <text x="26" y="44" fill="#334155" font-size="11" class="font-sans" font-weight="500">that are not just functional,</text>
        <text x="26" y="62" fill="#B45309" font-size="11" font-weight="700" class="font-sans">but memorable. <tspan fill="#D97706">”</tspan></text>
      </g>

      <g transform="translate(24, 298)" font-size="11" class="font-sans" fill="#334155">
        <text x="0" y="0" fill="#B45309" font-weight="700" class="font-mono" letter-spacing="1">// ABOUT ME</text>
        <text x="0" y="22" fill="#1E293B" font-weight="500">Computer Science student passionate</text>
        <text x="0" y="38" fill="#1E293B" font-weight="500">about building high-performance,</text>
        <text x="0" y="54" fill="#1E293B" font-weight="500">modern &amp; responsive web apps.</text>
        <text x="0" y="70" fill="#D97706" font-weight="600">HITEC University Taxila (6th Sem)</text>
      </g>

      <g transform="translate(24, 400)" font-size="11" class="font-sans" fill="#334155">
        <g transform="translate(0, 0)">
          <circle cx="5" cy="5" r="4" fill="#D97706"/>
          <text x="16" y="9" fill="#1E293B" font-weight="600">Rawalpindi, Pakistan</text>
        </g>
        <g transform="translate(0, 24)">
          <path d="M1 2L13 2L13 11L1 11Z" fill="none" stroke="#D97706" stroke-width="1.2"/>
          <text x="16" y="9" fill="#B45309" font-weight="600">mumaransari1607@gmail.com</text>
        </g>
        <g transform="translate(0, 48)">
          <circle cx="5" cy="5" r="4.5" fill="none" stroke="#D97706" stroke-width="1.2"/>
          <text x="16" y="9" fill="#1E293B" font-weight="700">umar-two.vercel.app</text>
        </g>
      </g>

      <!-- Tech Stack Pills Row 1 -->
      <g transform="translate(24, 492)">
        <g transform="translate(0, 0)" class="tech-pill-light">
          <rect width="102" height="32" rx="8" fill="rgba(255, 255, 255, 0.75)" stroke="rgba(217, 119, 6, 0.3)" stroke-width="1"/>
          <circle cx="18" cy="16" r="4" fill="#0284C7"/>
          <text x="30" y="20" fill="#0F172A" font-size="11" font-weight="600" class="font-sans">React.js</text>
        </g>
        <g transform="translate(112, 0)" class="tech-pill-light">
          <rect width="104" height="32" rx="8" fill="rgba(255, 255, 255, 0.75)" stroke="rgba(217, 119, 6, 0.3)" stroke-width="1"/>
          <circle cx="18" cy="16" r="6" fill="#0F172A"/>
          <text x="15" y="19" fill="#FFF" font-size="8" font-weight="900" class="font-sans">N</text>
          <text x="30" y="20" fill="#0F172A" font-size="11" font-weight="600" class="font-sans">Next.js</text>
        </g>
        <g transform="translate(226, 0)" class="tech-pill-light">
          <rect width="104" height="32" rx="8" fill="rgba(255, 255, 255, 0.75)" stroke="rgba(217, 119, 6, 0.3)" stroke-width="1"/>
          <rect x="12" y="9" width="14" height="14" rx="2" fill="#EAB308"/>
          <text x="14" y="20" fill="#000" font-size="9" font-weight="800" class="font-mono">JS</text>
          <text x="34" y="20" fill="#0F172A" font-size="11" font-weight="600" class="font-sans">JavaScript</text>
        </g>
      </g>

      <!-- Tech Stack Pills Row 2 -->
      <g transform="translate(24, 534)">
        <g transform="translate(0, 0)" class="tech-pill-light">
          <rect width="102" height="32" rx="8" fill="rgba(255, 255, 255, 0.75)" stroke="rgba(217, 119, 6, 0.3)" stroke-width="1"/>
          <rect x="12" y="9" width="14" height="14" rx="2" fill="#2563EB"/>
          <text x="14" y="20" fill="#FFF" font-size="9" font-weight="800" class="font-mono">TS</text>
          <text x="32" y="20" fill="#0F172A" font-size="11" font-weight="600" class="font-sans">TypeScript</text>
        </g>
        <g transform="translate(112, 0)" class="tech-pill-light">
          <rect width="104" height="32" rx="8" fill="rgba(255, 255, 255, 0.75)" stroke="rgba(217, 119, 6, 0.3)" stroke-width="1"/>
          <path d="M12,16 C13,13 15,13 16,14.5 C17,16 19,16.5 20.5,15" fill="none" stroke="#0284C7" stroke-width="2"/>
          <text x="30" y="20" fill="#0F172A" font-size="11" font-weight="600" class="font-sans">Tailwind</text>
        </g>
        <g transform="translate(226, 0)" class="tech-pill-light">
          <rect width="104" height="32" rx="8" fill="rgba(255, 255, 255, 0.75)" stroke="rgba(217, 119, 6, 0.3)" stroke-width="1"/>
          <text x="14" y="20" fill="#4F46E5" font-size="10" font-weight="800" class="font-mono">PHP</text>
          <text x="42" y="20" fill="#0F172A" font-size="11" font-weight="600" class="font-sans">MySQL</text>
        </g>
      </g>

      <g transform="translate(24, 584)">
        <g transform="translate(0, 0)" class="tech-pill-light">
          <rect x="0" y="0" width="160" height="36" rx="10" fill="url(#amberGradientDark)" />
          <text x="24" y="23" fill="#FFF" font-size="12" font-weight="700" class="font-sans">Visit Portfolio ↗</text>
        </g>
        <g transform="translate(172, 0)" class="tech-pill-light">
          <rect x="0" y="0" width="160" height="36" rx="10" fill="rgba(255, 255, 255, 0.85)" stroke="rgba(217, 119, 6, 0.4)" stroke-width="1"/>
          <text x="42" y="23" fill="#0F172A" font-size="12" font-weight="700" class="font-sans">GitHub 🐙</text>
        </g>
      </g>

    </g>

    <!-- RIGHT PANEL LIGHT MODE -->
    <g transform="translate(855, 45)">
      <rect x="0" y="0" width="380" height="650" rx="20" ry="20" class="glass-card-light" />

      <g transform="translate(24, 28)">
        <rect x="0" y="0" width="332" height="36" rx="8" fill="rgba(217, 119, 6, 0.15)" stroke="#D97706" stroke-width="1.2"/>
        <text x="166" y="23" text-anchor="middle" fill="#B45309" font-size="11" font-weight="700" class="font-mono" letter-spacing="2">BUILD • CREATE • INSPIRE</text>
      </g>

      <g transform="translate(24, 82)">
        <circle cx="6" cy="6" r="4" fill="#EF4444" />
        <circle cx="18" cy="6" r="4" fill="#F59E0B" />
        <circle cx="30" cy="6" r="4" fill="#10B981" />
        <text x="44" y="9" fill="#78350F" font-size="11" class="font-mono" font-weight="700">buildDreams.js</text>
      </g>

      <g transform="translate(24, 102)">
        <rect width="332" height="310" rx="10" fill="rgba(255, 255, 255, 0.85)" stroke="rgba(217, 119, 6, 0.3)" stroke-width="1"/>
        
        <g font-size="11" class="font-mono" fill="#94A3B8">
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

        <g font-size="11" class="font-mono" transform="translate(42, 0)">
          <text x="0" y="28" fill="#E11D48">function <tspan fill="#D97706">buildDreams</tspan>() {{</text>
          <text x="12" y="52" fill="#E11D48">return <tspan fill="#0F172A">{{</tspan></text>
          <text x="24" y="76" fill="#0284C7">discipline<tspan fill="#0F172A">:</tspan> <tspan fill="#D97706">"Daily"</tspan><tspan fill="#0F172A">,</tspan></text>
          <text x="24" y="100" fill="#0284C7">consistency<tspan fill="#0F172A">:</tspan> <tspan fill="#B45309">true</tspan><tspan fill="#0F172A">,</tspan></text>
          <text x="24" y="124" fill="#0284C7">learning<tspan fill="#0F172A">:</tspan> <tspan fill="#D97706">"Never Stops"</tspan><tspan fill="#0F172A">,</tspan></text>
          <text x="24" y="148" fill="#0284C7">goal<tspan fill="#0F172A">:</tspan> <tspan fill="#D97706">"Impact"</tspan><tspan fill="#0F172A">,</tspan></text>
          <text x="24" y="172" fill="#0284C7">passion<tspan fill="#0F172A">:</tspan> <tspan fill="#D97706">"Infinite"</tspan></text>
          <text x="12" y="196" fill="#0F172A">}};</text>
          <text x="0" y="220" fill="#0F172A">}}</text>
          <g transform="translate(0, 252)">
            <text x="0" y="0" fill="#64748B" font-style="italic">// Code. Build. Deploy. Repeat. 🚀</text>
            <rect x="210" y="-10" width="7" height="14" fill="#D97706" class="cursor"/>
          </g>
        </g>
      </g>

      <g transform="translate(24, 432)">
        <rect width="332" height="195" rx="12" fill="rgba(255, 255, 255, 0.75)" stroke="rgba(217, 119, 6, 0.3)" stroke-width="1"/>
        <text x="16" y="24" fill="#B45309" font-size="11" font-weight="700" class="font-mono" letter-spacing="1">// METRICS &amp; ACHIEVEMENTS</text>
        
        <g transform="translate(16, 44)" font-size="11" class="font-sans">
          <g transform="translate(0, 0)">
            <text x="0" y="12" fill="#1E293B" font-weight="600">Completed Projects</text>
            <text x="290" y="12" fill="#D97706" font-weight="700" class="font-mono" text-anchor="end">15+</text>
          </g>
          <g transform="translate(0, 30)">
            <text x="0" y="12" fill="#1E293B" font-weight="600">Happy Clients</text>
            <text x="290" y="12" fill="#B45309" font-weight="700" class="font-mono" text-anchor="end">10+</text>
          </g>
          <g transform="translate(0, 60)">
            <text x="0" y="12" fill="#1E293B" font-weight="600">Cups of Coffee</text>
            <text x="290" y="12" fill="#D97706" font-weight="700" class="font-mono" text-anchor="end">∞</text>
          </g>
          <g transform="translate(0, 90)">
            <text x="0" y="12" fill="#1E293B" font-weight="600">Lines of Code Written</text>
            <text x="290" y="12" fill="#92400E" font-weight="700" class="font-mono" text-anchor="end">25K+</text>
          </g>
          <g transform="translate(0, 120)">
            <text x="0" y="12" fill="#1E293B" font-weight="600">Passion &amp; Dedication</text>
            <text x="290" y="12" fill="#10B981" font-weight="700" class="font-mono" text-anchor="end">100%</text>
          </g>
        </g>
      </g>

    </g>

  </g>
</svg>'''

    with open(r"d:\github\banner-light.svg", "w", encoding="utf-8") as f:
        f.write(banner_light_svg)
    print("banner-light.svg created successfully!")

if __name__ == "__main__":
    create_light_banner()
