import React, { useState } from 'react';
import { Target, Bookmark, Info, Menu, X, Compass, Home, UserCheck } from 'lucide-react';

interface NavbarProps {
  currentScreen: 'home' | 'problem' | 'solution';
  onNavigateHome: () => void;
  onNavigateExplore: () => void;
  savedCount: number;
  onOpenSaved: () => void;
  onOpenAbout: () => void;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentScreen,
  onNavigateHome,
  onNavigateExplore,
  savedCount,
  onOpenSaved,
  onOpenAbout,
}) => {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const [showSignInModal, setShowSignInModal] = useState(false);

  return (
    <>
      <header className="sticky top-0 z-40 bg-white/95 backdrop-blur-md border-b border-slate-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-16">
            
            {/* Logo & Tagline */}
            <div 
              onClick={onNavigateHome}
              className="flex items-center gap-3 cursor-pointer group select-none"
            >
              <div className="w-10 h-10 rounded-xl bg-blue-600 text-white flex items-center justify-center shadow-sm shadow-blue-500/20 group-hover:bg-blue-700 transition-colors">
                <Target className="w-5 h-5 text-white" />
              </div>
              <div>
                <span className="text-xl font-bold tracking-tight text-slate-900 group-hover:text-blue-600 transition-colors">
                  Liteage <span className="text-blue-600">Focus</span>
                </span>
                <span className="hidden sm:block text-[11px] text-slate-500 font-medium">
                  Find your solution. Focus on your goals.
                </span>
              </div>
            </div>

            {/* Desktop Navigation */}
            <nav className="hidden md:flex items-center gap-1">
              <button
                onClick={onNavigateHome}
                className={`flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                  currentScreen === 'home'
                    ? 'text-blue-600 bg-blue-50/80'
                    : 'text-slate-600 hover:text-slate-900 hover:bg-slate-100'
                }`}
              >
                <Home className="w-4 h-4" />
                Home
              </button>

              <button
                onClick={onNavigateExplore}
                className="flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-medium text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors"
              >
                <Compass className="w-4 h-4" />
                Explore Problems
              </button>

              <button
                onClick={onOpenAbout}
                className="flex items-center gap-2 px-3 py-2 rounded-lg text-sm font-medium text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors"
              >
                <Info className="w-4 h-4" />
                About
              </button>
            </nav>

            {/* Actions: Saved solutions & Sign in */}
            <div className="hidden md:flex items-center gap-3">
              <button
                onClick={onOpenSaved}
                className="flex items-center gap-2 px-3.5 py-2 rounded-lg text-sm font-medium border border-slate-200 text-slate-700 hover:bg-slate-50 hover:border-slate-300 transition-all"
                title="View your saved solutions"
              >
                <Bookmark className="w-4 h-4 text-blue-600" />
                <span>My Focus</span>
                {savedCount > 0 && (
                  <span className="bg-blue-600 text-white text-xs px-2 py-0.5 rounded-full font-semibold">
                    {savedCount}
                  </span>
                )}
              </button>

              <button
                onClick={() => setShowSignInModal(true)}
                className="flex items-center gap-2 px-3.5 py-2 rounded-lg text-sm font-medium text-slate-600 hover:text-slate-900 hover:bg-slate-100 transition-colors"
              >
                <span>Sign in</span>
                <span className="text-[10px] uppercase font-bold text-slate-400 bg-slate-100 px-1.5 py-0.5 rounded">Optional</span>
              </button>
            </div>

            {/* Mobile menu button */}
            <div className="flex md:hidden items-center gap-2">
              <button
                onClick={onOpenSaved}
                className="p-2 rounded-lg text-slate-600 hover:bg-slate-100 relative"
                aria-label="Saved solutions"
              >
                <Bookmark className="w-5 h-5 text-blue-600" />
                {savedCount > 0 && (
                  <span className="absolute top-1 right-1 w-2 h-2 bg-blue-600 rounded-full" />
                )}
              </button>
              <button
                onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                className="p-2 rounded-lg text-slate-600 hover:bg-slate-100"
                aria-label="Toggle menu"
              >
                {mobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
              </button>
            </div>

          </div>
        </div>

        {/* Mobile dropdown */}
        {mobileMenuOpen && (
          <div className="md:hidden border-b border-slate-200 bg-white px-4 pt-2 pb-4 space-y-2">
            <button
              onClick={() => { onNavigateHome(); setMobileMenuOpen(false); }}
              className="flex w-full items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-100"
            >
              <Home className="w-4 h-4 text-blue-600" />
              Home
            </button>
            <button
              onClick={() => { onNavigateExplore(); setMobileMenuOpen(false); }}
              className="flex w-full items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-100"
            >
              <Compass className="w-4 h-4 text-blue-600" />
              Explore Problems
            </button>
            <button
              onClick={() => { onOpenAbout(); setMobileMenuOpen(false); }}
              className="flex w-full items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-100"
            >
              <Info className="w-4 h-4 text-blue-600" />
              About Liteage Focus
            </button>
            <button
              onClick={() => { onOpenSaved(); setMobileMenuOpen(false); }}
              className="flex w-full items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-100"
            >
              <div className="flex items-center gap-3">
                <Bookmark className="w-4 h-4 text-blue-600" />
                <span>My Saved Focus</span>
              </div>
              {savedCount > 0 && (
                <span className="bg-blue-600 text-white text-xs px-2 py-0.5 rounded-full font-semibold">
                  {savedCount}
                </span>
              )}
            </button>
            <button
              onClick={() => { setShowSignInModal(true); setMobileMenuOpen(false); }}
              className="flex w-full items-center justify-between px-3 py-2.5 rounded-lg text-sm font-medium text-slate-700 hover:bg-slate-100 border-t border-slate-100 pt-3"
            >
              <div className="flex items-center gap-3">
                <UserCheck className="w-4 h-4 text-slate-500" />
                <span>Account Status</span>
              </div>
              <span className="text-xs bg-emerald-100 text-emerald-800 px-2 py-0.5 rounded font-medium">Guest Mode (Free)</span>
            </button>
          </div>
        )}
      </header>

      {/* Sign In / Guest Mode Modal */}
      {showSignInModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-900/40 backdrop-blur-sm animate-in fade-in duration-200">
          <div className="bg-white rounded-2xl max-w-md w-full p-6 shadow-xl border border-slate-200">
            <div className="flex items-start justify-between">
              <div className="w-10 h-10 rounded-xl bg-blue-50 text-blue-600 flex items-center justify-center mb-4">
                <UserCheck className="w-5 h-5" />
              </div>
              <button 
                onClick={() => setShowSignInModal(false)}
                className="text-slate-400 hover:text-slate-600 p-1 rounded-lg"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            
            <h3 className="text-lg font-bold text-slate-900">
              Zero Login Required in v0
            </h3>
            <p className="text-sm text-slate-600 mt-2 leading-relaxed">
              In accordance with the <strong>Liteage Focus</strong> philosophy, students can browse, search, and view all 50+ problem recommendations without creating an account.
            </p>
            <div className="mt-4 p-3 bg-blue-50 rounded-xl border border-blue-100 text-xs text-blue-900 leading-relaxed space-y-1">
              <p className="font-semibold">Current Version Status:</p>
              <p>• Your "Saved to My Focus" items are automatically saved in your browser's local storage.</p>
              <p>• Cloud account sync will be added in a future update as an optional convenience.</p>
            </div>

            <div className="mt-6 flex justify-end">
              <button
                onClick={() => setShowSignInModal(false)}
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2.5 px-4 rounded-xl text-sm transition-colors shadow-sm"
              >
                Got It, Continue Browsing
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};
