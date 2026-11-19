import { Problem, Solution } from '../types';

export const SOLUTIONS: Record<string, Solution> = {
  'leechblock-ng': {
    id: 'leechblock-ng',
    name: 'LeechBlock NG',
    tagline: 'Simple, lightweight, and completely free web productivity tool for blocking time-wasting sites.',
    verifiedOfficialUrl: 'https://www.proginosko.com/leechblock/',
    category: 'Distractions',
    pricingStatus: '100% Free & Open Source',
    isCompletelyFree: true,
    freePlanDetails: 'Completely free forever with no premium tier, no paywalled features, and no tracking/ads.',
    platforms: ['Chrome / Edge Extension', 'Windows', 'macOS', 'Linux'],
    whyRecommended: [
      'Allows selective whitelisting (e.g. keep educational YouTube channels accessible while blocking shorts and home feed).',
      'No account or registration required to set up customized study blocks.',
      'Includes strict lockdown delay modes (e.g. prevents disabling blocks when willpower is low).',
      'Lightweight with zero background battery drain on student laptops.'
    ],
    honestLimitations: [
      'Works inside your web browser (Chrome, Edge, Firefox, Brave) but does not block native desktop programs (like standalone Discord or games).',
      'Setup requires 5 minutes to configure your blocked domain list initially.'
    ],
    setupGuide: [
      {
        stepNumber: 1,
        title: 'Install Extension',
        description: 'Install LeechBlock NG directly from the Chrome Web Store or Firefox Add-ons repository.',
        tip: 'Ensure you enable the extension in "Incognito / InPrivate" mode in your browser extension settings.'
      },
      {
        stepNumber: 2,
        title: 'Define Block Sets',
        description: 'Open LeechBlock Options and paste distraction domains into Block Set 1 (e.g., instagram.com, twitter.com, reddit.com, netflix.com).',
        tip: 'To allow educational YouTube while blocking distractions, add youtube.com/shorts* to the blocklist.'
      },
      {
        stepNumber: 3,
        title: 'Set Time Periods',
        description: 'Configure your active study window (e.g. 15:00-21:00 on weekdays) or set an allowed quota of 15 minutes per day.',
        tip: 'You can select "Prevent access during these times" or "Limit access after X minutes".'
      },
      {
        stepNumber: 4,
        title: 'Enable Lockdown Protection',
        description: 'Turn on password protection or a delayed override code (e.g., must type a 64-character random string) so you do not cancel it impulsively.',
        tip: 'Ask a parent or study buddy to set an emergency password if you struggle with self-control.'
      }
    ],
    alternatives: [
      {
        id: 'cold-turkey',
        name: 'Cold Turkey Blocker',
        tagline: 'Deep system-level blocker for Windows & macOS.',
        pricingType: 'Generous Free Tier',
        bestFor: 'Students who need to block desktop apps and full computers, not just browser tabs.',
        websiteUrl: 'https://getcoldturkey.com',
        keyDifference: 'Locks down the entire operating system, but advanced schedule rotations require a one-time pro license.'
      },
      {
        id: 'unhook',
        name: 'Unhook (Remove YouTube Distractions)',
        tagline: 'Hides YouTube recommendations, shorts, and comments.',
        pricingType: '100% Free',
        bestFor: 'Students whose main distraction is getting sucked into YouTube sidebar rabbit holes.',
        websiteUrl: 'https://unhook.app',
        keyDifference: 'Specialized specifically for YouTube only; keeps search and lectures clean without blocking the site completely.'
      }
    ]
  },

  'pomofocus': {
    id: 'pomofocus',
    name: 'Pomofocus',
    tagline: 'Customizable, web-based Pomodoro timer designed for distraction-free subject task blocks.',
    verifiedOfficialUrl: 'https://pomofocus.io',
    category: 'Time Management',
    pricingStatus: '100% Free Web App',
    isCompletelyFree: true,
    freePlanDetails: 'All core features (custom interval times, task lists, break cycles, sound alerts, background dark mode) are free without any account.',
    platforms: ['Web', 'Windows', 'macOS', 'Android', 'iOS'],
    whyRecommended: [
      'Requires zero sign-up or phone number: open the webpage and start studying immediately.',
      'Lets you list distinct subjects (e.g. "Physics Electrostatics - 2 pomodoros", "Maths Matrices - 3 pomodoros").',
      'Provides customizable intervals (e.g. 50 min study / 10 min break instead of the rigid 25/5).',
      'Minimalist, low-contrast interface that does not strain tired eyes during evening study.'
    ],
    honestLimitations: [
      'Saved tasks are stored locally in browser storage unless an account is connected.',
      'Web-based, so you need an active browser tab open.'
    ],
    setupGuide: [
      {
        stepNumber: 1,
        title: 'Open in Browser & Bookmark',
        description: 'Navigate to pomofocus.io and bookmark it in your browser bookmarks bar for instant access.',
        tip: 'Press F11 on your keyboard to enter fullscreen mode for zero screen distraction.'
      },
      {
        stepNumber: 2,
        title: 'Adjust Subject Intervals',
        description: 'Click "Setting" in the top bar. Set Pomodoro time (recommended: 45 or 50 minutes for JEE/class 12 subjects) and Short Break to 10 minutes.',
        tip: 'Enable "Auto Start Pomodoros" only if you want strict pacing without touching your mouse.'
      },
      {
        stepNumber: 3,
        title: 'Add Daily Study Targets',
        description: 'Click "+ Add Task" and break down your evening: "Organic Chem - NCERT Reading", "Physics - 15 HCV Problems". Estimate required pomodoros.',
        tip: 'Focus exclusively on the top task until the timer chimes.'
      },
      {
        stepNumber: 4,
        title: 'Take Honest Breaks',
        description: 'When the timer rings, step away from your chair, drink water, and rest your eyes without opening social media.',
        tip: 'Do not use phone screen during the 10-minute break.'
      }
    ],
    alternatives: [
      {
        id: 'toggl-track',
        name: 'Toggl Track',
        tagline: 'Detailed time auditing and study hours tracker.',
        pricingType: 'Generous Free Tier',
        bestFor: 'Students who want weekly analytics on how much time went into Physics vs. Chemistry vs. School.',
        websiteUrl: 'https://toggl.com/track/',
        keyDifference: 'Focuses on retrospective time logs and charts rather than a simple countdown timer.'
      },
      {
        id: 'google-calendar',
        name: 'Google Calendar (Time Blocking)',
        tagline: 'Standard digital calendar for visual routine blocks.',
        pricingType: '100% Free',
        bestFor: 'Balancing fixed school schedules, coaching classes, and self-study slots on a weekly calendar.',
        websiteUrl: 'https://calendar.google.com',
        keyDifference: 'High-level weekly planning tool rather than a minute-by-minute focus timer.'
      }
    ]
  },

  'obsidian': {
    id: 'obsidian',
    name: 'Obsidian',
    tagline: 'A fast, private, offline-first markdown knowledge base that stores your notes and PDFs locally on your device.',
    verifiedOfficialUrl: 'https://obsidian.md',
    category: 'Notes & Material',
    pricingStatus: '100% Free for Personal Use',
    isCompletelyFree: true,
    freePlanDetails: '100% free for 100% of personal use. All local note-taking, PDF viewing, linking, plugins, and graph view are free with no card required.',
    platforms: ['Windows', 'macOS', 'Linux', 'Android', 'iOS'],
    whyRecommended: [
      'Stores everything as plain text files and PDFs directly on your hard drive — works 100% offline without internet lag.',
      'Supports bi-directional linking (`[[Chapter]]`), letting you connect formulas, question references, and concept notes seamlessly.',
      'Native built-in PDF viewer allows copying text, highlighting, and linking directly to specific PDF pages.',
      'Zero risk of losing your notes if a cloud provider shuts down or charges higher fees.'
    ],
    honestLimitations: [
      'Has a slight learning curve if you have never used Markdown formatting before.',
      'Official automated cloud sync is a paid add-on, but students can easily sync for free using Google Drive, OneDrive, or Syncthing.'
    ],
    setupGuide: [
      {
        stepNumber: 1,
        title: 'Download & Create Vault',
        description: 'Download Obsidian for your operating system (Windows/Mac/Linux/Android) and create a folder named "Class 12 Study Vault".',
        tip: 'Store this folder inside your existing Google Drive or OneDrive folder if you want free cloud backup.'
      },
      {
        stepNumber: 2,
        title: 'Create Subject Folders',
        description: 'Inside your vault, create clean folders: "01-Physics", "02-Chemistry", "03-Mathematics", "04-PYQ-PDFs".',
        tip: 'Drop your downloaded PDF question banks directly into the "04-PYQ-PDFs" folder.'
      },
      {
        stepNumber: 3,
        title: 'Take Linked Notes',
        description: 'When summarizing a chapter like "Electrostatics", link formula terms using double brackets `[[Coulombs Law]]`.',
        tip: 'Type `$$` to write clear mathematical formulas in standard LaTeX formatting.'
      },
      {
        stepNumber: 4,
        title: 'Search Anything Instantly',
        description: 'Press Ctrl+O (or Cmd+O) to jump to any note or PDF in less than a second.',
        tip: 'Use Ctrl+Shift+F to search within the text of all your saved notes simultaneously.'
      }
    ],
    alternatives: [
      {
        id: 'notion',
        name: 'Notion',
        tagline: 'All-in-one workspace with visual databases and templates.',
        pricingType: 'Generous Free Tier',
        bestFor: 'Students who prefer drag-and-drop boards, visual tables, and collaborative project planning.',
        websiteUrl: 'https://notion.so',
        keyDifference: 'Requires continuous internet connection; can feel slower on older laptops compared to Obsidian.'
      },
      {
        id: 'joplin',
        name: 'Joplin',
        tagline: 'Open-source encrypted note-taking app with notebook folders.',
        pricingType: '100% Free & Open Source',
        bestFor: 'Students seeking a traditional Evernote-style notebook hierarchy with end-to-end encryption.',
        websiteUrl: 'https://joplinapp.org',
        keyDifference: 'Traditional notebook tree structure rather than linked interconnected network graphs.'
      }
    ]
  },

  'anki': {
    id: 'anki',
    name: 'Anki',
    tagline: 'Powerful, intelligent flashcards utilizing spaced repetition to make forgetting virtually impossible.',
    verifiedOfficialUrl: 'https://apps.ankiweb.net',
    category: 'Revision & Memory',
    pricingStatus: '100% Free & Open Source on PC & Android',
    isCompletelyFree: true,
    freePlanDetails: 'Completely free on Windows, macOS, Linux, Web (AnkiWeb), and Android (AnkiDroid). Only iOS app is paid to support project maintenance.',
    platforms: ['Windows', 'macOS', 'Linux', 'Android', 'Web'],
    whyRecommended: [
      'Employs scientific spaced repetition algorithm (SM-2) that schedules card reviews right at the moment you are about to forget.',
      'Massively cuts revision time by never showing cards you already know well, focusing only on your weak spots.',
      'Supports image occlusion (hide labels on biology/chemistry diagrams and test yourself).',
      'Free sync with AnkiWeb to review flashcards on your Android phone while traveling.'
    ],
    honestLimitations: [
      'The user interface is functional and classic rather than modern/glossy.',
      'Requires daily consistency: cards accumulate if you skip reviews for a week.'
    ],
    setupGuide: [
      {
        stepNumber: 1,
        title: 'Install on Laptop or Android',
        description: 'Install Anki on your computer from apps.ankiweb.net, or download AnkiDroid from the Google Play Store.',
        tip: 'Create a free account on ankiweb.net to sync cards seamlessly between your laptop and phone.'
      },
      {
        stepNumber: 2,
        title: 'Create Subject Decks',
        description: 'Create individual decks for subjects: "Organic Reactions", "Physics Formulas", "Inorganic Exceptions".',
        tip: 'Keep decks focused on small recall items rather than entire paragraphs of notes.'
      },
      {
        stepNumber: 3,
        title: 'Make High-Quality Cards',
        description: 'Add cards with "Front" (Question/Prompt) and "Back" (Concise Answer). For formulas, use Cloze Deletion (fill-in-the-blank).',
        tip: 'A good card should take less than 10 seconds to answer.'
      },
      {
        stepNumber: 4,
        title: 'Complete 15-Minute Daily Reviews',
        description: 'Open Anki every morning or before bed. Rate how easily you recalled each card (Again, Hard, Good, Easy).',
        tip: 'Anki automatically calculates the next review date (tomorrow, 4 days, 16 days, 2 months).'
      }
    ],
    alternatives: [
      {
        id: 'quizlet',
        name: 'Quizlet',
        tagline: 'Visual flashcard app with gamified study modes.',
        pricingType: 'Generous Free Tier',
        bestFor: 'Students who want quick pre-made card decks and matching games.',
        websiteUrl: 'https://quizlet.com',
        keyDifference: 'Modern interface with pre-made community decks, but advanced spaced repetition and test modes require Quizlet Plus.'
      },
      {
        id: 'remnote',
        name: 'RemNote',
        tagline: 'Note-taking app with built-in spaced repetition flashcards.',
        pricingType: 'Generous Free Tier',
        bestFor: 'Students who want their notes and flashcards in the same single workspace.',
        websiteUrl: 'https://remnote.com',
        keyDifference: 'Combines note outlining with flashcard generation, but features some premium tier limits on complex media.'
      }
    ]
  },

  'marks-app': {
    id: 'marks-app',
    name: 'Marks App (by Score99)',
    tagline: 'Comprehensive question practice platform with chapter-wise and topic-wise Previous Year Questions (PYQs).',
    verifiedOfficialUrl: 'https://web.getmarks.app',
    category: 'Exam Preparation',
    pricingStatus: 'Free Access for Core PYQs',
    isCompletelyFree: true,
    freePlanDetails: 'Access to chapter-wise previous year questions (JEE Main, Advanced, NEET, NDA, CBSE) and solutions with bookmarking is free.',
    platforms: ['Web', 'Android'],
    whyRecommended: [
      'Directly solves the problem of finding organized, topic-wise practice without buying expensive physical question guides.',
      'Categorizes questions by difficulty, year, and specific sub-topic (e.g. "Work Energy Power - Work-Energy Theorem").',
      'Provides verified step-by-step solutions for every question right after attempting.',
      'Lets students filter out questions they already completed to focus on unattempted questions.'
    ],
    honestLimitations: [
      'Primarily focused on Indian STEM competitive exams (JEE, NEET, BITSAT, CBSE Class 11/12 boards).',
      'Requires internet connection to view questions and solutions.'
    ],
    setupGuide: [
      {
        stepNumber: 1,
        title: 'Open Web App or Download',
        description: 'Visit web.getmarks.app on your browser or install Marks App from the Google Play Store.',
        tip: 'No complex onboarding required; select your target examination (e.g. JEE Main 2026 or CBSE 12).'
      },
      {
        stepNumber: 2,
        title: 'Select Chapter & Topic',
        description: 'Choose your subject (Physics/Chemistry/Maths) and pick the chapter you just finished in school or coaching.',
        tip: 'Filter questions by "Topic-wise" instead of doing whole-year papers right away.'
      },
      {
        stepNumber: 3,
        title: 'Practice with Real Timer',
        description: 'Solve questions one by one. Use the built-in scratchpad or physical notebook, then submit your answer to check accuracy.',
        tip: 'Bookmark tricky questions into a custom "Revise Before Mock Test" bucket.'
      },
      {
        stepNumber: 4,
        title: 'Review Detailed Solutions',
        description: 'Read the detailed explanation for questions you got wrong, noting down the concept error in your notebook.',
        tip: 'Re-attempt bookmarked questions every Sunday to verify retention.'
      }
    ],
    alternatives: [
      {
        id: 'examgoal',
        name: 'ExamGoal',
        tagline: 'Real exam interface simulator with PYQs.',
        pricingType: 'Generous Free Tier',
        bestFor: 'Students who want exact NTA-style test screen simulation.',
        websiteUrl: 'https://examgoal.com',
        keyDifference: 'Affordable low-cost / free credits model with realistic exam interface, compared to Marks App mobile-first practice.'
      },
      {
        id: 'cbse-academic',
        name: 'CBSE Academic Official Portal',
        tagline: 'Official question bank, sample papers, and marking schemes.',
        pricingType: '100% Free',
        bestFor: 'Class 12 board students seeking exact official board marking patterns.',
        websiteUrl: 'https://cbseacademic.nic.in',
        keyDifference: 'Raw official PDFs from the government board without interactive tracking or topic categorization.'
      }
    ]
  },

  'stayfree': {
    id: 'stayfree',
    name: 'StayFree - Screen Time & App Limit',
    tagline: 'Clean, privacy-friendly screen time tracking and app-blocking tool for mobile devices and browsers.',
    verifiedOfficialUrl: 'https://stayfreeapps.com',
    category: 'Distractions',
    pricingStatus: 'Generous Free Tier',
    isCompletelyFree: true,
    freePlanDetails: 'Full daily limits, usage tracking, focus mode, and browser extension syncing are available on the free tier.',
    platforms: ['Android', 'iOS', 'Chrome / Edge Extension', 'macOS'],
    whyRecommended: [
      'Specifically prevents falling into Instagram reels and YouTube shorts loops right after evening classes.',
      'Includes "Focus Mode" that blocks chosen apps with a single tap during study hours.',
      'Cross-platform sync: pair your mobile and laptop usage to see real daily screen time.',
      'Does not sell personal data or display intrusive full-screen video ads.'
    ],
    honestLimitations: [
      'Advanced multi-profile scheduling requires StayFree Pro, but the basic daily app limits and instant focus mode are free.',
      'iOS version has more restrictions due to Apple system sandboxing.'
    ],
    setupGuide: [
      {
        stepNumber: 1,
        title: 'Install StayFree',
        description: 'Install StayFree on your Android phone or as a browser extension on your computer.',
        tip: 'Grant Usage Access permission on Android so it can accurately track foreground apps.'
      },
      {
        stepNumber: 2,
        title: 'Set App Limits on Traps',
        description: 'Put strict 15-minute daily caps on your worst distraction apps (Instagram, YouTube, Gaming, Discord).',
        tip: 'Enable "Block App immediately upon limit expiry".'
      },
      {
        stepNumber: 3,
        title: 'Set Up Study Schedule',
        description: 'Define your study window (e.g. 17:00 to 22:00) where only educational apps (Drive, Calculator, Zoom) remain open.',
        tip: 'Turn on PIN protection and let a trusted sibling or parent set the PIN.'
      },
      {
        stepNumber: 4,
        title: 'Check Weekly Trends',
        description: 'Review your total screen time every Sunday night to celebrate reduced distraction hours.',
        tip: 'Aim to reduce daily recreation phone time below 60 minutes during exam season.'
      }
    ],
    alternatives: [
      {
        id: 'digital-wellbeing',
        name: 'Android Digital Wellbeing',
        tagline: 'Built-in operating system focus tool.',
        pricingType: '100% Free',
        bestFor: 'Zero-install basic app timers on Android phones.',
        websiteUrl: 'https://wellbeing.google',
        keyDifference: 'Already pre-installed on Android phones, but easy to disable without friction.'
      },
      {
        id: 'forest-app',
        name: 'Forest App',
        tagline: 'Gamified tree-planting focus timer.',
        pricingType: 'Generous Free Tier',
        bestFor: 'Students who love visual gamification and rewards for staying off their phone.',
        websiteUrl: 'https://forestapp.cc',
        keyDifference: 'Gamified focus timer rather than strict blocking; free on Android with ads, paid on iOS.'
      }
    ]
  }
};

export const PROBLEMS: Problem[] = [
  {
    id: 'laptop-distractions-youtube',
    title: 'Too many distractions while studying on laptop (need YouTube for lectures, but get pulled into shorts)',
    shortSummary: 'Students need YouTube and the web for studying, but algorithmic recommendations and feeds derail their focus.',
    category: 'Distractions',
    targetAudience: 'Students studying with laptop & web browser',
    difficultyTag: 'High Priority',
    commonSymptoms: [
      'Opening YouTube for a 15-min physics lecture and waking up 2 hours later in shorts feed.',
      'Opening new tabs compulsively during difficult question-solving.',
      'Blockers that completely block YouTube prevent accessing valid educational lectures.'
    ],
    recommendedSolutionId: 'leechblock-ng'
  },
  {
    id: 'time-management-school-jee',
    title: 'How to manage time between school, coaching classes and self-study?',
    shortSummary: 'School ends late, coaching takes evenings, and students are left with zero structured time for self-study and homework.',
    category: 'Time Management',
    targetAudience: 'Class 11 & 12 students & competitive aspirants',
    difficultyTag: 'Critical Exam',
    commonSymptoms: [
      'Feeling exhausted after school and sitting idle until night without knowing what to start.',
      'No clear breakdown of how many minutes to give to Physics vs. Chemistry vs. School homework.',
      'Existing planning apps feel too complex or demand paid subscriptions.'
    ],
    recommendedSolutionId: 'pomofocus'
  },
  {
    id: 'scattered-notes-pdfs',
    title: 'Notes, formula sheets and PDF resources are scattered across folders and WhatsApp',
    shortSummary: 'Students waste 20–30 minutes searching for notes they already saved across WhatsApp, Telegram, and Drive.',
    category: 'Notes & Material',
    targetAudience: 'School & college students handling heavy study PDFs',
    difficultyTag: 'Common Daily',
    commonSymptoms: [
      'Downloading PDFs multiple times because they get lost in Download folder.',
      'No single place to connect class notes with question bank solutions.',
      'Cloud tools that require fast internet fail during offline study sessions.'
    ],
    recommendedSolutionId: 'obsidian'
  },
  {
    id: 'revision-forgetting-cycle',
    title: 'Revision gap: Understanding concepts today but forgetting them by the test date',
    shortSummary: 'Students understand the chapter when the teacher explains it, but formulas and exceptions vanish after two weeks.',
    category: 'Revision & Memory',
    targetAudience: 'Students preparing for tests and board exams',
    difficultyTag: 'High Priority',
    commonSymptoms: [
      'Rereading entire 50-page chapters repeatedly because of passive revision.',
      'Blanking on formulas or organic reaction reagents inside the exam hall.',
      'No scheduled system to know exactly which chapter needs review today.'
    ],
    recommendedSolutionId: 'anki'
  },
  {
    id: 'free-topic-wise-pyqs',
    title: 'Finding reliable, topic-wise practice questions & PYQs without expensive books',
    shortSummary: 'Students want to practice specific topics they just finished, but good question banks are expensive or paywalled.',
    category: 'Exam Preparation',
    targetAudience: 'JEE, NEET & CBSE Class 12 aspirants',
    difficultyTag: 'Critical Exam',
    commonSymptoms: [
      'Searching random websites and getting conflicting or unverified answer keys.',
      'Having full-year question papers but not being able to practice only one specific sub-topic.',
      'Educational apps locking solutions behind costly monthly subscriptions.'
    ],
    recommendedSolutionId: 'marks-app'
  },
  {
    id: 'phone-social-media-post-class',
    title: 'Falling into social media rabbit holes right after online classes end',
    shortSummary: 'The moment online class ends, students switch to Instagram or gaming to "unwind" and lose their entire evening.',
    category: 'Distractions',
    targetAudience: 'Students attending online live classes & using mobile',
    difficultyTag: 'Common Daily',
    commonSymptoms: [
      'Intending to take a 5-minute break and losing 90 minutes to reel scrolling.',
      'Fatigue and eye strain leading to procrastination on self-study.',
      'Feeling guilty at night and sleeping late, creating a cycle of exhaustion.'
    ],
    recommendedSolutionId: 'stayfree'
  }
];

export const CATEGORIES: { label: string; value: import('../types').Category; description: string }[] = [
  { label: 'All Problems', value: 'All', description: 'Browse all researched student problems and vetted tools.' },
  { label: 'Distractions', value: 'Distractions', description: 'Block feeds, shorts, and social media without blocking study sites.' },
  { label: 'Time Management', value: 'Time Management', description: 'Structure self-study hours around school and coaching schedules.' },
  { label: 'Notes & Material', value: 'Notes & Material', description: 'Organize PDFs, handwritten notes, and formulas in one place.' },
  { label: 'Revision & Memory', value: 'Revision & Memory', description: 'Active recall and spaced repetition to retain formulas long-term.' },
  { label: 'Exam Preparation', value: 'Exam Preparation', description: 'Free topic-wise practice, PYQs, and test-taking strategies.' },
];
