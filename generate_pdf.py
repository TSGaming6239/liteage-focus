import os
import subprocess

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>YIIC 9 · Week 2 Submission: Make v0 clickable and test it</title>
<style>
  @page {
    size: A4;
    margin: 1.5cm;
  }
  body {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif;
    color: #1f2937;
    line-height: 1.45;
    font-size: 10.5pt;
    margin: 0;
    padding: 0;
  }
  h1 {
    color: #1d4ed8;
    font-size: 17pt;
    margin-bottom: 4px;
    font-weight: 700;
  }
  .subtitle {
    color: #4b5563;
    font-style: italic;
    font-size: 9.5pt;
    margin-bottom: 16px;
  }
  h2 {
    color: #111827;
    font-size: 12.5pt;
    margin-top: 20px;
    margin-bottom: 6px;
    border-bottom: 1.5px solid #e5e7eb;
    padding-bottom: 4px;
  }
  .section-desc {
    color: #4b5563;
    font-style: italic;
    font-size: 9pt;
    margin-bottom: 8px;
  }
  table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 14px;
    font-size: 9pt;
  }
  th, td {
    border: 1px solid #d1d5db;
    padding: 7px 9px;
    vertical-align: top;
    text-align: left;
  }
  th {
    background-color: #f3f4f6;
    font-weight: 600;
    color: #111827;
  }
  .td-label {
    background-color: #f9fafb;
    font-weight: 600;
    width: 25%;
    color: #111827;
  }
  .screenshot-img {
    width: 100%;
    max-width: 250px;
    border-radius: 6px;
    border: 1px solid #e5e7eb;
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
  }
  .comparison-container {
    display: flex;
    gap: 12px;
    margin-top: 4px;
  }
  .comparison-box {
    flex: 1;
  }
  .comparison-box img {
    width: 100%;
    border-radius: 5px;
    border: 1px solid #cbd5e1;
  }
  .checklist {
    list-style: none;
    padding-left: 0;
    font-size: 9.5pt;
  }
  .checklist li {
    margin-bottom: 4px;
  }
  .page-break {
    page-break-before: always;
  }
</style>
</head>
<body>

<h1>YIIC 9 · Week 2 Submission: Make v0 clickable and test it</h1>
<div class="subtitle">A simple app that works beats a fancy one that doesn’t. Honest notes beat perfect ones.</div>

<h2>Your details</h2>
<table>
  <tr>
    <td class="td-label">Full name</td>
    <td><strong>Shivendra Kumar Sharma</strong></td>
  </tr>
  <tr>
    <td class="td-label">Registered email</td>
    <td>tech.stud.gaming2011@gmail.com</td>
  </tr>
  <tr>
    <td class="td-label">App name</td>
    <td><strong>Liteage Focus</strong></td>
  </tr>
  <tr>
    <td class="td-label">Replit app link (anyone can open)</td>
    <td>https://replit.com/@liteage/liteage-focus <em>(Live production app: https://tsgaming6239.github.io/liteage-focus)</em></td>
  </tr>
  <tr>
    <td class="td-label">The problem it solves (one line from your Week 1 brief)</td>
    <td>Students struggle to find suitable digital solutions for study and productivity problems because resources are scattered, some tools do not fit their devices or routines, and useful features may be paid.</td>
  </tr>
</table>

<h2>1 · Your 3 core screens</h2>
<div class="section-desc">A user should be able to click through the main flow from start to finish using sample data, with no dead ends.</div>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Screen</th>
      <th style="width: 45%;">What it shows and does</th>
      <th style="width: 30%;">Paste screenshot</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Screen 1 · Home (Discovery & Search)</strong></td>
      <td>
        • <strong>Liteage Focus branding</strong>, tagline, and navigation (Home, Explore, About, My Focus, Sign in Optional).<br>
        • <strong>Real-time search bar</strong> filtering student problems by keyword, symptom, or subject.<br>
        • <strong>Category filter pills</strong> (Distractions, Time Management, Notes & Material, Revision & Memory, Exam Preparation).<br>
        • <strong>Popular Student Problems grid</strong> showing problem context, target audience, and primary recommendation preview.<br>
        • <strong>My Focus bookmarking</strong>: Clicking any card navigates seamlessly to Screen 2.
      </td>
      <td>
        <img class="screenshot-img" src="screenshots/screen1_home.png" alt="Screen 1 Home">
      </td>
    </tr>
    <tr>
      <td><strong>Screen 2 · Problem Page (Problem & Recommendation Overview)</strong></td>
      <td>
        • <strong>Breadcrumbs and back navigation</strong> to Home/Explore.<br>
        • <strong>Problem context</strong> reflecting real student interview struggles (e.g. YouTube distractions).<br>
        • <strong>Our Primary Recommendation card</strong>: ONE vetted tool (LeechBlock NG) with verified pricing status (100% Free & Open Source).<br>
        • <strong>Supported device badges</strong> (Chrome/Edge Extension, Windows, macOS, Linux).<br>
        • <strong>Why We Recommend It</strong> vs. <strong>Important Limitations to Know</strong>.<br>
        • Primary action button: <em>"View Step-by-Step Guide"</em> leading directly to Screen 3.<br>
        • Secondary link: <em>"Visit Tool Website (External)"</em>.<br>
        • <strong>Alternative solutions</strong>: Curated options (Cold Turkey, Unhook).
      </td>
      <td>
        <img class="screenshot-img" src="screenshots/screen2_problem.png" alt="Screen 2 Problem Page">
      </td>
    </tr>
    <tr>
      <td><strong>Screen 3 · Solution Details (Implementation Deep-Dive)</strong></td>
      <td>
        • <strong>Full tool overview</strong>, verified official URL, and verified free pricing status.<br>
        • <strong>Device compatibility matrix</strong> for laptops, phones, and browsers.<br>
        • <strong>100% Free Plan Transparency</strong> explaining zero hidden paywalls.<br>
        • <strong>Practical 4-step setup guide</strong> tailored for students with specific action tips (e.g. how to whitelist educational lectures).<br>
        • <strong>Comparison with alternatives</strong> explaining exact differences.<br>
        • <strong>Action bar</strong>: <em>"Launch Official Website"</em>, <em>"Save to My Focus"</em> with toast feedback, and <em>"Back to Problem"</em>.
      </td>
      <td>
        <img class="screenshot-img" src="screenshots/screen3_solution.png" alt="Screen 3 Solution Details">
      </td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h2>2 · User test (2 people)</h2>
<div class="section-desc">Give each person one task (e.g. "place an order"), then watch silently. Don't explain or help. Write down every moment they hesitated, tapped the wrong thing or asked a question.</div>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Person (role only)</th>
      <th style="width: 30%;">Task you gave</th>
      <th style="width: 25%;">Where they got confused</th>
      <th style="width: 20%;">What they said</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Person 1:</strong> Classmate, Class 12 (JEE Aspirant)</td>
      <td>Open Liteage Focus on laptop, find a free tool to block YouTube distractions while keeping lecture channels accessible, and find the step-by-step setup guide.</td>
      <td>Tapped "Visit Official Site" at the top of the card thinking it would open our setup tutorial; got redirected away to the external site and had to click back. Scrolled looking for the tutorial steps.</td>
      <td><em>"Where is the setup guide you mentioned? It took me to another website."</em></td>
    </tr>
    <tr>
      <td><strong>Person 2:</strong> Classmate, Class 11 (CBSE Board Student)</td>
      <td>Find a free tool to organize scattered PDF notes and formula sheets, verify whether it is 100% free, and save it to 'My Focus'.</td>
      <td>Clicked the bookmark icon on the problem card, but wasn't sure if it saved locally or required an account login first. Looked around for a confirmation message.</td>
      <td><em>"Did it save to my account, or do I need to sign up first?"</em></td>
    </tr>
  </tbody>
</table>

<p><strong>The 3 biggest confusions:</strong></p>
<ul class="checklist">
  <li>☑ User clicked 'Visit Official Site' expecting the in-app setup guide, not realizing it redirects to an external developer website.</li>
  <li>☑ User wondered whether saving a tool to 'My Focus' required an account or if it worked in guest mode.</li>
  <li>☑ Clicking an active category filter pill did not toggle back to 'All Problems' (had to find the small 'Reset to All' text).</li>
</ul>

<h2>3 · The fix you shipped</h2>
<div class="section-desc">Fix the biggest confusion with one detective-style prompt: what you expected, what actually happened, and "explain the cause before you change anything".</div>

<table>
  <tr>
    <td class="td-label">The confusion you fixed</td>
    <td>Users clicked 'Visit Official Site' expecting the in-app setup guide, accidentally leaving the website before seeing the step-by-step instructions.</td>
  </tr>
  <tr>
    <td class="td-label">The exact prompt you used</td>
    <td>
      <em>Expected behaviour: When a student opens a problem page, the primary action to view the 4-step setup guide (Screen 3) should be the most prominent action, while the external link should be clearly designated as an external destination.<br>
      Actual behaviour: The student clicked 'Visit Official Site' in the top header thinking it was the guide, navigated away, and asked 'Where is the guide you wrote?'.<br>
      Explain the cause before changing anything, then update Screen 2 to make 'View Step-by-Step Guide' the primary prominent CTA directly in the card header with a '4-Step Guide Included' badge, and re-label the external link as 'Visit Tool Website (External)'.</em>
    </td>
  </tr>
  <tr>
    <td class="td-label">What changed in the app</td>
    <td>Added a prominent '4-Step Guide Included' badge next to the pricing pill, moved 'View Step-by-Step Guide' directly into the card header as the primary high-contrast blue CTA, and re-labeled the developer link as 'Visit Tool Website (External)' with a clear external icon. Also updated category filter pills to toggle back to 'All' when clicked twice.</td>
  </tr>
  <tr>
    <td class="td-label">Before and after screenshots</td>
    <td>
      <div class="comparison-container">
        <div class="comparison-box">
          <strong>Before:</strong> External link was top CTA<br>
          <img src="screenshots/fix_before.png" alt="Before fix">
        </div>
        <div class="comparison-box">
          <strong>After:</strong> Clear Guide CTA + External Label<br>
          <img src="screenshots/fix_after.png" alt="After fix">
        </div>
      </div>
    </td>
  </tr>
</table>

<h2>4 · What your app must remember</h2>
<div class="section-desc">List everything your app needs to save between visits, and the details for each. This becomes your database in Session 3.<br>
Don't plan to store phone numbers, addresses or other sensitive details. A name and email are enough for login.</div>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Thing to remember</th>
      <th style="width: 45%;">Details to store</th>
      <th style="width: 30%;">Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Saved Solutions ('My Focus')</strong></td>
      <td>userId / guestSessionId, problemId, solutionId, dateSaved, customStudentNotes (e.g. personal study routine note)</td>
      <td><em>user_401, 'laptop-distractions-youtube', 'leechblock-ng', 2026-11-20, 'Use Block Set 1 for evening 4 PM - 9 PM study'</em></td>
    </tr>
    <tr>
      <td><strong>User Study Preferences & Device Filter</strong></td>
      <td>userId, primaryDevice (Laptop / Android / iOS / Web), academicStage (Class 11, Class 12, Dropper, College), targetExam (JEE, NEET, CBSE Boards, General)</td>
      <td><em>user_401, primaryDevice: 'Laptop (Windows)', academicStage: 'Class 12', targetExam: 'JEE Main & Advanced'</em></td>
    </tr>
    <tr>
      <td><strong>Student Problem Feedback & Reports</strong></td>
      <td>feedbackId, problemId, wasHelpful (Boolean), reportedStatus (e.g. 'Link Broken', 'Tool Started Charging', 'Works Great'), timestamp</td>
      <td><em>fb_891, problemId: 'free-topic-wise-pyqs', wasHelpful: true, reportedStatus: 'Works Great on mobile', 2026-11-20</em></td>
    </tr>
  </tbody>
</table>

<div class="page-break"></div>

<h2>5 · Thinking question: label your build prompt</h2>
<div class="section-desc">Paste the main prompt you used to build your app, split into the 6 parts from Session 2. Leave a part empty if you didn't use it, and note that.</div>

<table>
  <thead>
    <tr>
      <th style="width: 15%;">Part</th>
      <th style="width: 25%;">What it means</th>
      <th style="width: 60%;">Your prompt text</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Role</strong></td>
      <td><em>Who the AI should act as</em></td>
      <td>Act as a senior full-stack web developer, UI/UX designer, product engineer, and YIIC mentor.</td>
    </tr>
    <tr>
      <td><strong>Context</strong></td>
      <td><em>Background it needs (your user, their problem)</em></td>
      <td>Students struggle to find suitable digital solutions for their academic and productivity problems because resources are scattered, tools don't match their devices or routines, and useful features are paid. Liteage Focus is a student-first web app that helps students discover verified, free-first solutions organized by problem.</td>
    </tr>
    <tr>
      <td><strong>Task</strong></td>
      <td><em>Exactly what to build</em></td>
      <td>Build a complete, clickable, responsive website prototype with exactly three core screens: Screen 1 — Home (Search & Categories), Screen 2 — Problem Page (Problem overview & 1 primary recommendation), and Screen 3 — Solution Details (Step-by-step implementation guide & limitations).</td>
    </tr>
    <tr>
      <td><strong>Constraints</strong></td>
      <td><em>Limits (screens, mobile-first, "no login yet")</em></td>
      <td>Zero AI (no chatbots or fake recommendation engines); no mandatory login (browsing is 100% open); frontend-only prototype (no database yet); exactly 1 primary vetted recommendation per problem; use verified real tools only without fabricating pricing or capabilities.</td>
    </tr>
    <tr>
      <td><strong>Format</strong></td>
      <td><em>Shape of the output (list screens first, then build)</em></td>
      <td>Vite + React 18 + TypeScript + Tailwind CSS with Lucide icons. Hash-based client routing, clean component structure, sample data separated in src/data/problemsData.ts, responsive on desktop and mobile.</td>
    </tr>
    <tr>
      <td><strong>Examples</strong></td>
      <td><em>What it should feel like</em></td>
      <td>Follow Week 1 paper sketches. Real problem examples: 'Distractions on laptop while needing YouTube' -> LeechBlock NG; 'Managing time between school and coaching' -> Pomofocus; 'Scattered notes & PDFs' -> Obsidian; 'Revision gap' -> Anki.</td>
    </tr>
  </tbody>
</table>

<p><strong>One change you made after testing, and why (80–150 words):</strong></p>
<p style="background: #f9fafb; border-left: 3px solid #3b82f6; padding: 10px 14px; font-size: 9.5pt; color: #374151;">
  During user testing with a Class 12 classmate, I noticed immediate hesitation on Screen 2. The student clicked "Visit Official Site" at the top of the recommendation card expecting our step-by-step setup guide, but got navigated to an external website and asked, "Where are the instructions?". They completely missed the "View Full Setup Guide" button placed at the bottom.<br><br>
  To fix this, I made the internal guide the primary prominent CTA directly in the card header with an animated arrow, added a "4-Step Guide Included" badge, and clearly labeled the external link as "Visit Tool Website (External)". In subsequent testing, the student immediately clicked the guide button, seamlessly reaching Screen 3 without confusion.
</p>

<h2>Before you submit</h2>
<ul class="checklist">
  <li>☑ My Replit link opens and the main flow works end to end</li>
  <li>☑ 3 screenshots pasted</li>
  <li>☑ 2 user tests logged, with 3 confusions</li>
  <li>☑ One fix shipped, with the prompt I used</li>
  <li>☑ Data list filled in</li>
  <li>☑ Build prompt labelled + one change explained</li>
  <li>☑ Example rows deleted</li>
  <li>☑ Saved as PDF named YIIC9_Week2_YourName.pdf and uploaded on the dashboard</li>
</ul>

</body>
</html>
"""

html_path = "D:\\YIIC 9TH\\submission_template.html"
pdf_path = "D:\\YIIC 9TH\\YIIC9_Week2_Shivendra_Kumar_Sharma.pdf"

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Wrote HTML to {html_path}")

chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
cmd = [
    chrome_exe,
    "--headless",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_path}",
    html_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
print(f"Generated PDF at {pdf_path}, return code: {res.returncode}")
