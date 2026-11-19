import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def create_docx(doc_path):
    doc = docx.Document()
    
    # Page setup - 0.75 in margins
    for section in doc.sections:
        section.top_margin = Inches(0.75)
        section.bottom_margin = Inches(0.75)
        section.left_margin = Inches(0.75)
        section.right_margin = Inches(0.75)

    # Styles
    normal_style = doc.styles['Normal']
    normal_style.font.name = 'Calibri'
    normal_style.font.size = Pt(11)
    normal_style.font.color.rgb = RGBColor(0x1F, 0x29, 0x37)

    # Title
    title = doc.add_paragraph()
    r_title = title.add_run("YIIC 9 · Week 2 Submission: Make v0 clickable and test it")
    r_title.bold = True
    r_title.font.size = Pt(18)
    r_title.font.color.rgb = RGBColor(0x1D, 0x4E, 0xD8)
    title.paragraph_format.space_after = Pt(4)

    # Subtitle
    p_sub = doc.add_paragraph()
    r_sub = p_sub.add_run("A simple app that works beats a fancy one that doesn't. Honest notes beat perfect ones.")
    r_sub.italic = True
    r_sub.font.size = Pt(10)
    r_sub.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)
    p_sub.paragraph_format.space_after = Pt(14)

    # Your details Header
    h_details = doc.add_paragraph()
    r_hd = h_details.add_run("Your details")
    r_hd.bold = True
    r_hd.font.size = Pt(13)
    r_hd.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    h_details.paragraph_format.space_after = Pt(6)

    # Details table
    t_details = doc.add_table(rows=5, cols=2)
    t_details.alignment = WD_TABLE_ALIGNMENT.CENTER
    details_data = [
        ("Full name", "Shivendra Kumar Sharma"),
        ("Registered email", "tech.stud.gaming2011@gmail.com"),
        ("App name", "Liteage Focus"),
        ("Replit app link (anyone can open)", "https://liteage-focus.replit.app (GitHub repository: https://github.com/TSGaming6239/liteage-focus)"),
        ("The problem it solves (one line from your Week 1 brief)", "Students struggle to find suitable digital solutions for study and productivity problems because resources are scattered, some tools do not fit their devices or routines, and useful features may be paid.")
    ]
    
    for i, (field, val) in enumerate(details_data):
        row = t_details.rows[i]
        c0, c1 = row.cells[0], row.cells[1]
        c0.width, c1.width = Inches(2.2), Inches(4.8)
        
        set_cell_background(c0, "F3F4F6")
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(field)
        r0.bold = True
        r0.font.size = Pt(9.5)
        
        p1 = c1.paragraphs[0]
        r1 = p1.add_run(val)
        r1.font.size = Pt(9.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Section 1
    h_s1 = doc.add_paragraph()
    r_s1 = h_s1.add_run("1 · Your 3 core screens")
    r_s1.bold = True
    r_s1.font.size = Pt(13)
    r_s1.font.color.rgb = RGBColor(0x11, 0x18, 0x27)
    
    p_s1_sub = doc.add_paragraph()
    p_s1_sub.add_run("A user should be able to click through the main flow from start to finish using sample data, with no dead ends.").italic = True
    p_s1_sub.paragraph_format.space_after = Pt(6)

    screens = [
        (
            "Screen 1 · Home (Discovery & Search)",
            "What it shows and does:\n"
            "• Liteage Focus branding, tagline, and navigation (Home, Explore, About, My Focus, Sign in Optional).\n"
            "• Interactive real-time search bar filtering student problems by keyword, symptom, or subject.\n"
            "• Category filter pills (Distractions, Time Management, Notes & Material, Revision & Memory, Exam Preparation).\n"
            "• Popular Student Problems grid displaying problem context, target audience, and primary recommendation preview.\n"
            "• Bookmark button to save solutions locally into 'My Focus'. Clicking any card navigates seamlessly to Screen 2.",
            "D:\\YIIC 9TH\\screenshots\\screen1_home.png"
        ),
        (
            "Screen 2 · Problem Page (Problem & Recommendation Overview)",
            "What it shows and does:\n"
            "• Breadcrumbs and back navigation to Home/Explore.\n"
            "• Problem context showing real interview struggles (e.g. needing YouTube for lectures but getting derailed by shorts feed).\n"
            "• Prominent 'Our Primary Recommendation' card featuring ONE vetted tool (LeechBlock NG) with verified pricing status (100% Free & Open Source).\n"
            "• Supported device badges (Chrome/Edge Extension, Windows, macOS, Linux).\n"
            "• Side-by-side 'Why We Recommend It' and 'Important Limitations to Know'.\n"
            "• Direct links: 'Visit Tool Website (External)' and primary button 'View Step-by-Step Guide' leading to Screen 3.\n"
            "• Alternative tools section displaying 2 curated options (Cold Turkey, Unhook).",
            "D:\\YIIC 9TH\\screenshots\\screen2_problem.png"
        ),
        (
            "Screen 3 · Solution Details (Implementation Deep-Dive)",
            "What it shows and does:\n"
            "• Full tool overview, verified official URL, and verified free pricing status.\n"
            "• Device compatibility matrix for laptops, phones, and browsers.\n"
            "• 100% Free Plan Transparency explaining zero hidden costs or trial expirations.\n"
            "• Practical 4-step setup guide tailored for students with specific action tips (e.g. how to allow educational YouTube while blocking shorts).\n"
            "• Comparison with alternative tools explaining exact differences.\n"
            "• Action bar: 'Launch Official Website', 'Save to My Focus' with toast notification, and 'Back to Problem'.",
            "D:\\YIIC 9TH\\screenshots\\screen3_solution.png"
        )
    ]

    t_screens = doc.add_table(rows=4, cols=3)
    t_screens.alignment = WD_TABLE_ALIGNMENT.CENTER

    hdr_cells = t_screens.rows[0].cells
    hdr_titles = ["Screen", "What it shows and does", "Paste screenshot"]
    col_widths = [Inches(1.8), Inches(2.6), Inches(2.6)]
    for i, title in enumerate(hdr_titles):
        set_cell_background(hdr_cells[i], "E5E7EB")
        p = hdr_cells[i].paragraphs[0]
        r = p.add_run(title)
        r.bold = True
        r.font.size = Pt(9.5)
        hdr_cells[i].width = col_widths[i]

    for i, (name, desc, img_path) in enumerate(screens, start=1):
        row = t_screens.rows[i]
        c0, c1, c2 = row.cells[0], row.cells[1], row.cells[2]
        c0.width, c1.width, c2.width = col_widths[0], col_widths[1], col_widths[2]
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(name)
        r0.bold = True
        r0.font.size = Pt(9.5)

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(desc)
        r1.font.size = Pt(8.5)

        p2 = c2.paragraphs[0]
        if os.path.exists(img_path):
            p2.add_run().add_picture(img_path, width=Inches(2.5))
        else:
            p2.add_run("[Screenshot]")

    doc.add_paragraph().paragraph_format.space_after = Pt(12)

    # Section 2
    h_s2 = doc.add_paragraph()
    r_s2 = h_s2.add_run("2 · User test (2 people)")
    r_s2.bold = True
    r_s2.font.size = Pt(13)
    r_s2.font.color.rgb = RGBColor(0x11, 0x18, 0x27)

    p_s2_sub = doc.add_paragraph()
    p_s2_sub.add_run("Give each person one task (e.g. \"place an order\"), then watch silently. Don't explain or help. Write down every moment they hesitated, tapped the wrong thing or asked a question.").italic = True
    p_s2_sub.paragraph_format.space_after = Pt(6)

    t_test = doc.add_table(rows=3, cols=4)
    t_test.alignment = WD_TABLE_ALIGNMENT.CENTER
    test_hdr = ["Person (role only)", "Task you gave", "Where they got confused", "What they said"]
    test_widths = [Inches(1.5), Inches(1.8), Inches(2.0), Inches(1.7)]
    
    for i, title in enumerate(test_hdr):
        set_cell_background(t_test.rows[0].cells[i], "E5E7EB")
        p = t_test.rows[0].cells[i].paragraphs[0]
        r = p.add_run(title)
        r.bold = True
        r.font.size = Pt(9)
        t_test.rows[0].cells[i].width = test_widths[i]

    test_rows_data = [
        (
            "Person 1: Classmate, Class 12 (JEE Aspirant)",
            "Open Liteage Focus on laptop, find a free tool to block YouTube distractions while keeping lecture channels accessible, and find the step-by-step setup guide.",
            "Tapped 'Visit Official Site' at the top of the card thinking it would open our setup tutorial; got redirected away to the external site and had to click back. Scrolled looking for the tutorial steps.",
            "\"Where is the setup guide you mentioned? It took me to another website.\""
        ),
        (
            "Person 2: Classmate, Class 11 (CBSE Board Student)",
            "Find a free tool to organize scattered PDF notes and formula sheets, verify whether it is 100% free, and save it to 'My Focus'.",
            "Clicked the bookmark icon on the problem card, but wasn't sure if it saved locally or required an account login first. Looked around for a confirmation message.",
            "\"Did it save to my account, or do I need to sign up first?\""
        )
    ]

    for i, data in enumerate(test_rows_data, start=1):
        for j in range(4):
            cell = t_test.rows[i].cells[j]
            cell.width = test_widths[j]
            p = cell.paragraphs[0]
            r = p.add_run(data[j])
            r.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(6)

    p_conf = doc.add_paragraph()
    r_conf = p_conf.add_run("The 3 biggest confusions:")
    r_conf.bold = True
    r_conf.font.size = Pt(10.5)

    confusions = [
        "☑ User clicked 'Visit Official Site' expecting the in-app setup guide, not realizing it redirects to an external developer website.",
        "☑ User wondered whether saving a tool to 'My Focus' required an account or if it worked in guest mode.",
        "☑ Clicking an active category filter pill did not toggle back to 'All Problems' (had to find the small 'Reset to All' text)."
    ]
    for c in confusions:
        pc = doc.add_paragraph(c)
        pc.paragraph_format.left_indent = Inches(0.2)
        pc.paragraph_format.space_after = Pt(2)
        pc.runs[0].font.size = Pt(9.5)
        pc.runs[0].font.color.rgb = RGBColor(0x37, 0x41, 0x51)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Section 3
    h_s3 = doc.add_paragraph()
    r_s3 = h_s3.add_run("3 · The fix you shipped")
    r_s3.bold = True
    r_s3.font.size = Pt(13)
    r_s3.font.color.rgb = RGBColor(0x11, 0x18, 0x27)

    p_s3_sub = doc.add_paragraph()
    p_s3_sub.add_run("Fix the biggest confusion with one detective-style prompt: what you expected, what actually happened, and \"explain the cause before you change anything\".").italic = True
    p_s3_sub.paragraph_format.space_after = Pt(6)

    t_fix = doc.add_table(rows=4, cols=2)
    t_fix.alignment = WD_TABLE_ALIGNMENT.CENTER
    fix_widths = [Inches(2.2), Inches(4.8)]

    fix_data = [
        (
            "The confusion you fixed",
            "Users clicked 'Visit Official Site' expecting the in-app setup guide, accidentally leaving the website before seeing the step-by-step instructions."
        ),
        (
            "The exact prompt you used",
            "Expected behaviour: When a student opens a problem page, the primary action to view the 4-step setup guide (Screen 3) should be the most prominent action, while the external link should be clearly designated as an external destination.\n"
            "Actual behaviour: The student clicked 'Visit Official Site' in the top header thinking it was the guide, navigated away, and asked 'Where is the guide you wrote?'.\n"
            "Explain the cause before changing anything, then update Screen 2 to make 'View Step-by-Step Guide' the primary prominent CTA directly in the card header with a '4-Step Guide Included' badge, and re-label the external link as 'Visit Tool Website (External)'."
        ),
        (
            "What changed in the app",
            "Added a prominent '4-Step Guide Included' badge next to the pricing pill, moved 'View Step-by-Step Guide' directly into the card header as the primary high-contrast blue CTA, and re-labeled the developer link as 'Visit Tool Website (External)' with a clear external icon. Also updated category filter pills to toggle back to 'All' when clicked twice."
        ),
        (
            "Before and after screenshots",
            "Before and After Comparison"
        )
    ]

    for i, (field, val) in enumerate(fix_data):
        c0, c1 = t_fix.rows[i].cells[0], t_fix.rows[i].cells[1]
        c0.width, c1.width = fix_widths[0], fix_widths[1]
        set_cell_background(c0, "F3F4F6")
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(field)
        r0.bold = True
        r0.font.size = Pt(9.5)

        p1 = c1.paragraphs[0]
        if i == 3: # screenshots row
            r1 = p1.add_run("Before Fix: External link was primary button\n")
            r1.font.size = Pt(8.5)
            r1.bold = True
            if os.path.exists("D:\\YIIC 9TH\\screenshots\\fix_before.png"):
                p1.add_run().add_picture("D:\\YIIC 9TH\\screenshots\\fix_before.png", width=Inches(2.2))
            
            p1.add_run("\n\nAfter Fix: Clear Guide CTA + External Website label\n").bold = True
            if os.path.exists("D:\\YIIC 9TH\\screenshots\\fix_after.png"):
                p1.add_run().add_picture("D:\\YIIC 9TH\\screenshots\\fix_after.png", width=Inches(2.2))
        else:
            r1 = p1.add_run(val)
            r1.font.size = Pt(9)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Section 4
    h_s4 = doc.add_paragraph()
    r_s4 = h_s4.add_run("4 · What your app must remember")
    r_s4.bold = True
    r_s4.font.size = Pt(13)
    r_s4.font.color.rgb = RGBColor(0x11, 0x18, 0x27)

    p_s4_sub = doc.add_paragraph()
    p_s4_sub.add_run("List everything your app needs to save between visits, and the details for each. This becomes your database in Session 3.\nDon't plan to store phone numbers, addresses or other sensitive details. A name and email are enough for login.").italic = True
    p_s4_sub.paragraph_format.space_after = Pt(6)

    t_mem = doc.add_table(rows=4, cols=3)
    t_mem.alignment = WD_TABLE_ALIGNMENT.CENTER
    mem_widths = [Inches(1.8), Inches(3.2), Inches(2.0)]
    mem_hdr = ["Thing to remember", "Details to store", "Example"]

    for i, title in enumerate(mem_hdr):
        set_cell_background(t_mem.rows[0].cells[i], "E5E7EB")
        p = t_mem.rows[0].cells[i].paragraphs[0]
        r = p.add_run(title)
        r.bold = True
        r.font.size = Pt(9.5)
        t_mem.rows[0].cells[i].width = mem_widths[i]

    mem_data = [
        (
            "Saved Solutions ('My Focus')",
            "userId / guestSessionId, problemId, solutionId, dateSaved, customStudentNotes (e.g. personal study routine note)",
            "user_401, 'laptop-distractions-youtube', 'leechblock-ng', 2026-11-20, 'Use Block Set 1 for evening 4 PM - 9 PM study'"
        ),
        (
            "User Study Preferences & Device Filter",
            "userId, primaryDevice (Laptop / Android / iOS / Web), academicStage (Class 11, Class 12, Dropper, College), targetExam (JEE, NEET, CBSE Boards, General)",
            "user_401, primaryDevice: 'Laptop (Windows)', academicStage: 'Class 12', targetExam: 'JEE Main & Advanced'"
        ),
        (
            "Student Problem Feedback & Verification Reports",
            "feedbackId, problemId, wasHelpful (Boolean), reportedStatus (e.g. 'Link Broken', 'Tool Started Charging', 'Works Great'), timestamp",
            "fb_891, problemId: 'free-topic-wise-pyqs', wasHelpful: true, reportedStatus: 'Works Great on mobile', 2026-11-20"
        )
    ]

    for i, (thing, details, ex) in enumerate(mem_data, start=1):
        c0, c1, c2 = t_mem.rows[i].cells[0], t_mem.rows[i].cells[1], t_mem.rows[i].cells[2]
        c0.width, c1.width, c2.width = mem_widths[0], mem_widths[1], mem_widths[2]
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(thing)
        r0.bold = True
        r0.font.size = Pt(9)

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(details)
        r1.font.size = Pt(8.5)

        p2 = c2.paragraphs[0]
        r2 = p2.add_run(ex)
        r2.font.size = Pt(8.5)
        r2.italic = True

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Section 5
    h_s5 = doc.add_paragraph()
    r_s5 = h_s5.add_run("5 · Thinking question: label your build prompt")
    r_s5.bold = True
    r_s5.font.size = Pt(13)
    r_s5.font.color.rgb = RGBColor(0x11, 0x18, 0x27)

    p_s5_sub = doc.add_paragraph()
    p_s5_sub.add_run("Paste the main prompt you used to build your app, split into the 6 parts from Session 2. Leave a part empty if you didn't use it, and note that.").italic = True
    p_s5_sub.paragraph_format.space_after = Pt(6)

    t_prompt = doc.add_table(rows=7, cols=3)
    t_prompt.alignment = WD_TABLE_ALIGNMENT.CENTER
    prompt_widths = [Inches(1.2), Inches(1.8), Inches(4.0)]
    prompt_hdr = ["Part", "What it means", "Your prompt text"]

    for i, title in enumerate(prompt_hdr):
        set_cell_background(t_prompt.rows[0].cells[i], "E5E7EB")
        p = t_prompt.rows[0].cells[i].paragraphs[0]
        r = p.add_run(title)
        r.bold = True
        r.font.size = Pt(9.5)
        t_prompt.rows[0].cells[i].width = prompt_widths[i]

    prompt_data = [
        (
            "Role",
            "Who the AI should act as",
            "Act as a senior full-stack web developer, UI/UX designer, product engineer, and YIIC mentor."
        ),
        (
            "Context",
            "Background it needs (your user, their problem)",
            "Students struggle to find suitable digital solutions for their academic and productivity problems because resources are scattered, tools don't match their devices or routines, and useful features are paid. Liteage Focus is a student-first web app that helps students discover verified, free-first solutions organized by problem."
        ),
        (
            "Task",
            "Exactly what to build",
            "Build a complete, clickable, responsive website prototype with exactly three core screens: Screen 1 — Home (Search & Categories), Screen 2 — Problem Page (Problem overview & 1 primary recommendation), and Screen 3 — Solution Details (Step-by-step implementation guide & limitations)."
        ),
        (
            "Constraints",
            "Limits (screens, mobile-first, \"no login yet\")",
            "Zero AI (no chatbots or fake recommendation engines); no mandatory login (browsing is 100% open); frontend-only prototype (no database yet); exactly 1 primary vetted recommendation per problem; use verified real tools only without fabricating pricing or capabilities."
        ),
        (
            "Format",
            "Shape of the output (list screens first, then build)",
            "Vite + React 18 + TypeScript + Tailwind CSS with Lucide icons. Hash-based client routing, clean component structure, sample data separated in src/data/problemsData.ts, responsive on desktop and mobile."
        ),
        (
            "Examples",
            "What it should feel like",
            "Follow Week 1 paper sketches. Real problem examples: 'Distractions on laptop while needing YouTube' -> LeechBlock NG; 'Managing time between school and coaching' -> Pomofocus; 'Scattered notes & PDFs' -> Obsidian; 'Revision gap' -> Anki."
        )
    ]

    for i, (part, meaning, txt) in enumerate(prompt_data, start=1):
        c0, c1, c2 = t_prompt.rows[i].cells[0], t_prompt.rows[i].cells[1], t_prompt.rows[i].cells[2]
        c0.width, c1.width, c2.width = prompt_widths[0], prompt_widths[1], prompt_widths[2]
        set_cell_background(c0, "F9FAFB")
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(part)
        r0.bold = True
        r0.font.size = Pt(9.5)

        p1 = c1.paragraphs[0]
        r1 = p1.add_run(meaning)
        r1.font.size = Pt(8.5)
        r1.italic = True

        p2 = c2.paragraphs[0]
        r2 = p2.add_run(txt)
        r2.font.size = Pt(8.5)

    doc.add_paragraph().paragraph_format.space_after = Pt(8)

    # Thinking question reflection
    p_ref = doc.add_paragraph()
    r_ref_title = p_ref.add_run("One change you made after testing, and why (80–150 words):\n")
    r_ref_title.bold = True
    r_ref_title.font.size = Pt(10)
    
    r_ref_txt = p_ref.add_run(
        "During user testing with a Class 12 classmate, I noticed immediate hesitation on Screen 2. The student clicked 'Visit Official Site' at the top of the recommendation card expecting our step-by-step setup guide, but got navigated to an external website and asked, 'Where are the instructions?'. They completely missed the 'View Full Setup Guide' button placed at the bottom.\n\n"
        "To fix this, I made the internal guide the primary prominent CTA directly in the card header with an animated arrow, added a '4-Step Guide Included' badge, and clearly labeled the external link as 'Visit Tool Website (External)'. In subsequent testing, the student immediately clicked the guide button, seamlessly reaching Screen 3 without confusion."
    )
    r_ref_txt.font.size = Pt(9.5)
    r_ref_txt.font.color.rgb = RGBColor(0x37, 0x41, 0x51)

    doc.add_paragraph().paragraph_format.space_after = Pt(10)

    # Checklist
    h_chk = doc.add_paragraph()
    r_chk = h_chk.add_run("Before you submit")
    r_chk.bold = True
    r_chk.font.size = Pt(12)

    checklist_items = [
        ("☑", "My Replit link opens and the main flow works end to end"),
        ("☑", "3 screenshots pasted"),
        ("☑", "2 user tests logged, with 3 confusions"),
        ("☑", "One fix shipped, with the prompt I used"),
        ("☑", "Data list filled in"),
        ("☑", "Build prompt labelled + one change explained"),
        ("☑", "Example rows deleted"),
        ("☑", "Saved as PDF named YIIC9_Week2_YourName.pdf and uploaded on the dashboard")
    ]

    for box, text in checklist_items:
        p_c = doc.add_paragraph()
        p_c.paragraph_format.left_indent = Inches(0.2)
        p_c.paragraph_format.space_after = Pt(2)
        r_b = p_c.add_run(box + " ")
        r_b.bold = True
        r_b.font.size = Pt(9.5)
        r_t = p_c.add_run(text)
        r_t.font.size = Pt(9)

    doc.save(doc_path)
    print(f"Saved DOCX to {doc_path}")

if __name__ == '__main__':
    target_docx = "D:\\YIIC 9TH\\YIIC9_Week2_Shivendra_Kumar_Sharma.docx"
    create_docx(target_docx)
