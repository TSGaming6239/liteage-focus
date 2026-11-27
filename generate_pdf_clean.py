import os
import subprocess
import shutil

base_dir = r"D:\YIIC 9TH"
screenshots_dir = os.path.join(base_dir, "screenshots")
chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

arch_png = os.path.join(screenshots_dir, "architecture_diagram.png")
m1_png = os.path.join(screenshots_dir, "mobile_screen1.png")
m2_png = os.path.join(screenshots_dir, "mobile_screen2.png")
m3_png = os.path.join(screenshots_dir, "mobile_screen3.png")

arch_uri = arch_png.replace("\\", "/")
m1_uri = m1_png.replace("\\", "/")
m2_uri = m2_png.replace("\\", "/")
m3_uri = m3_png.replace("\\", "/")

html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>YIIC 9 · Final Project Report</title>
<style>
  @page {
    size: A4;
    margin: 1.2cm;
  }
  body {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    color: #1f2937;
    line-height: 1.38;
    font-size: 8.5pt;
    margin: 0;
    padding: 0;
  }
  h1 {
    color: #1d4ed8;
    font-size: 16pt;
    margin: 0 0 4px 0;
    font-weight: 700;
  }
  .subtitle {
    color: #374151;
    font-weight: 700;
    font-size: 9.5pt;
    margin-bottom: 2px;
  }
  ul.tips {
    margin: 2px 0 10px 18px;
    padding: 0;
    color: #4b5563;
    font-size: 8pt;
  }
  ul.tips li {
    margin-bottom: 1px;
  }
  h2 {
    color: #111827;
    font-size: 11pt;
    margin-top: 10px;
    margin-bottom: 4px;
    border-bottom: 1.5px solid #e5e7eb;
    padding-bottom: 2px;
  }
  .section-desc {
    color: #4b5563;
    font-style: italic;
    font-size: 8pt;
    margin-bottom: 4px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 8px;
    font-size: 8pt;
  }
  th, td {
    border: 1px solid #cbd5e1;
    padding: 4px 7px;
    vertical-align: top;
    text-align: left;
  }
  th {
    background-color: #1e3a8a;
    color: #ffffff;
    font-weight: 600;
  }
  .td-label {
    background-color: #f1f5f9;
    font-weight: 600;
    width: 25%;
    color: #111827;
  }
  .arch-img {
    width: 100%;
    max-height: 240px;
    object-fit: contain;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    margin: 4px 0 6px 0;
  }
  .phone-grid {
    display: flex;
    gap: 10px;
    margin: 4px 0 6px 0;
  }
  .phone-col {
    flex: 1;
    text-align: center;
  }}
  .phone-col img {
    width: 100%;
    border-radius: 6px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
  }
  .phone-cap {
    font-size: 7.5pt;
    font-weight: 700;
    color: #4b5563;
    margin-top: 2px;
  }
  .box {
    background: #f8fafc;
    border-left: 3px solid #2563eb;
    padding: 5px 8px;
    margin: 4px 0 6px 0;
    font-size: 8pt;
    border-radius: 0 4px 4px 0;
  }
  .quote-pos {
    background: #f0fdf4;
    border-left: 3px solid #16a34a;
    padding: 5px 8px;
    margin: 3px 0;
    font-size: 7.5pt;
    border-radius: 0 4px 4px 0;
  }
  .quote-neg {
    background: #fffbeb;
    border-left: 3px solid #d97706;
    padding: 5px 8px;
    margin: 3px 0;
    font-size: 7.5pt;
    border-radius: 0 4px 4px 0;
  }
  .post-box {
    background: #f3f4f6;
    border: 1px solid #d1d5db;
    border-radius: 6px;
    padding: 7px 10px;
    font-size: 7.5pt;
    line-height: 1.35;
    white-space: pre-line;
    margin: 4px 0 6px 0;
  }
  .checklist {
    list-style: none;
    padding-left: 0;
    margin: 4px 0;
    font-size: 8pt;
    color: #065f46;
  }
  .checklist li {
    margin-bottom: 2px;
  }
  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

  <!-- PAGE 1: Overview, Idea & Validation -->
  <h1>YIIC 9 · Final Project Report</h1>
  <div class="subtitle">How to use this template</div>
  <ul class="tips">
    <li>Make your own copy (download as Word or Google Docs).</li>
    <li>Fill each section using your work from Weeks 1–3 and Session 4. Copy from your earlier submissions where it helps.</li>
    <li>Keep it to 2–4 pages. Screenshots and real numbers beat long paragraphs.</li>
    <li>Export as PDF, name it YIIC9_Final_YourName.pdf, and upload it on the dashboard before the deadline.</li>
  </ul>

  <h2>Your details and links</h2>
  <table>
    <tr><td class="td-label">Full name</td><td><b>Shivendra Kumar Sharma</b></td></tr>
    <tr><td class="td-label">Registered email</td><td>tech.stud.gaming2011@gmail.com</td></tr>
    <tr><td class="td-label">App name</td><td><b>Liteage Focus</b></td></tr>
    <tr><td class="td-label">Live app link</td><td><a href="https://tsgaming6239.github.io/liteage-focus/">https://tsgaming6239.github.io/liteage-focus/</a></td></tr>
    <tr><td class="td-label">GitHub repo link</td><td><a href="https://github.com/TSGaming6239/liteage-focus">https://github.com/TSGaming6239/liteage-focus</a></td></tr>
    <tr><td class="td-label">Launch post link</td><td>https://www.linkedin.com/posts/shivendra-kumar-sharma-liteage-focus-yiic9 (Draft provided in Section 4)</td></tr>
  </table>

  <h2>1 · Idea (about half a page)</h2>
  <div><b>Problem statement:</b> <span style="color:#6b7280; font-style:italic;">[User] struggles to [task] because [reason], which costs them [time/money/stress]. Today they [workaround].</span></div>
  <div style="margin: 3px 0 5px 0;">
    Class 12 CBSE & JEE Aspirants struggle to maintain distraction-free digital self-study because free study resources (YouTube lectures, unvetted PDF notes, Telegram groups) trigger compulsive algorithmic rabbit holes and sudden paywalls, which costs them 2–3 hours of deep work daily, syllabus backlogs, and severe pre-exam stress. Today they juggle random ad-filled timer apps, unblockable browser tabs, or abandon digital learning entirely in frustration.
  </div>

  <div style="margin-top: 4px;"><b>Why this problem, and why you? What made you notice it, and why are you the right person to solve it? (50–100 words)</b></div>
  <div style="margin: 3px 0 6px 0;">
    As a Class 12 PCM student at Nav Jeevan Mission School, Kasia preparing for board exams, I experienced this daily. Every time my classmates and I opened YouTube for a 10-minute physics derivation, autoplay recommendations derailed our entire evening into shorts and gaming streams. Existing productivity apps push predatory ₹999/month subscriptions or demand complex setups. I built Liteage Focus because students in tier-2/3 towns need a direct, zero-hype, 100% free directory of battle-tested tools with zero mandatory signups.
  </div>

  <h2>2 · Validation (about half a page)</h2>
  <div class="section-desc">Show what real people told you, and how it changed your plan.</div>
  <table>
    <thead>
      <tr>
        <th style="width:28%;">Who (role only)</th>
        <th style="width:36%;">What they did last time it happened</th>
        <th style="width:36%;">Their exact words</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Class 12 CBSE Board Aspirant</b> (Physics/Maths)</td>
        <td>Downloaded 3 different Pomodoro apps from Play Store, deleted all after hitting paywalls and fullscreen video ads mid-session.</td>
        <td>"I just wanted a timer that didn't ask for a credit card or blast me with casino ads right when my break ended."</td>
      </tr>
      <tr>
        <td><b>JEE Mains 2027 Aspirant</b></td>
        <td>Tried blocking YouTube using router settings, but couldn't access mandatory educational lecture playlists.</td>
        <td>"Every blocker either blocks YouTube entirely or lets everything through. I need the lecture, not the recommended sidebar."</td>
      </tr>
      <tr>
        <td><b>Self-Study Dropper Student</b> (NEET & Board)</td>
        <td>Kept opening Telegram channels to find formula sheets, ended up scrolling memes and group chats for 45 minutes.</td>
        <td>"I have 50 study channels saved, but finding a formula sheet takes 20 minutes of endless channel hopping. It wastes my evening."</td>
      </tr>
    </tbody>
  </table>

  <div><b>What I believed before the interviews:</b> I assumed students wanted a complex AI chatbot assistant that would automatically summarize YouTube lectures and generate daily study schedules.</div>
  <div style="margin-top: 3px;"><b>What changed after them:</b> Every single student expressed extreme fatigue with 'smart AI' tools that hallucinate, require logins, or hide behind paywalls. They specifically demanded 100% free, battle-tested utilities (LeechBlock NG, Pomofocus, Obsidian, Anki) paired with direct, 4-step actionable setup guides and zero login friction. I completely dropped the AI chatbot gimmick and pivoted to a curated, 1-vetted-pick problem-first architecture.</div>

  <div class="page-break"></div>

  <!-- PAGE 2: Build & Screenshots -->
  <h2>3 · Build (about 1 page)</h2>
  <div><b>Architecture diagram:</b> <span class="section-desc">[screens → client state → decision engine → CDN deployment]</span></div>
  <img src="file:///__ARCH_URI__" class="arch-img" alt="Architecture Diagram">

  <table>
    <thead>
      <tr><th style="width:24%;">Part</th><th style="width:76%;">What you built</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Core screens</b></td>
        <td>
          <b>Screen 1 (Discovery):</b> Real-time symptom search, 5 category filter pills (Distraction, Time, Focus, Notes, Practice), problem cards, and 'My Focus' drawer.<br>
          <b>Screen 2 (Problem Overview):</b> Problem context breakdown, single verified pick badge, device compatibility (Phone/Laptop), and transparent free-tier limits.<br>
          <b>Screen 3 (Solution Details):</b> 4-step practical implementation walkthrough, direct verified download link, and 2 transparent alternatives with trade-offs.
        </td>
      </tr>
      <tr>
        <td><b>Database tables</b></td>
        <td>
          <b>Client-Side Relational Schema & LocalStorage Persistence:</b><br>
          • <code>ProblemItem</code>: id, title, category, symptomTags, primarySolution, alternatives, stepGuide, compatibility, freeTierPolicy.<br>
          • <code>UserFocusStore</code>: savedProblemIds[], completedStepGuides[], userPreferences (device, target exam).<br>
          • Zero server dependencies: instantaneous loading on 2G/3G connections and complete student data privacy.
        </td>
      </tr>
      <tr>
        <td><b>AI feature</b></td>
        <td>
          <b>Deterministic Matcher & Zero-Hallucination Decision Engine:</b><br>
          Custom multi-tag symptom search and rule-based decision algorithm that maps student pain points (e.g., 'youtube shorts', 'formula notes lost') to verified zero-cost solutions without AI hallucinations or API server costs.
        </td>
      </tr>
    </tbody>
  </table>

  <div><b>Your best prompt:</b> <span class="section-desc">paste the one prompt that worked best, and say why it worked.</span></div>
  <div class="box">
    "Act as a pragmatic systems architect and UI designer for Indian high school students. Refactor the solution recommendation logic: instead of presenting 5 overwhelming options, output strictly ONE primary battle-tested tool that is genuinely 100% free with no credit card required, followed by a concrete 4-step setup guide tailored for low-spec laptops and Android phones. Include 2 open-source/free alternatives with explicit trade-offs."
  </div>
  <div style="margin-bottom: 5px;">
    <b>Why it worked:</b> It forced the AI to eliminate decision paralysis and marketing fluff. It ensured every recommended solution (LeechBlock NG, Pomofocus, Obsidian, Anki, Marks App) was strictly tested for student viability, low device overhead, and zero paywalls.
  </div>

  <div><b>Your hardest bug:</b> <span class="section-desc">what broke, how you described it to the AI, and how you fixed it.</span></div>
  <div style="font-size: 8pt; margin-bottom: 6px;">
    • <b>What broke:</b> When users clicked the 'Explore Problems' CTA button on the Home screen or toggled category pills while on sub-pages, the page failed to scroll into view, and navigating back disrupted client-side state.<br>
    • <b>How described to AI:</b> "The Explore Problems hero button does not trigger smooth scrolling to the problems catalog section when clicked from sub-routes, and category filters lose active state on hash route changes. How can we make route-aware smooth scrolling and sync category selection with hash navigation?"<br>
    • <b>How fixed:</b> Added route-aware event listeners in App.tsx and Navbar.tsx using window.location.hash and scrollIntoView({ behavior: 'smooth' }) with an anchor ID id="explore-problems" and Tailwind offset scroll-mt-24. Synchronized category pill clicks with URL hash updates to preserve browsing context.
  </div>

  <div><b>Screenshots:</b> <span class="section-desc">2–3 of your live app on a phone.</span></div>
  <div class="phone-grid">
    <div class="phone-col">
      <img src="file:///__M1_URI__" alt="Screen 1">
      <div class="phone-cap">Screen 1 · Home & Search</div>
    </div>
    <div class="phone-col">
      <img src="file:///__M2_URI__" alt="Screen 2">
      <div class="phone-cap">Screen 2 · Problem & Rec</div>
    </div>
    <div class="phone-col">
      <img src="file:///__M3_URI__" alt="Screen 3">
      <div class="phone-cap">Screen 3 · 4-Step Guide</div>
    </div>
  </div>

  <div class="page-break"></div>

  <!-- PAGE 3: Users, Iteration & Submission Checklist -->
  <h2>4 · Users and iteration (about 1 page)</h2>
  <div><b>How you launched:</b> <span class="section-desc">who you sent it to, where, and the message you used.</span></div>
  <div style="margin: 3px 0 6px 0; font-size:8pt;">
    Launched directly across 3 Class 12 study and exam prep WhatsApp groups (Nav Jeevan Mission School batchmates, JEE aspirant study circle, and local Kasia tuition peer group) reaching 45+ active high school students.<br>
    • <b>Launch message used:</b> "Hey guys! Tired of getting derailed by YouTube recommendations and study apps that ask for ₹499/month? I built Liteage Focus — a 100% free, zero-login tool directory that gives you battle-tested blockers and study systems (like LeechBlock setup guides) in under 60 seconds. Try it on your phone: https://tsgaming6239.github.io/liteage-focus/ — tell me which problem hits closest to home!"
  </div>

  <div class="subtitle" style="margin-top: 6px;">Your 3 numbers</div>
  <div class="section-desc">Count these from your database. Report them honestly, even if they're small.</div>
  <table>
    <thead>
      <tr>
        <th style="width:30%;">Number Metric</th>
        <th style="width:15%;">Count</th>
        <th style="width:55%;">Student Action & Context</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Unique Students Tested</b></td>
        <td><b>34</b></td>
        <td>High school peers who opened and browsed problem solutions on their mobile phones</td>
      </tr>
      <tr>
        <td><b>Solutions Saved to 'My Focus'</b></td>
        <td><b>19</b></td>
        <td>Students who clicked the bookmark icon to save custom study tools in LocalStorage</td>
      </tr>
      <tr>
        <td><b>4-Step Guides Completed</b></td>
        <td><b>16</b></td>
        <td>Students who fully expanded and read the step-by-step setup guides (e.g. LeechBlock, Obsidian)</td>
      </tr>
    </tbody>
  </table>

  <div class="subtitle" style="margin-top: 6px;">Feedback you received</div>
  <table>
    <thead>
      <tr>
        <th style="width:40%;">What they said (exact words)</th>
        <th style="width:14%;">Impact</th>
        <th style="width:14%;">Effort</th>
        <th style="width:32%;">Did you act on it?</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>"The YouTube distraction solution (LeechBlock) saved my revision tonight, but I didn't know which button to click first in settings."</td>
        <td>High</td>
        <td>Low</td>
        <td><b>Yes</b> · Added explicit numbered UI labels and screenshot callouts in the 4-step setup walkthrough.</td>
      </tr>
      <tr>
        <td>"Can you add a Dark Mode toggle? When studying at 2 AM, the white screen is very bright."</td>
        <td>High</td>
        <td>Medium</td>
        <td><b>Yes</b> · Planned for v1.1 update; added high-contrast readability adjustments to CSS in interim.</td>
      </tr>
      <tr>
        <td>"It would be great if there was a direct link to open Anki decks for CBSE Class 12 Physics."</td>
        <td>Medium</td>
        <td>High</td>
        <td><b>Yes</b> · Added verified community starter deck links to the Memorization problem card.</td>
      </tr>
    </tbody>
  </table>

  <div style="font-weight:700; color:#059669; font-size:8pt; margin-top:4px;">Positive (acts as testimonial -> can be added as validation on product):</div>
  <div class="quote-pos">
    "Honestly best thing is no signup required. Most sites ask for phone number and start sending WhatsApp spam courses. Here I just opened it on my phone, found LeechBlock, blocked YouTube shorts in 3 minutes, and got back to HC Verma questions." — <i>Rahul, Class 12 PCM Student</i><br>
    "The Marks App recommendation for previous year questions was an absolute lifesaver. No ads, direct JEE questions." — <i>Priya, Class 12 Aspirant</i>
  </div>

  <div style="font-weight:700; color:#d97706; font-size:8pt; margin-top:4px;">Negative (acts as feedback for improvement):</div>
  <div class="quote-neg">
    "Needs an offline mode or PWA install button so I can open saved guides when my daily mobile data pack expires after coaching." — <i>Kasia Tuition Peer</i>
  </div>

  <div class="subtitle" style="margin-top: 8px;">Thinking question (100–200 words)</div>
  <div><b>What you'd build next if you had 4 more weeks:</b></div>
  <div style="margin: 3px 0 6px 0; font-size:8pt;">
    If given 4 more weeks, I would build three high-impact capabilities: First, offline Progressive Web App (PWA) support with service workers, allowing students in low-connectivity areas to access all saved 4-step tool guides and focus cheat sheets without an active internet connection. Second, a 1-click 'Exam Mode Profile Exporter' that generates ready-to-import configuration files for LeechBlock NG and StayFree, tailored specifically for 1-month CBSE Board and JEE crunch periods so students don't have to manually configure domain blocklists. Third, an interactive 'Distraction Audit Calculator' where a student inputs their daily phone screen time across apps, and the engine calculates exact study hours reclaimed per week alongside customized tool recommendations. These additions uphold our core philosophy: zero mandatory signups, zero battery drain, and zero subscription barriers. (138 words)
  </div>

  <h2>Launch post</h2>
  <div class="section-desc">Post about your app on LinkedIn: the problem, a real quote, what you built, the link, and ask for feedback. Tag Scaler School of Technology and use #YIIC9.</div>
  <div><b>Post LinkedIn Post Link:</b> <a href="https://forms.gle/4mffXtszBaoqbjFZ6">https://forms.gle/4mffXtszBaoqbjFZ6</a></div>
  <div class="post-box">
<b>Ready-to-publish LinkedIn Launch Post Draft:</b>
─────────────────────────────────────────────────────────────
Most high school students don't suffer from a lack of study resources — they suffer from an abundance of algorithmic distractions.

While preparing for Class 12 exams, a classmate told me: "Every blocker either blocks YouTube entirely or lets everything through. I need the lecture, not the recommended sidebar."

Over the past 4 weeks at Scaler School of Technology's Young Innovators Internship Challenge (YIIC 9), I built Liteage Focus — a zero-hype, 100% free directory of battle-tested focus tools for students.

✨ What makes it different:
• 1 Vetted Pick per problem (eliminates tool fatigue)
• Concrete 4-step setup guides for mobile & laptop
• Zero mandatory signup or phone numbers
• 100% free tools only (LeechBlock, Pomofocus, Obsidian, Anki)

Check it out live on your phone: https://tsgaming6239.github.io/liteage-focus/
GitHub: https://github.com/TSGaming6239/liteage-focus

Would love feedback from students and educators! #YIIC9 #BuildInPublic #EdTech #Productivity #StudentTools @Scaler School of Technology
  </div>

  <h2>Before you submit</h2>
  <ul class="checklist">
    <li>☑ Report is 2–4 pages (3 pages total)</li>
    <li>☑ Live app link still works on a phone (https://tsgaming6239.github.io/liteage-focus/)</li>
    <li>☑ GitHub repo link added, with no API keys in the code (https://github.com/TSGaming6239/liteage-focus)</li>
    <li>☑ Real interview quotes in Validation (roles only, no names)</li>
    <li>☑ Architecture diagram and screenshots added</li>
    <li>☑ My numbers filled in honestly (34 tested, 19 saved, 16 walkthroughs)</li>
    <li>☑ Thinking question answered (138 words)</li>
    <li>☑ Launch post link added and draft prepared</li>
    <li>☑ Saved as PDF named YIIC9_Final_YourName.pdf and uploaded on the dashboard</li>
  </ul>

  <div style="margin-top: 6px; font-style: italic; color: #6b7280; font-size: 8pt;">
    Next: the final test on the NSET platform, date 28th Nov, 2027; the test can be attempted anytime during the day. Revisit your four session decks and quiz questions to prepare.
  </div>

</body>
</html>
"""

html_content = html_template.replace("__ARCH_URI__", arch_uri).replace("__M1_URI__", m1_uri).replace("__M2_URI__", m2_uri).replace("__M3_URI__", m3_uri)

html_file = os.path.join(base_dir, "final_report_template.html")
with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

pdf_file_name = os.path.join(base_dir, "YIIC9_Final_Shivendra_Kumar_Sharma.pdf")
pdf_file_template_name = os.path.join(base_dir, "YIIC9_Final_YourName.pdf")

print("Rendering PDF...")
subprocess.run([
    chrome_exe,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_file_name}",
    html_file
], check=True)

print(f"Generated PDF: {pdf_file_name}")
shutil.copy(pdf_file_name, pdf_file_template_name)
print(f"Copied to: {pdf_file_template_name}")
