import React, { useState, useEffect } from 'react';
import { PROBLEMS, SOLUTIONS } from './data/problemsData';
import { Navbar } from './components/Navbar';
import { Footer } from './components/Footer';
import { HomePage } from './pages/HomePage';
import { ProblemPage } from './pages/ProblemPage';
import { SolutionDetailPage } from './pages/SolutionDetailPage';
import { SavedModal } from './components/SavedModal';
import { AboutModal } from './components/AboutModal';
import { Bookmark } from 'lucide-react';

export function App() {
  // Screen state: 'home' | 'problem' | 'solution'
  const [currentScreen, setCurrentScreen] = useState<'home' | 'problem' | 'solution'>('home');
  const [activeProblemId, setActiveProblemId] = useState<string>('laptop-distractions-youtube');
  const [activeSolutionId, setActiveSolutionId] = useState<string>('leechblock-ng');

  // Modals state
  const [isSavedModalOpen, setIsSavedModalOpen] = useState(false);
  const [isAboutModalOpen, setIsAboutModalOpen] = useState(false);

  // Toast state
  const [toastMessage, setToastMessage] = useState<string | null>(null);

  // Local storage for saved items
  const [savedProblemIds, setSavedProblemIds] = useState<string[]>(() => {
    try {
      const stored = localStorage.getItem('liteage_focus_saved');
      return stored ? JSON.parse(stored) : ['laptop-distractions-youtube'];
    } catch {
      return ['laptop-distractions-youtube'];
    }
  });

  useEffect(() => {
    try {
      localStorage.setItem('liteage_focus_saved', JSON.stringify(savedProblemIds));
    } catch {
      // ignore in sandboxed environments
    }
  }, [savedProblemIds]);

  // Sync with browser hash routing for browser Back/Forward support
  useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash;
      if (!hash || hash === '#/' || hash === '#') {
        setCurrentScreen('home');
        window.scrollTo(0, 0);
      } else if (hash === '#/explore') {
        setCurrentScreen('home');
        setTimeout(() => {
          const el = document.getElementById('explore-problems');
          if (el) {
            el.scrollIntoView({ behavior: 'smooth' });
          }
        }, 100);
      } else if (hash.startsWith('#/problem/')) {
        const id = hash.replace('#/problem/', '');
        const p = PROBLEMS.find((item) => item.id === id);
        if (p) {
          setActiveProblemId(p.id);
          setActiveSolutionId(p.recommendedSolutionId);
          setCurrentScreen('problem');
        } else {
          setCurrentScreen('home');
        }
        window.scrollTo(0, 0);
      } else if (hash.startsWith('#/solution/')) {
        const id = hash.replace('#/solution/', '');
        const s = SOLUTIONS[id];
        if (s) {
          setActiveSolutionId(s.id);
          // find related problem
          const p = PROBLEMS.find((item) => item.recommendedSolutionId === s.id);
          if (p) setActiveProblemId(p.id);
          setCurrentScreen('solution');
        } else {
          setCurrentScreen('home');
        }
        window.scrollTo(0, 0);
      }
    };

    window.addEventListener('hashchange', handleHashChange);
    handleHashChange(); // initial check

    return () => window.removeEventListener('hashchange', handleHashChange);
  }, []);

  const showToast = (msg: string) => {
    setToastMessage(msg);
    setTimeout(() => {
      setToastMessage(null);
    }, 2800);
  };

  const handleSelectProblem = (problemId: string) => {
    const p = PROBLEMS.find((item) => item.id === problemId);
    if (p) {
      setActiveProblemId(p.id);
      setActiveSolutionId(p.recommendedSolutionId);
      window.location.hash = `#/problem/${p.id}`;
      setCurrentScreen('problem');
      window.scrollTo(0, 0);
    }
  };

  const handleNavigateToSolution = (solutionId: string) => {
    const s = SOLUTIONS[solutionId];
    if (s) {
      setActiveSolutionId(s.id);
      window.location.hash = `#/solution/${s.id}`;
      setCurrentScreen('solution');
      window.scrollTo(0, 0);
    }
  };

  const handleNavigateBackToProblem = () => {
    window.location.hash = `#/problem/${activeProblemId}`;
    setCurrentScreen('problem');
    window.scrollTo(0, 0);
  };

  const handleNavigateHome = () => {
    window.location.hash = '#/';
    setCurrentScreen('home');
    window.scrollTo(0, 0);
  };

  const handleNavigateExplore = () => {
    window.location.hash = '#/explore';
    setCurrentScreen('home');
    setTimeout(() => {
      const el = document.getElementById('explore-problems');
      if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
      }
    }, 50);
  };

  const handleToggleSave = (problemId: string, e?: React.MouseEvent) => {
    if (e) e.stopPropagation();

    setSavedProblemIds((prev) => {
      if (prev.includes(problemId)) {
        showToast(`Removed from My Focus`);
        return prev.filter((id) => id !== problemId);
      } else {
        showToast(`Saved to My Focus`);
        return [...prev, problemId];
      }
    });
  };

  // Find active problem and solution
  const currentProblem = PROBLEMS.find((p) => p.id === activeProblemId) || PROBLEMS[0];
  const currentSolution = SOLUTIONS[currentProblem.recommendedSolutionId] || SOLUTIONS['leechblock-ng'];

  return (
    <div className="flex flex-col min-h-screen bg-slate-50 text-slate-900">
      
      {/* Global Navigation */}
      <Navbar
        currentScreen={currentScreen}
        onNavigateHome={handleNavigateHome}
        onNavigateExplore={handleNavigateExplore}
        savedCount={savedProblemIds.length}
        onOpenSaved={() => setIsSavedModalOpen(true)}
        onOpenAbout={() => setIsAboutModalOpen(true)}
      />

      {/* Main Content Area */}
      <main className="flex-1">
        {currentScreen === 'home' && (
          <HomePage
            problems={PROBLEMS}
            solutions={SOLUTIONS}
            onSelectProblem={handleSelectProblem}
            savedProblemIds={savedProblemIds}
            onToggleSave={handleToggleSave}
          />
        )}

        {currentScreen === 'problem' && (
          <ProblemPage
            problem={currentProblem}
            solution={currentSolution}
            onNavigateHome={handleNavigateHome}
            onNavigateExplore={handleNavigateExplore}
            onNavigateToSolution={handleNavigateToSolution}
            isSaved={savedProblemIds.includes(currentProblem.id)}
            onToggleSave={handleToggleSave}
          />
        )}

        {currentScreen === 'solution' && (
          <SolutionDetailPage
            solution={SOLUTIONS[activeSolutionId] || currentSolution}
            relatedProblem={currentProblem}
            onNavigateBackToProblem={handleNavigateBackToProblem}
            onNavigateHome={handleNavigateHome}
            isSaved={savedProblemIds.includes(currentProblem.id)}
            onToggleSave={(e) => handleToggleSave(currentProblem.id, e)}
          />
        )}
      </main>

      {/* Footer */}
      <Footer
        onNavigateHome={handleNavigateHome}
        onOpenAbout={() => setIsAboutModalOpen(true)}
      />

      {/* Modals */}
      <SavedModal
        isOpen={isSavedModalOpen}
        onClose={() => setIsSavedModalOpen(false)}
        savedProblemIds={savedProblemIds}
        problems={PROBLEMS}
        solutions={SOLUTIONS}
        onSelectProblem={handleSelectProblem}
        onRemoveSaved={(id) => handleToggleSave(id)}
      />

      <AboutModal
        isOpen={isAboutModalOpen}
        onClose={() => setIsAboutModalOpen(false)}
      />

      {/* Toast Notification */}
      {toastMessage && (
        <div className="fixed bottom-6 right-6 z-50 bg-slate-900 text-white px-4 py-3 rounded-2xl shadow-xl flex items-center gap-2.5 text-xs font-medium animate-in slide-in-from-bottom-5 duration-200 border border-slate-700">
          <Bookmark className="w-4 h-4 text-blue-400 fill-blue-400" />
          <span>{toastMessage}</span>
        </div>
      )}

    </div>
  );
}

export default App;
