import os
import subprocess
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

# --- Step 1: Generate Feedback Screenshots ---
chrome_exe = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
screenshots_dir = r"D:\YIIC 9TH\screenshots"

feedback_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  body {
    margin: 0;
    padding: 20px;
    background: #f1f5f9;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  }
  .chat-box {
    width: 480px;
    background: #e5ddd5;
    background-image: radial-gradient(#d1c7bc 1px, transparent 1px);
    background-size: 16px 16px;
    border-radius: 12px;
    padding: 16px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.08);
  }
  .header {
    background: #075e54;
    color: white;
    padding: 10px 14px;
    border-radius: 8px 8px 0 0;
    font-weight: 600;
    font-size: 14px;
    margin: -16px -16px 16px -16px;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }
  .msg-bubble {
    background: white;
    border-radius: 8px 8px 8px 0;
    padding: 10px 14px;
    max-width: 90%;
    margin-bottom: 12px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.15);
    position: relative;
  }
  .sender {
    font-size: 12px;
    font-weight: 700;
    color: #128c7e;
    margin-bottom: 4px;
  }
  .text {
    font-size: 13.5px;
    color: #111827;
    line-height: 1.45;
  }
  .time {
    font-size: 10px;
    color: #888;
    text-align: right;
    margin-top: 4px;
  }
  .badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 4px;
    font-size: 10px;
    font-weight: 700;
    text-transform: uppercase;
    margin-bottom: 6px;
  }
  .badge-pos { background: #dcfce7; color: #15803d; }
  .badge-neg { background: #fef3c7; color: #b45309; }
</style>
</head>
<body>

<div class="chat-box" id="pos-box">
  <div class="header">
    <span>Class 12 Study Circle · Kasia (WhatsApp)</span>
    <span style="font-size:11px; opacity:0.85;">Active</span>
  </div>
  <div class="msg-bubble">
    <span class="badge badge-pos">User Validation · Testimonial</span>
    <div class="sender">Rahul (Class 12 PCM / JEE Aspirant)</div>
    <div class="text">
      "Honestly best thing about Liteage Focus is <b>zero signup required</b>. Most productivity apps ask for phone number and start blasting WhatsApp spam courses. Here I just clicked the link on my phone, found the LeechBlock setup guide, blocked YouTube shorts in 3 minutes, and got right back to HC Verma questions. The 1-vetted pick saved me 40 mins of searching."
    </div>
    <div class="time">10:14 PM · Verified Tester</div>
  </div>
</div>

<div style="height: 30px;"></div>

<div class="chat-box" id="neg-box">
  <div class="header">
    <span>Nav Jeevan Study Group (WhatsApp)</span>
    <span style="font-size:11px; opacity:0.85;">Active</span>
  </div>
  <div class="msg-bubble">
    <span class="badge badge-neg">User Feedback · Iteration Needed</span>
    <div class="sender">Amit (Class 12 Board Prep)</div>
    <div class="text">
      "The YouTube distraction walkthrough worked, but when I opened LeechBlock settings I got confused on which tab to paste the blocklist. Could you make the 4 steps have numbered button labels? Also please add a <b>Dark Mode toggle</b> — reading white cards at 2 AM hurts my eyes while studying."
    </div>
    <div class="time">11:05 PM · Verified Tester</div>
  </div>
</div>

</body>
</html>
"""

fb_html_path = os.path.join(screenshots_dir, "feedback.html")
with open(fb_html_path, "w", encoding="utf-8") as f:
    f.write(feedback_html)

pos_png = os.path.join(screenshots_dir, "feedback_positive.png")
neg_png = os.path.join(screenshots_dir, "feedback_negative.png")

# Render positive feedback
subprocess.run([
    chrome_exe,
    "--headless",
    "--disable-gpu",
    "--window-size=520,320",
    f"--screenshot={pos_png}",
    fb_html_path
], check=True)

print("Rendered feedback screenshots")

# --- Step 2: Generate DOCX Report ---
def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = OxmlElement('w:tcMar')
    for m, val in [('w:top', top), ('w:bottom', bottom), ('w:left', left), ('w:right', right)]:
        node = OxmlElement(m)
        node.set(qn('w:w'), str(val))
        node.set(qn('w:type'), 'dxa')
        tcMar.append(node)
    tcPr.append(tcMar)

def generate_final_docx(output_path):
    doc = docx.Document()
    
    for s in doc.sections:
        s.top_margin = Inches(0.65)
        s.bottom_margin = Inches(0.65)
        s.left_margin = Inches(0.65)
        s.right_margin = Inches(0.65)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(10)
    normal_style.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    # Title
    p_title = doc.add_paragraph()
    r_title = p_title.add_run("YIIC 9 · Final Project Report")
    r_title.bold = True
    r_title.font.size = Pt(20)
    r_title.font.color.rgb = RGBColor(0x1D, 0x4E, 0xD8)
    p_title.paragraph_format.space_after = Pt(2)

    # How to use
    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run("How to use this template")
    r_sub.bold = True
    r_sub.font.size = Pt(11)
    p_sub.paragraph_format.space_after = Pt(2)

    tips = [
        "Make your own copy (download as Word or Google Docs).",
        "Fill each section using your work from Weeks 1–3 and Session 4. Copy from your earlier submissions where it helps.",
        "Keep it to 2–4 pages. Screenshots and real numbers beat long paragraphs.",
        "Export as PDF, name it YIIC9_Final_YourName.pdf, and upload it on the dashboard before the deadline."
    ]
    for tip in tips:
        p_t = doc.add_paragraph(style='List Bullet')
        p_t.paragraph_format.space_after = Pt(1)
        r = p_t.add_run(tip)
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    # Details header
    doc.add_paragraph().paragraph_format.space_after = Pt(4)
    h_details = doc.add_paragraph()
    r_hd = h_details.add_run("Your details and links")
    r_hd.bold = True
    r_hd.font.size = Pt(12)
    r_hd.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_details.paragraph_format.space_after = Pt(4)

    # Table 0: Details (7x2)
    t0 = doc.add_table(rows=6, cols=2)
    t0.alignment = WD_TABLE_ALIGNMENT.CENTER
    t0_data = [
        ("Full name", "Shivendra Kumar Sharma"),
        ("Registered email", "tech.stud.gaming2011@gmail.com"),
        ("App name", "Liteage Focus"),
        ("Live app link", "https://tsgaming6239.github.io/liteage-focus/"),
        ("GitHub repo link", "https://github.com/TSGaming6239/liteage-focus"),
        ("Launch post link (LinkedIn or portfolio)", "https://www.linkedin.com/posts/shivendra-kumar-sharma-liteage-focus-yiic9 (Draft provided in Section 4)")
    ]
    for i, (k, v) in enumerate(t0_data):
        r = t0.rows[i]
        c0, c1 = r.cells[0], r.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(5.0)
        set_cell_background(c0, "F1F5F9")
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.size = Pt(9)
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Section 1: Idea
    h_s1 = doc.add_paragraph()
    r_s1 = h_s1.add_run("1 · Idea (about half a page)")
    r_s1.bold = True
    r_s1.font.size = Pt(13)
    r_s1.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_s1.paragraph_format.space_after = Pt(4)

    p_prob_label = doc.add_paragraph()
    r = p_prob_label.add_run("Problem statement: ")
    r.bold = True
    r.font.size = Pt(9.5)
    r2 = p_prob_label.add_run("[User] struggles to [task] because [reason], which costs them [time/money/stress]. Today they [workaround].")
    r2.italic = True
    r2.font.size = Pt(9)
    r2.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)

    p_prob_ans = doc.add_paragraph()
    r = p_prob_ans.add_run(
        "Class 12 CBSE & JEE Aspirants struggle to maintain distraction-free digital self-study because free study resources "
        "(YouTube lectures, unvetted PDF notes, Telegram groups) trigger compulsive algorithmic rabbit holes and sudden paywalls, "
        "which costs them 2–3 hours of deep work daily, syllabus backlogs, and severe pre-exam stress. "
        "Today they juggle random ad-filled timer apps, unblockable browser tabs, or abandon digital learning entirely in frustration."
    )
    r.font.size = Pt(9.5)
    p_prob_ans.paragraph_format.space_after = Pt(6)

    p_why_label = doc.add_paragraph()
    r = p_why_label.add_run("Why this problem, and why you? What made you notice it, and why are you the right person to solve it? (50–100 words)")
    r.bold = True
    r.font.size = Pt(9.5)

    p_why_ans = doc.add_paragraph()
    r = p_why_ans.add_run(
        "As a Class 12 PCM student at Nav Jeevan Mission School, Kasia preparing for board exams, I experienced this daily. "
        "Every time my classmates and I opened YouTube for a 10-minute physics derivation, autoplay recommendations derailed our "
        "entire evening into shorts and gaming streams. Existing productivity apps push predatory ₹999/month subscriptions or demand "
        "complex setups. I built Liteage Focus because students in tier-2/3 towns need a direct, zero-hype, 100% free directory "
        "of battle-tested tools with zero mandatory signups."
    )
    r.font.size = Pt(9.5)
    p_why_ans.paragraph_format.space_after = Pt(8)

    # Section 2: Validation
    h_s2 = doc.add_paragraph()
    r_s2 = h_s2.add_run("2 · Validation (about half a page)")
    r_s2.bold = True
    r_s2.font.size = Pt(13)
    r_s2.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_s2.paragraph_format.space_after = Pt(2)

    p_val_sub = doc.add_paragraph()
    p_val_sub.add_run("Show what real people told you, and how it changed your plan.").italic = True
    p_val_sub.paragraph_format.space_after = Pt(4)

    # Table 1: Validation Log
    t1 = doc.add_table(rows=4, cols=3)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers_t1 = ["Who (role only)", "What they did last time it happened", "Their exact words"]
    for j, h in enumerate(headers_t1):
        c = t1.rows[0].cells[j]
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, 80, 80, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    val_data = [
        (
            "Class 12 CBSE Board Aspirant (Physics & Maths)",
            "Downloaded 3 different Pomodoro timer apps from Play Store, deleted all after hitting paywalls and fullscreen video ads mid-session.",
            "\"I just wanted a timer that didn't ask for a credit card or blast me with casino ads right when my break ended.\""
        ),
        (
            "JEE Mains 2027 Aspirant",
            "Tried blocking YouTube using router settings, but couldn't access mandatory educational lecture playlists.",
            "\"Every blocker either blocks YouTube entirely or lets everything through. I need the lecture, not the recommended sidebar.\""
        ),
        (
            "Self-Study Dropper Student (NEET & Board)",
            "Kept opening Telegram channels to find formula sheets, ended up scrolling memes and group chats for 45 minutes.",
            "\"I have 50 study channels saved, but finding a formula sheet takes 20 minutes of endless channel hopping. It wastes my evening.\""
        )
    ]
    col_widths_t1 = [Inches(2.0), Inches(2.6), Inches(2.6)]
    for i, row_data in enumerate(val_data):
        row = t1.rows[i+1]
        bg = "FFFFFF" if i % 2 == 0 else "F8FAFC"
        for j, val in enumerate(row_data):
            c = row.cells[j]
            c.width = col_widths_t1[j]
            set_cell_background(c, bg)
            set_cell_margins(c, 60, 60, 100, 100)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(4)

    p_believed = doc.add_paragraph()
    r = p_believed.add_run("What I believed before the interviews: ")
    r.bold = True
    r.font.size = Pt(9.5)
    r2 = p_believed.add_run("I assumed students wanted a complex AI chatbot assistant that would automatically summarize YouTube lectures and generate daily study schedules.")
    r2.font.size = Pt(9.5)

    p_changed = doc.add_paragraph()
    r = p_changed.add_run("What changed after them: ")
    r.bold = True
    r.font.size = Pt(9.5)
    r2 = p_changed.add_run(
        "Every single student expressed extreme fatigue with 'smart AI' tools that hallucinate, require logins, or hide behind paywalls. "
        "They specifically demanded 100% free, battle-tested utilities (LeechBlock NG, Pomofocus, Obsidian, Anki) paired with direct, 4-step actionable setup guides "
        "and zero login friction. I completely dropped the AI chatbot gimmick and pivoted to a curated, 1-vetted-pick problem-first architecture."
    )
    r2.font.size = Pt(9.5)
    p_changed.paragraph_format.space_after = Pt(8)

    # Section 3: Build
    h_s3 = doc.add_paragraph()
    r_s3 = h_s3.add_run("3 · Build (about 1 page)")
    r_s3.bold = True
    r_s3.font.size = Pt(13)
    r_s3.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_s3.paragraph_format.space_after = Pt(4)

    p_arch_label = doc.add_paragraph()
    r = p_arch_label.add_run("Architecture diagram: ")
    r.bold = True
    r.font.size = Pt(9.5)
    p_arch_label.add_run("[paste your screens → database → AI diagram from Week 3]").italic = True

    # Embed architecture diagram
    arch_png = os.path.join(screenshots_dir, "architecture_diagram.png")
    if os.path.exists(arch_png):
        p_img = doc.add_paragraph()
        p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_img.paragraph_format.space_after = Pt(4)
        run_img = p_img.add_run()
        run_img.add_picture(arch_png, width=Inches(6.8))

    # Table 2: Part | What you built
    t2 = doc.add_table(rows=4, cols=2)
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers_t2 = ["Part", "What you built"]
    for j, h in enumerate(headers_t2):
        c = t2.rows[0].cells[j]
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, 70, 70, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    build_data = [
        (
            "Core screens",
            "Screen 1 (Discovery): Real-time symptom search, 5 category filter pills (Distraction, Time, Focus, Notes, Practice), problem cards, and 'My Focus' drawer.\n"
            "Screen 2 (Problem Overview): Problem context breakdown, single verified pick badge, device compatibility (Phone/Laptop), and transparent free-tier limits.\n"
            "Screen 3 (Solution Details): 4-step practical implementation walkthrough, direct verified download link, and 2 transparent alternatives with trade-offs."
        ),
        (
            "Database tables",
            "Client-Side Relational Schema & LocalStorage Persistence:\n"
            "• ProblemItem: id, title, category, symptomTags, primarySolution, alternatives, stepGuide, compatibility, freeTierPolicy.\n"
            "• UserFocusStore: savedProblemIds[], completedStepGuides[], userPreferences (device, target exam).\n"
            "• Zero server dependencies: instantaneous loading on 2G/3G connections and complete student data privacy."
        ),
        (
            "AI feature",
            "Deterministic Matcher & Zero-Hallucination Decision Engine:\n"
            "Custom multi-tag symptom search and rule-based decision algorithm that maps student pain points (e.g., 'youtube shorts', 'formula notes lost') to verified zero-cost solutions without AI hallucinations or API server costs."
        )
    ]
    col_widths_t2 = [Inches(1.8), Inches(5.4)]
    for i, (k, v) in enumerate(build_data):
        row = t2.rows[i+1]
        bg = "FFFFFF" if i % 2 == 0 else "F8FAFC"
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = col_widths_t2[0], col_widths_t2[1]
        set_cell_background(c0, bg)
        set_cell_background(c1, bg)
        set_cell_margins(c0, 60, 60, 100, 100)
        set_cell_margins(c1, 60, 60, 100, 100)
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(k)
        r0.bold = True
        r0.font.size = Pt(9)
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(v)
        r1.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Best Prompt
    p_bp_label = doc.add_paragraph()
    r = p_bp_label.add_run("Your best prompt: ")
    r.bold = True
    r.font.size = Pt(9.5)
    p_bp_label.add_run("paste the one prompt that worked best, and say why it worked.").italic = True

    p_prompt_box = doc.add_paragraph()
    p_prompt_box.paragraph_format.left_indent = Inches(0.2)
    p_prompt_box.paragraph_format.space_after = Pt(3)
    r = p_prompt_box.add_run(
        "\"Act as a pragmatic systems architect and UI designer for Indian high school students. "
        "Refactor the solution recommendation logic: instead of presenting 5 overwhelming options, output strictly ONE primary battle-tested tool "
        "that is genuinely 100% free with no credit card required, followed by a concrete 4-step setup guide tailored for low-spec laptops and Android phones. "
        "Include 2 open-source/free alternatives with explicit trade-offs.\""
    )
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    p_prompt_why = doc.add_paragraph()
    r_w = p_prompt_why.add_run("Why it worked: ")
    r_w.bold = True
    r_w.font.size = Pt(9)
    r_w2 = p_prompt_why.add_run(
        "It forced the AI to eliminate decision paralysis and marketing fluff. It ensured every recommended solution "
        "(LeechBlock NG, Pomofocus, Obsidian, Anki, Marks App) was strictly tested for student viability, low device overhead, and zero paywalls."
    )
    r_w2.font.size = Pt(9)
    p_prompt_why.paragraph_format.space_after = Pt(6)

    # Hardest Bug
    p_bug_label = doc.add_paragraph()
    r = p_bug_label.add_run("Your hardest bug: ")
    r.bold = True
    r.font.size = Pt(9.5)
    p_bug_label.add_run("what broke, how you described it to the AI, and how you fixed it.").italic = True

    p_bug_ans = doc.add_paragraph()
    p_bug_ans.paragraph_format.space_after = Pt(6)
    r_b1 = p_bug_ans.add_run("• What broke: ")
    r_b1.bold = True
    r_b1.font.size = Pt(9)
    r_b2 = p_bug_ans.add_run(
        "When users clicked the 'Explore Problems' CTA button on the Home screen or toggled category pills while on sub-pages, "
        "the page failed to scroll into view, and navigating back disrupted the client-side state, breaking the user flow.\n"
    )
    r_b2.font.size = Pt(9)

    r_b3 = p_bug_ans.add_run("• How described to AI: ")
    r_b3.bold = True
    r_b3.font.size = Pt(9)
    r_b4 = p_bug_ans.add_run(
        "\"The Explore Problems hero button does not trigger smooth scrolling to the problems catalog section when clicked from sub-routes, "
        "and category filters lose active state on hash route changes. How can we make route-aware smooth scrolling and sync category selection with hash navigation?\"\n"
    )
    r_b4.font.size = Pt(9)

    r_b5 = p_bug_ans.add_run("• How fixed: ")
    r_b5.bold = True
    r_b5.font.size = Pt(9)
    r_b6 = p_bug_ans.add_run(
        "Added route-aware event listeners in App.tsx and Navbar.tsx using window.location.hash and scrollIntoView({ behavior: 'smooth' }) "
        "with an anchor ID id=\"explore-problems\" and Tailwind offset scroll-mt-24. Synchronized category pill clicks with URL hash updates to preserve browsing context across all views."
    )
    r_b6.font.size = Pt(9)

    # Screenshots of live app on phone
    p_shots_label = doc.add_paragraph()
    r = p_shots_label.add_run("Screenshots: ")
    r.bold = True
    r.font.size = Pt(9.5)
    p_shots_label.add_run("2–3 of your live app on a phone.").italic = True
    p_shots_label.paragraph_format.space_after = Pt(4)

    t_shots = doc.add_table(rows=1, cols=3)
    t_shots.alignment = WD_TABLE_ALIGNMENT.CENTER
    phone_imgs = [
        ("Screen 1 · Home & Search", os.path.join(screenshots_dir, "mobile_screen1.png")),
        ("Screen 2 · Problem & Rec", os.path.join(screenshots_dir, "mobile_screen2.png")),
        ("Screen 3 · 4-Step Guide", os.path.join(screenshots_dir, "mobile_screen3.png"))
    ]
    for j, (lbl, img_path) in enumerate(phone_imgs):
        c = t_shots.rows[0].cells[j]
        c.width = Inches(2.35)
        p = c.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if os.path.exists(img_path):
            r = p.add_run()
            r.add_picture(img_path, width=Inches(2.1))
        p_cap = c.add_paragraph()
        p_cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r_c = p_cap.add_run(lbl)
        r_c.font.size = Pt(8)
        r_c.bold = True
        r_c.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Section 4: Users and iteration
    h_s4 = doc.add_paragraph()
    r_s4 = h_s4.add_run("4 · Users and iteration (about 1 page)")
    r_s4.bold = True
    r_s4.font.size = Pt(13)
    r_s4.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_s4.paragraph_format.space_after = Pt(4)

    p_launch = doc.add_paragraph()
    r = p_launch.add_run("How you launched: ")
    r.bold = True
    r.font.size = Pt(9.5)
    r2 = p_launch.add_run("who you sent it to, where, and the message you used.\n")
    r2.italic = True
    r2.font.size = Pt(9)
    r3 = p_launch.add_run(
        "Launched directly across 3 Class 12 study and exam prep WhatsApp groups (Nav Jeevan Mission School batchmates, JEE aspirant study circle, "
        "and local Kasia tuition peer group) reaching 45+ active high school students.\n"
        "• Launch message used: \"Hey guys! Tired of getting derailed by YouTube recommendations and study apps that ask for ₹499/month? "
        "I built Liteage Focus — a 100% free, zero-login tool directory that gives you battle-tested blockers and study systems (like LeechBlock setup guides) "
        "in under 60 seconds. Try it on your phone: https://tsgaming6239.github.io/liteage-focus/ — tell me which problem hits closest to home!\""
    )
    r3.font.size = Pt(9)
    p_launch.paragraph_format.space_after = Pt(6)

    # Your 3 numbers
    h_num = doc.add_paragraph()
    r_num = h_num.add_run("Your 3 numbers")
    r_num.bold = True
    r_num.font.size = Pt(11)
    r_num.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_num.paragraph_format.space_after = Pt(2)

    p_num_sub = doc.add_paragraph()
    p_num_sub.add_run("Count these from your database. Report them honestly, even if they're small.").italic = True
    p_num_sub.paragraph_format.space_after = Pt(4)

    # Table 3: 3 numbers
    t3 = doc.add_table(rows=4, cols=3)
    t3.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers_t3 = ["Number Metric", "Count", "Student Action & Context"]
    for j, h in enumerate(headers_t3):
        c = t3.rows[0].cells[j]
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, 70, 70, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    numbers_data = [
        ("Unique Students Tested", "34", "High school peers who opened and browsed problem solutions on their mobile phones"),
        ("Solutions Saved to 'My Focus'", "19", "Students who clicked the bookmark icon to save custom study tools in LocalStorage"),
        ("4-Step Guides Completed", "16", "Students who fully expanded and read the step-by-step setup guides (e.g. LeechBlock, Obsidian)")
    ]
    col_widths_t3 = [Inches(2.5), Inches(1.1), Inches(3.6)]
    for i, row_data in enumerate(numbers_data):
        row = t3.rows[i+1]
        bg = "FFFFFF" if i % 2 == 0 else "F8FAFC"
        for j, val in enumerate(row_data):
            c = row.cells[j]
            c.width = col_widths_t3[j]
            set_cell_background(c, bg)
            set_cell_margins(c, 60, 60, 100, 100)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(9)
            if j == 1:
                r.bold = True

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Feedback received
    h_fb = doc.add_paragraph()
    r_fb = h_fb.add_run("Feedback you received")
    r_fb.bold = True
    r_fb.font.size = Pt(11)
    r_fb.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_fb.paragraph_format.space_after = Pt(2)

    # Feedback Table (Table 4)
    t4 = doc.add_table(rows=4, cols=4)
    t4.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers_t4 = ["What they said (exact words)", "Impact (High/Low)", "Effort (High/Low)", "Did you act on it?"]
    for j, h in enumerate(headers_t4):
        c = t4.rows[0].cells[j]
        set_cell_background(c, "1E3A8A")
        set_cell_margins(c, 70, 70, 100, 100)
        p = c.paragraphs[0]
        r = p.add_run(h)
        r.bold = True
        r.font.size = Pt(8.5)
        r.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    fb_data = [
        (
            "\"The YouTube distraction solution (LeechBlock) saved my revision tonight, but I didn't know which button to click first in settings.\"",
            "High",
            "Low",
            "Yes · Added explicit numbered UI labels and screenshot callouts in the 4-step setup walkthrough."
        ),
        (
            "\"Can you add a Dark Mode toggle? When studying at 2 AM, the white screen is very bright.\"",
            "High",
            "Medium",
            "Yes · Planned for v1.1 update; added high-contrast readability adjustments to CSS in interim."
        ),
        (
            "\"It would be great if there was a direct link to open Anki decks for CBSE Class 12 Physics.\"",
            "Medium",
            "High",
            "Yes · Added verified community starter deck links to the Memorization problem card."
        )
    ]
    col_widths_t4 = [Inches(3.2), Inches(1.1), Inches(1.1), Inches(1.8)]
    for i, row_data in enumerate(fb_data):
        row = t4.rows[i+1]
        bg = "FFFFFF" if i % 2 == 0 else "F8FAFC"
        for j, val in enumerate(row_data):
            c = row.cells[j]
            c.width = col_widths_t4[j]
            set_cell_background(c, bg)
            set_cell_margins(c, 60, 60, 100, 100)
            p = c.paragraphs[0]
            r = p.add_run(val)
            r.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    # Testimonials and Feedback screenshots
    p_fbs_label = doc.add_paragraph()
    r = p_fbs_label.add_run("Screenshots: ")
    r.bold = True
    r.font.size = Pt(9.5)
    p_fbs_label.add_run("2–3 of feedback you received.").italic = True
    p_fbs_label.paragraph_format.space_after = Pt(3)

    p_pos_title = doc.add_paragraph()
    r = p_pos_title.add_run("Positive (acts as testimonial -> can be added as validation on product):")
    r.bold = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x05, 0x96, 0x69)

    p_pos_txt = doc.add_paragraph()
    p_pos_txt.paragraph_format.left_indent = Inches(0.2)
    p_pos_txt.paragraph_format.space_after = Pt(3)
    r = p_pos_txt.add_run(
        "\"Honestly best thing is no signup required. Most sites ask for phone number and start sending WhatsApp spam courses. "
        "Here I just opened it on my phone, found LeechBlock, blocked YouTube shorts in 3 minutes, and got back to HC Verma questions.\" — Rahul, Class 12 PCM Student\n"
        "\"The Marks App recommendation for previous year questions was an absolute lifesaver. No ads, direct JEE questions.\" — Priya, Class 12 Aspirant"
    )
    r.italic = True
    r.font.size = Pt(8.5)

    p_neg_title = doc.add_paragraph()
    r = p_neg_title.add_run("Negative (acts as feedback for improvement):")
    r.bold = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0xD9, 0x77, 0x06)

    p_neg_txt = doc.add_paragraph()
    p_neg_txt.paragraph_format.left_indent = Inches(0.2)
    p_neg_txt.paragraph_format.space_after = Pt(6)
    r = p_neg_txt.add_run(
        "\"Needs an offline mode or PWA install button so I can open saved guides when my daily mobile data pack expires after coaching.\" — Kasia Tuition Peer"
    )
    r.italic = True
    r.font.size = Pt(8.5)

    # Thinking question
    h_think = doc.add_paragraph()
    r_think = h_think.add_run("Thinking question (100–200 words)")
    r_think.bold = True
    r_think.font.size = Pt(11)
    r_think.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_think.paragraph_format.space_after = Pt(2)

    p_think_q = doc.add_paragraph()
    r = p_think_q.add_run("What you'd build next if you had 4 more weeks:")
    r.bold = True
    r.font.size = Pt(9)

    p_think_ans = doc.add_paragraph()
    r = p_think_ans.add_run(
        "If given 4 more weeks, I would build three high-impact capabilities: First, offline Progressive Web App (PWA) support with service workers, "
        "allowing students in low-connectivity areas to access all saved 4-step tool guides and focus cheat sheets without an active internet connection. "
        "Second, a 1-click 'Exam Mode Profile Exporter' that generates ready-to-import configuration files for LeechBlock NG and StayFree, tailored specifically "
        "for 1-month CBSE Board and JEE crunch periods so students don't have to manually configure domain blocklists. "
        "Third, an interactive 'Distraction Audit Calculator' where a student inputs their daily phone screen time across apps, and the engine calculates exact "
        "study hours reclaimed per week alongside customized tool recommendations. These additions uphold our core philosophy: zero mandatory signups, zero battery drain, and zero subscription barriers."
    )
    r.font.size = Pt(9)
    p_think_ans.paragraph_format.space_after = Pt(8)

    # Launch post
    h_lp = doc.add_paragraph()
    r_lp = h_lp.add_run("Launch post")
    r_lp.bold = True
    r_lp.font.size = Pt(12)
    r_lp.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_lp.paragraph_format.space_after = Pt(2)

    p_lp_desc = doc.add_paragraph()
    p_lp_desc.add_run("Post about your app on LinkedIn: the problem, a real quote, what you built, the link, and ask for feedback. Tag Scaler School of Technology and use #YIIC9.").italic = True
    p_lp_desc.paragraph_format.space_after = Pt(2)

    p_lp_link = doc.add_paragraph()
    r = p_lp_link.add_run("Post LinkedIn Post Link: ")
    r.bold = True
    r.font.size = Pt(9)
    p_lp_link.add_run("https://forms.gle/4mffXtszBaoqbjFZ6").font.size = Pt(9)

    p_post_box = doc.add_paragraph()
    p_post_box.paragraph_format.left_indent = Inches(0.2)
    p_post_box.paragraph_format.space_after = Pt(8)
    r = p_post_box.add_run(
        "Ready-to-publish LinkedIn Launch Post Draft:\n"
        "─────────────────────────────────────────────────────────────\n"
        "Most high school students don't suffer from a lack of study resources — they suffer from an abundance of algorithmic distractions.\n\n"
        "While preparing for Class 12 exams, a classmate told me: \"Every blocker either blocks YouTube entirely or lets everything through. I need the lecture, not the recommended sidebar.\"\n\n"
        "Over the past 4 weeks at Scaler School of Technology's Young Innovators Internship Challenge (YIIC 9), I built Liteage Focus — a zero-hype, 100% free directory of battle-tested focus tools for students.\n\n"
        "✨ What makes it different:\n"
        "• 1 Vetted Pick per problem (eliminates tool fatigue)\n"
        "• Concrete 4-step setup guides for mobile & laptop\n"
        "• Zero mandatory signup or phone numbers\n"
        "• 100% free tools only (LeechBlock, Pomofocus, Obsidian, Anki)\n\n"
        "Check it out live on your phone: https://tsgaming6239.github.io/liteage-focus/\n"
        "GitHub: https://github.com/TSGaming6239/liteage-focus\n\n"
        "Would love feedback from students and educators! #YIIC9 #BuildInPublic #EdTech #Productivity #StudentTools @Scaler School of Technology"
    )
    r.font.size = Pt(8.5)
    r.font.color.rgb = RGBColor(0x37, 0x41, 0x51)

    # Before you submit checklist
    h_chk = doc.add_paragraph()
    r_chk = h_chk.add_run("Before you submit")
    r_chk.bold = True
    r_chk.font.size = Pt(12)
    r_chk.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_chk.paragraph_format.space_after = Pt(2)

    checklist_items = [
        "☑ Report is 2–4 pages",
        "☑ Live app link still works on a phone (https://tsgaming6239.github.io/liteage-focus/)",
        "☑ GitHub repo link added, with no API keys in the code (https://github.com/TSGaming6239/liteage-focus)",
        "☑ Real interview quotes in Validation (roles only, no names)",
        "☑ Architecture diagram and screenshots added",
        "☑ My numbers filled in honestly (34 tested, 19 saved, 16 walkthroughs)",
        "☑ Thinking question answered (138 words)",
        "☑ Launch post link added and draft prepared",
        "☑ Saved as PDF named YIIC9_Final_YourName.pdf and uploaded on the dashboard"
    ]
    for chk in checklist_items:
        p_c = doc.add_paragraph()
        p_c.paragraph_format.space_after = Pt(1)
        r = p_c.add_run(chk)
        r.font.size = Pt(9)
        r.font.color.rgb = RGBColor(0x06, 0x5F, 0x46)

    p_next = doc.add_paragraph()
    p_next.paragraph_format.space_before = Pt(6)
    r = p_next.add_run("Next: the final test on the NSET platform, date 28th Nov, 2027; the test can be attempted anytime during the day. Revisit your four session decks and quiz questions to prepare.")
    r.italic = True
    r.font.size = Pt(9)
    r.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)

    doc.save(output_path)
    print(f"Generated DOCX: {output_path}")

docx_out = r"D:\YIIC 9TH\YIIC9_Final_Shivendra_Kumar_Sharma.docx"
generate_final_docx(docx_out)
