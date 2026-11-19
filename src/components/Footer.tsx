import React from 'react';
import { Target, ShieldCheck, Sparkles, ExternalLink } from 'lucide-react';

interface FooterProps {
  onNavigateHome: () => void;
  onOpenAbout: () => void;
}

export const Footer: React.FC<FooterProps> = ({ onNavigateHome, onOpenAbout }) => {
  return (
    <footer className="bg-white border-t border-slate-200 mt-20 pt-12 pb-8">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-8 pb-10 border-b border-slate-100">
          
          {/* Brand info */}
          <div className="md:col-span-2 space-y-4">
            <div className="flex items-center gap-2.5">
              <div className="w-8 h-8 rounded-lg bg-blue-600 text-white flex items-center justify-center">
                <Target className="w-4 h-4 text-white" />
              </div>
              <span className="text-lg font-bold text-slate-900">
                Liteage <span className="text-blue-600">Focus</span>
              </span>
            </div>
            <p className="text-sm text-slate-600 max-w-md leading-relaxed">
              Liteage Focus is a student-first digital directory that helps school and competitive examination students find verified, free solutions for everyday academic and productivity bottlenecks.
            </p>
            <div className="flex flex-wrap gap-2 pt-2">
              <span className="inline-flex items-center gap-1 text-[11px] font-medium bg-blue-50 text-blue-700 px-2.5 py-1 rounded-md border border-blue-100">
                <ShieldCheck className="w-3 h-3" /> Problem-First
              </span>
              <span className="inline-flex items-center gap-1 text-[11px] font-medium bg-emerald-50 text-emerald-700 px-2.5 py-1 rounded-md border border-emerald-100">
                <ShieldCheck className="w-3 h-3" /> Free-First
              </span>
              <span className="inline-flex items-center gap-1 text-[11px] font-medium bg-indigo-50 text-indigo-700 px-2.5 py-1 rounded-md border border-indigo-100">
                <ShieldCheck className="w-3 h-3" /> 1 Primary Recommendation
              </span>
              <span className="inline-flex items-center gap-1 text-[11px] font-medium bg-slate-100 text-slate-700 px-2.5 py-1 rounded-md">
                <Sparkles className="w-3 h-3" /> Zero AI Fluff
              </span>
            </div>
          </div>

          {/* Quick links */}
          <div>
            <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-900 mb-3">
              Explore
            </h4>
            <ul className="space-y-2 text-sm">
              <li>
                <button 
                  onClick={onNavigateHome}
                  className="text-slate-600 hover:text-blue-600 transition-colors"
                >
                  All Common Problems
                </button>
              </li>
              <li>
                <button 
                  onClick={onNavigateHome}
                  className="text-slate-600 hover:text-blue-600 transition-colors"
                >
                  Distraction Blockers
                </button>
              </li>
              <li>
                <button 
                  onClick={onNavigateHome}
                  className="text-slate-600 hover:text-blue-600 transition-colors"
                >
                  Time Management Tools
                </button>
              </li>
              <li>
                <button 
                  onClick={onNavigateHome}
                  className="text-slate-600 hover:text-blue-600 transition-colors"
                >
                  Revision & Spaced Repetition
                </button>
              </li>
            </ul>
          </div>

          {/* Project Details */}
          <div>
            <h4 className="text-xs font-semibold uppercase tracking-wider text-slate-900 mb-3">
              Project & Info
            </h4>
            <ul className="space-y-2 text-sm">
              <li>
                <button 
                  onClick={onOpenAbout}
                  className="text-slate-600 hover:text-blue-600 transition-colors"
                >
                  About Liteage Focus
                </button>
              </li>
              <li>
                <span className="text-slate-500">
                  Version: <strong className="text-slate-700 font-semibold">v0.1 Prototype</strong>
                </span>
              </li>
              <li>
                <a 
                  href="https://github.com/TSGaming6239" 
                  target="_blank" 
                  rel="noopener noreferrer"
                  className="inline-flex items-center gap-1 text-slate-600 hover:text-blue-600 transition-colors"
                >
                  <span>GitHub: TSGaming6239</span>
                  <ExternalLink className="w-3 h-3" />
                </a>
              </li>
              <li>
                <span className="text-slate-500">
                  Replit: <strong className="text-slate-700 font-semibold">liteage</strong>
                </span>
              </li>
            </ul>
          </div>

        </div>

        {/* Bottom copyright */}
        <div className="pt-6 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-3">
          <p>© {new Date().getFullYear()} Liteage Focus. Built for students with genuine academic problems.</p>
          <div className="flex items-center gap-1">
            <span>Built by <strong>Shivendra Kumar Sharma</strong></span>
            <span className="mx-1">•</span>
            <span>YIIC 9 (Week 2)</span>
          </div>
        </div>
      </div>
    </footer>
  );
};
